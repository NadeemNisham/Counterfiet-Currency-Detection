import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import arduino
import utility


# note value is the value of the note as an int or string. Eg: 20,50,100,500,1000,5000
def fake_classifier(note_value):
    # Start the prediction loop
    while True:
        arduino.uv_on()
        # Capture an image from the camera
        if not utility.capture_fake():
            continue
        else:
            frame = cv2.imread("uv.jpg")
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resized = tf.image.resize(rgb, (120, 120))
            # assuming the models are saved in the same file as the python file
            model = keras.models.load_model('../model/weights/fake-' + str(note_value) + '.h5')
            yhat = model.predict(np.expand_dims(resized / 255, 0))
            # returns a string saying real or fake
            if yhat[0] > 0.99:
                arduino.uv_off()
                return 'Real'
            else:
                arduino.uv_off()
                return 'Fake'
