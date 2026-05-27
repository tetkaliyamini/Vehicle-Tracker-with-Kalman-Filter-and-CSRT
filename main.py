import cv2

from tracker_module import VehicleTracker
from motion_model import MotionModel
from fusion import FusionSystem

# -----------------------------------
# LOAD VIDEO
# -----------------------------------

video_path = "videos/video2.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video")
    exit()

# -----------------------------------
# READ FIRST FRAME
# -----------------------------------

ret, frame = cap.read()

if not ret:
    print("Cannot read video")
    exit()

# -----------------------------------
# SELECT VEHICLE
# -----------------------------------

print("Select the target vehicle and press ENTER")

bbox = cv2.selectROI(
    "Select Vehicle",
    frame,
    False
)

x, y, w, h = [int(v) for v in bbox]

# Initial center point
cx = x + w // 2
cy = y + h // 2

# -----------------------------------
# INITIALIZE MODULES
# -----------------------------------

tracker = VehicleTracker(frame, bbox)

motion_model = MotionModel(cx, cy)

fusion_system = FusionSystem()

# -----------------------------------
# OUTPUT VIDEO SAVING
# -----------------------------------

frame_width = int(
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
)

frame_height = int(
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
)

fps_video = int(
    cap.get(cv2.CAP_PROP_FPS)
)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(
    'outputs/output.mp4',
    fourcc,
    fps_video,
    (frame_width, frame_height)
)

print("Output video recording started...")

# -----------------------------------
# MAIN LOOP
# -----------------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # FPS timer
    timer = cv2.getTickCount()

    # -----------------------------------
    # MOTION PREDICTION
    # -----------------------------------

    pred_x, pred_y = motion_model.predict()

    # -----------------------------------
    # TRACKER UPDATE
    # -----------------------------------

    success, bbox = tracker.update(frame)

    # ===================================
    # TRACKER SUCCESS
    # ===================================

    if success:

        x, y, w, h = [int(v) for v in bbox]

        cx = x + w // 2
        cy = y + h // 2

        # Correct Kalman Filter
        motion_model.correct(cx, cy)

        final_x = x
        final_y = y

        box_color = (0, 255, 0)

    # ===================================
    # TRACKER FAILURE
    # ===================================

    else:

        final_x = pred_x - w // 2
        final_y = pred_y - h // 2

        box_color = (0, 0, 255)

    # -----------------------------------
    # FUSION SYSTEM
    # -----------------------------------

    (
        tracker_confidence,
        motion_confidence,
        trusted_source
    ) = fusion_system.get_confidence(success)

    # -----------------------------------
    # KEEP BOX INSIDE FRAME
    # -----------------------------------

    final_x = max(0, final_x)
    final_y = max(0, final_y)

    end_x = min(frame.shape[1], final_x + w)
    end_y = min(frame.shape[0], final_y + h)

    # -----------------------------------
    # DRAW BOUNDING BOX
    # -----------------------------------

    cv2.rectangle(
        frame,
        (final_x, final_y),
        (end_x, end_y),
        box_color,
        4
    )

    # -----------------------------------
    # LABEL
    # -----------------------------------

    cv2.putText(
        frame,
        "TARGET VEHICLE",
        (final_x, final_y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        box_color,
        2
    )

    # -----------------------------------
    # DRAW PREDICTION POINT
    # -----------------------------------

    cv2.circle(
        frame,
        (pred_x, pred_y),
        6,
        (255, 0, 0),
        -1
    )

    # -----------------------------------
    # DISPLAY INFORMATION
    # -----------------------------------

    cv2.putText(
        frame,
        f"Trusted Source: {trusted_source}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Tracker Confidence: {tracker_confidence:.2f}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Motion Confidence: {motion_confidence:.2f}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    fps = cv2.getTickFrequency() / (
        cv2.getTickCount() - timer
    )

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"BBox: x={final_x} y={final_y} w={w} h={h}",
        (20, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    # -----------------------------------
    # SAVE OUTPUT VIDEO
    # -----------------------------------

    out.write(frame)

    # -----------------------------------
    # SHOW FRAME
    # -----------------------------------

    cv2.imshow(
        "Vehicle Tracking System",
        frame
    )

    key = cv2.waitKey(30)

    if key == 27:
        break

# -----------------------------------
# RELEASE RESOURCES
# -----------------------------------

cap.release()

out.release()

cv2.destroyAllWindows()

print("Output video saved successfully!")