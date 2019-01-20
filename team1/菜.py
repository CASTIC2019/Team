import numpy as np
import cv2
import datetime
# Create a black image
diameter=20
sun=0
c=0
chickenfilename=0
celeryfilename=0
tomatofilename=0
fishballfilename=0
stringbeanfilename=0
pigfilename=0
average=0
number=[]





chessbord=[[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        a=int(x/50)
        b=int(y/50)
        print(a,b) 
        chessbord[b][a]+=1
        chessbord[b][a]%=9
        print(chessbord[b][a])





    
# 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((500,500,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
pic = cv2.imread('20.jpg')
img = cv2.resize(pic, (500, 500), interpolation=cv2.INTER_CUBIC)
imgconst = cv2.resize(pic, (500, 500), interpolation=cv2.INTER_CUBIC)
chicken = cv2.imread('1.jpg')
chicken=cv2.resize(chicken,(50,50), interpolation=cv2.INTER_CUBIC)
rows,cols,channels = chicken.shape
chickengray = cv2.cvtColor(chicken,cv2.COLOR_BGR2GRAY)
celery = cv2.imread('celery.jpg')
celery = cv2.resize(celery,(50,50),interpolation=cv2.INTER_CUBIC)
rows,cols,channels = celery.shape
tomato = cv2.imread('tomato.jpg')
tomato = cv2.resize(tomato,(50,50),interpolation=cv2.INTER_CUBIC)
rows,cols,channels = tomato.shape
fishball = cv2.imread('fishball.jpg')
fishball = cv2.resize(fishball,(50,50),interpolation=cv2.INTER_CUBIC)
rows,cols,channels = fishball.shape
stringbean = cv2.imread('stringbean.jpg')
stringbean = cv2.resize(stringbean,(50,50),interpolation=cv2.INTER_CUBIC)
rows,cols,channels = stringbean.shape
pig = cv2.imread('pig.jpg')
pig = cv2.resize(pig,(50,50),interpolation=cv2.INTER_CUBIC)
rows,cols,channels = pig.shape









        
while(1):
    for a in range (10):
        for b in range(10):
            #imggreen=cv2.rectangle(img,(50*b,50*a),(50*(b+1),50*(a+1)),(0,100,0),-1)
            if chessbord[a][b]==0:
                img[50*b:50*(b+1),50*a:50*(a+1)]=imgconst[50*b:50*(b+1),50*a:50*(a+1)]                
            if chessbord[b][a]==1:
                img_result= cv2.addWeighted(imgconst[50*b:50*(b+1),50*a:50*(a+1)],0.5,chicken,0.5,0)
                img[50*b:50*(b+1),50*a:50*(a+1)]=img_result
            if chessbord[b][a]==2:
                img_result= cv2.addWeighted(imgconst[50*b:50*(b+1),50*a:50*(a+1)],0.5,celery,0.5,0)
                img[50*b:50*(b+1),50*a:50*(a+1)]=img_result
            if chessbord[b][a]==3:
                img_result= cv2.addWeighted(imgconst[50*b:50*(b+1),50*a:50*(a+1)],0.5,tomato,0.5,0)
                img[50*b:50*(b+1),50*a:50*(a+1)]=img_result
            if chessbord[b][a]==4:
                img_result= cv2.addWeighted(imgconst[50*b:50*(b+1),50*a:50*(a+1)],0.5,fishball,0.5,0)
                img[50*b:50*(b+1),50*a:50*(a+1)]=img_result
            if chessbord[b][a]==5:
                img_result= cv2.addWeighted(imgconst[50*b:50*(b+1),50*a:50*(a+1)],0.5,stringbean,0.5,0)
                img[50*b:50*(b+1),50*a:50*(a+1)]=img_result
            if chessbord[b][a]==6:
                img_result= cv2.addWeighted(imgconst[50*b:50*(b+1),50*a:50*(a+1)],0.5,pig,0.5,0)
                img[50*b:50*(b+1),50*a:50*(a+1)]=img_result






                
                
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break




for a in range (10):
    for b in range(10):            
        if chessbord[a][b]==1:
            filename='chicken'+str(a)+str(b)+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
            cv2.imwrite(filename,imgconst[50*b:50*(b+1),50*a:50*(a+1)])
            chickenfilename=chickenfilename+1
        if chessbord[a][b]==2:
            filename='celery'+str(a)+str(b)+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
            cv2.imwrite(filename,imgconst[50*b:50*(b+1),50*a:50*(a+1)])
            celeryfilename=celeryfilename+1
        if chessbord[a][b]==3:
            filename='tomato'+str(a)+str(b)+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
            cv2.imwrite(filename,imgconst[50*b:50*(b+1),50*a:50*(a+1)])
            tomatofilename=tomatofilename+1
        if chessbord[a][b]==4:
            filename='fishball'+str(a)+str(b)+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
            cv2.imwrite(filename,imgconst[50*b:50*(b+1),50*a:50*(a+1)])
            fishballfilename=fishballfilename+1
        if chessbord[a][b]==5:
            filename='stringbean'+str(a)+str(b)+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
            cv2.imwrite(filename,imgconst[50*b:50*(b+1),50*a:50*(a+1)])
            stringbeanfilename=stringbeanfilename+1
        if chessbord[a][b]==6:
            filename='pig'+str(a)+str(b)+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
            cv2.imwrite(filename,imgconst[50*b:50*(b+1),50*a:50*(a+1)])
            pigfilename=pigfilename+1







f=open("食堂.csv",'a',newline='')
#f.write('时间'+','+'鸡'+','+'芹菜'+','+'番茄'+','+'鱼丸'+','+'青豆'+','+'猪肉')
f.write(datetime.datetime.now().strftime('%Y%m%d')+','+str(chickenfilename)+','+str(celeryfilename)+','+str(tomatofilename)+','+str(fishballfilename)+','+str(stringbeanfilename)+','+str(pigfilename))
f.close()













cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
