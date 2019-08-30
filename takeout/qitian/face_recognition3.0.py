
import cv2
import time
import serial #导入模块
import serial.tools.list_ports

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
count = 0
count2 = 0
count3 = 0
state = 1
#1 = waiting for food
#2 = food is ready
#3 = dangerous
#4 = got food

ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or"UART" in p[1] or "Arduino" in p[1] :
	    ser=serial.Serial(port=p[0])
	    break
    else :
	    print ("No Arduino Device was found connected to the computer")
time.sleep(5)
'''
def response(inp_data):
    if 'foodready' in inp_data:
        print('food is ready')
        state = 2
'''

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
while state == 1:
    input_data = ser.readline()
    inp_data = str(input_data)
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5) 
    for (x,y,w,h) in faces: 
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 
    
    if len(faces) != 0:
        count += 1
        frame = cv2.circle(frame,(20,20),5,(0,0,255),5)
    else:
        count2 += 1

    if count2 >= 30:
        frame = cv2.circle(frame,(20,20),5,(0,255,0),5)
        print('delivery man is away')
        count = 0
        count2 = 0
        time.sleep(1)
        ser.write('0'.encode()) 
        time.sleep(1) 
        
        if 'foodready' in inp_data:
            print('food is ready')
            state = 2
    elif count >= 30:
        print('alarm')
        count = 0
        count2 = 0
        count3 += 1
        #ser.write('1'.encode())
        time.sleep(1)
              
    elif count3 >= 3:
        print('dangerous situation')
        #ser.write('danger'.encode()) ###############

    print(count2)
    cv2.imshow('img',frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
    time.sleep(.5)

while state == 2:
    input_data = ser.readline()
    inp_data = str(input_data)
    print('come and get your food')
    time.sleep(3)
    if 'something' in inp_data:          ############
        print('user taken the food')
        state = 4
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


while state == 4:
    input_data = ser.readline()
    inp_data = str(input_data)
    #ser.write('gotfood'.encode())        ##########
    if 'something' in inp_data:    ###############
        print('close the cover')
        time.sleep(10)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


cap.release()
cv2.destroyAllWindows()
