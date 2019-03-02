import numpy as np
import cv2
w = cv2.imread('umbrella.jpg')
rd = cv2.imread('rd.jpg')
w = cv2.resize(w,(100,100),interpolation=cv2.INTER_CUBIC)
w[0:15,0:10]=rd[0:15,0:10]
w[0:15,15:25] = rd[0:15,0:10]
w[0:15,30:40] = rd[0:15,0:10]
cv2.imshow('hi',w)


