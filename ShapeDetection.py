import cv2
import numpy as np


def getCountours(img):
    countours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print(counters)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        # print(area)
        cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 3)
        # now we have to check for shape
        peri = cv2.arcLength(cnt,True)  #perimeter of close shapes
        # print(peri)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        print(len(approx))

        x,y,w,h = cv2.boundingRect(approx)
        if len(approx) == 3:
            aspectRatio = w / float(h)
            print(aspectRatio)
            shapeType = "Triangle"
        elif len(approx) == 4:
            aspectRatio = w/float(h)
            print(aspectRatio)
            shapeType = "Rectangle"
        else:
            aspectRatio = w / float(h)
            print(aspectRatio)
            shapeType = "Circle"
        print(shapeType)

img = cv2.imread("shapes.png")
# img = cv2.imread("shape2.jpg")
# img = cv2.imread("shape3.png")

imgContours = img[:]
# firstly we have to detect edges
# FOR DETECTIONG EDGES IMG HAS TO BE IN GRAYSCALE
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)  # ksize must be given as odd
imgCanny = cv2.Canny(imgBlur, 220, 470)
# Contour represents the shape
getCountours(imgCanny)

cv2.imshow("Shape", img)
cv2.imshow("Shape in GrayScale", imgGray)
cv2.imshow("Shape in Blur", imgBlur)
cv2.imshow("Shape in Canny(Edges)", imgCanny)
cv2.imshow("Contour)", imgContours)

cv2.waitKey(0)
cv2.destroyAllWindows()
