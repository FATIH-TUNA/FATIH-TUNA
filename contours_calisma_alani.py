import cv2

cam=cv2.VideoCapture(0)

while True:
    ret,camera=cam.read()
    h,w,_=camera.shape
    gray=cv2.cvtColor(camera,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(7,7),3)
    canny=cv2.Canny(blur,100,200)
    t=cv2.getRotationMatrix2D((w/2,h/2),57,1)
    dene=cv2.warpAffine(camera,t,(w,h))
    cv2.imshow("KAMERA",dene)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()