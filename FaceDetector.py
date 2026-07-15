from ultralytics import YOLO
import cv2

# Load YOLOv8 model (pretrained on COCO dataset)
model = YOLO('yolov8n.pt')  # or yolov8s.pt for higher accuracy

# Open webcam or video
cap = cv2.VideoCapture(0)  # Use 'video.mp4' for video file

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)[0]

    # Count people
    person_count = 0

    for box in results.boxes:
        class_id = int(box.cls[0])
        if model.names[class_id] == 'person':
            person_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, 'Student', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    # Show count
    cv2.putText(frame, f'Students: {person_count}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("Student Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
