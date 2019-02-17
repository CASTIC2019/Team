import numpy as np
import cv2
import random

print(int(random.uniform(0,3)))

cap=cv2.VideoCapture(0)
ret,frame = cap.read()

L=len(frame)
W=len(frame[0])

print(L,W)

SIZE=100


X0=int(W/2-1.5*SIZE)
Y0=int(L/2-1.5*SIZE)

R=int(SIZE/2)

chessboard=[[0,0,0],[0,0,0],[0,0,0]]
print(chessboard)

playsteps=0

#顺序查找空格版本
def AIplayer2():
    for i in range(3):
        for j in range(3):
            if chessboard[i][j]==0:
                chessboard[i][j]=2
                return
#随机数AI版本
def AIplayerR2():
    i=0
    j=0
    trycounter=0
    while(chessboard[i][j]!=0):
        i=int(random.uniform(0,3))
        j=int(random.uniform(0,3))
        trycounter+=1
        if(trycounter>=20):
            break
        print("AIR2 play",i,j)
        if chessboard[i][j]==0:
            chessboard[i][j]=2
            return
    AIplayer2()

#j堵活二版
def AIplayerA2():
    #找竖的2，堵之
    for i in range(3):
        counter1=0
        for j in range(3):
            if chessboard[i][j]==1: 
                counter1+=1
        if counter1==2:
            for j in range(3):
                if chessboard[i][j]==0:
                    chessboard[i][j]=2
                    return

    #找横的2，堵之                    
    for j in range(3):
        counter1=0
        for i in range(3):
            if chessboard[i][j]==1: 
                counter1+=1
        if counter1==2:
            for j in range(3):
                if chessboard[i][j]==0:
                    chessboard[i][j]=2
                    return
    #没有纵横2，则随机下
    AIplayerR2()

                    
def mouse_dclick(event,x,y,flags,param):
    global playsteps
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if x>X0 and y>Y0 and x<(X0+SIZE*3) and y<(Y0+SIZE*3):
            i=int((x-X0)/SIZE)
            j=int((y-Y0)/SIZE)
            if chessboard[i][j]==0:
                player=playsteps%2+1
                print("mc",player)
                chessboard[i][j]=player
                playsteps+=1
                if player==1:
                    player=playsteps%2+1
                    print("mc",player)
                    AIplayerA2()
                    playsteps+=1
 
# 创建图像与窗口并将窗口与回调函数绑定
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse_dclick)

while(True):
    ret,frame = cap.read()
    #画棋盘和棋子
    for i in range(3):
        for j in range(3):
            cv2.rectangle(frame,(i*SIZE+X0,j*SIZE+Y0),(i*SIZE+SIZE+X0,j*SIZE+SIZE+Y0),(255,128,255),2)
            if chessboard[i][j]==1:
                cv2.circle(frame,(i*SIZE+X0+R,j*SIZE+Y0+R),R,(255,0,0),-1)
            elif chessboard[i][j]==2:
                cv2.circle(frame,(i*SIZE+X0+R,j*SIZE+Y0+R),R,(255,0,0),3)

    cv2.imshow('frame',frame)

    #判断输赢，检查每行
    winner=0
    for i in range(3):
        counter1=0
        counter2=0
        for j in range(3):
            if chessboard[i][j]==1:
                counter1+=1
            elif chessboard[i][j]==2:
                counter2+=1
        if counter1==3:
            winner=1
            break
        elif counter2==3:
            winner=2
            break
    
    if winner !=0:
        print("winner=",winner)
        break
    # 判断输赢，坚持每列
    for j in range(3):
        counter1=0
        counter2=0
        for i in range(3):
            if chessboard[i][j]==1:
                counter1+=1
            elif chessboard[i][j]==2:
                counter2+=1
        if counter1==3:
            winner=1
            break
        elif counter2==3:
            winner=2
            break
        
    if winner !=0:
        print("winner=",winner)
        break

    # 判断输赢，检查对角线。
    counter1=0
    counter2=0
    for j in range(3):
        if chessboard[j][j]==1:
            counter1+=1
        elif chessboard[j][j]==2:
            counter2+=1
    if counter1==3:
        winner=1
    elif counter2==3:
        winner=2
    if winner !=0:
        print("winner=",winner)
        break

    # 判断输赢，检查对角线。
    counter1=0
    counter2=0
    for j in range(3):
        if chessboard[j][2-j]==1:
            counter1+=1
        elif chessboard[j][2-j]==2:
            counter2+=1
    if counter1==3:
        winner=1
    elif counter2==3:
        winner=2
    if winner !=0:
        print("winner=",winner)
        break

    if cv2.waitKey(1000)&0xFF==ord('q'):
        break

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(frame,'Winnner '+str(winner),(160,70), font, 2,(255,255,255),4)
cv2.imshow("frame",frame)
cv2.waitKey(5000)
cap.release()
cv2.destroyAllWindows()
