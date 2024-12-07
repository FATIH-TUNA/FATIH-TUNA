import cv2
import numpy as np

cam=cv2.VideoCapture(0)
while True:
    ret,camera=cam.read()
    veri_1=np.float32([[100,100],[289,52],[68,380],[389,297]])
    veri_2=np.float32([[0,0],[380,0],[0,380],[300,300]])
    matrix=cv2.getPerspectiveTransform(veri_1,veri_2)
    dene=cv2.warpPerspective(camera,matrix,(camera.shape[1],camera.shape[0]),flags=cv2.INTER_LINEAR)
    cv2.imshow("KAMERA",camera)
    cv2.imshow("PERSPECTIVE",dene)

    if cv2.waitKey(1)&0xff==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()