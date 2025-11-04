 🔐 Hybrid Authentication System using BLE & Facial Recognition

 🚀 A Smart, Secure, and Proxy-Free Attendance System



 🧠 Overview
This project presents a **hybrid authentication system** that integrates:

- 📡 **BLE-based Proximity Detection**  
- 🤖 **AI-based Facial Recognition**

It ensures that only **authorized and physically present** individuals can mark attendance — preventing proxy or fake entries.  
The system combines **IoT (Bluetooth Low Energy)** and **AI (Computer Vision)** for enhanced accuracy and security.



 ⚙️ Features
- 🔵 **BLE Proximity Check:** Detects if the user’s device is within allowed range.  
- 🧑‍💻 **AI Facial Recognition:** Identifies users using FaceNet embeddings.  
- 👁️ **Liveness Detection:** Detects blinking/head movement to prevent spoofing.  
- 📊 **Admin Dashboard:** Displays BLE detections and attendance logs.  
- 🧾 **Secure Attendance Marking:** Only verified users can mark presence.



 🧩 System Architecture
1. **Frontend:** HTML, CSS, JavaScript  
2. **Backend:** Python (Flask Framework)  
3. **AI Models:** FaceNet, MTCNN, and MediaPipe for face and liveness detection  
4. **BLE Logic:** RSSI-based distance simulation for proximity validation  
5. **Database:** Stores user details, embeddings, and attendance logs  



 🧰 Tech Stack

| Category | Tools / Technologies |
|-----------|----------------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask (Python) |
| **AI/ML** | TensorFlow, OpenCV, MTCNN, FaceNet, MediaPipe |
| **Database** | SQLite / MySQL |
| **IoT Simulation** | BLE (Bluetooth Low Energy) |
| **Version Control** | Git & GitHub |


 🧪 How It Works
1. **User Enrollment:** Capture and store face embeddings.  
2. **BLE Detection:** System verifies if user device is within range.  
3. **Face Recognition:** AI matches the face against stored embeddings.  
4. **Liveness Check:** Ensures real-time face movement/blinking.  
5. **Attendance Marking:** If both checks pass, attendance is recorded.


  Team Members

| Name | Role |
|------|------|
| Saumya Upadhyay | AI & Backend Developer |
| Om Makhija      | BLE & API Integration |
| Srikant Choubey | Computer Vision Engineer |
| Tanishka Jadaun | Frontend Developer & UI Designer |



🧾 Future Enhancements
- Integration with **real BLE hardware**  
- **Cloud deployment** (AWS / Firebase)  
- Mobile app for user-side attendance  
- Advanced **data analytics dashboard**


