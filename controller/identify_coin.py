from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import numpy as np
import utility

print(">> Loading model >>")
# Load the saved models
model = load_model("C:\\Users\\yohan\\OneDrive\\Desktop\\models\\latest_coin_InceptionV3.h5")


def predict_value(model):
    # Create a Pandas DataFrame containing the path of the image to predict
    image_path = "coin_to_predict.jpg"
    data = pd.DataFrame({'filename': [image_path]})

    predict_datagen = ImageDataGenerator(rescale=1. / 255)
    predict_generator = predict_datagen.flow_from_dataframe(
        data,
        x_col='filename',
        y_col=None,
        class_mode=None,
        target_size=(512, 512),
        batch_size=1,
        shuffle=False,
        preprocessing_function=lambda x: x / 255.0 - 0.5
    )

    # Make predictions on the image to predict
    predictions = model.predict(predict_generator, steps=len(predict_generator), verbose=1)

    # Convert the predictions to class labels
    predicted_class_index = np.argmax(predictions)

    classes = ["1", "5", "2", "10"]
    value = classes[predicted_class_index]

    return value


value = 0


def main():
    global value
    # Start the prediction loop
    while True:
        # Capture an image from the camera
        if not utility.capture_image("coin_to_predict"):
            continue
        else:
            # Predict the value of the captured image
            value = predict_value(model)
            break


def get_value():
    return value

