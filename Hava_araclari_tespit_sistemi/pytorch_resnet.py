import os,shutil,random

ana_klasor=r"C:\Users\acer\Desktop\resnet_foto"
train_klasor=ana_klasor+r"\train"
val_klasor=ana_klasor+r"\val"
os.makedirs(train_klasor,exist_ok=True)
os.makedirs(val_klasor,exist_ok=True)
siniflar=list()
for isim in os.listdir(ana_klasor):
    if isim!="train" and isim!="val":
        siniflar.append(isim)
for sinif in siniflar:
    kaynak=os.path.join(ana_klasor,sinif)
    train_kaynak=os.path.join(train_klasor,sinif)
    val_kaynak=os.path.join(val_klasor,sinif)
    os.makedirs(train_kaynak,exist_ok=True)
    os.makedirs(val_kaynak,exist_ok=True)

    fotograflar=list()
    for dosya in os.listdir(kaynak):
        uzanti=dosya.lower()
        if uzanti.endswith((".jpg",".jpeg",".png",".bmp")):
            fotograflar.append(dosya)
    random.shuffle(fotograflar)
    toplam=len(fotograflar)
    train_sayisi=int(toplam*0.80)
    train_fotograflar=fotograflar[:train_sayisi]
    val_fotograflar=fotograflar[train_sayisi:]
    print()
    print("SINIF : ",sinif)
    print("TOPLAM : ",toplam)
    print("TRAIN : ",len(train_fotograflar))
    print("VAL : ",len(val_fotograflar))

    for dosya in train_fotograflar:
        ana_kaynak=os.path.join(kaynak,dosya)
        hedef_kaynak=os.path.join(train_kaynak,dosya)
        shutil.copy2(ana_kaynak,hedef_kaynak)

    for dosya in val_fotograflar:
        ana_kaynak=os.path.join(kaynak,dosya)
        hedef_kaynak=os.path.join(val_kaynak,dosya)
        shutil.copy2(ana_kaynak,hedef_kaynak)
print()
print("VERI SETI HAZIRLANDI...")