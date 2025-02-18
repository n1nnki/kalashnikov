import cv2


def adaptive_color_correction(frame):

    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2Lab)

    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    limg = cv2.merge((cl, a, b))

    corrected_frame = cv2.cvtColor(limg, cv2.COLOR_Lab2BGR)
    return corrected_frame


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    corrected_frame = adaptive_color_correction(frame)
    cv2.imshow('Color Corrected Frame', corrected_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
