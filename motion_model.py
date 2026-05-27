import cv2
import numpy as np

class MotionModel:

    def __init__(self, cx, cy):

        self.kf = cv2.KalmanFilter(4, 2)

        # Measurement Matrix
        self.kf.measurementMatrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ], np.float32)

        # Transition Matrix
        self.kf.transitionMatrix = np.array([
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], np.float32)

        # Process Noise
        self.kf.processNoiseCov = (
            np.eye(4, dtype=np.float32) * 0.03
        )

        # Initial State
        self.kf.statePre = np.array([
            [np.float32(cx)],
            [np.float32(cy)],
            [0],
            [0]
        ])

    def predict(self):

        predicted = self.kf.predict()

        pred_x = int(predicted[0][0])
        pred_y = int(predicted[1][0])

        return pred_x, pred_y

    def correct(self, cx, cy):

        measurement = np.array([
            [np.float32(cx)],
            [np.float32(cy)]
        ])

        self.kf.correct(measurement)