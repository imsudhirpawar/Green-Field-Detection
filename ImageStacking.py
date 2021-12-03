import cv2
import numpy as np

img = cv2.imread("lena.jpg")
print(img.shape)
img1 = cv2.imread("messi5.jpg")
print(img1.shape)
img1 = cv2.resize(img1,(img.shape[0],img.shape[1]))

imgHor = np.hstack((img,img1,img,img1)) #image stacking means horizontly placing imgaes in a single frame
imgVert = np.vstack((img,img1,img,img1))

# cv2.imshow("Lena's Image",img)
cv2.imshow(" Horizontal Stacking", imgHor)
cv2.imshow("Vertical Stacking", imgVert)
cv2.waitKey(0)
cv2.destroyAllWindows()