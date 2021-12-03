import cv2
import numpy as np

cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))

while True:
    ret, frame = cap.read()
    # draw line on frame
    # img = cv2.line(frame,(0,0),(width,height),(0,255,0),5)
    # img = cv2.line(img, (width, 0), (0, height), (0, 0, 255), 5)
    # img = cv2.line(img, (0, height//2), (width, height//2), (0, 255, 255), 5)

    # draw rectangle on frame
    # img = cv2.rectangle(frame,(100,100),(300,300),(0,255,255),1)

    # if you want filled rectangle then thickness should be -1
    # img = cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 255), -1)

    # draw circle on frame
    # img = cv2.circle(frame,(400,400),50,(255,255,0),1)

    # draw elips
    # img = cv2.ellipse(frame,(200,200),(200,100),70,0,360,(255,255,0),1)

    # draw text
    img = cv2.putText(frame,'SUDHIR PAWAR',(0,400),cv2.FONT_HERSHEY_COMPLEX,2,(100,100,0),2)
    cv2.imshow(".",img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()