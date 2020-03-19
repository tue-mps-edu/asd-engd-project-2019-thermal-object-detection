# Recommendations

In the lifecycle of this project, we encountered constraints/limitations as well as challenges for the next phases of this project. We categorize the recommendations in recommendations on hardware, recommendations on software and recommendations on training. 

##### Recommendations on hardware

- The FLIR Tau 2 camera is attached to a TeAx ThermalGrabber. This thermal grabber contains a FPGA which will convert the digital 14-bit raw data to a .jpeg or .tff file. This file will be sent via the USB to the NVIDIA Jetson Xavier or to the PC or another device connected to the thermal grabber. Figure 1 shows the architecture of the thermal camera together with the thermal grabber. We noticed that we had dark, raw images and videos so we wanted to calibrate the camera. When adjusting the camera settings in the GUI from FLIR we noticed nothing changed. The thermal grabber is blocking calibration capabilities of the FLIR camera which resulted in poor video captures. Our recommendation is not to use this thermal grabber, but the FLIR Camera Link Grabber.
  ![thermalgrabber](doc_images/tcgrabberusb_dataflowdiagram.jpeg)
  *Figure 1: data flow diagram of the FLIR Tau 2 camera connected to the thermal grabber*
- For full integration with the car you either have to install all software modules on the car or on the NVIDIA Jetson Xavier. As the Xavier has limited computation power and memory the recommendation is to either integrate the whole system into the PC in the car, or to install another NVIDIA engine in the vehicle like the PX2 used in a Tesla model S. 
- When integrating the full system in the car, and being able to use it when there is bad weather like rain, it is recommended to make a waterproof design for the cover of the thermal camera.

##### Recommendations on software

- If this system will be integrated on the PC in the vehicle, one should make it compatible with ROS Kinetic, Ubuntu 16.04 and CUDA9.0. These are the specifications of the cars' software.
- 

##### Recommendations on training

- When you would like to have a reliable system with high precision and recall (over 98%), you will need more than 3 million labelled images as training data set. 
- It is recommended to distinguish busses/trucks from cars in the classification, because they have other driving behaviour (speed and acceleration is different) as well as a different size.
- Because bikes do not emit heat, it is hard to distinguish these objects from the background. It is recommended to classify the person on the bike as bicyclist (based on his/her posture). We classified these people as 'person', but the speed of someone on a bike is different (on average 20 kmph) so they have other behaviour in traffic.
- Mopeds, motorbikes and animals are recommended to classify. They show other behaviour and shape on the thermal camera.

# Constraints