import tensorflow as tf
from numpy import*
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

img_height,img_width=128,128
epoch=30
batch_size=32
data_dir=r"C:\Users\acer\Desktop\new_cinsiyet\Training"

image_datagen=ImageDataGenerator(rescale=1./255,validation_split=0.2,horizontal_flip=True,rotation_range=20,
                                 zoom_range=0.1,height_shift_range=0.1,width_shift_range=0.1)
train_generator=image_datagen.flow_from_directory(data_dir,target_size=(img_height,img_width),
                                                  class_mode="categorical",subset="training")
val_generator=image_datagen.flow_from_directory(data_dir,target_size=(img_height,img_width),
                                                class_mode="categorical",subset="validation")
num_class=len(train_generator.class_indices)
inputs=Input(shape=(img_height,img_width,3))

x=Conv2D(32,(3,3),activation="relu")(inputs)
x=MaxPooling2D(pool_size=(2,2))(x)

x=Conv2D(64,(3,3),activation="relu")(x)
x=MaxPooling2D(pool_size=(2,2))(x)

x=Conv2D(128,(3,3),activation="relu")(x)
x=MaxPooling2D(pool_size=(2,2))(x)
x=Flatten()(x)
x=Dense(128,activation="relu")(x)
x=Dropout(0.5)(x)
outputs=Dense(num_class,activation="softmax")(x)
model=Model(inputs=inputs,outputs=outputs)

model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

callbacks = [
    EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
    ModelCheckpoint("best_model.keras", monitor='val_loss', save_best_only=True)
]

history=model.fit(train_generator,validation_data=val_generator,epochs=epoch,callbacks=callbacks)

model.save(r"C:\Users\acer\Desktop\modeller\kaggle.keras")

