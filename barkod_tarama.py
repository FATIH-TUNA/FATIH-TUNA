from pyzbar.pyzbar import decode
import cv2
import numpy as np

cam=cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
while True:
    ret,camera=cam.read()
    for barcode in decode(camera):
        mydata=barcode.data.decode("utf-8")
        print(mydata)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        pts2=barcode.rect
        cv2.polylines(camera,[pts],True,(255,0,255),5)
        cv2.putText(camera,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
    cv2.imshow("KAMERA",camera)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
