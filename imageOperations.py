import cv2
import numpy as np
# image is nothing but numpy matrix

img = cv2.imread("lena.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(img,(7,7),5)
imgBlur = cv2.medianBlur(img,5)
imgCanny = cv2.Canny(imgBlur,200,10)

cv2.imshow("Lena's Image",img)
cv2.imshow("Lena's Image in GrayScale",imgGray)
cv2.imshow("Lena's Image in GaussianBlur/medianBlur",imgBlur)
cv2.imshow("Lena's Canny(Edges) Image",imgCanny)

cv2.waitKey(5000)
cv2.destroyAllWindows()