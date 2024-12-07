import os
os.environ ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO
import cv2
import numpy as np


cam=cv2.VideoCapture(0)
model=YOLO("yolov8n.pt")
while True:
    ret,camera=cam.read()
    sonuc=model.track(camera,persist=True,verbose=False)[0]
    bboxes=np.array(sonuc.boxes.data.tolist(),dtype="int")
    for box in bboxes:
        x1,y1,x2,y2,track_id,score,class_id=box
        w,h=(x2-x1),(y2-y1)
        if class_id==0:
            cv2.rectangle(camera,(x1,y1),(x1+w,y1+h),(0,100,150),thickness=2)
            cv2.putText(camera,f"PERSON: {track_id}",(x1,y1),cv2.FONT_HERSHEY_DUPLEX,1,(100,200,100),2)
    cv2.imshow("KAMERA",camera)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()