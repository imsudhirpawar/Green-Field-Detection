import cv2

cap = cv2.VideoCapture('Megamind.avi')

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)

    # to run file in grayscale
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray Video", gray)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()