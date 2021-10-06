import cv2

print(cv2.__version__)



camSet='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=0 ! video/x-raw, width=1280, height=720, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink '



cam=cv2.VideoCapture(camSet)

while True:

    _, frame = cam.read()

    cv2.imshow('myCam',frame)

    cv2.moveWindow('myCam',0,0)

    if cv2.waitKey(1)==ord('q'):

        break

cam.release()

cv2.destroyAllWindows()