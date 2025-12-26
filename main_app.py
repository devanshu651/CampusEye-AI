import streamlit as st
import cv2
import face_recognition
import numpy as np
import pickle
import sqlite3
from datetime import datetime, timedelta

# Page config
st.set_page_config(page_title="Nexus Face-ID", layout="wide")
st.title("🚀 Smart Campus Face-ID System")

# 1. Database Connection with 5-Minute Cooldown
def mark_attendance(name, dept):
    conn = sqlite3.connect('campus_attendance.db')
    cursor = conn.cursor()
    now = datetime.now()
    
    # Check: Kya pichle 5 min mein iski entry hui hai?
    five_mins_ago = (now - timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("SELECT * FROM attendance WHERE name = ? AND timestamp > ?", (name, five_mins_ago))
    
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO attendance (name, department, timestamp) VALUES (?, ?, ?)", 
                       (name, dept, now.strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        st.toast(f"✅ Attendance marked for {name}!")
    
    conn.close()

# 2. Load Encodings
try:
    with open("encodings.p", "rb") as f:
        data = pickle.load(f)
    known_encodings = data["encodings"]
    known_metadata = data["metadata"]
except:
    st.error("Pehle encoder.py chalao!")
    st.stop()

# 3. Sidebar Logs
st.sidebar.header("Recent Logs")
def show_logs():
    conn = sqlite3.connect('campus_attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, department, timestamp FROM attendance ORDER BY timestamp DESC LIMIT 10")
    logs = cursor.fetchall()
    if logs:
        st.sidebar.table([{"name": l[0], "dept": l[1], "time": l[2]} for l in logs])
    conn.close()

# 4. Camera Loop
run = st.checkbox('Start Camera', value=True)
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret: break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Tolerance 0.55 se recognition better hogi
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.55)
        name = "Unknown"
        
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            full_metadata = known_metadata[best_match_index]
            name = full_metadata.split('_')[0]
            dept = full_metadata.split('_')[1]
            mark_attendance(name, dept)

        top, right, bottom, left = [v * 4 for v in face_location]
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    show_logs()

camera.release()
