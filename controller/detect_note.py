import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

model = keras.models.load_model('../model/weights/detect.h5')
cap = cv2.VideoCapture(0)


def detect_note():
    while cap.isOpened():
        _, frame = cap.read()
        frame = frame[50:500, 50:500, :]
        resized = tf.image.resize(frame, (256, 256))
        yhat = model.predict(np.expand_dims(resized / 255, 0))
        if yhat < 0.5:
            return True
    cap.release()
    cv2.destroyAllWindows()
