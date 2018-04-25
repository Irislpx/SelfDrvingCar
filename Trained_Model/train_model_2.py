import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow
from keras.models import Sequential
from keras.callbacks import EarlyStopping

from keras.optimizers import Adam, SGD
from keras.callbacks import ModelCheckpoint
from keras.callbacks import TensorBoard
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from keras.models import Model, Input
from keras.models import load_model
import glob
import os
import h5py
import sys
import keras

np.random.seed(0)

IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 120, 160, 3
INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)

def load_data():
	image_array = np.zeros((1,120,160,3))
	label_array = np.zeros((1,5), 'float')
	training_data = glob.glob('training_data_npz/*.npz')

	if not training_data:
		print("No training data in direcroty, exit check line 29")
		sys.exit()

	for single_npz in training_data:
		with np.load(single_npz) as data:
			print('data.keys = ', data.keys())
			train_temp = data['train_imgs']
			# print('line36 train_temp.shape = ', np.shape(train_temp))
			train_labels_temp = data['train_labels']
			# print('line38 train_labels_temp.shape = ', np.shape(train_labels_temp))

		# print('line37 ---- image_array.shape = ', np.shape(image_array))
		# print('line38 ---- label_array.shape = ', np.shape(label_array))
		image_array = np.vstack((image_array, train_temp))
		label_array = np.vstack((label_array, train_labels_temp))
		print('line41 ---- image_array.shape = ', np.shape(image_array))
		print('line42 ---- label_array.shape = ', np.shape(label_array))

	X = image_array[1:, :]
	y = label_array[1:, :]


	# X = image_array[1:, :]
	# y = label_array[1:, :]


	print('Image array shape = ', X.shape)
	print('Label array shape = ', y.shape)
	print('line 44 mean = ', np.mean(X))
	print('line 45 var = ', np.var(X))

	X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size = 0.2, random_state = 0)

	return X_train, X_valid, y_train, y_valid

def build_model(keep_prob):

	model = Sequential()
	# model.add(Lambda(lambda x: (x/102.83-1), input_shape = INPUT_SHAPE))
	model.add(Conv2D(24, (5, 5), activation = 'elu', input_shape = INPUT_SHAPE, strides = (2, 2)))
	model.add(Conv2D(36, (5, 5), activation = 'elu', strides = (2, 2)))
	model.add(Conv2D(48, (5, 5), activation = 'elu', strides = (2, 2)))

	model.add(Dropout(0.5))

	model.add(Conv2D(64, (3, 3), activation = 'elu'))

	model.add(Dropout(0.9))
	model.add(Flatten())
	model.add(Dense(500, activation = 'elu'))

	model.add(Dropout(0.1))

	model.add(Dense(250, activation = 'elu'))

	model.add(Dropout(0.1))

	model.add(Dense(50, activation = 'elu'))
	model.add(Dropout(0.1))

	model.add(Dense(5, activation = 'elu'))

	model.summary()


	return model



def train_model(model,learning_rate,np_epoch,samples_per_epoch,batch_size,X_train,X_valid,y_train,y_valid):
	# chechpoint=ModelCheckpoint('model-{epoch:03d}.h5',monitor='val_loss',verbose=0,save_best_only=True,mode='min')
	checkpoint=ModelCheckpoint('model-{epoch:03d}.h5',monitor='val_loss',verbose=0,save_best_only=True,mode='min')

	early_stop=EarlyStopping(monitor='val_loss',min_delta=.0005,patience=4,verbose=1,mode='min')
	tensorboard=TensorBoard(log_dir='./logs',histogram_freq=0,batch_size=20,write_graph=True,write_grads=True,write_images=False,embeddings_freq=0,embeddings_layer_names=None,embeddings_metadata=None)
	model.compile(loss='mean_squared_error',optimizer=Adam(lr=learning_rate),metrics=['accuracy'])
	model.fit_generator(batch_generator(X_train,y_train,batch_size),
					steps_per_epoch=samples_per_epoch/batch_size,
					epochs=np_epoch,
					max_queue_size=1,
					validation_data=batch_generator(X_valid,y_valid,batch_size),
					validation_steps=len(X_valid)/batch_size,
					callbacks=[tensorboard,checkpoint,early_stop],
					verbose=2)


def batch_generator(X, y, batch_size):
	images = np.empty([batch_size, IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS])
	steers = np.empty([batch_size, 5])
	while True:
		i = 0
		for index in np.random.permutation(X.shape[0]):
			images[i] = X[index]
			steers[i] = y[index]
			i += 1
			if i == batch_size:
				break
		yield (images, steers)

def main():
	print('line114', '-' * 30)
	print('Parameters')
	print('line116', '-' * 30)
	keep_prob = 0.5
	learning_rate = 0.0001
	np_epoch = 100
	samples_per_epoch = 3000
	batch_size = 40

	print('keep_prob = ', keep_prob)
	print('learning_rate = ', learning_rate)
	print('np_epoch = ', np_epoch)
	print('samples_per_epoch = ', samples_per_epoch)
	print('batch_size = ', batch_size)

	data = load_data()
	model = build_model(keep_prob)
	train_model(model, learning_rate, np_epoch, samples_per_epoch, batch_size, *data)

if __name__ == '__main__':
	main()


















