import food1dai
import time
import sys
import random
import tkinter as tk
from tkinter import *
import numpy as np
import cv2
import datetime
import re
import tkinter
import urllib.request
import glob

global chickenfilename
global celeryfilename
global tomatofilename
global fishballfilename
global stringbeanfilename
global pigfilename

class App:
    def __init__(self,root):
        frame = tk.Frame(root)
        
        frame.pack()
        self.hi_there = tk.Button(frame, text = '开启--OPEN', bg = 'pink', fg = 'black', command = self.say_hi)
        self.hi_there.pack(side = tk.LEFT)
    def say_hi(self):


        time.sleep(1)
        time.sleep(1)



        
        print('hollow  亲爱的生活委员')
        time.sleep(1)
        print('一天的午餐时间又结束了')
        time.sleep(1)


        root = tk.Tk()
        root.title('中学生午餐厨余垃圾')
        theLabel = tk.Label(root, text = '''                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
——————————请登录！———————————  ——————————请登录！———————————
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
——————————请登录！———————————  ——————————请登录！———————————
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
——————————请登录！———————————  ——————————请登录！———————————
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
|                                                 ||                                                 |
''')
        theLabel.pack()


        
         
        def getHtml(url):
            html = urllib.request.urlopen(url).read()
            return html
         
        def saveHtml(file_name, file_content):
            #    注意windows文件命名的禁用符，比如 /
            with open(file_name.replace('/', '_') + ".html", "wb") as f:
                #   写文件用bytes而不是str，所以要转码
                f.write(file_content)
         
        aurl = "http://www.view.sdu.edu.cn/info/1003/75240.htm"
        html = getHtml(aurl)
        saveHtml("sduview", html)



        top = tkinter.Tk()
        top.geometry('400x170+350+150')
        top.wm_title('中学生午餐厨余垃圾')

        def validateText():
            val = entry1.get()
            if re.findall('^[0-9a-zA-Z_]{1,}$',str(val)):
                return True
            else:
                label3['text'] = '信息提示区'
                return False







        def anw_button():
            if str.upper(entry1.get()) == '生活委员' and str.upper(entry2.get()) =='7535':
                label3['text'] = '登陆成功'
            else:
                label3['text'] = '用户名或密码错误，请重新输入！'

        label1 = tkinter.Label(top,text = '用户名:',font = ('宋体','18'))
        label1.grid(row = 0,column = 0)
        label2 = tkinter.Label(top,text = '密码:',font = ('宋体','18'))#集合为另一种形式的字典
        label2 .grid(row = 1 ,column = 0)
        v = tkinter.StringVar()
        entry1 = tkinter.Entry(top,font = ('宋体','18'),textvariable = v,\
                                validate = 'focusout',validatecommand = validateText)

        entry1.grid(row = 0,column = 1)
        entry1.focus_force()
        entry2 = tkinter.Entry(top,font = ('宋体','18'),show = '*')

        entry2.grid(row = 1,column = 1)
        button1 = tkinter.Button(top,text = '登陆', bg = 'yellow', fg = 'black', font = ('宋体','18'),\
                                 command = anw_button)
        button1.grid(row = 2,column = 0,padx = 50,pady = 10)
        button2 = tkinter.Button(top,text = '退出', bg = 'pink', fg = 'black', font = ('宋体','18'),\
                                 command = sys.exit)

        button2.grid(row = 2,column = 1,padx = 80,pady = 10)
        label3 = tkinter.Label(top,text = '信息提示区', bg = 'red', fg = 'yellow', font = ('华文新魏','16'),\
                               relief = 'ridge',width = 30)
        label3.grid(row = 3,column = 0,padx = 10,pady = 10,columnspan = 2,sticky = 's')
        top.mainloop()
        root.mainloop()


#_____________________________________________________________________________________________________________________________________________________________________________-------------------------------------------------------------------------------------------------------------------------






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
        
root = tk.Tk()
root.title('中学生午餐厨余垃圾')
app = App(root)
root.mainloop()
