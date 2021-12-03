import cv2

cap = cv2.VideoCapture(0)

# video properties
width = int(cap.get(3))
height = int(cap.get(4))
brightness = int(cap.get(10))
print(width,height,brightness)

while True:
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert color

    cv2.imshow("My Fram",frame)  #original video
    #cv2.imshow("My Fram", gray) # colored converted video here grayscale

    k = cv2.waitKey(1) #&0xFF # we didnt use zero bcoz there is a single image only if you use 0
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()