import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))

if webcam.isOpened():
    _, frame = webcam.read()
    while _:
        _, frame = webcam.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imshow("Ata", frame)

        key = cv2.waitKey(30)

        if key & 0xFF == ord("e"):
            break