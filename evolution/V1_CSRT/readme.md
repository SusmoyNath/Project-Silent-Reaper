# CSRT Object Tracker (Manual Target Selection)

This module implements a **real-time object tracking system** using a webcam.  
The user can **manually select any object or person on the live camera feed**, and the system will track that object continuously.

The tracker is implemented using **OpenCV's CSRT (Discriminative Correlation Filter Tracker)**.

This module is part of **Project Silent Reaper** and serves as a **basic vision prototype for drone-based target tracking**.

---

# Features

- Real-time webcam processing
- Manual object selection with mouse
- Continuous object tracking
- Visual bounding box around tracked target
- Live camera feed during selection

---

# Technologies Used

- Python
- OpenCV
- CSRT Tracking Algorithm

---

# System Workflow

```
Camera Feed
     ↓
User draws bounding box around target
     ↓
CSRT tracker initializes
     ↓
Object tracking begins
     ↓
Bounding box follows the object
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Skynet-Biogenics/Project-Silent-Reaper.git
cd Project-Silent-Reaper
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv env
```

Activate it:

Mac / Linux

```bash
source env/bin/activate
```

Windows

```bash
env\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install opencv-contrib-python
```

`opencv-contrib-python` is required because the **CSRT tracker is part of the OpenCV contrib module**.

---

# Running the Program

Navigate to the tracker folder:

```bash
cd Tracker/CSRT\ (Discriminative\ Correlation\ Filter\ Tracker)
```

Run the tracker:

```bash
python tracker.py
```

---

# How to Use

1. Run the program.
2. A **live webcam feed** will appear.
3. Click and drag the mouse to **draw a bounding box around the object/person you want to track**.
4. Release the mouse.
5. The system will **lock onto the selected object and begin tracking it**.

Controls:

| Action | Key |
|------|------|
Exit program | ESC |
Select object | Mouse drag |

---

# Example Behavior

- Draw a box around a person.
- The system initializes the CSRT tracker.
- A **red bounding box appears and follows the target** as it moves.

---

# Known Limitations

The CSRT tracker may lose the target if:

- The object moves very fast
- The object leaves the camera frame
- The object becomes fully occluded
- Lighting changes drastically

---

# Possible Improvements

Future upgrades may include:

- AI-based object detection (YOLO)
- Multi-object tracking
- Target re-identification
- Motion prediction using Kalman filters
- Integration with drone flight control

---

# Project Context

This tracker serves as the **foundation of the visual tracking system** used in **Project Silent Reaper**.

Future modules will integrate this tracking system with:

- drone navigation
- autonomous following
- AI-assisted target detection

---

# Author

Project Silent Reaper  
Skynet Biogenics
