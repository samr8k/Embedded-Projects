# Real-Time Sensor Data Logger with Live Python Visualization

This project provides a simple and reusable pipeline for **real-time sensor data acquisition and visualization** using an **Arduino Nano** and **Python**.

Sensor readings are streamed over serial communication and plotted live on a computer, making it useful for **embedded debugging, robotics experiments, battery monitoring, and research data logging**.

---

## Core Concept

Sensor → Arduino Nano → USB Serial → Python → Live Graph

The included example uses an **LDR (light sensor)**, but **any analog or serial-readable sensor** can be connected and visualized using the same architecture.

Supported use cases include:

- Battery voltage monitoring  
- Temperature sensing  
- Current measurement  
- Potentiometer / position sensing  
- Any analog sensor connected to the ADC  

This makes the project a **generic embedded data-logging framework**, not just a single-sensor demo.

---

## Features

- Real-time serial data streaming from Arduino Nano  
- Live plotting using Python (`matplotlib`)  
- Simple **CSV-based communication format**  
- Sensor-independent design  
- Easily extendable to multi-sensor logging and file storage  

---

## Hardware Required

- Arduino Nano  
- Analog sensor (example: LDR + 10kΩ resistor voltage divider)  
- USB cable  
- Breadboard and jumper wires  

---

## Software Requirements

- Arduino IDE  
- Python 3  

Install required Python libraries:

```bash
pip install pyserial matplotlib
```

---

## Connections

| Arduino Nano Pin | Connection |
|------------------|------------|
| 5V               | LDR (one terminal) |
| A0               | Junction of LDR and resistor |
| GND              | 10kΩ resistor |

---

### Using Other Analog Sensors

To use a different sensor:

- Connect the sensor output to **A0** (or any ADC pin)
- Ensure the output voltage stays within **0–5 V**
- If required, use a **voltage divider or signal conditioning circuit**

No changes are required in the Python visualization script as long as the serial data format remains the same.

---

## How It Works

1. Arduino reads the sensor value using ADC.

2. Data is transmitted over serial in CSV format:

```bash
raw_value,voltage
```


3. Python continuously reads the serial stream.

4. matplotlib updates a live real-time graph.

---


## Running the Project
1. Upload Firmware

Upload the Arduino sketch from:

```bash
/firmware/nano_serial_logger.ino
```

2. Install Python Libraries
```bash
pip install pyserial matplotlib
```

3. Set Serial Port

Update the COM/TTY port inside:

```bash
/python/live_plot.py
```

4. Run the Live Plot
```bash
python live_plot.py
```


Change the light on the LDR (or vary any connected sensor) to see the real-time graph update.

---


## Using a Different Sensor

To use another sensor:

1. Connect the sensor output to an analog pin (e.g., A0).

2. Ensure the voltage remains within the 0–5 V ADC range of the Arduino Nano.

3. Keep the same CSV serial format in firmware:

value,scaled_value


4. Run the same Python script — no modification required.

This allows quick reuse for:

- EV battery monitoring

- Temperature logging

- Current sensing

- Robotics sensor debugging

---


## Future Improvements

- Multi-sensor real-time plotting

- CSV file data recording

- Wireless logging (Wi-Fi / Bluetooth)

- Integration with ROS or dashboards

- Data analysis for AI/ML or energy research

---


## Learning Outcomes

This project demonstrates:

- Embedded ADC data acquisition

- Serial communication protocol design

- Real-time Python visualization

- End-to-end hardware-to-software data pipeline

It serves as a foundation for robotics telemetry, EV battery monitoring, and research-grade data logging.

