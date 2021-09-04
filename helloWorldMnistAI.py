'''
Created on 29.06.2021

@author: D028650
'''

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adam
#from deeplearning2020 import helpers
from PIL import Image
#from tensorflow.examples.tutorials.mnist import input_data


if __name__ == '__main__':
    data = keras.datasets.mnist 
    (train_images, train_labels), (test_images, test_labels) = data.load_data()
    #print("dimensions of train_images: " + str(train_images.ndim))
    
    
    image_index = 1486
    image = np.array(test_images[image_index], dtype='float')
    imageToShow = image.reshape((28, 28))
    plt.imshow(imageToShow, cmap='gray')
    plt.show()

    
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    
    total_classes = 10
    train_vec_labels = keras.utils.to_categorical(train_labels, total_classes)
    test_vec_labels  = keras.utils.to_categorical(test_labels, total_classes)
    
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='sigmoid'), 
        keras.layers.Dense(10, activation='sigmoid')
    ])

    
    model.compile(loss=categorical_crossentropy, # loss='mean_squared_error',
                  optimizer=Adam(), # optimizer='sgd',
                  metrics=['accuracy'])


    # predict with untrained model
    prediction = model.predict(test_images[image_index].reshape(1 , 28, 28))
    print("prediction of image_nine with untrained model")    
    print(prediction)    
    
    
    #eval_loss, eval_accuracy = model.evaluate(test_images, test_vec_labels, verbose=False)
    #print("Model accuracy for test data before training: %.2f" % eval_accuracy)

    model.fit(train_images, train_vec_labels, epochs=1, verbose=True)
    
    eval_loss, eval_accuracy = model.evaluate(test_images, test_vec_labels, verbose=False)
    print("Model accuracy for test data after training: %.2f" % eval_accuracy)
    
    # predict with trained model
    prediction = model.predict(test_images[image_index].reshape(1 , 28, 28))
    print("prediction of image_nine with trained model")    
    print(prediction)    
    #helpers.plot_predictions(model, test_images[:20], labels=test_vec_labels[:20])
    
    print("end of run")
    
