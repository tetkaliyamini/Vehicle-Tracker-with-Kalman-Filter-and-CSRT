class FusionSystem:

    def __init__(self):

        self.missed_frames = 0

    def get_confidence(self, tracker_success):

        if tracker_success:

            self.missed_frames = 0

            tracker_confidence = 0.95

            motion_confidence = 0.75

            trusted_source = "Tracker"

        else:

            self.missed_frames += 1

            tracker_confidence = max(
                0.1,
                0.5 - self.missed_frames * 0.08
            )

            motion_confidence = max(
                0.3,
                0.9 - self.missed_frames * 0.04
            )

            trusted_source = "Motion Model"

        return (
            tracker_confidence,
            motion_confidence,
            trusted_source
        )