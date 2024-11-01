import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

data=sns.load_dataset("penguins")
print(data.head())
lb=LabelEncoder()
baslik=data.columns.values.tolist()
print(data.info())
for i,j in enumerate(baslik):
    if data[j].dtype=="object":
        data[j]=lb.fit_transform(data[j])
def fonk(x,y,z):
    plt.figure(figsize=(10,10))
    ax=plt.axes(projection="3d")
    ax.scatter(x,y,c=z,cmap="RdYlBu")
    plt.show()
while True:
    veri_1=str(input("\nBIRINCI VERI GIRINIZ: "))
    veri_2=str(input("\nIKINCI VERIYI GIRINIZ: "))
    kilit_veri=str(input("\nKILIT VERIYI GIRINIZ: "))
    fonk(data[veri_1],data[veri_2],data[kilit_veri])
    cevap=str(input("\nISLEM DEVAM ETSIN MI: ")).upper()
    if cevap=='E':
        continue
    else:
        break