#!/usr/bin/env python3
import os
import cv2
import numpy as np
import torch
import pickle
from facenet_pytorch import MTCNN, InceptionResnetV1

# ——— Configuration ———
ENCODINGS_FILE   = 'encodings.pickle'
CAPTURE_DURATION = 10        # seconds to capture for embedding
FPS              = 10       # frames per second to sample
THRESHOLD        = 0.6      # unused here but aligns with recognition
DEVICE           = 'cpu'    # force CPU mode to avoid unsupported GPU hangs

# ——— Initialize models ———
mtcnn   = MTCNN(image_size=160, margin=0, keep_all=False, device=DEVICE)
resnet  = InceptionResnetV1(pretrained='vggface2').eval().to(DEVICE)

def capture_face_embeddings(duration=CAPTURE_DURATION, fps=FPS):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open your webcam.")

    embeddings   = []
    total_frames = duration * fps
    count        = 0

    # Determine how often to sample frames
    cam_fps  = cap.get(cv2.CAP_PROP_FPS) or 30
    interval = int(cam_fps // fps) or 1

    print(f"Capturing for {duration}s ({total_frames} frames)...")
    while count < total_frames:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame; stopping.")
            break

        # Show live frame and progress
        print(f"\r  capturing frame {count+1}/{total_frames}", end="", flush=True)
        cv2.imshow("Registration", frame)
        cv2.waitKey(1)

        if count % interval == 0:
            rgb  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face = mtcnn(rgb)  # runs on CPU now
            if face is not None:
                with torch.no_grad():
                    emb = resnet(face.unsqueeze(0).to(DEVICE))
                    embeddings.append(emb.cpu().numpy().flatten())

        count += 1

    cap.release()
    cv2.destroyAllWindows()

    if not embeddings:
        raise RuntimeError("No face detected during registration.")
    return np.mean(embeddings, axis=0)

def load_db(path=ENCODINGS_FILE):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return pickle.load(f)
    return []

def save_db(db, path=ENCODINGS_FILE):
    with open(path, 'wb') as f:
        pickle.dump(db, f)
    print(f"\nSaved {len(db)} record(s) to {path}")

def main():
    print("=== Student Registration ===")
    name = input("Full name: ").strip()
    roll = input("Roll number: ").strip()

    # Capture and compute embedding
    embedding = capture_face_embeddings()

    # Load existing DB, append new record, and save
    db = load_db()
    db.append({
        'name':      name,
        'roll':      roll,
        'embedding': embedding
    })
    save_db(db)

if __name__ == '__main__':
    main()
