import cv2
import numpy as np
import time
from adafruit_servokit import ServoKit
print(cv2.__version__)
timeMark=time.time()
dtFIL=0
 
kit=ServoKit(channels=16)
 
tilt=90
pan=90
dTilt=10
dPan=1
 
kit.servo[0].angle=pan
kit.servo[1].angle=tilt

 
width=720
height=480
flip=2
font=cv2.FONT_HERSHEY_SIMPLEX
camSet1='nvarguscamerasrc sensor-id=0 ee-mode=1 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.3 brightness=-.2 saturation=1.2 ! appsink drop=True'
cam1=cv2.VideoCapture(camSet1)
while True:
    _, frame1 = cam1.read()
    dt=time.time()-timeMark
    timeMark=time.time()
    dtFIL=.9*dtFIL + .1*dt
    fps=1/dtFIL
    cv2.rectangle(frame1,(0,0),(150,40),(0,0,255),-1)
    cv2.putText(frame1,'fps: '+str(round(fps,1)),(0,30),font,1,(0,255,255),2)
    print('fps: ',fps)
    cv2.imshow('myCam1',frame1)
    cv2.moveWindow('comboCam',0,450)
    kit.servo[0].angle=pan

    pan=pan+dPan
    if pan>=179 or pan<=1:
        dPan=dPan*(-1)
        tilt=tilt+dTilt
        kit.servo[1].angle=tilt

        if tilt>=169 or tilt<=11:
            dTilt=dTilt*(-1)
    if cv2.waitKey(1)==ord('q'):
        break
cam1.release()
cv2.destroyAllWindows()