import cv2

# img = cv2.imread("graf1.png")
img = cv2.imread("orange.jpg")
print(img[100,100]) #this is for printing pixel value at (x,y) in image
img1 = img[0:100,0:100] # this is crop part of the main image, this is the slicing opertor
# shape = 512 Rows , 512 Columns
if img is not None:
    cv2.imshow("Image",img)
    k = cv2.waitKey(0)
    if k == ord('q'):
        cv2.destroyAllWindows()
    if k == ord('s'):
        cv2.imwrite("Orange.png",img)
else:
    print("Invalid Image")
print(img.shape)
