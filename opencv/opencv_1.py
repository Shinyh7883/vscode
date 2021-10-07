import cv2
print(cv2.__version__)

width=800
height=600
flip=2 #0,2 --> rotation of the cam

camSet='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 !nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam = cv2.VideoCapture(camSet)
while True:
    _, frame = cam.read()
    cv2.imshow('mycam', frame)
    cv2.moveWindow('mycam',0,0)
    if cv2.waitKey(1) == ord('q'): #press 'q' to escape
        break
    
cam.release()
cv2.destroyAllWindows()