from keras.layers import Dense, GlobalAveragePooling2D, Conv2D, MaxPooling2D,Dropout
from keras.layers import Flatten,BatchNormalization
from keras import backend as K
from keras import optimizers
from keras.models import Sequential
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import load_training
import load_test
import cd_model
import write_submission


def main():

	img_mat_train = []
	labels_train = []
	test = []
	
	img_mat_train,labels_train = load_training()

	model1 = cd_model()
	sgd = keras.optimizers.SGD(lr=0.0001,momentum=0.9)
	model1.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['accuracy'])
	reduce_lr = keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=4)
	model1.fit(np.asarray(img_mat_train), np.asarray(labels_train), callbacks=[reduce_lr], batch_size = 64, epochs = 50)
	 
	test = load_test()
 	prediction = model1.predict(np.asarray(test))
 	predec = []
	pred = np.asarray(prediction)
	for pub in pred:
  		tep = np.around(pub,decimals=1)
  		predec.append(tep)
  	predec = [np.around(x[0],decimals=1) for x in prediction]
	f_store = []
	for per in test_img:
  		f_store.append((per)[5:])
	f_store = [x[:-4] for x in f_store]
	sub = write_submission(f_store,pred)

 	test_model()




main()