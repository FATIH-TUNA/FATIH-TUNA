import cv2
import numpy as np
import tensorflow as tf

model=tf.keras.models.load_model(r"C:\Users\acer\Desktop\fashion_mnist_calismalari\fashion_egitim.keras")
class_names=["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]
cam=cv2.VideoCapture(0)
while True:
    ret,camera=cam.read()
    camera=cv2.cvtColor(camera,cv2.COLOR_BGR2GRAY)
    img_resize=cv2.resize(camera,(28,28))

    img_array=np.array(img_resize)/255.0
    img_array=np.expand_dims(img_array,axis=0)

    predictions=model.predict(img_array)
    predicted_class=np.argmax(predictions[0])
    confidence=predictions[0][predicted_class]
    label=f"{class_names[predicted_class]}: {confidence*100:.2f}%"
    cv2.putText(camera,label,(10,30),cv2.FONT_HERSHEY_PLAIN,1,(200,255,10),2)
    print(label)

    cv2.imshow("KAMERA",camera)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()