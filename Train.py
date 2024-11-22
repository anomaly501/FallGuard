from ultralytics import YOLO

DYP = r"D:\FallGuard\data.yaml"
MT = "yolov8m.pt"
EP = 50
ISZ = 640
BS = 16
DEV = 0

def train_model():
    print("Starting YOLOv8 training...")
    model = YOLO(MT)
    model.train(
        data=DYP,
        epochs=EP,
        imgsz=ISZ,
        batch=BS,
        device=DEV,
        project="runs/detect/train"
    )
    print("Training completed!")

if __name__ == "__main__":
    train_model()
