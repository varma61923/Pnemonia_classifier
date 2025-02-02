from keras.models import Sequential
from keras.layers import Dense
from keras.layers import MaxPooling2D
from keras.layers import Convolution2D
from keras.layers import Flatten

classifier=Sequential()


classifier.add(Convolution2D(32,4,4,input_shape=(100,100,3),activation='relu'))
classifier.add(MaxPooling2D(3,3))

classifier.add(Convolution2D(32,4,4,input_shape=(100,100,3),activation='relu'))
classifier.add(MaxPooling2D(3,3))

classifier.add(Flatten())

classifier.add(Dense(output_dim=128,activation='relu'))
classifier.add(Dense(output_dim=1,activation='sigmoid'))

classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('train',
                                                 target_size = (100, 100),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('test',
                                            target_size = (100, 100),
                                            batch_size = 32,
                                            class_mode = 'binary')

classifier.fit_generator(training_set,
                         samples_per_epoch = 8000,
                         nb_epoch = 50,
                         validation_data = test_set,
                         nb_val_samples = 2000)

classifier.save_weights('phnemonia_wights.h5')
classifier.save('my_model.h5')