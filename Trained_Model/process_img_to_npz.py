# -*- coding: utf-8 -*-
# @Author: biying
# @Date:   2017-06-30 10:20:35
# @Last Modified by:   biying
# @Last Modified time: 2017-12-17 18:34:18

import os
os.environ['SDL_VIDEODRIVE'] = 'x11'
import numpy as np
import matplotlib.image as mpimg	
from time import time
import math

def process_img(img_path, key):
	global train_imgs, train_label, image_array, label_array
	print(img_path, key)

	# output = PIL.open(img_path)
	# temp_array = output.array
	# temp_array = np.expand_dims(temp_array,axis = 0)
		
	temp_array = mpimg.imread(img_path)
	temp_array = np.expand_dims(temp_array,axis = 0)
	print(temp_array.shape)
	print(image_array.shape)

	#stack the array
	image_array = np.vstack((image_array,temp_array))
		
	if key == 2:
		label_array = np.vstack((label_array,[ 0.,  0.,  1.,  0.,  0., 0.]))
		key = 4
	elif key ==3:
		label_array = np.vstack((label_array,[ 0.,  0.,  0.,  1.,  0., 0.]))
		key = 4
	elif key == 0:
		label_array = np.vstack((label_array,[ 1.,  0.,  0.,  0.,  0., 0.]))
		key = 4
	elif key == 1:
		label_array = np.vstack((label_array,[ 0.,  1.,  0.,  0.,  0., 0.]))
		key = 4
	elif key == 4:
		label_array = np.vstack((label_array,[ 0.,  0.,  0.,  0.,  1., 0.]))
	elif key == 5:
		label_array = np.vstack((label_array,[ 0. , 0.,  0.,  0.,  0., 1.]))

	#delete o indexed array of all zreos 
	train_imgs = image_array[1:, :]
	train_label = label_array[1:, :]

if __name__ == '__main__':
	global train_imgs, train_label, image_array, label_array

	path = "photos"
	files= os.listdir(path)
	turns = int(math.ceil(len(files) / 500))
	print("number of files: " , len(files))
	print("turns: " , turns)

	for turn in range(0, turns):
		label_array = np.zeros((1,6),'float')
		image_array = np.zeros((1,120,160,3))

		trunc_files = files[turn*500: (turn+1)*500]
		print("number of trunc files: ", len(trunc_files))
		for file in trunc_files:
			if not os.path.isdir(file) and file[len(file)-3:len(file)] == 'jpg': 
			#all photos endwith jpg in right directory would be selected
				try:
					key = int(file[len(file) - 5])
					process_img(path+"/"+file, key); 
				except:
					print('prcess error')
	
		file_name = str(int(time()))
		directory = "training_data_npz"

		if not os.path.exists(directory):
			os.makedirs(directory)
		try: 
			np.savez(directory + '/' + file_name + '.npz', train_images = train_imgs, train_labels = train_label)
		except IOError as e:
			print(e)
	

