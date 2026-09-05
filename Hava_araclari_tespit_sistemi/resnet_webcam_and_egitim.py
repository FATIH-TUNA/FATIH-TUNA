import cv2,os
import torch
import time
from PIL import Image
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torchvision.models import resnet18, ResNet18_Weights,resnet50,ResNet50_Weights
from torch.utils.data import DataLoader

cihaz=torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(cihaz)
ana_klasor=r"C:\Users\acer\Desktop\resnet_foto"
train_yolu=ana_klasor+r"\train"
val_yolu=ana_klasor+r"\val"
transform=transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])
train_dataset=ImageFolder(train_yolu,transform=transform)
val_dataset=ImageFolder(val_yolu,transform=transform)
sinif_sayisi=len(train_dataset.classes)
train_loader=DataLoader(train_dataset,batch_size=32,shuffle=True)
val_loader=DataLoader(val_dataset,batch_size=32,shuffle=True)
weights=ResNet50_Weights.DEFAULT
model=resnet50(weights=weights)
model.fc=torch.nn.Linear(model.fc.in_features,sinif_sayisi)
model.to(cihaz)
hata=torch.nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model.parameters(),lr=0.0001)
epoch_sayisi=10

for epoch in range(epoch_sayisi):
    model.train()
    toplam_loss=0
    toplam=0
    dogru=0
    for images,labels in train_loader:
        images=images.to(cihaz)
        labels=labels.to(cihaz)
        optimizer.zero_grad()
        output=model(images)
        loss=hata(output,labels)
        _, tahmin = torch.max(output, 1)
        loss.backward()
        optimizer.step()
        toplam_loss+=loss.item()
        toplam+=labels.size(0)
        dogru+=(tahmin==labels).sum().item()
    train_accuracy=(100*dogru/toplam)
    model.eval()
    val_toplam=0
    val_dogru=0

    with torch.no_grad():
        for images,labels in val_loader:
            images=images.to(cihaz)
            labels=labels.to(cihaz)
            output=model(images)
            _,tahmin=torch.max(output,1)
            val_toplam+=labels.size(0)
            val_dogru+=(tahmin==labels).sum().item()
    val_accuracy=(100*val_dogru/val_toplam)
    print(f"EPOCH: [{epoch+1}/{epoch_sayisi}]"
          f" LOSS: {toplam_loss/len(train_loader):.4f}"
          f" TRAIN: {train_accuracy:.2f}%"
          f" VAL: {val_accuracy:.2f}%")
torch.save(model.state_dict(),"MY_MODEL.pth")

cam=cv2.VideoCapture(0)
kare_sayisi=0
baslangic_zamani=time.time()

while True:
    ret,camera=cam.read()
    kare_sayisi+=1

    rgb=cv2.cvtColor(camera,cv2.COLOR_BGR2RGB)
    pil_image=Image.fromarray(rgb)
    input_tensor=transform(pil_image).unsqueeze(0).to(cihaz)
    with torch.no_grad():
        output=model(input_tensor)
        probabilities=torch.nn.functional.softmax(output[0],dim=0)
        torch_prob,torch_catid=torch.topk(probabilities,1)
    predicted_label=train_dataset.classes[torch_catid[0].item()]
    confidence=(torch_prob[0].item()*100)
    text=f"{predicted_label}: %{confidence:.2f}"
    if confidence>80:
        cv2.putText(camera,text,(10,30),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
    gecen_zaman=(time.time()-baslangic_zamani)
    fps=kare_sayisi/gecen_zaman
    cv2.putText(camera,f"FPS: {fps:.2f}",(10,50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    cv2.imshow("KAMERA",camera)
    if(cv2.waitKey(1)&0xff==ord('q')): break
cam.release()
cv2.destroyAllWindows()





