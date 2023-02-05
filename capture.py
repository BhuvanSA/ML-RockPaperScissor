import time
import cv2
cam = cv2.VideoCapture(0)

path = "./rps/scissor/"

time.sleep(2)
ret,frame = cam.read()
for i in range(1,501):
    ret,frame = cam.read()
    # frame = cv2.resize(frame,(500,500))


    rz = 1080
    x = frame.shape[1] // 2 - (rz//2)
    y = frame.shape[0] // 2 - (rz//2)
    
    # print(frame.shape[1])
    # print(frame.shape[0])
    


    
    frame = frame[y:y+rz,x:x+rz]
    cv2.imshow("jatere",frame)
    cv2.imwrite((path+str(i)+".jpeg"),frame)
    time.sleep(.5)

