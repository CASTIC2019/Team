import numpy as np
import cv2
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import serial
import serial.tools.list_ports
import time
global cn
ports = list(serial.tools.list_ports.comports())
ser=serial.Serial('/dev/ttyACM0',9600)
fullclk = False
clothclk = False
hatclk = False
pantsclk = False
resp=urlopen('http://www.weather.com.cn/weather/101020100.shtml')
soup=BeautifulSoup(resp,'html.parser')
tagDate=soup.find('ul', class_="t clearfix")
dates=tagDate.h1.string
tagToday=soup.find('p', class_="tem") 
try:
    temperatureHigh=tagToday.span.string
except AttributeError as e:
    temperatureHigh=tagToday.find_next('p', class_="tem").span.string
temperatureLow=tagToday.i.string
weather=soup.find('p', class_="wea").string
tagWind=soup.find('p',class_="win")
winL=tagWind.i.string
print(weather)
xcoord = 0
ycoord = 0
cutdates = dates[0:2]
cutwindlevel = winL[0:2]
cuttempL = temperatureLow[0:1]
cuttempH = temperatureHigh[0:2]
if weather[0] == '晴':
    weather = 'clear'
elif weather[1] == '雨' or weather[1] == '雨':
    weather = 'rain'
elif weather[0] != '晴' and weather[0] != '雨' and weather[1] != '雨':
    weather = 'cloudy'
if weather == 'clear':
    w = cv2.imread('sun.jpg')
elif weather == 'rain':
    w = cv2.imread('umbrella.jpg')
    rd = cv2.imread('rd.jpg')
    w = cv2.resize(w,(100,100),interpolation=cv2.INTER_CUBIC)
    w[0:15,0:10]=rd[0:15,0:10]
    w[0:15,15:25] = rd[0:15,0:10]
    w[0:15,30:40] = rd[0:15,0:10]
    
elif weather == 'cloudy':
    w = cv2.imread('cloudy.jpg')
cn = random.randint(1,2)
pn = random.randint(1,2)
hn = random.randint(1,2)
hc = 0
cc = 0
pc = 0
def clickdetector(event,x,y,flags,param):
    global fullclk
    global hatclk
    global clothclk
    global pantsclk
    if event==cv2.EVENT_LBUTTONDBLCLK:
        fullclk = True
    if event==cv2.EVENT_LBUTTONDOWN:
        xcoord = x
        ycoord = y
        if 90<ycoord<180:
            if hn == 1:
                hc = 'A'
            if hn == 2:
                hc = 'B'
            if cn == 1:
                cc = 'C'
            if cn == 2:
                cc = 'D'
            if pn == 1:
                pc = 'E'
            if pn == 2:
                pc = 'F'
            print(hc,cc,pc)
            ser.write(hc.encode())
            cv2.waitKey(10)
            ser.write(cc.encode())
            cv2.waitKey(10000)
            ser.write(pc.encode())

            cv2.waitKey()
        if 230<xcoord<340 and 341<ycoord<459:
            fullclk = 'cloth'
            xcoord = 0
            ycoord = 0
        if 255<xcoord<310 and 460<ycoord<580:
            fullclk = 'pants'
            xcoord = 0
            ycoord = 0
        if 260<xcoord<315 and 258<ycoord<300:
            fullclk = 'hat'
            xcoord = 0
            ycoord = 0
