import numpy as np
import cv2
import random

cap=cv2.VideoCapure(0)

while(True):
    ret,frame = cap.read()  
    cv2.imshow('imgkdlfjsklfj',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img',gray)
    imgaaa=frame
    imgaaa[0:50,0:50]=frame[100:150,100:150]
    cv2.imshow('imgaaa',imgaaa)
    # 按 键保存退出
    if cv2.waitKey(1000)&0xFF==ord(' '):
        break
cap.release()
cv2.destroyAllWindows()


