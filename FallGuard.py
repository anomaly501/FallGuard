from ultralytics import YOLO
import cv2

model_path = r"D:\FallGuard\runs\detect\train\train\weights\best.pt"
model = YOLO(model_path)

input_video_path = r"D:\FallGuard\inputvideo-1.mp4"
cap = cv2.VideoCapture(input_video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
output_video_path = r"D:\FallGuard\output_detected_video1.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

confidence_threshold = 0.7

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=confidence_threshold)  
    annotated_frame = results[0].plot()
    out.write(annotated_frame)
    cv2.imshow('YOLOv8 Real-Time Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Detection complete. Output video saved at:", output_video_path)
