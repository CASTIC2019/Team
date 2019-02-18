import numpy as np
import cv2
cap1 = cv2.VideoCapture(2)
#cap2 = cv2.VideoCapture(4)
while(True):
    ret1, frame1 = cap1.read()
    #ret2, frame2 = cap2.read()
    res1 = cv2.resize(frame1,(450,150),interpolation=cv2.INTER_CUBIC)
    #res2 = cv2.resize(frame2,(450,150),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('jingyangxiaojidaigong',res1)
    #cv2.imshow('jingyangxiaojidaigo',res2)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap1.release()
#cap2.release()
cv2.destroyAllWindows()
