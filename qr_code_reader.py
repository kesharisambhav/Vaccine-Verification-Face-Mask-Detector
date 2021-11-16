import cv2
import numpy as np
from pyzbar.pyzbar import decode
from qr_controller import doorAutomate

#img = cv2.imread('qrcode.png')
test='Vaccinated'

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,640)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        #control servo
        if myData!=test:
            doorAutomate(1)
        else:
            doorAutomate(0)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))

        cv2.polylines(img, [pts],True,(255,0,255),5)
        
        pts2= barcode.rect
        cv2.putText(img, myData,(pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
       

        

    cv2.imshow('Results', img)
    k=cv2.waitKey(1)

    if k==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()