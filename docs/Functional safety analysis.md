# Functional Safety Analysis

introduction:

current situation, our system embedded in the car

Hypothesis

structure of this analysis

## Assumptions

assumptions we made for this analysis

completely in car, waterproof, precision & recall really high

add visio image for assumed architecture

![Assumed architecture of the system](doc_images/05032020_integration_diagram_v2_koen.jpg | width=100)

## Scenarios

where is the vehicle being tested and the analysis (which situations?)

when it fails what is the damage

## Limitations

wrt technology

## Risk Analysis

In order to have a clear understanding of the additional value of the thermal camera detection system in terms of functional safety, a risk analysis is made for possible risks and their severity levels. This analysis is done for the autonomous vehicle with the thermal camera connected, and without the thermal camera detected (RGB only). The assumption is made that the thermal camera is connected to the PC via a USB cable and the detection system is embedded in the ROS node of the PC. 

(explanation ASIL)

| Risk # | Explanation                                                  | Severity (RGB only) | Severity (RGB +thermal) | Exposure Probability | Hazard Probability (RGB only) | Hazard probability (RGB+thermal) |
| ------ | ------------------------------------------------------------ | ------------------- | ----------------------- | -------------------- | ----------------------------- | -------------------------------- |
| 1      | RGB camera USB cable to PC malfunction                       | 5                   | 1                       | 1                    | 1                             | 1                                |
| 2      | Missed object detection during bad weather conditions        | 5                   | 5                       | 2                    | 4                             | 1                                |
| 3      | Missed object detection during nighttime driving             | 5                   | 5                       | 2                    | 5                             | 1                                |
| 4      | RGB camera malfunction                                       | 5                   | 1                       | 1                    | 1                             | 1                                |
| 5      | Missed object detection due to light glare                   | 5                   | 5                       | 3                    | 4                             | 1                                |
| 6      | Incorrect classification due to occlusion                    | 2                   | 2                       | 5                    | 3                             | 2                                |
| 8      | incorrect classification (good weather)                      | 2                   | 2                       | 4                    | 1                             | 1                                |
| 9      | incorrect classification (bad weather)                       | 2                   | 2                       | 2                    | 3                             | 1                                |
| 10     | incorrect classification because of light glare              | 2                   | 2                       | 3                    | 3                             | 1                                |
| 11     | incorrect classification (nighttime)                         | 2                   | 2                       | 2                    | 4                             | 1                                |
| 12     | Computer failure                                             | 5                   | 5                       | 1                    | 1                             | 1                                |
| 13     | Wrong x-y data of object sent to control node because of change in orientation of RGB camera | 5                   | 5                       | 1                    | 2                             | 1                                |
| 14     | Missed object detection due to change in orientation of RGB camera | 5                   | 5                       | 1                    | 2                             | 1                                |

#Put explanation and analysis here.

tell how incorrect/no classifications can happen (software based)

malfunction can happen due to short circuit or power supply failure





