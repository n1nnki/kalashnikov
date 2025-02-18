import cv2


def process_frame(frame):
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)

    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    edges = cv2.Canny(thresh, 100, 200)

    return blurred, gray, thresh, edges


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Ошибка: Не удалось открыть камеру.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Ошибка: Не удалось получить кадр.")
        break

    blurred, gray, thresh, edges = process_frame(frame)

    cv2.imshow('Original', frame)
    cv2.imshow('Blurred', blurred)
    cv2.imshow('Gray', gray)
    cv2.imshow('Threshold', thresh)
    cv2.imshow('Edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
