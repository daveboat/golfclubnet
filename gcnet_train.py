# -*- coding: utf-8 -*-
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Flatten, MaxPooling2D, Conv2D, Dropout
from keras.callbacks import EarlyStopping

batchsize=32
steps=667//batchsize + 1

train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'data\\train',
        target_size=(28, 28),
        batch_size=batchsize,
        shuffle=True)

model=Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28,28, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

es = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)

model.fit_generator(
        train_generator,
        epochs=50,
        steps_per_epoch=steps,
        callbacks=[es])

model.save('gcnet_trained.h5')