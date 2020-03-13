# **Results of Tweaking Hyper-Parameters**

Training is performed on Flir dataset containing 8862 images while testing is done with 1366 images. To check the influence of hyper-parameters on the model’s accuracy we have varied 1 hyper-parameter at a time and evaluated the mAP scores. The following hyper parameters were varied: 

| Sl.No |   Hyper-Parameter   |  Initial Value  | Modified Value                                               |
| ----- | :-----------------: | :-------------: | :----------------------------------------------------------- |
| 1.    | Activation function |     SIGMOID     | SOFTMAX                                                      |
| 2.    |      Optimizer      |       RMS       | 1. Adams with Manual Learning rate                                              2. Adams with exponential Learning rate |
| 3.    |  Data Augmentation  | Horizontal Flip | Black Patches                                                |
| 4.    |     Decay Steps     |    8,00,756     | 5000                                                         |
| 5.    |       DROPOUT       |       OFF       | ON                                                           |

 

Based on the below results we can infer that **DROPOUT** and **SOFTMAX** feature improved our model accuracy by close to 3% while the other parameters yielded us more or less the same mAP value but **ADAM optimizer** with manual learning rate giving us the worst results.  

### 1.)**Total Loss**

![img](doc_images\Total Loss.png)

 

### 2.) **Avg mAP Values**

![img](doc_images\Avg mAP.PNG)

 

### 3.) **mAP for Person**

![img](doc_images\mAP Person.PNG)

 

### 4.) **mAP for Bicycle**

![img](doc_images\mAP Bicycle.PNG)

 

### 5.) **mAP for Car**

![img](doc_images\mAP Car.PNG)

 

 