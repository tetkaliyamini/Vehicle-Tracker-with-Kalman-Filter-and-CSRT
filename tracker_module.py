import cv2

class VehicleTracker:

    def __init__(self, frame, bbox):

        self.tracker = cv2.TrackerCSRT_create()

        self.tracker.init(frame, bbox)

    def update(self, frame):

        success, bbox = self.tracker.update(frame)

        return success, bbox