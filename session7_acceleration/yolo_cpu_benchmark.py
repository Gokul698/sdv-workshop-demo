import time
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

frame_count = 0
start = time.time()

while frame_count < 100:

    ret, frame = cap.read()

    if not ret:
        break

    model(frame)

    frame_count += 1

end = time.time()

fps = frame_count/(end-start)

print(f"CPU FPS: {fps:.2f}")

cap.release()