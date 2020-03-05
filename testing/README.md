 

 

​																	TU Eindhoven

 

​											Department of Mathematics and Computer Science

​															Automotive Systems Design

 

![img](file:///C:\Users\20195009\AppData\Local\Temp\msohtmlclip1\01\clip_image002.png)

 

 

 

​											Thermal Object Detector Beta Testing Plan

 

 

​																		Prepared by 

​													T. S. Ram Parvathaneni & Ayush Maheshwari

 

 

 

 

 

 

 

 

 

 

© TU Eindhoven 2020. All rights reserved. No part of this publication may be reproduced without the written permission of the copyright owner.



TABLE OF CONTENTS

[LIST OF ABBREVIATIONS. ii](#_Toc34214322)

[1 Objective. 1](#_Toc34214328)

[1.1 Introduction. 1](#_Toc34214329)

[1.2 Architecture. 2](#_Toc34214330)

[2 Compliance. 2](#_Toc34214331)

[3 Constraints. 3](#_Toc34214332)

[4 Procedure. 4](#_Toc34214333)

[4.1 Procedure. 4](#_Toc34214334)

[4.2 Post Procedure. 4](#_Toc34214336)



 

 

 



 

LIST OF ABBREVIATIONS

VOC = Visual Object Classes 

COCO = Common Objects in Context

SSD = Single Shot Detector

mAP = Mean Average Precision

IoU = Intersection over Union

 

 

**
**

# 1 Objective

The objective of the Beta Test is to test and verify the efficiency of “trained neural network” for object detection using thermal camera in real time environment using NVIDIA Jetson.

## 1.1 Introduction

Thermal cameras are one of the emerging technologies in the field of autonomous vehicles. This is due to their ability to detect the things that emit heat irrespective of the weather conditions and they are insensitive to flare, glare when exposed to the direct light unlike normal RGB cameras. Many organisations increased their extent of research in object detection using thermal cameras alongside RGB cameras. Deep learning is playing crucial role in the object detection. Advancements in deep learning are significant in the past ten years. Powerful neural networks came to existence in the thorough research in this field. 

This ASD project delivers an thermal imaging system deployed on the vehicle which detects pedestrian, cyclists, cars during harsh weather conditions, low day-light and night-time conditions.

For this project, pre-trained neural network has been trained using the concept of transfer learning based on training set and validation set of thermal images provided by FLIR website. In general, the datasets that are going to be fed to the training are of two types either PASCAL VOC data sets or COCO datasets. PASCAL VOC datasets are of XML type and COCO datasets are of JSON type. 

The neural network that we have chosen for the object detection is MobileNet V2 SSD 300 based on its performance reasons. It surpassed all the networks available currently available with its speed and accuracy. For the training, we have used around 15000 FLIR thermal images and their corresponding annotated files in JSON format. After the training of the neural network, it provides a frozen graph which can be deployed in to NVIDIA Jetson Xavier for optimising its performance. 

## 1.2 Architecture

This NVIDIA Jetson Xavier is connected to thermal camera as shown below. It is mounted on the roof of the car. Thermal camera is further connected to The NVIDIA Jetson Xavier which is mounted in back of car (trunk) via mini B to USB wire. The Jetson is further connected to the monitor placed in second row of car to run the test as well as to observe the inference.

![img](file:///C:\Users\20195009\AppData\Local\Temp\msohtmlclip1\01\clip_image004.png)

Following is the setup of the system deployed in the vehicle:

![img](file:///C:\Users\20195009\AppData\Local\Temp\msohtmlclip1\01\clip_image006.jpg)

 

# 2 Compliances to Test

This section will give insights of the compliances need to be fulfilled to carry out the test for safety as well as seamless operation of test. Following are the compliances for the test: 

·    <u>No of people for the assistance in the car other than driver.</u>

​		Driver : Tijs (or AIIM personnel) 

​		Front Seat : Koen

​		Back Seat I : Hiram (for monitoring the inference on monitor/Laptop)

​		Back Seat II : *Any one can volunteer.*

·    <u>Trajectory and corresponding driving scenario</u>

​		Point to point trajectory (road path) will be decided by Koen and Tijs. The trajectory should cover both 		following urban and rural scenarios.

​		Urban Scenario I : Simulating Highway road @ 70-80 Kmph

​		Urban Scenario II : Simulating City road @ 40-50 Kmph

​		Rural Scenario : Simulating Rural road @ 20-30 Kmph

·    <u>Configuration of the Camera</u>

​		The camera configuration is controlled by the FLIR provided Camera Controller GUI software. It needs to be made sure that thermal camera configuration is in factory default settings (Setup<FFC<Auto<7200 Frames.)

·    <u>Time and duration of the test.</u>

​	Date : 6/3/2020

​	Time : 10:30 to 12:00 (1hour 30mins)

​	Backup day : If there is rain during that time, new test time will be set as per Tijs. 

·    <u>Rules before starting the test. (Checklist)</u>

​	Camera mounting should bolted to roof properly.

​	Camera should be mounted to camera holder by 4 screws properly.

​	Jetson should be mounted properly to the base plate in trunk of the car.

​	Wiring peripherals should be connected to devices properly.

​	The script required to initiate the test via NVIDIA Jetson.

​	Tyre Pressure check.

​	Note the odometer reading before the test.

·    <u>Environmental Conditions</u>

​	There should be no moderate or heavy rain during any point of test. If there will be any test will be halted.

 

 

# 3 Constraints 

This section describes in detail the constraints to the tests scenario. The preliminary constraints are as follows: 

·    <u>Weather Conditions</u>: This test is constrained to be performed only in absence of moderate or heavy rainfall.

·    <u>Thermal camera:</u> The thermal camera is recording the video based on the specific configuration given by Camera Controller GUI factory default set.

 

# 4 Procedure

## 4.1Procedure

​	The installation of the whole system and its verification should be done before the test starts. 

​	Installation of the system includes the mounting of the camera to the 3D printed CAD mounting which was fixed to the car using the nut and bolts. It also consider the mounting of the Jetson Xavier at the rear end of the car and its interface with both the camera and laptop should be ensured. 

​	Once after this process, the whole software integration of the system should be tested using the laptop to check the correct functioning of the system. 

​	Kindly run the camera on Jetson for 1 hour to check the 



## 4.2 Post Procedure

​	Once after the test is done, the data should be collected and stored in the local PC for the offline analysis of the inference that the trained neural network generated while testing. 

The laptop can be disconnected from the Jetson Xavier. The inference graph and the data obtained from the test will help to calculate the mAP(Mean Average Precision) score based on the IoU of the predicted bounding boxes of the trained neural network. 

Thermal Camera and Jetson Xavier can be unscrewed and detached from the mounting. Jetson Xavier is used to optimise the frozen inference graphs offline obtained after training the neural network. 

 

# 

 

 

 



 