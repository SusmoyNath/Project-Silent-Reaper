# Version 1 — CSRT Manual Tracking

## Development Phase: Initial Prototype

Version 1 represents the earliest implementation of Project Silent Reaper and serves as the foundation for all subsequent tracking architectures.

This version implements a real-time visual tracking system using OpenCV's CSRT (Discriminative Correlation Filter Tracker). A target is manually selected by the user, after which the tracker continuously estimates and updates the target's position across consecutive video frames.

Although simple compared to later versions, V1 established the fundamental concepts of target acquisition, tracking persistence, and visual feedback that would eventually evolve into adaptive memory, re-identification, autonomous re-acquisition, and hybrid recovery architectures.

---

## Objective

The objective of this version was to validate the feasibility of real-time target tracking using classical computer vision techniques before introducing object detection, multi-object tracking, and identity recovery systems.

---

## Demonstration

🎥 **Video Demonstration**

https://github.com/SusmoyNath/Project-Silent-Reaper/blob/main/media/demos/v1_csrt_tracking_demo.mp4

The demonstration shows manual target selection followed by continuous object tracking using the CSRT algorithm.

---

## Features

* Real-time webcam processing
* Manual target selection
* CSRT-based object tracking
* Continuous target tracking
* Bounding box visualization
* Lightweight implementation
* Real-time visual feedback

---

## Technologies Used

* Python
* OpenCV
* CSRT (Discriminative Correlation Filter Tracker)

---

## System Workflow

```text
Camera Feed
     │
     ▼
Manual Target Selection
     │
     ▼
CSRT Tracker Initialization
     │
     ▼
Real-Time Object Tracking
     │
     ▼
Bounding Box Update
     │
     ▼
Tracking Persistence
```

---

## Limitations

As an initial prototype, this version has several limitations:

* Requires manual target selection
* Supports only a single target
* No automatic object detection
* No multi-object tracking
* No appearance re-identification
* No adaptive memory system
* No recovery after complete target loss
* Sensitive to heavy occlusion and abrupt appearance changes

---

## Significance

Despite its simplicity, V1 established the core tracking pipeline that became the basis for future development.

The limitations encountered in this version directly motivated the introduction of:

* YOLO-based object detection
* DeepSORT multi-object tracking
* Appearance-based re-identification
* Adaptive memory architectures
* Autonomous target re-acquisition
* Hybrid recovery mechanisms

---

## Position in Project Evolution

```text
V1  →  CSRT Manual Tracking
V2  →  YOLO Detection
V3  →  DeepSORT Tracking
V4  →  Re-Identification
V5  →  Stream Integration
V6  →  Adaptive Memory
V7  →  Face-Aware Tracking
V8  →  Recovery Architecture
V8.1 → Protected Adaptive Memory
V9  →  Hybrid Recovery + Temporal Confirmation
```

---

This version marks the starting point of Project Silent Reaper's evolution from a simple visual tracker into a research-driven computer vision architecture focused on long-term target persistence and intelligent recovery.
