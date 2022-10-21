import cv2
import numpy as np
def main():
    cam = cv2.VideoCapture(0)
    while True:
        ret,frame = cam.read()
        #crop
        frame=frame[310:410,590:690]
        frame=cv2.cvtColor(frame,cv2.BGR2HSV)
        for x in range(frame):
            for y in range(frame[x]):

        cv2.imshow("name",frame)
        cv2.waitKey(1)
if __name__=='__main__':
    main()
