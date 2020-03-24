# Design and Manufacturing of Mounting Brackets

This document explains the CAD design and manufacturing part of mounting brackets. There are 2 mounting brackets, which are need to be designed and manufactured, first for mounting the thermal camera and another one for mounting NVIDIA Jetson Xavier to the vehicle. The following 2 parts are named as :

#### 1. Jetson Xavier Mounting Bracket 
#### 2. Thermal Camera Mounting Bracket 

The top priority for part design is that part must function properly without failing. While designing, it has been ensure that part can be made quickly and cost effectively. Following paragraph explains the design and development of mounting brackets in detail :

## Jetson Xavier mounting bracket

The function of this bracket is to rigidly mount Jetson Xavier on the vehicle. The mount must be capable of supporting Jetson Xavier without failure during its expected life span.

### Mounting Location
To mount the Xavier on the car, multiple locations were considered and their pros and cons were analysed. For instance, originally we considered, mounting Xavier on roof near to the camera which will require need of shorter cable connecting the thermal camera to the Jetson. But the disadvantage of placing it over there was the need of manufacturing water-proof housing (shield) to cover Xavier during bad weather such as heavy rain. This could have lead to longer manufacturing time as well as usage of extra material. 
Post-discussion with stakeholders, the final decision was taken to mount it inside the car which was a more safer and elegant option hence saving it from bad weather condition as well as usage of less material. Post-discussion with Tijs and Anweshan, it was clarified that wire harness' length, which connects thermal camera and Jetson, can be between 4-5 meters and will not cause any communication loss if Xavier is mounted at back of vehicle. The pre-installed base plate located in the boot space of the car hence was finally selected to mount Jetson Xavier.

### Design and Attachment Method
The Jetson Xavier is designed to reside on the mounting base plate which is rigidly connected to pre-existing backplate in the boot space of the car. The design consists of a simple rectangular mounting plate of 8 mm thickness with the provision of holes at the appropriate locations which coincides with the holes of the base plate. The base plate has holes of 5 mm diameter and spaced 50 mm apart in a grid format. Accordingly, the length and breadth of the mounting plate are 170 mm and 120 mm respectively. Four holes of 5.4 mm diameter (considering a manufacturing tolerance of 0.4 mm) were provided on the mounting plate spaced 150 mm apart lengthwise and 100 mm apart breadthwise. To mount the Jetson Xavier on the mounting plate, another 4 holes of 3.4 mm diameter were provided with correct spacing. Correspondingly, longer screws of (M5 X 40) were procured to account for the thickness of the mounting plate. 

Additionally, some material from the central portion of the mounting plate was saved by providing a circular hole of 55 mm in diameter. This helped in lesser manufacturing time and cost without affecting the strength and functionality of the mounting plate. Following images shows the CAD model for the Xavier mounting bracket:

[![img](https://github.com/tue-mps-edu/thermal_object_detection/raw/master/CAD/doc_images/xavier_image1.JPG)](https://github.com/tue-mps-edu/thermal_object_detection/blob/master/CAD/doc_images/xavier_image1.JPG)

*Figure 1: Top View of Xavier Mounting Bracket.*

[![img](https://github.com/tue-mps-edu/thermal_object_detection/raw/master/CAD/doc_images/xavier_image2.JPG)](https://github.com/tue-mps-edu/thermal_object_detection/blob/master/CAD/doc_images/xavier_image2.JPG)

*Figure 2: Isometric View of Xavier Mounting Bracket.*

## Thermal camera mounting bracket

The fucntion of this bracket is to mount the thermal camera on roof of the vehicle.The mount must be capable of rigidly supporting Jetson Xavier without failure during its expected life span.

### Mounting Location
To mount the thermal camera on the car, two options were available. 1.) The thermal camera can be mounted similar to the RGB camera mounting system inside the car just behind the windshield. 2.) The thermal camera can be also mounted on the roof (false roof) of the car like a LIDAR system. Attributing to the lack of enough space behind the windshield, the second option was chosen to mount the camera. The front left portion of the false roof of the car was selected as the most appropriate location to mount the thermal camera after discussion with the stakeholders. This is so because there was no other feasible location available as there were other sensor systems mounted across the roof.

### Design and Attachment Method
The design consists of a simple rectangular mounting plate of 8 mm thickness with the provision of a central enclosure to assemble the camera as well as holes and cavities at the appropriate locations. These holes are there for side mounting of a thermal camera to restrict its movement. 4 holes of 2.4 mm diameter on the sidewalls of the enclosure to mount the camera with the help of the procured M2 mounting screws; four holes of 6 mm diameter on the mounting plate spaced 113.45 mm lengthwise and 99 mm breadthwise to mount the mounting plate on the false roof; a rectangular cavity on one sidewall of the enclosure to account for the USB cable connection with the camera; a circular hole of 30 mm diameter on the front wall of the enclosure to account for the camera lens and help in mounting the camera on the enclosure via the locking ring. 

Additionally, a rectangular cavity was provided on the top face of the mounting plate to accommodate the small 3 mm protrusion on the bottom face of the camera. Also, the entire enclosure was made inclined upward at 5.6 degrees with respect to the horizontal direction to account for the slope of flase roof at mounting location. Following images shows the CAD model for the Xavier mounting bracket:

[![img](https://github.com/tue-mps-edu/thermal_object_detection/raw/master/CAD/doc_images/camera_image1.JPG)](https://github.com/tue-mps-edu/thermal_object_detection/blob/master/CAD/doc_images/camera_image1.JPG)

*Figure 3:  Isometric View of Thermal Camera Mounting Bracket.*

[![img](https://github.com/tue-mps-edu/thermal_object_detection/raw/master/CAD/doc_images/camera_image2.JPG)](https://github.com/tue-mps-edu/thermal_object_detection/blob/master/CAD/doc_images/camera_image2.JPG)

*Figure 4:  Sketch View of C-Section of Thermal Camera Mounting Bracket.*
