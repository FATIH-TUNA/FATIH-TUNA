import cv2
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
model=load_model(r"C:\Users\acer\Desktop\maske_denetim\new_model.keras")
resim=cv2.imread(r"C:\Users\acer\Desktop\12.jpg")
resim=cv2.resize(resim,(128,128))
resim=np.expand_dims(resim,axis=0)
tahmin=model.predict(resim)
tahmin_sinif=np.argmax(tahmin)
if tahmin_sinif==1:
    tahmin_sinif="maskeli"
else:
    tahmin_sinif="maskesiz"
plt.imshow(resim[0])
plt.title("Tahmin_sinif: {}".format(tahmin_sinif))
plt.show()
