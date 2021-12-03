# you have to process video such that it will detect such frames containning green colour
# then you must segment the video such that it will extract the green colour containning images
# and then you must do image stitching (make one panaromic image of all the images)
# the image that is made through this procedure is the one who contains the green color

# the main part is the deployment of the program on the raspberry pi
# raspberry pi has its unique camera which is usefull for this project
# attarde sir
# vaidya sir has done PHD in image stitching
'''
# Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
'''
''' we cannot directly detect perticular color from bgr img
    so we have to convert it first into HSV format
 if you want to detect color you have to fing out the mask for the perticular color and
    then performing some bitwise operations with each pixel then you can get the object of
    image having that pixel
to find out the mask you have to find out the exact value of hue, saturation and 
brightness
you have to change all the HSV values and then you want perticular values that if you applied
that on image then you will get the exact image as you are having in the directry 

'''

import cv2
import numpy as np

def empty(a):
    pass
''' we cannot directly detect perticular color from bgr img
    so we have to convert it first into HSV format
 if you want to detect color you have to fing out the mask for the perticular color and
    then performing some bitwise operations with each pixel then you can get the object of
    image having that pixel
to find out the mask you have to find out the exact value of hue, saturation and 
brightness
you have to change all the HSV values and then you want perticular values that if you applied
that on image then you will get the exact image as you are having in the directry 
        
'''

# creating pallet
cv2.namedWindow("Trackbars")
cv2.createTrackbar('Hue Min',"Trackbars",7,179,empty)  #min hue
cv2.createTrackbar('Hue Max',"Trackbars",29,179,empty)  #max hue
cv2.createTrackbar('Saturation Min',"Trackbars",19,255,empty)  #min saturation
cv2.createTrackbar('Saturation Max',"Trackbars",19,255,empty)  #max saturation
cv2.createTrackbar('Val Min',"Trackbars",114,255,empty)  #min Val
cv2.createTrackbar('Val Max',"Trackbars",255,255,empty)  #max Val

while True:

    img = cv2.imread("lamborghini.png")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # getting the values of max and min HSV using positioning
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    sat_min = cv2.getTrackbarPos('Saturation Min',"Trackbars")
    sat_max = cv2.getTrackbarPos('Saturation Max',"Trackbars")
    val_min = cv2.getTrackbarPos('Val Min',"Trackbars")
    val_max = cv2.getTrackbarPos('Val Max',"Trackbars")

    print(h_min,h_max,sat_min,sat_min,val_min,val_max)

    # creating mask
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    outputImg = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Image", img)
    cv2.imshow("HSV Image", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Output Image", outputImg)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()