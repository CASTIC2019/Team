import numpy as np
import cv2
img = cv2.imread('13.jpg')
import random
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
import os
import sys
import wave
import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt
import librosa.display
from datetime import datetime
from pyaudio import PyAudio, paInt16
import time


#这是手势识别

#kinkernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
skinkernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

x0 = 510
y0 = 100
height = 400
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

cnt=0
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
    frame = cv2.resize(frame, (800,600))   

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
    
    cnt=cnt+1
    if cnt>15:
        cnt=0
    if cnt==0:
        print(gesture)
        zhifa=gesture

while True:
    a1=input()
    b1=input()
    c1=input()
    

    a=str(a1)+str(b1)+str(c1)
    print(a)
    break

    
    
    
#这时乐谱实现
e=0
p=0
n=0
def abcr(x,y):
    
    cv2.rectangle(img,(x,22+y),(15+x,42+y),(0,0,125),3)
    cv2.imshow('image',img)
    cv2.waitKey(100)
def abcg(x,y):
    
    cv2.rectangle(img,(x,22+y),(15+x,42+y),(0,125,0),3)
    cv2.imshow('image',img)
    cv2.waitKey(100)
for x in range(6):
    for a in range (2):
        for z in range(2):
            b=random.randrange(0, 9, 1)
            if b==5:
                abcr(z*14+a*36+x*77,0)
                p=p+1
            else:
                abcg(z*14+a*36+x*77,0)
                e=e+1
for y in range(4):
    for x in range(7):
        for a in range (2):
            for z in range(2):
                b=random.randrange(0, 9, 1)
                if b==5:
                    abcr(z*14+a*36+x*77,y*63+63)
                    p=p+1
                else:
                    abcg(z*14+a*36+x*77,y*63+63)
                    e=e+1
#以下是综合评分
                    

#可以进行手势识别和综合评分目前无法进行综合评分，乐谱还不能接受外来指令
#只是需要改进



 
class GenAudio(object):
    def __init__(self):
        self.num_samples = 4000    #pyaudio内置缓冲大小
        self.sampling_rate =8000 #取样频率
        self.level = 100         #声音保存的阈值
        self.count_num = 15        #count_num个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
        self.save_length = 5      #声音记录的最小长度：save_length * num_samples 个取样
        self.time_count = 10*6       #录音时间，单位s
        self.voice_string = []
 
     
    #保存文件
    def save_wav(self, filename):
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(self.sampling_rate) 
        wf.writeframes(np.array(self.voice_string).tostring())
        wf.close()
     
     
    def read_audio(self):
        pa = PyAudio() 
        stream = pa.open(format=paInt16, channels=1, rate=self.sampling_rate, input=True, 
                frames_per_buffer=self.num_samples) 
         
        save_count = 0
        save_buffer = [] 
        time_count = self.time_count
 
        while True:
            time_count -= 1
             
            # 读入num_samples个取样
            string_audio_data = stream.read(self.num_samples)     
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype = np.short)
            #计算大于 level 的取样的个数
            large_sample_count = np.sum(audio_data > self.level)
             
            print(np.max(audio_data)),  "large_sample_count=>", large_sample_count
 
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.count_num:
                save_count = self.save_length
            else: 
                save_count -= 1
            if save_count < 0:
                save_count = 0
             
            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = [] 
                    print("Recode a piece of voice successfully!")
                    return True
             
            if time_count == 0: 
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = []
                    print("Recode a piece of voice successfully!")
                    return True
                else:
                    return False
        return True
 
def re_max():
    print(111)
 
 
if __name__ == "__main__":
    r = GenAudio()
    r.read_audio()
    r.save_wav("./test.wav")

