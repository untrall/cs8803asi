Adding Easy-to-use Fine-Tuning of Deep Learning Models with EVA
===

## Introduction
EVA is an open-source AI-relational database with support for deep learning models. It aims to support AI-powered database applications that operate on both structured and unstructured data with deep learning models. The database has built-in support for object detection system YOLO which is widely used. However, at the current stage, users often prefer to use their own fine-tuned configurations instead of the vanilla model the database provides.

## Project Statement
Currently, if users were to fine tune YOLO, they need to download the data, extract the labels from EVA or an external labeling library, fine tune YOLO locally and then submit their custom configurations to EVA. This process is time-consuming and such a complex procedure is pruned to errors. Our project aims to address this issue by extending the functionality of EVA to support ad-hoc fine-tuning for YOLO. With the added support, instead of going through a lengthy fine-tuning process locally, users can just enable fine-tuning for YOLO, and all will be taken care of by the database.

## Project Goals
Our 75\% goal is to add support for simple fine-tuning of YOLO. The fine-tuned model may not have performance on par with a locally fine-tuned version but is easy to use since it’s built in. Our 100\% goal is to support fine-tuning with performance comparable to locally fine-tuned versions by the user. In addition to all above, our 125\% goal aims to allow users to provide simple instructions or configurations for how they wish YOLO is to be fine-tuned on EVA. In this case, EVA will fine-tune YOLO with some user preferences. 

## How to fine-tune

Below are the steps to run the program

1. Change current directory to ```yolov5```
2. Use command ```python train.py --img 640 --batch batch_size --epochs epoch_num --data traffic.yaml --weights yolov5s.pt ``` to train YOLOv5 on traffic video, where ```batch_size``` is the your desired batch size and ```epoch_num``` is the total number of epoches used in training.
3. Training results are stored in ```yolov5/runs/train/exp```.
4. Use command ```python detect.py --source ../datasets/traffic/test/images --weights runs/train/exp2/weights/best.pt --conf conf_level --name traffic_test``` to run the model on test images, where ```conf_level``` is your desired confidence threshold.
5. Dection results are stored in ```yolov5/runs/detect/traffic_test```.

## How to use fine-tuned model in EVA

1. Download the saved model from ```/cs8803asi/yolov5/runs/train/exp2/weights/best.pt``` and rename it ```model.pt```, then upload the file to ```/cs8803asi``` directory.
2. Follow instructions in the [```Object_Detection_Fine_Tune.ipynb```](https://github.com/untrall/cs8803asi/blob/main/Object_Detection_Fine_Tune.ipynb) notebook.
## Results show case
---
## Fine tune results
Below are examples generated by the custom-trained YOLOv5 model. The example image without labels corresponds to the top-left image in subsequent figures. Due to limited computing resources, we are only able to train the custom YOLOv5 model in 50 epoches with batch size of 16. Therefore, our detection results may not be better than that of a pre-trained YOLO model, which no doubt has been trained extensively.
#### Example image without labels
![](https://i.imgur.com/UddTYEH.jpg)


#### Example image with ground-truth labels
![](https://i.imgur.com/FZe1sEf.jpg)


#### Example image with predicted labels
![](https://i.imgur.com/Rs8tpBa.jpg)

## Fine-tuned results with EVA

Registering the above fine-tuned model into EVA and apply object detection, we get the following result.

#### Original video
https://user-images.githubusercontent.com/119721683/232174690-40bce4f6-42a3-41fd-b8bf-d3d62b53b7da.mp4

#### Object-detection applied with EVA
https://user-images.githubusercontent.com/119721683/232174642-eb0f3c25-6d9d-4a6e-a2ce-9aadcea85e50.mp4

## How to filter specific labels in EVA
Follow instructions in the [Object_Detection_Fine_Tune.ipynb notebook](https://).
#### Example image filter out car
![filter_car](https://user-images.githubusercontent.com/40770106/235326195-83b0b77a-29d8-4d92-aea3-34c6da83a52b.png)

#### Example image filter out traffic light and motobike
![without_traffic_light](https://user-images.githubusercontent.com/40770106/235326198-664245a9-b4c1-4b42-9962-340c5898d728.png)

#### Example Video filter out car 


https://user-images.githubusercontent.com/40770106/235326199-68cbd72d-a6d7-4828-8ea4-cb363f553925.mp4


###### tags: `yolov5` `eva` `Georgia-Tech` `object-detection`

