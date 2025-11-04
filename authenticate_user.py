#!/usr/bin/env python3
import os
import sys
import random
import cv2
import numpy as np
import torch
import pickle
from facenet_pytorch import MTCNN, InceptionResnetV1

# ——— Configuration ———
ENCODINGS_FILE   = 'encodings.pickle'
RSSI_THRESHOLD   = -70       # dBm threshold for “in‑classroom” check
MATCH_THRESHOLD  = 0.6       # Euclidean distance threshold
DEVICE           = 'cuda' if torch.cuda.is_available() else 'cpu'

# ——— Initialize models ———
mtcnn  = MTCNN(image_size=160, margin=0, keep_all=False, device=DEVICE)
resnet = InceptionResnetV1(pretrained='vggface2').eval().to(DEVICE)

def load_db(path=ENCODINGS_FILE):
    if not os.path.exists(path):
        print("No registered users. Please run register_user.py first.")
        sys.exit(1)
    with open(path, 'rb') as f:
        return pickle.load(f)

def simulate_ble_check():
    # simulate a random RSSI value in a realistic BLE range
    rssi = random.randint(-100, -30)
    print(f"Simulated RSSI = {rssi} dBm (threshold = {RSSI_THRESHOLD} dBm)")
    if rssi < RSSI_THRESHOLD:
        print("RSSI not proper. Exiting.")
        sys.exit(1)
    print("RSSI OK. Proceeding to face recognition.\n")

def recognize():
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture & quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Authenticate - press q to scan', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame

def get_embedding(frame):
    rgb  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face = mtcnn(rgb)
    if face is None:
        print("No face detected. Exiting.")
        sys.exit(1)
    with torch.no_grad():
        emb = resnet(face.unsqueeze(0).to(DEVICE))
    return emb.cpu().numpy().flatten()

def match(known, probe, threshold=MATCH_THRESHOLD):
    names, rolls, embs = zip(*[
        (u['name'], u['roll'], u['embedding']) for u in known
    ])
    dists = np.linalg.norm(np.stack(embs) - probe, axis=1)
    idx   = np.argmin(dists)
    if dists[idx] < threshold:
        return names[idx], rolls[idx], float(dists[idx])
    return None, None, None

# — Roll-number prompt & filter DB —
roll_input = input("Enter roll number: ").strip()
full_db    = load_db()
known_db   = [u for u in full_db if u['roll'] == roll_input]
if not known_db:
    print(f"No registration found for roll '{roll_input}'. Exiting.")
    sys.exit(1)

def main():
    # 1) Simulate BLE/RSSI check
    simulate_ble_check()

    # 2) Load registered embeddings
    db = known_db

    # 3) Capture one frame on keypress
    frame = recognize()

    # 4) Compute its embedding
    probe = get_embedding(frame)

    # 5) Match against database
    name, roll, distance = match(db, probe)
    if name:
        print(f"✅ Recognized: {name} (Roll {roll}) — distance={distance:.4f}")
    else:
        print("❌ No match found.")

if __name__ == '__main__':
    main()
