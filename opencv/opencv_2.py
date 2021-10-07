import cv2
print(cv2.__version__)
width=1280
height=720
flip=2 #0, 2 rotate camera
tnr_mode=2 #noise reduction
#gst-inspect-1.0 videobalance --> adjust contrast, brightness, etc


camSet='nvarguscamerasrc sensor-id=0 ee-mode=1 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=1 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.3 brightness=-.2 saturation=1.2 ! appsink '
#camSet='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#camSet ='v4l2src device=/dev/video1 ! video/x-raw,width='+str(width)+',height='+str(height)+',framerate=20/1 ! videoconvert ! appsink'
cam=cv2.VideoCapture(camSet)
while True:
    _, frame = cam.read()
    cv2.imshow('myCam',frame)
    cv2.moveWindow('myCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()