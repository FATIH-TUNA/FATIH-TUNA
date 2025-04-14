import cv2
import numpy as np
import os
import pandas as pd

veriler=list()
etiketler=list()
konum=r"C:\Users\acer\Desktop\maske_denetim"
for i in os.listdir(konum):
    for j in os.listdir(konum+"//"+i):
        resim=cv2.imread(os.path.join(konum,i,j))
        resim=cv2.resize(resim,(128,128))
        resim=resim.astype("float32")
        resim=resim/255.0
        veriler.append(resim)
        if i=="maskeli":
            etiketler.append(1)
        else:
            etiketler.append(0)
veriler=np.array(veriler)
etiketler=np.array(etiketler)
np.savez(r"C:\Users\acer\Desktop\maske_denetim\veriler.npz",veriler)
np.savez(r"C:\Users\acer\Desktop\maske_denetim\etiketler.npz",etiketler)
