# Testing and Results

This folder has two sections:

The first section contains the beta test plan and its post analysis documentation including the images of assembly of the hardware on the car.

-  [Beta Test Plan](beta_test_plan/README.md)

The second section contains all the sub sections of the documentation on different types of tests performed during the training of neural network architecture along with the discussion on their results. The topics that are listed as follows:

- [Evaluation Metric](tensorflow_training_and_optimisation_results/evaluation_metric/README.md)

  This sub section is having the elaborate description of the metric that has been chosen for this project. To be specific, discussion about choosing mAP(Mean Average Precision) over the other metrics.

- [Object Detection Architectures Benchmarks](tensorflow_training_and_optimisation_results/object_detection_architecture_benchmarks/README.md)

  This sub section is related to details of choosing the specific neural network architecture between the available architectures based on their performance. 

- [Tweaking and Tuning of Hyperparameters](tensorflow_training_and_optimisation_results/tweaking_and_tuning_hyperparameters/README.md) 

  This sub section describes the type of hyperparameters have chosen to improve the performance of the  neural network. A detailed explanation of each parameter effect on the neural network performance after training was discussed in this section.

- [Results of Recorded Data Training](tensorflow_training_and_optimisation_results/recorded_data_training_results)

  This sub section contains all inclusive details of the results obtained after training the neural network on the recorded data in different ways than usual.
  
- [Optimisation Results](tensorflow_training_and_optimisation_results/optimisation_results/README.md)

  This sub section consists of document that intends to demonstrate the performance improvement enabled by TensorRT optimization in terms of inference speed on the SSD MobileNet v2 architecture. 

