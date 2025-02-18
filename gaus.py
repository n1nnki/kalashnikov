import cv2


def denoise_frame(frame):
    denoised_frame = cv2.medianBlur(frame, 5)
    return denoised_frame


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    denoised_frame = denoise_frame(frame)
    cv2.imshow('Denoised Frame', denoised_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
