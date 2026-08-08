import cv2
from hand_tracker import HandTracker
from flower import Flower

tracker = HandTracker()
flower = Flower()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frame, bloom, flower_position = tracker.get_hands(frame)

    if flower_position:
        flower.draw(
            frame,
            flower_position,
            bloom
        )
    cv2.imshow("Flower AI", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()