# Group12
## Raspberry Pi controled Self-Driving Car
## -- A Trained Autonamous Car using Keras and TensorFlow Based on CNN Network

### What we have done so far


![image of car](https://github.com/BUConnectedWorld/Group12/blob/master/road.JPG)

#### Milestone1

![image of car](https://github.com/BUConnectedWorld/Group12/blob/master/car.JPG)

- We set up Raspberry Pi and L298N H bridge.
  In [carControl.py](https://github.com/BUConnectedWorld/Group12/blob/master/carControl.pyc), we use L298N to control move direction when running the car. Here is how H bridge works
  
  
  | In4 | In3 | In2 | In1 | Function |
  | --- | --- | --- | --- | --- |

  | 0  |  0  |  0  |  0  | Stop/Free Wheel |
  
  | 0  |  0  |  0  |  1  | Motor 1 Forward |
  
  | 0  |  0  |  1  |  0  | Motor 1 Reverse |
  
  | 0  |  0  |  1  |  1  | Motor 1 Brake |
  
  | 0  |  1  |  0  |  0  | Motor 2 Forward |
  
  | 1  |  0  |  0  |  0  | Motor 2 Reverse |
  
  | 1  |  1  |  0  |  0  | Motor 2 Brake |
  
- We impelemented carControl.py file to let L298N motor driver control toy car. 

- camera.py is the file to control pi camera

- In collect.py file, we import pygame to control toy car when keyboard is pressed. 

- capture.py is a file that using multi-threading when user control car by keyboard and recording path images at the same time. Each time step, camera would save file to directory with direction we made as label. 

- folder /photos is images we captured after w running capture.py. As you can see, there are over 1,000 images showing paths and their corresponding direction. We are going to use these images as dataset to train neutral network.



