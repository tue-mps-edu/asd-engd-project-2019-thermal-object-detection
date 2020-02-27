# TensorFlow Training

 To commence the training of the Neural Network, we need annotated [images](images) with their respective annotated files. For annotating images, [Label Image](https://github.com/tzutalin/labelImg)  application is being employed which provides the annotated files in the format of [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) which is a XML file. The images and their corresponding annotated files must have same names and should be divided into two different sets named as training and test data sets.

TensorFlow requires the TFRecords format for training. Therefore, we  must convert XML files to TFRecords, in order to begin the training.

```
$  python xml_2_tfr.py --xml_input=data/test/  --output_path=training/test.record
$  python xml_2_tfr.py --xml_input=data/train/  --output_path=training/train.record
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

Evaluation of the trained network can be done to verify the mAP score of individual class as well as overall network and validate it.

```
python eval.py --logtostderr --checkpoint_dir=training/ --eval_dir=evaluation/ --pipeline_config_path=training/ssd_mobilenet_v2_coco.config
```

