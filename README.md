# Vehicle Tracker with Constant Velocity Motion Model

## Overview

This project implements a real-time vehicle tracking system capable of tracking a single car across video frames using:

- OpenCV CSRT Object Tracker
- Kalman Filter based Constant Velocity Motion Model
- Fusion Logic for stable and continuous tracking

The system combines visual object tracking with motion prediction to maintain smooth tracking even during temporary occlusions or tracker failures.

---

# Features

- Real-time vehicle tracking
- Constant velocity motion prediction
- Kalman Filter integration
- Dynamic confidence estimation
- Trusted source switching
- Bounding box visualization
- FPS monitoring
- Output video recording
- Occlusion handling

---

# Problem Statement

Design and implement a vehicle tracking system to track a single car across video frames.

The system should include:

- Car Object Tracker
- Constant Velocity Motion Model
- Fusion of tracking and motion prediction outputs

The final output should produce smooth, stable, and continuous vehicle tracking.

---

# System Architecture

```text
Video Input
     ↓
CSRT Tracker
     ↓
Kalman Filter Motion Model
     ↓
Fusion Logic
     ↓
Final Vehicle Tracking Output
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| OpenCV | Computer Vision |
| NumPy | Numerical Computation |
| Kalman Filter | Motion Prediction |
| CSRT Tracker | Vehicle Tracking |

---

# Project Structure

```text
vehicle_tracker_project/
│
├── main.py
├── tracker_module.py
├── motion_model.py
├── fusion.py
├── requirements.txt
├── README.md
│
├── videos/
│   └── video.mp4
│
├── outputs/
│   └── output.mp4
```

---

# How the Project Works

## Step 1 — Vehicle Selection

The user manually selects the target vehicle in the first frame using ROI selection.

---

## Step 2 — Object Tracking

The CSRT tracker tracks the selected vehicle in every frame and updates the bounding box position.

---

## Step 3 — Motion Prediction

The Kalman Filter predicts the next vehicle position using a constant velocity motion model.

### Motion Model

x_t = x_(t-1) + v_x

y_t = y_(t-1) + v_y

Where:

- x, y → vehicle position
- v_x, v_y → velocity components

---

## Step 4 — Fusion Logic

The outputs of:

- Object Tracker
- Motion Model

are combined to generate stable tracking.

If the tracker temporarily fails, the motion model prediction is used.

---

# Expected Output

For every frame, the system outputs:

- Bounding Box (x, y, width, height)
- Tracker Confidence
- Motion Model Confidence
- Trusted Output Source
- FPS

---

# Installation

## Clone Repository

---

## Move into Project Folder

```bash
cd Vehicle-Tracker-with-Kalman-Filter-and-CSRT
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How to Run the Project

## Step 1

Place your input video inside:

```text
videos/
```

Example:

```text
videos/video.mp4
```

---

## Step 2

Run the project:

```bash
python main.py
```

---

## Step 3

Select the target vehicle using the mouse and press ENTER.

---

## Step 4

Tracking begins automatically.

---

# Output

The processed tracking video is automatically saved in:

```text
outputs/output.mp4
```

---

# Visualization

The output video displays:

- Vehicle Bounding Box
- Kalman Prediction Point
- Tracker Confidence
- Motion Model Confidence
- Trusted Source
- FPS
- Bounding Box Coordinates

---

# Occlusion Handling

If the object tracker temporarily loses the vehicle:

- Kalman Filter prediction continues tracking
- Motion confidence gradually decreases
- Tracking remains smooth and stable

---

# Future Improvements

- YOLO-based automatic vehicle detection
- Multi-object tracking
- DeepSORT integration
- Optical flow motion estimation
- GPU acceleration
- Real-time webcam tracking

---

# Demo

The demo video should show:

- Input video
- Vehicle selection
- Real-time tracking
- Motion prediction
- Temporary occlusion handling
- Final tracking output

---
