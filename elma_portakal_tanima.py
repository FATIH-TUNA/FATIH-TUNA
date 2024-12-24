import math
import time
import winsound
import cv2
import cvzone
from ultralytics import YOLO

confidence = 0.5

cap = cv2.VideoCapture(0)  # For Webcam
cap.set(3, 640)
cap.set(4, 480)
# cap = cv2.VideoCapture("../Videos/motorbikes.mp4")  # For Video


model = YOLO(r"C:\Users\acer\PycharmProjects\PythonProject\runs\detect\train3\weights\best.pt")
# model = YOLO("last.pt")

classNames = ["ELMA","PORTAKAL"]

prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    img=cv2.resize(img,(1000,1000))
    results = model(img, stream=True, verbose=False)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            if conf > confidence:
                if(classNames[cls]=="ELMA"):
                    print("ELMA ALGILANDI...")
                    winsound.Beep(1500,200)
                if(classNames[cls]=="PORTAKAL"):
                    print("PORTAKAL ALGILANDI...")
                    winsound.Beep(1500,200)



                if classNames[cls] == 'acik':
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)

                cvzone.cornerRect(img, (x1, y1, w, h),colorC=color,colorR=color)
                cvzone.putTextRect(img, f'{classNames[cls].upper()} {int(conf*100)}%',
                                   (max(0, x1), max(35, y1)), scale=2, thickness=4,colorR=color,
                                   colorB=color)


    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    # print(fps)

    cv2.imshow("Image", img)
    cv2.waitKey(1)