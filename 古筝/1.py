import numpy as np
import cv2
img = cv2.imread('123456789.jpg')
cv2.imshow('image',img)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
print(hsv)
lower_blue=np.array([14,32,0])
upper_blue=np.array([139,50,255])
mask=cv2.inRange(hsv,lower_blue,upper_blue)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()