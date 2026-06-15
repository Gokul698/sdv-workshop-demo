import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()

config = rs.config()

config.enable_stream(
    rs.stream.depth,
    640,
    480,
    rs.format.z16,
    30
)

config.enable_stream(
    rs.stream.color,
    640,
    480,
    rs.format.bgr8,
    30
)

pipeline.start(config)

while True:

    frames = pipeline.wait_for_frames()

    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    color_image = np.asanyarray(
        color_frame.get_data()
    )

    h, w, _ = color_image.shape

    cx = int(w/2)
    cy = int(h/2)

    distance = depth_frame.get_distance(
        cx,
        cy
    )

    cv2.circle(
        color_image,
        (cx,cy),
        5,
        (0,0,255),
        -1
    )

    cv2.putText(
        color_image,
        f"{distance:.2f} m",
        (30,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow(
        "Distance Measurement",
        color_image
    )

    if cv2.waitKey(1) == 27:
        break

pipeline.stop()
cv2.destroyAllWindows()
