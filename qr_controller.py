from cv2 import displayOverlay
from pyfirmata import Arduino, SERVO, boards
import time

port ='COM5'
pin=10
boards= Arduino(port)

boards.digital[pin].mode=SERVO


def rotateServo(pin, angle):
    boards.digital[pin].write(angle)

def doorAutomate(val):
    if val==0:
        rotateServo(pin,95)
        time.sleep(3.0)
        rotateServo(pin,0)
        
    elif val==1:
        rotateServo(pin,0)