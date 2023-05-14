import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import utility

model = keras.models.load_model('../model/weights/detect.h5', compile=False)
cap = utility.cap


def detect_note():
    while cap.isOpened():
        _, frame = cap.read()
        resized = tf.image.resize(frame, (256, 256))
        yhat = model.predict(np.expand_dims(resized / 255, 0))
        if yhat < 0.5:
            utility.voice_out("Currency detected, now scanning")
            return True
    cv2.destroyAllWindows()
