from pyfirmata import Arduino, SERVO, boards

port ='COM5'
pin=9
boards= Arduino(port)

boards.digital[pin].mode=SERVO


def rotateServo(pin, angle):
    boards.digital[pin].write(angle)

def doorAutomate(val):
    if val==0:
        rotateServo(pin,180)
    elif val==1:
        rotateServo(pin,40)
