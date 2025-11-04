# PRESENCE
AI-enabled proxy free attendance system
🔐 Hybrid Authentication System using BLE & Facial Recognition
🚀 A Smart, Secure, and Proxy-Free Attendance System
🧠 Overview

This project presents a hybrid authentication system that integrates:

📡 BLE-based Proximity Detection

🤖 AI-based Facial Recognition

It ensures that only authorized and physically present individuals can mark attendance — preventing proxy or fake entries.
The system combines IoT (Bluetooth Low Energy) and AI (Computer Vision) for enhanced accuracy and security.

⚙️ Features
🔵 BLE Proximity Check: Detects if the user’s device is within allowed range.

🧑‍💻 AI Facial Recognition: Identifies users using FaceNet embeddings.

👁️ Liveness Detection: Detects blinking/head movement to prevent spoofing.

📊 Admin Dashboard: Displays BLE detections and attendance logs.

🧾 Secure Attendance Marking: Only verified users can mark presence.


🧩 System Architecture
Frontend: HTML, CSS, JavaScript

Backend: Python (Flask Framework)

AI Models: FaceNet, MTCNN, and MediaPipe for face and liveness detection

BLE Logic: RSSI-based distance simulation for proximity validation

Database: Stores user details, embeddings, and attendance logs

🧰 Tech Stack
Category	Tools / Technologies
Frontend	HTML, CSS, JavaScript
Backend	Flask (Python)
AI/ML	TensorFlow, OpenCV, MTCNN, FaceNet, MediaPipe
Database	SQLite / MySQL
IoT Simulation	BLE (Bluetooth Low Energy)
Version Control	Git & GitHub

🧪 How It Works

User Enrollment: Capture and store face embeddings.

BLE Detection: System verifies if user device is within range.

Face Recognition: AI matches the face against stored embeddings.

Liveness Check: Ensures real-time face movement/blinking.

Attendance Marking: If both checks pass, attendance is recorded.

🧑‍🤝‍🧑 Team Members
Name	                  Role
Saumya Upadhyay	        AI & Backend Developer
Om Makhija	            BLE & API Integration
Srikant Choubey       	Computer Vision Engineer
Tanishka Jadaun	        Frontend Developer & UI Designer

