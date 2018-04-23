from keras.datasets import mnist
import matplotlib as mpl 
mpl.use('TkAgg')
import matplotlib.pyplot as plt 
import keras
from keras.models import Sequential# sequential model 
from keras.layers import Dense, Dropout, Flatten #Dense: fully connection layer 
from keras.layers import Conv2D, MaxPooling2D# convolution layer, subsample using maximum vaule
#load dataset
(x_train, y_trian) , (x_test, y_test) = mnist.load_data() # return two tuples containing image data(nb_sample, 28,28)
#60000 to train 10000 to test
plt.figure()
plt.imshow(x_train[30], cmap = 'gray') # show the 30-th image
plt.show()

img_rows, img_cols = 28, 28

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols,1) # the input of convolution is 4D so we need to reshape array to encounter the requirement
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols,1)
input_shape = (img_rows,img_cols,1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0],'train sample')
print(x_test.shape[0],'test sample')
#convert vector to binary matrix
num_classes = 10
y_trian = keras.utils.to_categorical(y_trian, num_classes)
y_test = keras.utils.to_categorical(y_test,num_classes)
#build cnn
model = Sequential()
model.add(Conv2D(32,kernel_size = (3,3),
		activation = 'relu',
		input_shape = input_shape))
model.add(Conv2D(64,(3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation = 'softmax'))
#compile
model.compile(loss = keras.losses.categorical_crossentropy,
	optimizer = keras.optimizers.Adadelta(),
	metrics = ['accuracy'])

#train
model.fit(x_train,y_trian,
	batch_size = 128,
	epochs = 12,
	verbose = 1,
	validation_data = (x_test,y_test))

score = model.evaluate(x_test,y_test,verbose = 0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

prediction = model.predict(x_test[20].reshape(1,28,28,1))
prediction = prediction.argmax(axis = 1)#find the highest scored arguments
plt.figure()
plt.imshow(x_test[20].reshape(28,28))
plt.text(0,-3,prediction,color = 'black')
plt.show()
model.save('mnist.h5')


















