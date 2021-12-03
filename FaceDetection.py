import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread("sudhir.jpg")
# img = cv2.imread("sudhir savita.jpeg")
# img = cv2.imread("kiran.png")
# img = cv2.imread("img.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,5)
# print(faces)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)


cv2.imshow("Sudhir", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
