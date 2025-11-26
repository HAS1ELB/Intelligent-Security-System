# Intelligent Security System

## Overview

This project is a software simulation of an Intelligent IoT Security System. Designed to operate without physical hardware (PIR sensors, ESP32-CAM), it simulates the entire security workflow using software modules and synthetic/real data.

The system mimics a real-world scenario where a motion detector triggers a camera capture. The captured image is then processed by an advanced AI model (**YOLOv8**) to distinguish between harmless events (empty room) and potential threats (intruders).

## Features

- **Sensor Simulation**: Simulates a PIR motion sensor with randomized activation patterns.
- **Camera Simulation**: Simulates a camera feed by randomly selecting images from a curated dataset of real-world scenarios.
- **AI Detection**: Utilizes **YOLOv8** (You Only Look Once) for high-speed, accurate person detection.
- **Alert System**: Automatically triggers alerts (console output and `alerts.log`) when a person is identified.
- **Robust Dataset**: Includes a mix of empty rooms and "intruder" scenarios to verify system reliability.

## Project Structure

- `main.py`: The central controller that orchestrates the simulation loop (Sensor -> Camera -> AI -> Alert).
- `sensor_simulation.py`: Generates simulated PIR sensor signals (0 or 1).
- `camera_simulation.py`: Simulates the camera interface, providing images from the `data/` directory.
- `ai_inference.py`: Contains the YOLOv8 integration for object detection.
- `alert_system.py`: Manages alert logging and display.
- `data/`: Contains the image dataset used for simulation.

## Prerequisites

- Python 3.8+
- Internet access (for the first run to download the YOLOv8 model)

## Installation

1.  **Install dependencies**:
    ```bash
    pip install ultralytics opencv-python
    ```

## Usage

1.  **Start the simulation**:

    ```bash
    python main.py
    ```

2.  **Observe the output**:

    - The system will print the sensor status (`.` for idle, `[MOTION DETECTED]` for active).
    - When motion is detected, it will analyze an image.
    - If a person is found, an **ALERT** is displayed and logged.

3.  **Stop the system**:
    - Press `Ctrl+C` to exit the simulation.

## Authors

- **EL BAHRAOUI Hassan**
- **LAKHAL HALA**

## License

This project was developed for educational purposes.
