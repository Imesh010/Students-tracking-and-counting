# 🎓 Real-Time Classroom Attendance & Monitoring System

A real-time student detection and counting system built with **YOLOv8** and **OpenCV** in Python. The system uses full-body detection (no facial recognition) with smart filtering to reduce false positives, providing a live occupancy count overlay for classrooms — useful for attendance monitoring, occupancy tracking, and space utilization analysis without the privacy concerns of facial recognition.

---

## 📖 Overview

Traditional attendance systems rely on manual roll calls or facial recognition, both of which have drawbacks — manual methods are slow and error-prone, while facial recognition raises privacy concerns and can struggle with masks, angles, or lighting. This project takes a different approach: detecting and counting people using **full-body object detection**, giving an accurate real-time occupancy count while avoiding the need to identify individuals.

**Core goals:**
- Detect and count students in a classroom in real time from video/camera feed
- Avoid facial recognition entirely — full-body detection only, for privacy-conscious monitoring
- Reduce false positives (e.g. double-counting, detecting non-student objects) through smart filtering
- Overlay a live, readable count on the video feed for at-a-glance occupancy monitoring

---

## 🛠️ Tech Stack

| Component | Purpose |
|---|---|
| Python | Core implementation language |
| YOLOv8 (Ultralytics) | Real-time object/person detection model |
| OpenCV | Video capture, frame processing, overlay rendering |

---

## ⚙️ How It Works

1. **Video input** — captures frames from a live camera feed or pre-recorded video.
2. **Detection** — each frame is passed through a YOLOv8 model to detect full-body person bounding boxes.
3. **Filtering** — smart filtering logic removes likely false positives (e.g. overlapping/duplicate detections, low-confidence detections, detections outside the region of interest).
4. **Counting** — the number of valid detections per frame is tallied to produce a live occupancy count.
5. **Overlay** — bounding boxes and the current count are drawn directly onto the video feed for real-time visual monitoring.

---


## ✅ Features

- Real-time full-body person detection using YOLOv8
- No facial recognition — privacy-friendly by design
- False-positive reduction through smart filtering (confidence thresholding, duplicate/overlap suppression)
- Live count overlay directly on the video feed
- Works with both live camera input and recorded video

---

## 🗺️ Roadmap

- [x] Real-time person detection with YOLOv8
- [x] Smart filtering to reduce false positives
- [x] Live count overlay on video feed
- [ ] Logging occupancy counts over time (CSV/database)
- [ ] Multi-camera / multi-room support
- [ ] Web dashboard for remote occupancy viewing
- [ ] Attendance report generation (entry/exit tracking)

---


