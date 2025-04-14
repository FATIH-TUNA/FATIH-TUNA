import cv2,os
import numpy as np
import pandas as pd
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout,BatchNormalization
from keras.optimizers import Adam
from keras.regularizers import l1_l2
from torch.ao.quantization.utils import activation_dtype
x=np.load(r"C:\Users\acer\Desktop\maske_denetim\veriler.npz")["arr_0"]
y=np.load(r"C:\Users\acer\Desktop\maske_denetim\etiketler.npz")["arr_0"]

y=to_categorical(y,2)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
x_train,x_val,y_train,y_val=train_test_split(x_train,y_train,test_size=0.15,random_state=42)


satir,sutun,katman=x_train.shape[1:]
model=Sequential()

model.add(Conv2D(32,(3,3),activation="relu",padding="same",input_shape=(satir,sutun,katman),kernel_regularizer=l1_l2(0.0001,0.0001)))
model.add(BatchNormalization())

model.add(Conv2D(32,(3,3),activation="relu",padding="same",kernel_regularizer=l1_l2(0.0001,0.0001)))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))

model.add(Conv2D(128,(3,3),activation="relu",kernel_regularizer=l1_l2(0.0001,0.0001)))
model.add(BatchNormalization())
model.add(Dropout(0.35))

model.add(Flatten())

model.add(Dense(256,activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(512,activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(2,activation="softmax"))
model.compile(optimizer=Adam(0.0001),loss="categorical_crossentropy",metrics=["accuracy"])
cikti=model.fit(x_train,y_train,validation_data=(x_val,y_val),epochs=30,verbose=0)
model.save(r"C:\Users\acer\Desktop\maske_denetim\new_model.keras")

