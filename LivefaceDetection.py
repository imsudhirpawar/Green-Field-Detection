import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascades/haarcascade_eye.xml') #frontalface_default
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,380)

while cap.isOpened():
    ret, frame = cap.read()
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("frame",frame)
    faces = faceCascade.detectMultiScale(imgGray,1.1,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow("Detecting Faces",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()