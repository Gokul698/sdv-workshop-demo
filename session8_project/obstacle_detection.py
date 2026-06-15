import pyrealsense2 as rs
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

pipeline.start(config)

try:

    while True:

        frames = pipeline.wait_for_frames()

        depth_frame = frames.get_depth_frame()

        if not depth_frame:
            continue

        distance = depth_frame.get_distance(320, 240)

        depth_image = cv2.applyColorMap(
            cv2.convertScaleAbs(
                cv2.UMat(depth_frame.get_data()).get(),
                alpha=0.03
            ),
            cv2.COLORMAP_JET
        )

        cv2.putText(
            depth_image,
            f"Distance: {distance:.2f} m",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        if distance < 1.0:

            cv2.putText(
                depth_image,
                "WARNING: OBSTACLE!",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

        cv2.imshow("Obstacle Detection", depth_image)

        if cv2.waitKey(1) == ord('q'):
            break

finally:

    pipeline.stop()
    cv2.destroyAllWindows()