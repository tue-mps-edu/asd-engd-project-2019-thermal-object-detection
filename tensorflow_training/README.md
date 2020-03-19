## Tensorflow Training

This repository is based on [tensorflow object detection API](https://github.com/tensorflow/models/tree/v1.12.0/research/object_detection) and a tutorial on [Custom Object Detection for Nvidia Jetson Nano](https://medium.com/swlh/nvidia-jetson-nano-custom-object-detection-from-scratch-using-tensorflow-and-opencv-113fe4dba134). This setup enables transfer learning with a set of pre-trained deep learning models built into the tensorflow object detection API. Before you can start with the training, be sure to follow the steps and install all the dependencies from the main [README.md](../). 

In supervised deep learning, the recorded data needs to be cleaned and labelled before it can be used for training. It is assumed here that the recorded data is already cleaned and ready for labelling.

![tftworkflow](doc_images/tftworkflow.jpg)

## Data labelling
The most popular labelling formats used for object detection are Common Objects in Context (COCO) and Pascal Visual Object Classes(VOC) which are both suitable for this setup. While the choice between the two is left to user discretion, it should be noted that the workflow for both the formats is marginally different. The data needs to be divided in advanced   change in workflow if used one or the other


To commence the training of the Neural Network, we need annotated [images](images) with their respective annotated files. For annotating images, [Label Image](https://github.com/tzutalin/labelImg)  application is being employed which provides the annotated files in the format of [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) which is a XML file. The images and their corresponding annotated files must have same names and should be divided into two different sets named as training and test data sets.

* [annotated_data](annotated_data/) 
* [label_map](label_map/)
* [model_config](model_config/)
* [model_evalulation](model_evalulation/)
* [model_frozen_inference_graph](model_frozen_inference_graph/)
* [model_training_checkpoints](model_training_checkpoints/)
* [pretrained_baseline_google_models](pretrained_baseline_google_models/)
* [supporting_scripts](supporting_scripts/)
* [training_data](training_data/)

 To commence the training of the Neural Network, we need annotated [images](images) with their respective annotated files. For annotating images, [Label Image](https://github.com/tzutalin/labelImg)  application is being employed which provides the annotated files in the format of [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) which is a XML file. The images and their corresponding annotated files must have same names and should be divided into two different sets named as training and test data sets.

TensorFlow requires the TFRecords format for training. Therefore, we  must convert XML files to TFRecords, in order to begin the training.

```
$  python supporting_scripts/xml_2_tfr.py --xml_input=data/test/  --output_path=training/test.record
$  python supporting_scripts/xml_2_tfr.py --xml_input=data/train/  --output_path=training/train.record
```


```
$  python json_2_tfr.py --input_image_dir=Train_flir/ --input_annotations_file=Train_Flir/thermal_annotation.json --output_dir=Train_tfrecord/
```

Once the process of TFRecords generation has done, move these files to training folder. Alongside adding TFRecords, include .config file of the chosen neural network for the training in the  [training](https://github.com/tue-mps-edu/thermal_object_detection/tree/master/tensorflow_training/training) folder. Config file can be found in the  [samples](https://github.com/tensorflow/models/tree/6518c1c7711ef1fdbe925b3c5c71e62910374e3e/research/object_detection/samples) and can be adjusted according to the requirements by modifying parameters like batch size, number of classes, number of epochs, learning rate and enabling and disabling the dropout layer alongside choosing the dropout keep probability.

Next to this, paths has to be specified for the training and testing data records, .pbtxt file, checkpoint file of the neural network. 

.pbtxt file can be edited depending on the number and types of classes that our network has to be trained. This file is already available in  [training](https://github.com/tue-mps-edu/thermal_object_detection/tree/master/tensorflow_training/training) folder.

```
item {
    id: 1
    name: 'Car'
}
item {
    id: 2
    name: 'Person'
}
```

Checkpoint file can be found in the [ssd_mobilenet_v2_coco_208_03_29](https://github.com/tue-mps-edu/thermal_object_detection/tree/master/tensorflow_training/ssd_mobilenet_v2_coco_2018_03_29) . This folder is available from the link provided. 

[1]: https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

After following these steps, training can be started in the python environment by using the following command.

```
$ python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v2_coco.config
```

During training, use the TensorBoard to catch up the training.

```
$ tensorboard --logdir=training/
```

Once upon finishing the training, the .pb file has to be generated in order to feed it in to the Jetson Xavier for the optimization of inference model. The .pb file is called as frozen inference graph which is an input for loading the model.

```
$ python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssdlite_mobilenet_v2_coco.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
```

Evaluation of the trained network can be done by running eval.py file. Pycocotools needs to be installed on Windows and Linux operating systems. In the Conda virtual environment execute the following commands for respective operating systems.

For Windows:

```
pip install git+https://github.com/philferriere/cocoapi.git#egg=pycocotools^&subdirectory=PythonAPI
```

For Linux:

```
pip install pycocotools
```


# mAP evaluation code 

- Open the anaconda command prompt(virtual environment), the code should be run in the following virtual environment   

  ​    

  ```
  $ activate virtual environment
  $ activate tf1_12_gpu
  ```

  

- Copy the python eval.py file from the legacy folder and paste it where you have your checkpoints and pipeline_config_path saved(folder).

- Run the below code in the virtual environment to get mAP score for entire dataset and each class in both tensorboard and command prompt.
- The mAP score of individual class as well as overall network can then be generated by running eval.py as follows: 

  ```
  
  $ python eval.py --logtostderr --checkpoint_dir=model_for_training/ --  	eval_dir=evaluation/ --pipeline_config_path=model_for_training/ssd_mobilenet_v2_coco.config
  ```



where,

`checkpoint_ dir` = This is the directory where you have your checkpoint meta file which is saved at the end of your training simulation.

`eval_dir`= This the directory where you want your mAP scores to be saved.

`pipeline_config_path=` This is the directory which contains your network configuration file. E.g. ssd_mobilenet_v2_coco.config which you have modified according to your requirement's before training the dataset.
