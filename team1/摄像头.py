import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.imshow('my_frame',frame)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
