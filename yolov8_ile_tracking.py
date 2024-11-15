import cv2
from ultralytics import YOLO
import numpy as np
import dlib,face_recognition
import winsound
cap=cv2.VideoCapture(0)
model=YOLO("yolov8n.pt")
while True:
    ret,camera=cap.read()
    sonuc=model.track(camera,verbose=False)[0]
    bboxes=np.array(sonuc.boxes.data.tolist(),dtype="int")
    for box in bboxes:
        x1,y1,x2,y2,track_id,score,class_id=box
        if class_id==0:
            cv2.rectangle(camera,(x1,y1),(x1+x2,y1+y2),(100,0,255),2)
            cv2.putText(camera,"person",(x1,y1),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
            winsound.Beep(1500,2000)
            cv2.imwrite("KAYIT.jpg",camera)
    cv2.imshow("KAMERA",camera)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()