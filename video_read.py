import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#0 is default camera

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == False:
        continue
    
    cv2.imshow('video_frame', frame)
    
    if cv2.waitKey(1) & 0xff == ord('x'):
        break
    
cap.release()
cv2.destroyAllWindows()