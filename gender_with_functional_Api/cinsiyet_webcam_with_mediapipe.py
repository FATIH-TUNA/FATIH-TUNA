import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp


model = tf.keras.models.load_model(r"C:\Users\acer\Desktop\modeller\kaggle.keras")
img_height, img_width = 128, 128
class_names = ['female', 'male']

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.6)


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

print("Kamera başlatıldı. 'q' ile çıkabilirsin.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb)

    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            width = int(bbox.width * w)
            height = int(bbox.height * h)

            up_expand = int(height * 0.4)
            side_expand = int(width * 0.2)
            down_expand = int(height * 0.1)

            x1 = max(x - side_expand, 0)
            y1 = max(y - up_expand, 0)
            x2 = min(x + width + side_expand, w)
            y2 = min(y + height + down_expand, h)

            face_crop = frame[y1:y2, x1:x2]
            if face_crop.size == 0:
                continue

            face_resized = cv2.resize(face_crop, (img_width, img_height))
            face_normalized = face_resized / 255.0
            input_data = np.expand_dims(face_normalized, axis=0)

            predictions = model.predict(input_data, verbose=0)
            idx = np.argmax(predictions)
            label = class_names[idx]
            confidence = predictions[0][idx]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"{label} ({confidence * 100:.1f}%)"
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 255, 0), 2)

    cv2.imshow("Canli Tahmin (Yüz+Saç)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
