<div align="center">

```
 ██████╗ █████╗ ███╗   ███╗██████╗ ██╗   ██╗███████╗███████╗██╗   ██╗███████╗
██╔════╝██╔══██╗████╗ ████║██╔══██╗██║   ██║██╔════╝██╔════╝╚██╗ ██╔╝██╔════╝
██║     ███████║██╔████╔██║██████╔╝██║   ██║███████╗█████╗   ╚████╔╝ █████╗  
██║     ██╔══██║██║╚██╔╝██║██╔═══╝ ██║   ██║╚════██║██╔══╝    ╚██╔╝  ██╔══╝  
╚██████╗██║  ██║██║ ╚═╝ ██║██║     ╚██████╔╝███████║███████╗   ██║   ███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝
```

# 👁️ CampusEye AI
### *Smart Campus Face-ID Attendance System*

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Working%20Prototype-22c55e?style=for-the-badge)

<br/>

> **Automate. Recognize. Log.**  
> *A real-time, computer vision–powered attendance system — built solo, from scratch.*

---

</div>

<br/>

## 🧠 What is CampusEye?

CampusEye AI is a **real-time face recognition attendance system** that eliminates manual roll-calls entirely. Built as an end-to-end solo project, it captures live webcam frames, identifies faces using a 128-dimensional encoding model, and logs attendance with timestamps — all reflected instantly on a live dashboard.

No spreadsheets. No paper. No delays.

<br/>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Real-time Detection** | Face detection and recognition via live webcam feed |
| ✅ **Auto Attendance Logging** | Timestamps recorded automatically on every match |
| 🔁 **Anti-Duplicate Logic** | Prevents repeated entries within a configurable time window |
| 📊 **Live Dashboard** | Streamlit-powered UI for real-time monitoring |
| 🗄️ **Persistent Storage** | Lightweight SQLite database — no setup overhead |

<br/>

---

## 🛠️ Tech Stack

```
┌──────────────────────────────────────────────────────┐
│                    CampusEye AI                      │
├──────────────┬───────────────────────────────────────┤
│  Language    │  Python 3.x                           │
│  Vision      │  OpenCV + face_recognition (dlib)     │
│  Database    │  SQLite                               │
│  UI          │  Streamlit                            │
└──────────────┴───────────────────────────────────────┘
```

<br/>

---

## 📁 Project Structure

```
CampusEye/
│
├── 📂 student_db/          # Face image dataset (privacy-safe, prototype scale)
│
├── 🔧 encoder.py           # Generates & serializes 128-d face encodings
├── 🧹 data_cleaner.py      # Preprocessing & cleanup of image data
├── 🗄️  db_init.py           # Initializes SQLite schema
└── 🚀 main_app.py          # Core logic: recognition + attendance + Streamlit UI
```

<br/>

---

## ⚙️ How It Works

```
  📷 Webcam Frame
       │
       ▼
  [ Face Detection ]  ◄── OpenCV
       │
       ▼
  [ 128-d Encoding ]  ◄── dlib / face_recognition
       │
       ▼
  [ Match Against DB ] ◄── Stored Encodings
       │
    ┌──┴──┐
    │Match│
    └──┬──┘
       │
       ▼
  [ Log Attendance ]  ◄── SQLite (with timestamp + anti-duplicate check)
       │
       ▼
  [ Streamlit Dashboard ] ◄── Live update
```

<br/>

---

## 📌 Current Status

- ✅ Fully working prototype
- ✅ Tested on a limited dataset for demonstration
- ✅ Runs locally with no cloud dependency
- ✅ Designed to scale to multiple users without architectural changes

<br/>

---

## 🚧 Known Limitations

- 🔬 Tested on a small dataset *(privacy-safe prototype)*
- 🛡️ Basic anti-spoofing not yet implemented
- ☁️ No cloud deployment in current version

<br/>

---

## 🔮 Planned Improvements

- [ ] **Liveness / Anti-Spoofing** — Prevent photo-based spoofing attacks
- [ ] **Low-End Device Optimization** — Better performance on constrained hardware
- [ ] **Streamlined Deployment** — Cleaner setup and deployment workflow

<br/>

---

## 🤖 AI Usage Disclosure

> AI tools were used **only** as a mentor and documentation assistant.  
> All core logic, system design, implementation, and debugging were done **independently**.

<br/>

---

## 👤 Author

<div align="center">

**Devanshu Raut**  
*Solo Developer · CampusEye AI*

---

*Built with focus, curiosity, and a lot of webcam testing.* 👁️

</div>