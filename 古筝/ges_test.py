# coding: utf-8

from keras.models import load_model
from imutils import paths
import numpy as np
import imutils
import cv2
import pickle
import time
import os
import win32api
import win32con
import serial
import binascii
import time



#kinkernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
skinkernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

minValue = 70
x0 = 400
y0 = 200
height = 200
width = 200
flag_next=1         #防止连续切歌
flag_stop=1         #防止连续暂停

count1=0                    #防抖动
count2=0
count3=0
count4=0
count5=0
count6=0

def keybd_event(VK_CODE):
    #VK_CODE为键盘编码
    VK_CODE = int(VK_CODE)
    #按键按下
    win32api.keybd_event(VK_CODE, 0, 0, 0)
    #按键弹起
    #win32api.keybd_event(VK_CODE, 0, win32con.KEYEVENTF_KEYUP, 0)


# #手势处理函数(二值掩模)
# def binaryMask(frame, x0, y0, width, height):
#     global guessGesture, visualize, mod, lastgesture, saveImg
#     cv2.rectangle(frame, (x0,y0),(x0+width,y0+height),(0,255,0),1)
#     roi = frame[y0:y0+height, x0:x0+width]
#     gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray,(5,5),2)
#     th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
#     ret, res = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#     return res


# 使用肤色检测模型
def binaryMask(frame, x0, y0, width, height):
    # HSV values
    low_range = np.array([0, 50, 80])
    upper_range = np.array([30, 200, 255])

    cv2.rectangle(frame, (x0, y0), (x0 + width, y0 + height), (0, 255, 0), 1)
    roi = frame[y0:y0 + height, x0:x0 + width]

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # 设阈值，去除背景部分,低于这个lower_red的值，图像值变为0,高于这个upper_red的值，图像值变为0
    mask = cv2.inRange(hsv, low_range, upper_range)
		
	#腐蚀操作，减少整幅图像的白色区域
    mask = cv2.erode(mask, skinkernel, iterations=1)
	#膨胀操作，增加图像中的白色区域
    mask = cv2.dilate(mask, skinkernel, iterations=1)

    # 用高斯分布权值矩阵与原始图像矩阵做卷积运算
    mask = cv2.GaussianBlur(mask, (15, 15), 1)
    # cv2.imshow("Blur", mask)

    # 图像与运算
    res = cv2.bitwise_and(roi, roi, mask=mask)
    # color to grayscale
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    return res


#模型和标签名
MODEL_NAME = "ss_model.h5"
LABEL_NAME = "ss_labels.dat"


#加载标签
with open(LABEL_NAME, "rb") as f:
    lb = pickle.load(f)

#加载神经网络
model = load_model(MODEL_NAME)


#打开摄像头
cap = cv2.VideoCapture(0)

framecount = 0
fps = ""
#开始时间
start = time.time()
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 3)
    frame = cv2.resize(frame, (640,480))   

    if ret == True:
        roi = binaryMask(frame, x0, y0, width, height)
        
        roi1 = cv2.resize(roi,(100,100))
        # 添加维度
        roi1 = np.expand_dims(roi1, axis=2)
        roi1 = np.expand_dims(roi1, axis=0)
        prediction = model.predict(roi1)
        # 预测手势
        gesture = lb.inverse_transform(prediction)[0]
        cv2.putText(frame,gesture,(100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        #计算帧率
        framecount = framecount + 1
        end  = time.time()
        second = (end - start)
        if( second >= 1):
            fps = 'FPS:%s' %(framecount)
            start = time.time()
            framecount = 0
    #输出fps
    cv2.putText(frame,fps,(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0),2,1)

    #显示摄像头内容和处理后手势的图像内容
    cv2.imshow('Original',frame)          #摄像头内容
    cv2.imshow('ROI', roi)                #手势小框
    print(gesture)

        
#################################切歌#####################################
    if gesture=='next_song':
        count3=count3+1
        if count3==30:
            keybd_event(18)                #ALT+RIGHT
            keybd_event(39) 
                    
        
    elif gesture=='start_stop' and flag_stop==1:
        count4=count4+1
        if count4==30:
            keybd_event(18)                #ALT+numb‘0’
            keybd_event(96)
    key = cv2.waitKey(5) & 0xff
    #Esc键退出
    if key == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
    #手势识别框动态移动
    elif key == ord('i'):
        y0 = y0 - 5
    elif key == ord('k'):
        y0 = y0 + 5
    elif key == ord('j'):
        x0 = x0 - 5
    elif key == ord('l'):
        x0 = x0 + 5
