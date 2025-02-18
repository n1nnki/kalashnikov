import cv2
import numpy as np


def sharpen_frame(frame):

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened_frame = cv2.filter2D(frame, -1, kernel)
    return sharpened_frame



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    sharpened_frame = sharpen_frame(frame)
    cv2.imshow('Sharpened Frame', sharpened_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
