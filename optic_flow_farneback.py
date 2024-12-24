import cv2
import numpy as np

cam=cv2.VideoCapture(0)
ret_1,camera_1=cam.read()
gray_1=cv2.cvtColor(camera_1,cv2.COLOR_BGR2GRAY)
mask=np.zeros_like(camera_1)
mask[...,1]=255
while True:
    ret,camera=cam.read()
    gray=cv2.cvtColor(camera,cv2.COLOR_BGR2GRAY)
    basla=cv2.calcOpticalFlowFarneback(gray_1,gray,None,0.5,3,15,3,5,1.2,0)
    deneme,aci=cv2.cartToPolar(basla[...,0],basla[...,1])
    mask[...,0]=aci*180/np.pi/2
    mask[...,2]=cv2.normalize(deneme,None,0,255,cv2.NORM_MINMAX)
    yeni=cv2.cvtColor(mask,cv2.COLOR_HSV2BGR)
    cv2.imshow("KAMERA",camera)
    cv2.imshow("YENI",yeni)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()