# Group12
## Raspberry Pi controled Self-Driving Car

### What we have done so far

![image of car](https://github.com/BUConnectedWorld/Group12/blob/master/car.JPG)
![image of car](https://github.com/BUConnectedWorld/Group12/blob/master/road.JPG)
- We impelemented carControl.py file to let L298N motor driver control toy car. 

- camera.py is the file to control pi camera

- In collect.py file, we import pygame to control toy car when keyboard is pressed. 

- capture.py is a file that using multi-threading when user control car by keyboard and recording path images at the same time. Each time step, camera would save file to directory with direction we made as label. 

- folder /photos is images we captured after w running capture.py. As you can see, there are over 1,000 images showing paths and their corresponding direction. We are going to use these images as dataset to train neutral network.



