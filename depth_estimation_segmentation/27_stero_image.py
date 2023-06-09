# Render camera frame in a window

import cv2
import numpy

clicked = False
window_name = "My window"
global gFrame
global imgCount
imgCount = 0

def onMouse(event, x, y, flags, param):
    global clicked
    global imgCount
    if event == cv2.EVENT_MOUSEMOVE:
        print("Mouse MOVED")
        print(flags, param)
        clicked = True
    
    if event == cv2.EVENT_LBUTTONUP:
        print("Mouse left button released!")
        name = "webcam"+str(imgCount)+".png"
        imgCount += 1
        cv2.imwrite(name, gFrame)
        

#    EVENT_MOUSEMOVE     = 0,
#    EVENT_LBUTTONDOWN   = 1,
#    EVENT_RBUTTONDOWN   = 2,
#    EVENT_MBUTTONDOWN   = 3,
#    EVENT_LBUTTONUP     = 4,
#    EVENT_RBUTTONUP     = 5,
#    EVENT_MBUTTONUP     = 6,
#    EVENT_LBUTTONDBLCLK = 7,
#    EVENT_RBUTTONDBLCLK = 8,
#    EVENT_MBUTTONDBLCLK = 9,
#    EVENT_MOUSEWHEEL    = 10,
#    EVENT_MOUSEHWHEEL   = 11,

cameraCapture = cv2.VideoCapture(2)

#print(cv2.CAP_V4L2)

print(cameraCapture.isOpened())
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, onMouse, "Any param here..")

print("Showing camera feed. Click window or press any key to stop")

success, frame = cameraCapture.read()
gFrame = frame

while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow(window_name, frame)
    success, frame = cameraCapture.read()
    gFrame = frame

cv2.destroyWindow(window_name)
cameraCapture.release()
