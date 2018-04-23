# Group12
## Raspberry Pi controled Self-Driving Car
## -- A Trained Autonomous Car using Keras and TensorFlow Based on CNN Network

### What we have done so far

#### Week1

![image of car](https://github.com/BUConnectedWorld/Group12/blob/master/car.JPG)

- We set up Raspberry Pi and L298N H bridge.
  In [carControl.py](https://github.com/BUConnectedWorld/Group12/blob/master/carControl.pyc), we use L298N to control move direction when running the car. Here is how H bridge works:
  
  | In4 | In3 | In2 | In1 | Function |
  | --- | --- | --- | --- | --- |
  | 0  |  0  |  0  |  0  | Stop/Free Wheel |
  | 0  |  0  |  0  |  1  | Motor 1 Forward |
  | 0  |  0  |  1  |  0  | Motor 1 Reverse |
  | 0  |  0  |  1  |  1  | Motor 1 Brake |
  | 0  |  1  |  0  |  0  | Motor 2 Forward |
  | 1  |  0  |  0  |  0  | Motor 2 Reverse |
  | 1  |  1  |  0  |  0  | Motor 2 Brake |

#### Week2

![image of car](https://github.com/BUConnectedWorld/Group12/blob/master/road.JPG)

- We configured picamera and gathered images from road. [camera.py](https://github.com/BUConnectedWorld/Group12/blob/master/camera.py) is the file to control pi camera, the camera is capable of capturing a sequence of images extremely rapidly by utilizing its video-capture capabilities with a JPEG encoder. Here is the [reference](https://picamera.readthedocs.io/en/release-1.13/recipes2.html#rapid-capture-and-streaming)

- In [collect.py](https://github.com/BUConnectedWorld/Group12/blob/master/collect.py)file, we imported pygame to control toy car when keyboard is pressed. We took it as a thread, since we need to capture images as well as drive car in the same time. Therefore, in [capture.py](https://github.com/BUConnectedWorld/Group12/blob/master/capture.py), we implemented muti-threading program to let two models work together. At each time step, camera would save files to directory with direction we made as label. 

- folder /photos is images we captured after running capture.py. As you can see, there are over 1,000 images showing paths and their corresponding direction. We used these images as dataset to train neutral network.

### Week3

- This week, we first installed Keras and Tensorflow library with their dependencies. In order to be familiar with how Keras works, we worked on the official datasets [MNIST database of handwritten digits](https://keras.io/datasets/).The folder [/Practice_with_handWriting_Dataset](https://github.com/BUConnectedWorld/Group12/tree/master/Practice_with_handWriting_Dataset)includes the model we bulit and the returned trained model.  




