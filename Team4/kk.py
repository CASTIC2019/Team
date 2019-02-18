import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
file = open ('/var/www/html/1.html','r' )
k=file.read()
n=0
t=0
if (k[n]>=k[14]):
    print(k[14])
    t=k[14]
    if t!=0:
        RelayPin = 11    # pin11
   
        def setup():
	        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	        GPIO.setup(RelayPin, GPIO.OUT)
	        GPIO.output(RelayPin, GPIO.HIGH)

        def loop():
	    while True:
		    print '...relayd on'
		    GPIO.output(RelayPin, GPIO.LOW)
		    time.sleep(0.5)
		    print 'relay off...'
		    GPIO.output(RelayPin, GPIO.HIGH)
		    time.sleep(0.5)

def destroy():
	GPIO.output(RelayPin, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
