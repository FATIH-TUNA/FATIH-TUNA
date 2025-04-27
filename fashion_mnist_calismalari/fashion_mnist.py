import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
fashion_mnist=tf.keras.datasets.fashion_mnist.load_data()

(x_train_full,y_train_full),(x_test,y_test)=fashion_mnist
x_train,y_train=x_train_full[:-5000],y_train_full[:-5000]
x_val,y_val=x_train_full[-5000:],y_train_full[-5000:]

print(x_train.shape)
x_train,x_val,x_test=x_train/255.,x_val/255.,x_test/255.
class_names=["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]
print(class_names[y_train[7]])
tf.random.set_seed(42)
model=tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=[28,28]))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(300,activation="relu"))
model.add(tf.keras.layers.Dense(100,activation="relu"))
model.add(tf.keras.layers.Dense(10,activation="softmax"))
print(model.summary())

model.compile(optimizer="sgd",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
history=model.fit(x_train,y_train,epochs=30,validation_data=(x_val,y_val))

model.save(r"C:\Users\acer\Desktop\fashion_mnist_calismalari\fashion_egitim.keras")