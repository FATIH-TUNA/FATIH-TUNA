import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp

model_path = r"C:\Users\acer\Desktop\maske_kontrol\best_model_maske.keras"
model = tf.keras.models.load_model(model_path)

class_labels = ['maske', 'maskesiz']

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.6)

cap = cv2.VideoCapture(0)
img_size = (128, 128)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_frame)

    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            x_min = int(bbox.xmin * w)
            y_min = int(bbox.ymin * h)
            box_width = int(bbox.width * w)
            box_height = int(bbox.height * h)

            x_min = max(0, x_min)
            y_min = max(0, y_min)
            x_max = min(w, x_min + box_width)
            y_max = min(h, y_min + box_height)
            face_img = frame[y_min:y_max, x_min:x_max]
            if face_img.size == 0:
                continue
            face_resized = cv2.resize(face_img, img_size)
            face_array = np.expand_dims(face_resized / 255.0, axis=0)
            prediction = model.predict(face_array, verbose=0)
            class_idx = np.argmax(prediction)
            confidence = prediction[0][class_idx]
            label = f"{class_labels[class_idx]} ({confidence*100:.1f}%)"

            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(frame, label, (x_min, y_min - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Maske Tespiti - MediaPipe", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()