re_map=["1c","1c","2d","2d","3e","4f","4f","5g","5g","6a","6a","7b"]
audio_path='test.wav'
def fun1(audio_path):   
    x,sr = librosa.load(audio_path)
    ipd.Audio(x,rate=sr)

    hop_length = 512*8
    chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
    a2=len(chromagram)
    b2=len(chromagram[0])
    print(a2,b2)
    result=[[0]*b2]*a2
    re=[0 for i in range(60)]
   # ret=get_wav_time(audio_path)
    #print(ret)
   
    cnt=0
    for i in range(0,b):
        max=0
        m=0
        
        for j in range(0,a2):
            
            result[j][i]=re_map[j]
            if max < chromagram[j][i]:
                max=chromagram[j][i]
                
                if cnt>10:
                    print(j,i,re[m])
                    re[m]=re_max
                    cnt=0
                m=m+1
    return re

###音频分解为0.5秒一个


class GenAudio(object):
    def __init__(self):
        self.num_samples = 4000    #pyaudio内置缓冲大小
        self.sampling_rate =8000 #取样频率
        self.level = 0.5         #声音保存的阈值
        self.count_num = 0.5       #count_num个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
        self.save_length = 0.5      #声音记录的最小长度：save_length * num_samples 个取样
        self.time_count = 20       #录音时间，单位s
        self.voice_string = []
 
     
    #保存文件
    def save_wav(self, filename):
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(self.sampling_rate) 
        wf.writeframes(np.array(self.voice_string).tostring())
        wf.close()
     
     
    def read_audio(self):
        pa = PyAudio() 
        stream = pa.open(format=paInt16, channels=1, rate=self.sampling_rate, input=True, 
                frames_per_buffer=self.num_samples) 
         
        save_count = 0
        save_buffer = [] 
        time_count = self.time_count
 
        while True:
            time_count -= 1
             
            # 读入num_samples个取样
            string_audio_data = stream.read(self.num_samples)     
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype = np.short)
            #计算大于 level 的取样的个数
            large_sample_count = np.sum(audio_data > self.level)
             
            print(np.max(audio_data)),  "large_sample_count=>", large_sample_count
 
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.count_num:
                save_count = self.save_length
            else: 
                save_count -= 1
            if save_count < 0:
                save_count = 0
             
            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = [] 
                    print("Recode a piece of voice successfully!")
                    return True
             
            if time_count == 0: 
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = []
                    print("Recode a piece of voice successfully!")
                    return True
                else:
                    return False
        return True
 
 
 
 
if __name__ == "__main__":
    r = GenAudio()
    r.read_audio()
    r.save_wav("./test.wav")

re_map=["1c","1c","2d","2d","3e","4f","4f","5g","5g","6a","6a","7b"]
audio_path='test.wav'
def fun1(audio_path):   
    x,sr = librosa.load(audio_path)
    ipd.Audio(x,rate=sr)

    hop_length = 512*8
    chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
    a=len(chromagram)
    b=len(chromagram[0])
    #print(a,b)
    result=[[0]*b]*a

   # ret=get_wav_time(audio_path)
    #print(ret)
   
    cnt=0
    for i in range(b):
        max=0
        resul=''
        for j in range(a):          
            result[j][i]=re_map[j]
            if max < chromagram[j][i]:
                max=chromagram[j][i]
                resul=result[j][i]

                cnt=cnt+1
                if cnt>17:
                    print(result[j][i])
                    cnt=0

            
    return resul
    
 
ohohoh=fun1(audio_path)+gesture
for i in range (0,len(ohohoh)):
    print("最终结果"+ohohoh[i])


#将分解出来的音频传给fun1

print("错误数量:",p)
print("正确数量:",e)
n=e/(p+e)
print("正确率:",n*100,"%")
score2=80
score1=n*100
score3=score1+score2

if score3>=180:
    print("优秀 分数：",score3)
    if score1<90:
        print("您的指法姿势不太标准，请练习，您的指法已经很高超了")
    if score2<90:
        print("您的音不太标准，请练习，您的音准已经很高了")
if 180>score3>=160:
    print("良 分数：",score3)
    if score1<80:
        print("您的指法姿势不好，请多练习")
    if score2<80:
        print("您的音不标准，请多练习")
if score3<160:
    print("还需努力 分数：",score3)
    if score1<70:
        print("您的指法很不好，请多加练习，加油")
    if score2<70:
        print("您的音实在不行，请多加练习，加油")
print("谢谢使用")

























































































                

 



        
    
    







   





             
































