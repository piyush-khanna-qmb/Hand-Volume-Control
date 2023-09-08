import cv2
import serial
import math
import mediapipe as mp
import numpy as np

haath = serial.Serial('COM16', baudrate=9600, timeout=0.5)
mpPose= mp.solutions.pose
pose= mpPose.Pose()
mpDraw= mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
width, height= 1020, 720
cap.set(3, width)
cap.set(4, height)
x1=y1=x2=y2= 0
while True:
    success, img= cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c= img.shape
            if id==12:
                x1, y1= int(lm.x * w) , int(lm.y * h)
            if id==16:
                x2, y2= int(lm.x * w) , int(lm.y * h)
            if y2!=0:
                cv2.line(img, (x1,y1), (x2,y2), (125,0,0), 2)
                dist=int(math.hypot(x2-x1, y2-y1))
                # print(dist)
                if 115<dist<430:
                    vol=180- int(0.416 * dist)
                    print(vol)
                    if 20<vol<180:
                        command = f"#1ZZ#2ZZ#3{chr(vol)}Z#4ZZ#5ZZ#6ZZ****"
                        haath.write(command.encode())

            cx= int(lm.x * w)
            cy= int(lm.y * h)
            cv2.circle(img, (cx,cy), 10, (0,0,255), -1)

    cv2.imshow("Hello", img)

    if cv2.waitKey(1) & 0xff== ord('q'):
        cap.release()
        quit()
