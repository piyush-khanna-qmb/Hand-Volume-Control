'''Program ka kaam hai overall cam resolution and screen pe window positioning
Ye program me 4 elements henge:
Widthset- Cam... Abe use karke dekhle 
'''
import cv2
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FPS, 30)

width=720
height=500
xPos=0
yPos=0

def WidthSet(value):
    global width
    width=value
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def HeightSet(value):
    global height
    height=value
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def XSet(value):
    global xPos
    xPos=value

def YSet(value):
    global yPos
    yPos=value

cv2.namedWindow("Trackbars")
cv2.createTrackbar("Width:", "Trackbars", width, 1366, WidthSet)
cv2.createTrackbar("Height:", "Trackbars", height, 768, HeightSet)
cv2.createTrackbar("X-axis Control", "Trackbars", xPos, 1366, XSet)
cv2.createTrackbar("Y-axis Control", "Trackbars", yPos, 768, YSet)

while True:
    ignore, frame=cam.read()
    cv2.imshow("Webcam", frame)
    cv2.moveWindow("Webcam",xPos,yPos)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()