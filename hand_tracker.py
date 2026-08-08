import cv2
import math
from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils


class HandTracker:
    def __init__(self):
        self.mp_hands = hands

        self.hands = hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = drawing_utils

    def get_hands(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.hands.process(rgb)

        bloom = 0.0
        flower_position = None

        if result.multi_hand_landmarks:

            for hand in result.multi_hand_landmarks:

                self.drawer.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS
                )

                h, w, _ = frame.shape

                palm = hand.landmark[0]

                px = int(palm.x * w)
                py = int(palm.y * h)

                flower_position = (px, py - 120)

                thumb = hand.landmark[4]
                index = hand.landmark[8]

                x1 = int(thumb.x * w)
                y1 = int(thumb.y * h)

                x2 = int(index.x * w)
                y2 = int(index.y * h)

                cv2.circle(frame, (x1, y1), 8, (0, 255, 255), -1)
                cv2.circle(frame, (x2, y2), 8, (0, 255, 255), -1)

                distance = math.hypot(x2 - x1, y2 - y1)

                bloom = min(distance / 150, 1.0)

                cv2.putText(
                    frame,
                    f"Bloom : {bloom:.2f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2
                )

        return frame, bloom, flower_position