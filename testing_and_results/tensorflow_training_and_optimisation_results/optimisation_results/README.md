# Optimization Results 

This document intends to demonstrate the performance improvement enabled by TensorRT optimization in terms of inference speed on the SSD MobileNet v2 architecture. To achieve this, we make a comparison between the original non-optimized model and the TensorRT engine. Moreover, we evaluate and compare the mean average precision (mAP) of both models to identify any performance degradation and illustrate the optimization trade-off. 



## Inference Speed Results

To provide meaningful information for the application at hand, both models were evaluated on the Jetson Xavier AGX with Jetpack 4.3 installed. Moreover, inference is performed on image data fetched from FLIR's Tau2 Camera using TeAx's ThermalCapture USB grabber, using the v4l2loopback 0.10.0 kernel module and TeAx's thermal grabber library version 1.0 to interface with it. To diminish the runtime impact of blocking I/O operations, we run a separate thread to fetch image data. Optimization and inference is then done using Floating Point 16 (FP16) precision with TensorRT version 6.0.1 and Pycuda 2019.1.2 on Python 3.6. For the non-optimized model, inference is performed using TensorFlow-GPU version 1.15. Furthermore, we record inference speed over a period of 10 minutes for both models, and average these results to produce a significant output.



|             | Non-Optimized Model | Optimized Model (FP16) |
| :---------: | :-----------------: | :--------------------: |
| Average FPS |        24.83        |         119.3          |
| Minimum FPS |        23.24        |         101.1          |
| Maximum FPS |        30.13        |         128.1          |

*Table 1: results of the FPS test for both the non-optimized and optimized network*



The obtained results are shown in Table 1. The non-optimized network shows an average of approximately 25 FPS, and an average of over 119 FPS for the optimized model, with a maximum of 128 FPS. This is an increment of almost a factor of 5 over the non-optimized model. These results prove the fulfillment of the "100 FPS inference time" requirement. Moreover, the minimum FPS after optimization is 101.1, so we can conclude that the FPS of the network is over 100 at all times during regular operating conditions. 



## mAP Results

To identify any precision degradation due to optimization, we use FLIR's ADAS testing ground truth annotations as a baseline for comparison. We run inference on each of the testing set images using both the optimized and non-optimized models and create a *json* file for each run. Afterward, we compare these with the ground truth data using pycocotools to derivate mAP scores using different Intersection over Union (IoU) settings. 

|                                                              | Non-Optimized Model | Optimized Model  (FP16) |
| :----------------------------------------------------------- | :-----------------: | :---------------------: |
| IoU=0.50:0.95      \| area = all            \| maxDets = 100 |       15.14 %       |         14.07 %         |
| IoU=0.50               \| area = all            \| maxDets = 100 |       36.15 %       |         32.53 %         |
| IoU=0.75               \| area = all            \| maxDets = 100 |       10.81 %       |         10.43 %         |
| IoU=0.50 : 0.95    \| area = small       \| maxDets = 100    |       4.31 %        |         3.82 %          |
| IoU=0.50 : 0.95    \| area = medium \| maxDets = 100         |       21.52 %       |         19.91 %         |
| IoU=0.50 : 0.95    \| area = large       \| maxDets = 100    |       41.64 %       |         39.88 %         |

*Table 2: mAP comparison between the baseline non-optimized model and the TensorRT Engine.*



The obtained results are shown in Table 2. Results show that mAP between models are highly similar, showing an average degradation of 1.48% between benchmarks. This degradation can mainly be explained due to the FP16 selection during optimization. Nevertheless, this decision was made to enable a good balance between execution speed and precision. With these results, we aim to provide information that can be used to make a design decision in future stages of the project, where more data for training, as well as different architectures, can be used to mitigate this degradation.

*Note: The results shown in this document are provided only for comparison between models. For a detailed explanation of the mAP results related to the overall object detection performance per class, please refer to testing results.*

