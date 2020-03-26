#             Beta Test Post Analysis

## 1. Objective

The post analysis is the retrospection of the Beta test. This document gives a subjective analysis of the test performed in accordance to the test procedure planned. 

## 2. Analysis

This section will explain the step by step analysis alongside the testing setup described in the test plan.

- The test went according to the plan, the preliminary checkups before the test had been checked before starting the test. 
   - ​	Checked camera holder mounting.
   - ​	Checked camera in to camera holder mounting.
   - ​	Checked Jetson mount to the base plate in trunk of the car.
   - ​	Checked wiring peripherals connections to devices properly.
   - ​	Checked the script required to initiate the test via NVIDIA Jetson.
   - ​	Checked the Tyre Pressure.
   - ​	Noted down the odometer reading before the test.
- As mentioned four people were present in the car during the test.
   - Driver : Tijs (or AIIM personnel)
   - Front Seat : Koen(Project Manager)
   - Back Seat I : Hiram (for monitoring the inference on monitor/Laptop)
   - Back Seat II : Sukrut(for recording data in parallel to inference)
- The test covered both urban scenario I and II driving situations. But due to time constraints rural scenario was skipped and driving in the university area had been replaced it. In total of 30 kilometres had been covered for the test.
- The configuration of the camera was unchanged from the default during the test. During the test we have encountered the exposure problems with the camera. This lead to improper inference of the object detection system. 
- The test started at 11 AM in the morning with delay of 30 minutes. And the test lasts for 30 minutes.
- The weather was clear during the test day which allowed us to perform the task successfully.

The images were recorded simultaneously by Sukrut while real time time inference setup was handled by the Hiram during the test. Totally 65000 images were recorded which needed to be cleaned and labelled for the further training of the Neural Network.

The exposure problem of the thermal camera should be adjusted by tweaking the configuration. This is going to be done by contacting the Thermal Camera provider for the support. 

