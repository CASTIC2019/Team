import numpy as np
import cv2
cap1 = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(1)
#cap4 = cv2.VideoCapture(4)
while(True):
    ret1, frame1 = cap1.read()
    #ret2, frame2 = cap2.read()
    #ret3, frame3 = cap3.read()
    #ret4, frame4 = cap4.read()
    input_image = np.ones((300,300,3), dtype=np.uint8)
    res1 = cv2.resize(frame1,(300,100),interpolation=cv2.INTER_CUBIC)
    #res2 = cv2.resize(frame2,(300,100),interpolation=cv2.INTER_CUBIC)
    #res3 = cv2.resize(frame3,(300,100),interpolation=cv2.INTER_CUBIC)
    input_image[0:100,0:300] = res1[0:100,0:300]
    #input_image[100:200,0:300] = res2[0:100,0:300]
    #input_image[200:300,0:300] = res3[0:100,0:300]
    #gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    #gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    cv2.imshow('jingyangxiaojidaigong',input_image)
    #cv2.imshow('jingyangxiaojidaqq',frame4)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap1.release()
#cap2.release()
#cap3.release()
#cap4.release()
cv2.destroyAllWindows()