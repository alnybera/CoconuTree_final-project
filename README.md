# CoconuTree Counting (Final Project The Woz)

## Project Overview 
This project developed an automated system to count coconut trees using YOLO v9 object detection technology from aerial imagery. High-resolution aerial photos were collected using drones over coconut plantations. These images were pre-processed and manually annotated to create a dataset for training the YOLO v9 model. The trained model was evaluated using metrics such as Precision, Recall, and Mean Average Precision (mAP), showing high performance with mAP > 90%. The model was then integrated into an automated system for real-time image analysis, enabling quick and accurate counting of coconut trees in new images captured by drones. The results of this project demonstrate that YOLO v9 is effective for detecting and counting coconut trees from aerial imagery, and this implementation can improve the efficiency of coconut plantation management through automated counting processes. Future steps include enhancing the model with more data, developing additional features, and conducting field tests in various locations with different environmental conditions.

## Method
Implementation of paper - [YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information](https://arxiv.org/abs/2402.13616)

Data Collection & Preparation
In this project, we use aerial imagery as the primary material for counting coconut trees. The aerial photos have been processed into a mosaic, resulting in orthomosaic data. 
Orthomosaic data definition:
The output from a process where a number of overlapping photos (e.g. from a drone or aerial camera) are stitched together with distortions removed to create a complete and continuous image representation or map of a portion of the earth

<img width="478" alt="image" src="https://github.com/alnybera/CoconuTree_final-project/assets/163568585/d0d5f2d3-9574-4b48-98f6-93808d295552">

## Training & Optimization
Arsitektur : YOLO V9

Epoch : 30

Batch size : 8

Image size: 640x640px

Advanced analytics : Non-Maximum Suppression (NMS) & Deep sort (tracking)

<img width="230" alt="image" src="https://github.com/alnybera/CoconuTree_final-project/assets/163568585/735223c4-24a8-47b2-a6e9-f279531c0220">

lr0: 0.01  # initial learning rate (SGD=1E-2, Adam=1E-3)
lrf: 0.01  # final OneCycleLR learning rate (lr0 * lrf)
momentum: 0.937  # SGD momentum/Adam beta1
weight_decay: 0.0005  # optimizer weight decay 5e-4
warmup_epochs: 3.0  # warmup epochs (fractions ok)
warmup_momentum: 0.8  # warmup initial momentum
warmup_bias_lr: 0.1  # warmup initial bias lr
box: 7.5  # box loss gain
cls: 0.5  # cls loss gain
cls_pw: 1.0  # cls BCELoss positive_weight
obj: 0.7  # obj loss gain (scale with pixels)
obj_pw: 1.0  # obj BCELoss positive_weight
dfl: 1.5  # dfl loss gain
iou_t: 0.20  # IoU training threshold
anchor_t: 5.0  # anchor-multiple threshold
anchors: 3  # anchors per output layer (0 to ignore)
fl_gamma: 0.0  # focal loss gamma (efficientDet default gamma=1.5)
hsv_h: 0.015  # image HSV-Hue augmentation (fraction)
hsv_s: 0.7  # image HSV-Saturation augmentation (fraction)
hsv_v: 0.4  # image HSV-Value augmentation (fraction)
degrees: 0.0  # image rotation (+/- deg)
translate: 0.1  # image translation (+/- fraction)
scale: 0.9  # image scale (+/- gain)
shear: 0.0  # image shear (+/- deg)
perspective: 0.0  # image perspective (+/- fraction), range 0-0.001
flipud: 0.0  # image flip up-down (probability)
fliplr: 0.5  # image flip left-right (probability)
mosaic: 1.0  # image mosaic (probability)
mixup: 0.15  # image mixup (probability)
copy_paste: 0.3  # segment copy-paste (probability)

## Evaluation
mAP (Mean Average Precision) from validation data.

50    : 0,975  
50-95 : 0,951
 

Precision Curve:

<img width="240" alt="image" src="https://github.com/alnybera/CoconuTree_final-project/assets/163568585/d8f22dd5-4c9b-46d8-9cfb-aac20847915e">
  
Recall Curve:

<img width="247" alt="image" src="https://github.com/alnybera/CoconuTree_final-project/assets/163568585/6a6459ae-56f7-493e-8247-201e251aed5f">
  
Precision - Recall Curve:

<img width="243" alt="image" src="https://github.com/alnybera/CoconuTree_final-project/assets/163568585/9ceebb53-b2b0-4f6d-a69d-dcd4191e3e6c">

## Testing
<img width="516" alt="image" src="https://github.com/alnybera/CoconuTree_final-project/assets/163568585/fa11775e-e4a9-4e77-9cb8-6f47c27a2cf4">

## Future Improvement
Improve the coconut tree counting model by adding samples of smaller plants (immature), specifically young coconut trees. This step will help the model to more accurately detect and recognize the anatomy and shape of the crown of young coconut trees.

## Acknowledgements
Team : The Woz

ADITYA LESMANA

BERNADETTA ALNYBERA F

C YONGKY PRANOWO

IBNU FARKHAN

<details><summary> <b>Expand</b> </summary>

* [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
* [https://github.com/WongKinYiu/yolor](https://github.com/WongKinYiu/yolor)
* [https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)
* [https://github.com/VDIGPKU/DynamicDet](https://github.com/VDIGPKU/DynamicDet)
* [https://github.com/DingXiaoH/RepVGG](https://github.com/DingXiaoH/RepVGG)
* [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
* [https://github.com/meituan/YOLOv6](https://github.com/meituan/YOLOv6)

</details>
