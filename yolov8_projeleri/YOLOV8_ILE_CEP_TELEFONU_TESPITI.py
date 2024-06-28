from ultralytics import YOLO
import math,time,cv2,winsound
pen=cv2.VideoCapture(0)
model=YOLO("yolov8n.pt")
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
classNamess=list(classNames)
rahmen=0
neu_rahmen=0
while True:
    rahmen=time.time()
    ret,camera=pen.read()
    camera=cv2.resize(camera,(1000,800))
    ergebnisse=model(camera,stream=True)
    for k in ergebnisse:
        boxes=k.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            w,h=(x2-x1),(y2-y1)
            conf=math.ceil((box.conf[0]*100))/100
            cls=int(box.cls[0])
            cv2.rectangle(camera,(x1,y1),(x1+w,y1+h),(0,200,255),thickness=2)
            cv2.putText(camera,classNames[classNamess[cls]],(x1,y1),cv2.FONT_HERSHEY_DUPLEX,1,(255,200,100),thickness=2)
            if classNames[classNamess[cls]]=="cep telefonu":
                winsound.Beep(1500,2000)

    cv2.imshow("DENEME",camera)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break
pen.release()
cv2.destroyAllWindows()