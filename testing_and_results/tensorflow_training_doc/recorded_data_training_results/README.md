# Results of Recorded Data

A number of tests were performed on the Mobilenet v2 network in order to get optimal performance in terms of speed and mAP score. The sequence of the performed tests were:-

- First the baseline network of Mobilenet v2 was downloaded which was pre-trained on google dataset containing RGB images. The benefit of using this is to use transfer learning at its full potential.
- Now since the old dataset contains RGB images on which the pretrained model trained and our requirement is to train on Thermal (greyscale) images, there is a necessity to have a sufficient bunch of thermal images dataset to ensure that transfer learning. As first part of this process, we are using FLIR thermal images for training.

- The MobileNet v2 network was trained using the last checkpoint of the previously trained data (google images) with the thermal images of FLIR. After the training, evaluation is performed on test images (Thermal) to check the mean Average Precision (mAP) value, this mAP value is used as a performance indicator for our network.
- The results obtained were quite satisfactory but it is always good to tweak some important parameters (hyperparameters) to increase our network’s accuracy. So, a study was performed to evaluate the improvement in accuracy of our network based on tweaking hyperparameters.

- The results obtained showed that by changing the activation function from SIGMOID to SOFTMAX yielded us the best performance as shown in fig.1.

 

**Case-1**:- Optimization of network based on hyperparameters

![img](doc_images/hyperparameters.jpeg)

*Figure 1: Effect of hyperparameters on network accuracy(mAP)*

**Case 1**:- Collection of additional data and combining dataset 

Now in order to further improve the mAP score of the neural network model for thermal dataset it was decided to collect additional thermal images and build on top of the optimized Mobilenet v2 network which was with activation function SOFTMAX. Accordingly, 1548 good quality thermal images were obtained using FLIR TAU camera mounted on top of TOYOTA PRIUS vehicle during the Beta Test.

These collected images along with FLIR images were combined together and the baseline Mobilenet v2 network was trained only with the intuition that a larger dataset would eventually yield us better result.

From figure 2(below) it was observed that the overall model accuracy was lesser in comparison to the optimized Mobilenet v2 model. Also there were quite unusual trends with respect to different classes which are hard to understand why.

For example, the new 1548 images had only 2 classes (car, person) whereas the FLIR dataset had 3 classes (car, person and bicycle). The idea here was that since we are adding additional dataset for car and person we should see improvement w.r.t these classes but on the contrary there was an performance improvement of bicycle class and a reduction in performance w.r.t. person class. 

Due to this variation in results it was hard to make any conclusion about this training process.

![img](doc_images/combined_results.jpeg)

*Figure 2: Performance comparison between 2 modified networks*

**Case 2**:- Using additional recorded data and building on top of optimized network

Another approach to improve neural network accuracy was to use the recorded data and fed into the last checkpoint of the optimized network. This approach is done due to 3 reasons :- 

- The camera installed on the car is going to capture images having the recorded quality and making an inference on that dataset would be the most idealistic. 
- The network trained earlier had frozen weights and features extracted with respect to FLIR images which means that using this optimized network on our vehicle would perform very bad inference results as the quality and exposure of images are completely different, leading to confusing the network.

- To avoid confusing the network if we train our network with optimized hyperparameters and our recorded dataset we would eventually get new weights and features extracted which will be useful for the network to perform accurately.

From figure 3 it was observed that the network actually performed better in comparison to optimized Mobilenet v2 network with class person showing an improvement of 14% and bicycle class as 0% since there are no bicycle class in the network trained.

![img](doc_images/recorded_results.jpeg)

*Figure 3: Performance comparison between Optimized network Vs Recorded Results on Optimized Network*

 

 

 