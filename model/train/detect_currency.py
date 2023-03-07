import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Dense,Flatten

#0 = have note ,  1 = note
data = tf.keras.utils.image_dataset_from_directory('Data')
data = data.map(lambda x,y:(x/255,y))

train_size = int(len(data)*0.7)
test_size = int(len(data)*0.1)
val_size = int(len(data)*0.2)

train = data.take(train_size)
test = data.skip(train_size).take(test_size)
val = data.skip(train_size+test_size).take(val_size)

logdir = 'logs'
callback = tf.keras.callbacks.TensorBoard(log_dir = logdir)
hist = model.fit(train,epochs = 10,validation_data = val,callbacks = [callback])

model.save('detect.h5')