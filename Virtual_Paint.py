import cv2
import numoy as np
# `frameWidth` is a variable that stores the desired width of the video frame. It is used to set the width of the video capture using the `cap.set(3, frameWidth)` function.
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)
    
    
    
    
while True:
    success , img = cap.read()
    cv2.imshow("Results",img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break