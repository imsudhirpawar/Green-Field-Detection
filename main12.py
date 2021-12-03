# you have to process video such that it will detect such frames containning green colour
# then you must segment the video such that it will extract the green colour containning images
# and then you must do image stitching (make one panaromic image of all the images)
# the image that is made through this procedure is the one who contains the green color

# the main part is the deployment of the program on the raspberry pi
# raspberry pi has its unique camera which is usefull for this project
# attarde sir
# vaidya sir has done PHD in image stitching
import cv2

# to read library

img = cv2.imread('lena.jpg')

# if you wanna read image in other modes like colour mode, grayscale mode, etc
# img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)  #grayscale
# img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR) #color mode
# img = cv2.imread('lena.jpg', 0)  #grayscale
# img = cv2.imread('lena.jpg', 1) #color mode
# img = cv2.imread('lena.jpg',cv2.IMREAD_UNCHANGED) #for not changing anything
# img = cv2.imread('lena.jpg',-1) #for not changing anything

# image properties (shape, size, data type)
print(img.shape) #shape
print(img.size) #size
print(img.dtype) #data type

# to show the image
if img is not None:
    cv2.imshow('My Image',img)   #open image as My Image
    #cv2.waitKey(5000) #if you do not use waitkey image will open and will close immediately if you want to open image for infinite time until you close/stops the project so write 0 in th ewaitkey paranthesis
    key = cv2.waitKey(0)
    if key == ord('q'):
        cv2.destroyAllWindows()
else:
    print("Image cannot be read.")
