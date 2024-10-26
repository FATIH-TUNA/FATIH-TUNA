def SIRA(x=list(),y=len(list())):
    for i in range(y):
        for j in range(y):
            if(x[i]<x[j]):
                t=x[i]
                x[i]=x[j]
                x[j]=t
def ARA(anah,x=list(),y=len(list())):
    for i in range(len(x)):
        if(x[i]==anah):
            return i
        else:
            print("\nARANAN VERI LISTEDE BULUNAMADI...")
liste=list()
while True:
    sayi=int(input("\nBIR SAYI GIRINIZ: "))
    for k in range(sayi):
        veri=str(input("\nBIR VERI GIRINIZ: "))
        liste.append(veri)
    print(liste)
    print()
    SIRA(liste,len(liste))
    print(liste)
    while True:
        cev=str(input("\nARAMA ISLEMI YAPILSIN MI: ")).upper()
        if cev=='E':
            ara=str(input("\nARANACAK VERIYI GIRINIZ: "))
            f=ARA(ara,liste,len(liste))
            if(f==-1):
                print(ara," VERISI LISTEDE BULUNAMADI...")
            else:
                print(ara," VERISI LISTEDE ",f,". KONUMUNDA BULUNMAKTADIR...")
        else:
            break
    cevap=str(input("\nISLEM DEVAM ETSIN MI: ")).upper()
    if cevap=='E':
        continue
    else:
        break
