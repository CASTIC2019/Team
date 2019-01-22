import numpy as np
import cv2
import glob
import re

piclist=[]
piclist=glob.glob(r'C:\Users\zhouz\Desktop\*.jpg')
print (piclist)
print(len(piclist))
for filename in piclist:
    print(filename)
    img=cv2.imread(filename)
    cv2.imshow('img',img)
    cv2.waitKey(0)
