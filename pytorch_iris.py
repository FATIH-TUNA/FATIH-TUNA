import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from mlxtend.plotting import heatmap
from sklearn.metrics import*

data=sns.load_dataset("iris")
print(data.head())
baslik=data.columns.values.tolist()
print(baslik)

for i,j in enumerate(baslik):
    if data[j].dtype=="object":
        data[j]=LabelEncoder().fit_transform(data[j])
print(data.head())

grf=np.corrcoef(data[baslik].values.T)
corr=heatmap(grf,row_names=baslik,column_names=baslik,figsize=(10,10))
plt.show()
data_np=data.to_numpy()
x=data_np[:,:-1]
y=data_np[:,4:5]

a=plt.hist(y,bins="auto")
plt.show()

x_egitim,x_test,y_egitim,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("x_egitim.dtype: ",x_egitim.dtype)
print("x_test.dtype: ",x_test.dtype)
print("y_egitim.dtype: ",y_egitim.dtype)
print("y_test.dtype: ",y_test.dtype)
print()

x_egitim=x_egitim.astype(np.float32)
x_test=x_test.astype(np.float32)
y_egitim=y_egitim.astype(np.int64)
y_test=y_test.astype(np.int64)
print("x_egitim.dtype: ",x_egitim.dtype)
print("x_test.dtype: ",x_test.dtype)
print("y_egitim.dtype: ",y_egitim.dtype)
print("y_test.dtype: ",y_test.dtype)
print()

x_egitim_pt=torch.from_numpy(x_egitim)
x_test_pt=torch.from_numpy(x_test)
y_egitim_pt=torch.from_numpy(y_egitim)
y_test_pt=torch.from_numpy(y_test)

iris_egitim_list=[(x_egitim_pt[i],y_egitim_pt[i].item()) for i in range(x_egitim.shape[0])]
iris_test_list=[(x_test_pt[i],y_test_pt[i].item()) for i in range(x_test.shape[0])]
print("iris_egitim_list: ")
print(iris_egitim_list)
print()
print("iris_test_list: ")
print(iris_test_list)
batch_size    = 16
learning_rate = 0.003 ## 0.001
N_Epochs      = 4000
epsilon = 0.0001
x_means=x_egitim_pt.mean(0,keepdim=True)
x_deviations=x_egitim_pt.std(0,keepdim=True)+epsilon
print("x_means: ")
print(x_means)
print()
print("x_deviations: ")
print(x_deviations)
print()
all_test_data=x_test.shape[0]

egitim_dl=torch.utils.data.DataLoader(iris_egitim_list,batch_size=batch_size,shuffle=True)
test_dl=torch.utils.data.DataLoader(iris_test_list,batch_size=all_test_data,shuffle=True)
print("egitim_dl: ")
print(egitim_dl)
print()
print("test_dl: ")
print(test_dl)
print()
class deneme(nn.Module):
    def __init__(self,x_means,x_deviations):
        super().__init__()
        self.x_means=x_means
        self.x_deviations=x_deviations
        self.linear1=nn.Linear(4,3)
        self.act1=nn.Sigmoid()
        self.linear2=nn.Linear(3,3)
        self.act2=nn.Softmax(dim=1)
        self.dropout=nn.Dropout(0.25)
    def forward(self,x):
        x=self.linear1(x)
        x=self.act1(x)
        x=self.linear2(x)
        y_pred=self.act2(x)
        return y_pred
def baslik(N_Epochs,model,loss_fn,opt):
    for epoch in range(N_Epochs):
        for xb,yb in egitim_dl:
            y_pred=model(xb)
            loss=loss_fn(y_pred,yb)
            opt.zero_grad()
            loss.backward()
            opt.step()
        if epoch%50==0:
            print(epoch,"loss: ",loss)
model=deneme(x_means,x_deviations)
opt=torch.optim.Adam(model.parameters(),lr=learning_rate)
loss_fn=nn.CrossEntropyLoss()
baslik(N_Epochs,model,loss_fn,opt)
def olcumler(y_test,y_pred):
    print("Accuracy: %.2f"%accuracy_score(y_test,y_pred))
    confmat=confusion_matrix(y_true=y_test,y_pred=y_pred)
    print("Confusio Matrix: ")
    print(confmat)
    print("Precision: %.2f"%precision_score(y_true=y_test,y_pred=y_pred,average="weighted"))
with torch.no_grad():
    for x_real,y_real in test_dl:
        y_pred=model(x_real)
        degerler,veriler=torch.max(y_pred,dim=1)
        tahminler=veriler
        olcumler(y_real,tahminler)
