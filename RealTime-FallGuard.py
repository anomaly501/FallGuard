from ultralytics import YOLO
import cv2


model_path = r"D:\fall detection\runs\detect\train\train\weights\best.pt"
model = YOLO(model_path)


cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


confidence_threshold = 0.7 

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=confidence_threshold)  
    annotated_frame = results[0].plot()

    cv2.imshow('YOLOv8 Real-Time Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Webcam feed stopped.")
