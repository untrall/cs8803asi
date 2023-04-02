Adding Easy-to-use Fine-Tuning of Deep Learning Models with EVA
===

## How to train

Below are the steps to run the program

1. Change current directory to ```yolov5```
2. Use command ```python train.py --img 640 --batch batch_size --epochs epoch_num --data traffic.yaml --weights yolov5s.pt ``` to train YOLOv5 on traffic video. ```batch_size``` is the your desired batch size and ```epoch_num``` is the total number of epoches used in training.
3. Results are stored in ```yolov5/runs/train/exp```.

Results show case
---
### Before
![](https://i.imgur.com/BuXbg0Z.jpg)

### Prediction
![](https://i.imgur.com/3lD5UYv.jpg)

### Labels
![](https://i.imgur.com/jNw4Tiu.jpg)


###### tags: `yolov5` `eva` `Georgia-Tech` `object-detection`