cv2.namedWindow('result')
cv2.setMouseCallback('result',clickdetector)
def xykfullplan(cn,pn,hn):
    face = cv2.imread('face2.jpg')
    pd = cv2.imread('msrc04.jpg')
    cf = "cloth"+str(cn)+".jpg"
    pf = "pants"+str(pn)+".jpg"
    hf = "hat"+str(hn)+".jpg"
    cloth = cv2.imread(cf)
    pants = cv2.imread(pf)
    hat = cv2.imread(hf)
    res1 = cv2.resize(cloth,(200,200),interpolation=cv2.INTER_CUBIC)
    res2 = cv2.resize(pants,(200,200),interpolation=cv2.INTER_CUBIC)
    res3 = cv2.resize(hat,(80,80),interpolation=cv2.INTER_CUBIC)
    resw = cv2.resize(w,(100,100),interpolation=cv2.INTER_CUBIC)
    faceres = cv2.resize(face,(120,120),interpolation=cv2.INTER_CUBIC)
    pd[530:640,465:575] = faceres[10:120,10:120]
    res = cv2.resize(pd,(600,800),interpolation=cv2.INTER_CUBIC)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(res,'2019/2/'+cutdates,(100,90), font,0.5,(255,25,0),1)
    cv2.putText(res,cuttempL+'-'+cuttempH+' C',(140,215), font,0.5,(255,25,0),1)
    cv2.putText(res,'bag',(100,700), font,1,(0,0,255),2)
    cv2.putText(res,'red scarves',(100,730), font,1,(0,0,255),2)
    cv2.putText(res,'watch',(100,760), font,1,(0,0,255),2)
    res[335:525,185:385] = res1[10:200,0:200]
    res[500:670,188:388] = res2[30:200,0:200]
    res[220:285,245:325] = res3[5:70,0:80]
    res[95:195,110:210] = resw[0:100,0:100]
    return res
res = xykfullplan(cn,pn,hn)
cv2.imshow('result',res)
cv2.setMouseCallback('result',clickdetector)
def xykclothplan(c,p,h):
    face = cv2.imread('face2.jpg')
    pd = cv2.imread('msrc04.jpg')
    c = random.randint(1,2)
    cf = "cloth"+str(c)+".jpg"
    pf = "pants"+str(p)+".jpg"
    hf = "hat"+str(h)+".jpg"
    c = 1
    cloth = cv2.imread(cf)
    pants = cv2.imread(pf)
    hat = cv2.imread(hf)
    res1 = cv2.resize(cloth,(200,200),interpolation=cv2.INTER_CUBIC)
    res2 = cv2.resize(pants,(200,200),interpolation=cv2.INTER_CUBIC)
    res3 = cv2.resize(hat,(80,80),interpolation=cv2.INTER_CUBIC)
    faceres = cv2.resize(face,(120,120),interpolation=cv2.INTER_CUBIC)
    pd[530:640,465:575] = faceres[10:120,10:120]
    res = cv2.resize(pd,(600,800),interpolation=cv2.INTER_CUBIC)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(res,'dates:'+cutdates,(100,75), font,0.5,(255,25,0),1)
    cv2.putText(res,'wind level:'+cutwindlevel,(100,90), font,0.5,(255,25,0),1)
    cv2.putText(res,'lowest temp:'+cuttempL,(100,105), font,0.5,(255,25,0),1)
    cv2.putText(res,'highest temp:'+cuttempH,(100,120), font,0.5,(255,25,0),1)
    cv2.putText(res,'weather:'+weather,(100,135), font,0.5,(255,25,0),1)
    cv2.putText(res,'please take:',(100,150),font,0.5,(255,25,0),1)
    res[335:525,185:385] = res1[10:200,0:200]
    res[500:670,188:388] = res2[30:200,0:200]
    res[220:285,245:325] = res3[5:70,0:80]
    return res
    return res
while True:
    if fullclk == True:
        cv2.destroyAllWindows()
        cn = random.randint(1,2)
        pn = random.randint(1,2)
        hn = random.randint(1,2)
        res = xykfullplan(cn,pn,hn)
        cv2.imshow('result',res)
        cv2.setMouseCallback('result',clickdetector)
        fullclk = False
    if fullclk == 'cloth':
        cv2.destroyAllWindows()
        cn = random.randint(1,2)
        res = xykfullplan(cn,pn,hn)
        cv2.imshow('result',res)
        cv2.setMouseCallback('result',clickdetector)
        fullclk = False
    if fullclk == 'pants':
        cv2.destroyAllWindows()
        pn = random.randint(1,2)
        res = xykfullplan(cn,pn,hn)
        cv2.imshow('result',res)
        cv2.setMouseCallback('result',clickdetector)
        fullclk = False
    if fullclk == 'hat':
        cv2.destroyAllWindows()
        hn = random.randint(1,2)
        res = xykfullplan(cn,pn,hn)
        cv2.imshow('result',res)
        cv2.setMouseCallback('result',clickdetector)
        fullclk = False
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()

