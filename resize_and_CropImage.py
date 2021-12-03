import cv2
import numpy as np

img = cv2.imread("lena.jpg")
print(img.shape)
# resize
# resizeImage = cv2.resize(img,(255,255))

# Cropping
# imgCropped = img[248:280,248:370]

cv2.imshow("Original Lena's Image", img)
# cv2.imshow("Resized Lena's Image", resizeImage) #resized Image
# cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(3000)
cv2.destroyAllWindows()