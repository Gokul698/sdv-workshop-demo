import cv2
import time

cap = cv2.VideoCapture(0)

frame_count = 0

start = time.time()

while frame_count < 300:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

end = time.time()

fps = frame_count / (end - start)

print(f"Average FPS: {fps:.2f}")

cap.release()