import cv2

# Open the default camera (webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read one frame
    if not ret:
        break

    # 🟩 Draw a green rectangle
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)

    # 🔵 Draw a blue circle
    cv2.circle(frame, (200, 200), 50, (255, 0, 0), 3)

    # ✍️ Put some text
    cv2.putText(frame, 'Hello OpenCV!', (110, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # 🖼️ Show the frame
    cv2.imshow("Live Feed", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🧹 Clean up
cap.release()
cv2.destroyAllWindows()
