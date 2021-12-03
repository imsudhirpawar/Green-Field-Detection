import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    height = int(cap.get(4))
    width = int(cap.get(3))

    # make 4 frames of one and show it
    #for this you have to make a canvas and that is possible with the help of numpy
    image = np.zeros(frame.shape,np.uint8)  # you have made a frame containing zeros(black color) and same shape as before we are having in videocapture
    smaller_frame = cv2.resize(frame,(0,0), fx = 0.5, fy = 0.5)
    # image[0:height//2, 0:width//2] = smaller_frame
    # image[height // 2:height, 0:width//2] = smaller_frame   # // means getting div in int
    # image[0:height // 2, width // 2:] = smaller_frame
    # image[height // 2:, width // 2:] = smaller_frame

    # now we have to rotate the frames
    image[0:height // 2, 0:width // 2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    image[height // 2:height, 0:width // 2] = smaller_frame
    image[0:height // 2, width // 2:] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    image[height // 2:, width // 2:] = smaller_frame

    cv2.imshow("My Video", image)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()