import cv2
import numpy as np
def main():
    cam = cv2.VideoCapture(0)
    while True:
        ret,frame = cam.read()
        #crop
        frame=frame[310:410,590:690]
        lower_bound = np.array([0,0,0])   
        upper_bound = np.array([255,100,100])
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(hsv,lower_bound,upper_bound);
        kernel = np.ones((7,7),np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        
        frame=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("name",frame)
        cv2.waitKey(1)
if __name__=='__main__':
    main()
