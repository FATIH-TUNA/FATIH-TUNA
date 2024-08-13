from ultralytics import YOLO
import time,math,cv2

pen=cv2.VideoCapture(0)
submask=cv2.createBackgroundSubtractorMOG2()
c=0
classNames={"person":"insan","bicycle":"bisiklet","car":"araba","motorbike":"motorsiklet",
            "aeroplane":"ucak","bus":"otobus","train":"tren","truck":"traktor","boat":"bot","traffic light":"trafik isigi","fire hydrant":"yangin muslugu",
            "stop sign":"stop sinyali","parking meter":"parkmeter","bench":"bank","bird":"kus","cat":"kedi","dog":"kopek",
            "horse":"at","sheep":"koyun","cow":"inek","elephant":"fil","bear":"ayi","zebra":"zebra","giraffe":"zurafa",
            "backpack":"sirt cantasi","umbrella":"semsiye","handbag":"el cantasi","tie":"kiravat","suitcase":"bavul",
            "frisbee":"frizbi","skis":"kayaklar","snowboard":"kar kayagi","sports ball":"spor topu","kite":"ucurtma",
            "baseball bat":"beyzbol sopasi","baseball glove":"beyzbol eldiveni","skateboard":"kaykay","surfboard":"sorf tahtasi",
            "tennis racket":"tenis raketi","bottle":"sise","wine glass":"sarap bardagi","cup":"bardak","fork":"catal",
            "knife":"bicak","spoon":"kasik","bowl":"kase", "banana":"muz", "apple":"elma", "sandwich":"sandvic",
            "orange":"portakal", "broccoli":"brokoli","carrot":"havuc", "hot dog":"sosis", "pizza":"pizza",
            "donut":"tatli corek", "cake":"kek", "chair":"sandalye", "sofa":"kanepe", "pottedplant":"saksi bitkisi",
            "bed":"yatak","diningtable":"yemek masasi", "toilet":"tuvalet", "tvmonitor":"tv monitoru", "laptop":"dizustu bilgisayar",
            "mouse":"fare", "remote":"uzaktan kumanda", "keyboard":"klavye", "cell phone":"cep telefonu",
            "microwave":"mikrodalga firin", "oven":"firin", "toaster":"tost makinasi", "sink":"atmak", "refrigerator":"buz dolabi",
            "book":"kitap", "clock":"saat", "vase":"vazo", "scissors":"makas","teddy bear":"oyucak ayi",
            "hair drier":"sac kurutma makinesi", "toothbrush":"dis fircasi"}
liste=list(classNames)
model=YOLO("yolov8n.pt")
neu_rahmen=0
prev_rahmen=0
while True:
    neu_rahmen=time.time()
    ret,camera=pen.read()
    sonuc=model(camera,stream=True)
    for k in sonuc:
        boxes=k.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            w,h=(x2-x1),(y2-y1)
            conf=math.ceil((box.conf[0]*100))/100
            cls=int(box.cls[0])
            cv2.rectangle(camera,(x1,y1),(w+x1,h+y1),(0,255,100),thickness=2)
            cv2.putText(camera,classNames[liste[cls]],(x1,y1),cv2.FONT_HERSHEY_PLAIN,1,(0,100,200),thickness=2)
    if ret==1:
        fmask=submask.apply(camera)
        cv2.line(camera,(200,0),(200,800),(0,0,200),thickness=2)
        cv2.line(camera,(300,0),(300,800),(0,0,200),thickness=2)
        contours,hiers=cv2.findContours(fmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            (x1,y1,x2,y2)=cv2.boundingRect(contour)
            if x2>400 and y2>410:
                cv2.rectangle(camera,(x1,y1),(x1+x2,y1+y2),(255,255,0),thickness=2)
                if classNames[liste[cls]]=="cep telefonu":
                    c=c+1
        cv2.putText(camera,str(c),(255,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),thickness=2)
    fps=1/(prev_rahmen-neu_rahmen)
    prev_rahmen=neu_rahmen
    print("fps: ",fps)
    cv2.imshow("CAMERA",camera)
    cv2.imwrite("KAYIT_FOTO.jpg",camera)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break
pen.release()
cv2.destroyAllWindows()