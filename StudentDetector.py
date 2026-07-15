from ultralytics import YOLO
import cv2
import time

# Load YOLOv8 model (pretrained on COCO dataset)
model = YOLO('yolov8n.pt')  # You can try 'yolov8s.pt' for higher accuracy

# ✅ Replace 1 with the correct camera index for OBS Virtual Camera (try 0, 1, 2...)
cap = cv2.VideoCapture(1)

# Give camera time to warm up
time.sleep(2)

# Check if OBS Virtual Camera is detected
if not cap.isOpened():
    print("❌ Failed to open OBS Virtual Camera. Try changing the index (e.g., 0, 1, 2).")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Frame not received. Make sure OBS Virtual Camera is running.")
        time.sleep(1)   
        continue

    # Run YOLOv8 detection
    results = model(frame)[0]

    person_count = 0

    for box in results.boxes:
        class_id = int(box.cls[0])
        conf = float(box.conf[0])

        if model.names[class_id] == 'person':
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            width = x2 - x1
            height = y2 - y1
            area = width * height
            aspect_ratio = height / (width + 1e-5)

            # Filter out weak, small, or odd-shaped detections
            if conf < 0.5 or area < 5000 or aspect_ratio < 1.2:
                continue

            person_count += 1
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, 'Student', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display student count
    cv2.putText(frame, f'Students: {person_count}', (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Student Detector - OBS Virtual Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()