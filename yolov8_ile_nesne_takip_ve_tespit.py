import cv2
from ultralytics import YOLO
import numpy as np
import dlib,face_recognition
import winsound

veri=str(input("\nTANINACAK KISI ADI GIRINIZ: "))
sahis=r"C:\Users\LENOVO\Desktop\fotograflar\\"+veri+".jpg"
deneme=face_recognition.load_image_file(sahis)
dene=face_recognition.face_encodings(deneme)[0]
detector=dlib.get_frontal_face_detector()
model=YOLO("yolov8n.pt")
cap=cv2.VideoCapture(0)

while True:
    ret,camera=cap.read()
    camera = cv2.resize(camera, (1300, 1000))
    result = model.track(camera, verbose=False)[0]
    liste=list()
    detect=detector(camera)
    boxes = np.array(result.boxes.data.tolist(), dtype="int")

    for ekle in detect:
        x=ekle.left()
        y=ekle.top()
        w=ekle.right()
        h=ekle.bottom()
        liste.append((y,w,h,x))

    face_kod=face_recognition.face_encodings(camera,liste)
    i=0
    for face in face_kod:
        y,w,h,x=liste[i]
        sonuc=face_recognition.compare_faces([dene],face)

        for box in boxes:
            x,y, w, h,track_id, score, class_id = box

            if class_id==0:
                cv2.rectangle(camera,(x,y),(x+w,y+h),(100,100,0),2)
                cv2.putText(camera,"person",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,100,100),2)

            if sonuc[0]==True and class_id==0:
                cv2.rectangle(camera,(x,y),(x+w,y+h),(100,255,255),2)
                cv2.putText(camera,str(veri),(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
                winsound.Beep(1500,2000)

    cv2.imshow("KAMERA",camera)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()