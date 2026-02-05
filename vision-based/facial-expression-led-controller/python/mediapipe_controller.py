import cv2
import mediapipe as mp
import serial
import time
import math
import numpy as np

# ---------------- SERIAL ----------------
arduino = serial.Serial('COM3', 9600)  # Change COM port
time.sleep(2)

# ---------------- MEDIAPIPE ----------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

last_signal = '0'
ratio_history = []

def distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    signal = '0'
    status = "No Face"

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0]

        # ---------------- MULTI-POINT MOUTH WIDTH ----------------
        left_points = [78, 61, 191]
        right_points = [308, 291, 415]

        widths = []
        for l, r in zip(left_points, right_points):
            widths.append(distance(
                landmarks.landmark[l],
                landmarks.landmark[r]
            ))

        avg_width = np.mean(widths)

        # ---------------- MULTI-POINT MOUTH HEIGHT ----------------
        top_points = [13, 0]
        bottom_points = [14, 17]

        heights = []
        for t, b in zip(top_points, bottom_points):
            heights.append(distance(
                landmarks.landmark[t],
                landmarks.landmark[b]
            ))

        avg_height = np.mean(heights)

        if avg_height < 0.01:
            ratio = 0
        else:
            ratio = avg_width / avg_height

        # ---------------- SMOOTHING ----------------
        ratio_history.append(ratio)
        if len(ratio_history) > 5:
            ratio_history.pop(0)

        smooth_ratio = np.mean(ratio_history)

        print("Smile Ratio:", round(smooth_ratio, 2))

        # ---------------- DETECTION ----------------
        if smooth_ratio > 3.2:
            signal = '2'
            status = "Smile"
        else:
            signal = '1'
            status = "Neutral"

    # ---------------- SERIAL SEND ----------------
    if signal != last_signal:
        arduino.write(signal.encode())
        last_signal = signal

    # ---------------- DISPLAY ----------------
    cv2.putText(frame, status, (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0,255,0), 2)

    cv2.imshow("MediaPipe Multi-Point Smile Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
