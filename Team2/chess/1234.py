import numpy as np
import cv2
import random

face_cascade = cv2.CascadeClassifier('C:\chess\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\chess\haarcascade_eye.xml')

#先检测人脸，存到face.jpg中
cap=cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()    
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cv2.imshow('roi_color',roi_color)
            cv2.imwrite('face.jpg',roi_color)
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                
    cv2.imshow('img',img)
    # 按s键保存退出
    if cv2.waitKey(1000)&0xFF==ord('s'):
        break
cv2.destroyAllWindows()
