Adding Easy-to-use Fine-Tuning of Deep Learning Models with EVA
===

## How to train

Below are the steps to run the program

1. Change current directory to ```yolov5```
2. Use command ```python train.py --img 640 --batch batch_size --epochs epoch_num --data traffic.yaml --weights yolov5s.pt ``` to train YOLOv5 on traffic video, where ```batch_size``` is the your desired batch size and ```epoch_num``` is the total number of epoches used in training.
3. Training results are stored in ```yolov5/runs/train/exp```.
4. Use command ```python detect.py --source ../datasets/traffic/test/images --weights runs/train/exp/weights/best.pt --conf conf_level --name traffic_test``` to run the model on test images, where ```conf_level``` is your desired confidence threshold.
5. Dection results are stored in ```yolov5/runs/detect/traffic_test```.

Results show case
---
### Before
![](https://i.imgur.com/hoRSozd.jpg)

### Prediction
![](https://i.imgur.com/3lD5UYv.jpg)

### Labels (ground truth)
![](https://i.imgur.com/P7kUiUU.jpg)




###### tags: `yolov5` `eva` `Georgia-Tech` `object-detection`

