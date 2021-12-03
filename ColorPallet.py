import cv2
import numpy as np


def empty(a):
    pass

img = np.zeros((300, 512, 3), np.uint8) #creating a empty frame
cv2.namedWindow("Image Slider") # naming to the frame

# creating three trackbars
cv2.createTrackbar('Blue', 'Image Slider', 0, 255, empty)
cv2.createTrackbar('Green', 'Image Slider', 0, 255, empty)
cv2.createTrackbar('Red', 'Image Slider', 0, 255, empty)

while True:
    cv2.imshow("Image Slider", img)

    # collectiong values from trackbar positions
    red = cv2.getTrackbarPos("Red","Image Slider")
    blue = cv2.getTrackbarPos("Blue", "Image Slider")
    green = cv2.getTrackbarPos("Green", "Image Slider")

    # putting that values in the frame so we can visualize the color
    img[:] = [blue,green,red]

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
