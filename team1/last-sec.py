import serial
import serial.tools.list_ports
import time,datetime
import cv2
ports = list(serial.tools.list_ports.comports())
print (ports)
SIZE = 6
cap=cv2.VideoCapture(0)
i=0
def photo():
    now = time.strftime("%Y%m%d%H%M%S")
    ret,frame = cap.read()
    #cv2.namedWindow("img",0)
    #cv2.resizeWindow("img",100,200)
    
    k=cv2.waitKey(1)
    #time.sleep(1)
    cv2.imwrite('/home/pi/Desktop/photo/'+now+'.jpg',frame)
    #i+=1
    
    
for p in ports:
    print (p[1])
    if "Serial" in p[1] or "ttyUSB" in p[1]:
        ser=serial.Serial(port=p[0])
        print(ser)
    else :
        
        print ("No Arduino Device was found connected to the computer")
while(True):
    now = time.strftime("%Y%m%d%H%M%S")
    ret,frame = cap.read()
    
    for i in range(10):
        cv2.namedWindow("img",0)
        cv2.resizeWindow("img",600,400)
        cv2.imshow("img",frame)
        k=cv2.waitKey(1)
        i+=1
    resp=ser.read()
    rs=str(resp)
    print(rs)
    if 'a' in rs:
        #photo()
        cv2.imwrite('/home/pi/Desktop/photo/'+now+'.jpg',frame)
        ser.write("b".encode())
        i=0
        #time.sleep(2)
cap.release()
cv2.destroyAllWindows()   

