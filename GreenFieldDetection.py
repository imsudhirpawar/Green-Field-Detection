
import cv2
import numpy as np

hue_min = 25
sat_min = 52
val_min = 72

hue_max = 102
sat_max = 255
val_max = 255

cap = cv2.VideoCapture(0) # video capturing

while cap.isOpened():
    ret, frame = cap.read()   # original frame

    vidGray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #hsv frame

    # creating mask
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    mask = cv2.inRange(vidGray, lower, upper) #applying mask to the hsv frame

    # bitwise anding to each pixel to get the object
    Green = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Green Field Detection", Green)
    # cv2.imshow("Original Frame", frame) #original video

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()