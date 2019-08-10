# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:14:50 2019

@author: Daveboat
"""

from keras.models import load_model
from keras.preprocessing import image
import numpy as np

labels=['driver','iron','putter']

model = load_model('gcnet_trained.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

img = image.load_img('testimg.jpg', target_size=(28, 28))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
pred = model.predict(x)
print(pred)
print(labels[np.argmax(pred)])
