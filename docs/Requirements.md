# Requirements

Condition: while driving autonomously, 

| Description of requirement                                   | Justification                                                | S/B/E |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----- |
| The object detection system must detect  pedestrian, cyclists, mopeds, motor bikes and vehicles at the required frequency (100 FPS) or higher | These objects are the most frequent road users in the Netherlands. We want to detect dynamic objects, no static objects (trees, houses) |       |
| The object detection system using thermal images must run at the same FPS as the RGB camera (100 FPS) | Syncing purposes, otherwise the RGB and Thermal camera get out of sync and the  detection can go wrong due to undesired delay |       |
| After  the thermal camera makes an image and sends it to the object detection system, the delay of the object detector plus controls must be less than 1/FPS s | the vehicle must respond on a certain situation before the next frame comes in |       |
| When deploying the detection algorithm on the Jetson Xavier, the object detection algorithm must be  compatible with CUDA10.0, ROS Melodic and Ubuntu 18.04 | This is for deploying the system on the Jetson Xavier which will make inference |       |
| The object detection system must detect objects in a range of at least 20 meter in front of the car when the car is standing still | This is the distance required to detect objects in order to take the relevant corrective action |       |
| The total thermal camera assembly needs to be water resistant | To prevent the thermal camera from malfunctioning when it is raining. It does not need to be waterproof as the car is not allowed to drive when it is raining |       |
| The thermal camera must be mounted on the roof of the vehicle via a robust mounting system | It is not possible to place the camera inside the vehicle (too many other equipment) |       |
| The size of the mounting system for the thermal camera must be smaller than 210x210x250 mm | This is the maximum size of the available 3D printer         |       |
| The mounting of the Jetson Xavier must be in the back of the car on the pre-installed base plate | There is no significant loss of signal quality when installed inside in the back of the car (Anweshan Das). More waterproof. Less work to make housing for installing on top of the roof |       |
| The object detection system must process all incoming frames from the thermal camera | No frames should be lost due to bad signal distribution (too long cables) or intended skipping frames (software) because a detection could be missed |       |
| The wiring peripheral should account for no data loss at all times | USB cables can break or get loose                            |       |
| The camera mounting system must be attached to the roof of the car via bolts which fit into the holes in the roof of the car | At this position it is possible to have a clear field of view. Secondly, the bolts into the holes is a Robust option |       |
| The mounting system height must be such that the images contain no unnecessary information like the car roof or bonnet | This is useless information and could result into missed detections |       |
| The mounting system must allow the USB cable to be attached to the camera | This is essential for receiving data. Without proper connection between the USB cable and connector there will be no constant data flow |       |
| The thermal camera must be attached to the mounting system by two independent locking systems | Stability, no fuzzy images because of vibrations. Backup in case one of the attaching systems breaks |       |
| The probability-class value of a detected object must be at least 60 percent in order to classify the object in a certain class | This number is often used in literature and can tell with sufficient certainty that it will lead to accurate detection |       |
| Installing the object detection system must be plug and play for any third party vendor which contains the compatible hardware | This should not take too long as it is really inconvenient for the user if he doesn't have a guide containing instructions |       |
|                                                              |                                                              |       |

Table with less feasible requirements:

| Description                                                  | justification                                                | Why not feasible?                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| The object detection system must give the distance of the object from the vehicle | It can send this information to the control algorithm of the car | Project time, only one camera, other strategies not accurate enough, focus is only on creating inference |
| The object detection system must detect with precision and recall of at least 98% (10-fold cross validation) at all times when driving autonomously | Required precision and recall from the stakeholders to meet system reliability | Need a lot of training data (3+ million trained images) which is not feasible within the project timeline given |
| The object detection system has to detect the objects at all day and night weather conditions | Safety has to be guaranteed, so no missed detections are allowed to happen. | The weather conditions differ during the year, only 8 weeks project. The thermal image of captured environment depends on difference ambient temperature in day and night |
|                                                              |                                                              |                                                              |
|                                                              |                                                              |                                                              |
|                                                              |                                                              |                                                              |
|                                                              |                                                              |                                                              |
|                                                              |                                                              |                                                              |
|                                                              |                                                              |                                                              |

