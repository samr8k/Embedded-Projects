# Facial Expression–Based LED Controller

A real-time embedded system that uses computer vision to detect facial expressions
and control LEDs connected to an Arduino via serial communication.

This project demonstrates the integration of perception (vision), decision logic,
and hardware actuation, and is designed to be extended as a scalable
human–machine interface (HMI).

---

## System Overview

Webcam → Python (OpenCV + MediaPipe) → Serial Interface → Arduino → LEDs

---

## Hardware Setup

**Components**
- Arduino Nano / Uno
- 3 × LEDs
- 3 × 220Ω resistors
- Breadboard and jumper wires

**Pin Mapping**

| Function            | Arduino Pin |
|---------------------|-------------|
| No face detected    | D2          |
| Neutral expression  | D3          |
| Smile detected      | D4          |
| Ground              | GND         |


---

## Software Stack

**Python**
- Python 3.11
- OpenCV
- MediaPipe
- NumPy
- PySerial

**Install dependencies:**

- pip install opencv-python mediapipe pyserial numpy


**Arduino**
- Arduino IDE
- Standard Arduino core

---

## Communication Protocol

Single-character commands sent over serial at **9600 baud**:

| Command | Description          |
|--------:|----------------------|
| `0`     | No face detected     |
| `1`     | Neutral expression   |
| `2`     | Smile detected       |

---

## Functional Description

1. Video frames are captured from a webcam.
2. MediaPipe Face Mesh extracts facial landmarks.
3. Mouth geometry is analyzed using multiple landmark points.
4. A smoothed smile metric is computed.
5. The detected state is transmitted to the Arduino.
6. The Arduino activates the corresponding LED.

---


---

## Design Goals

- Clear separation between vision and control layers
- Minimal communication protocol
- Real-time performance
- Easy extensibility

---

## Future Work

- User-specific calibration
- PWM brightness control
- State-machine-based Arduino logic
- Blink and mouth-open detection
- Servo / relay actuation
- Data logging and analysis

---

## License

MIT License




