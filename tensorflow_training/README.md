## Tensorflow Training

This repository is based on [tensorflow object detection API](https://github.com/tensorflow/models/tree/v1.12.0/research/object_detection) and a tutorial on [Custom Object Detection for Nvidia Jetson Nano](https://medium.com/swlh/nvidia-jetson-nano-custom-object-detection-from-scratch-using-tensorflow-and-opencv-113fe4dba134). This setup enables transfer learning with a set of pre-trained deep learning models built into the tensorflow object detection API. Before you can start with the training, be sure to follow the steps and install all the dependencies from the main [README.md](../). 

In supervised deep learning, the recorded data needs to be cleaned and labelled before it can be used for training. It is assumed here that the recorded data is already cleaned and ready for labelling.


![tftworkflow](doc_images/tftworkflow.jpg)

*Figure 1: General workflow of tensorflow training* 

## Data Split
As a first step, unannotated dataset needs to be divided into two subsets namely training and testing. A training subset, as the name suggests, is used to train the model, while test subset is used to test the trained model.Please note that test subset is only used when the model is completely trained in order to evaluate its performance. As a general guideline, the complete dataset is divided into the subsets of  80% training and 20% testing. More information on this topic can be found at  [Training and Test Sets: Splitting Data](https://developers.google.com/machine-learning/crash-course/training-and-test-sets/splitting-data).

The divided data should then be kept in the [data](data/) directory. As an example a Dummy_dataset in the required format is showm as follows 
 
```
data
 ├── Dummy_dataset
 │ ├── train
 │ ├── test
```

<em>Note: For reference, [data](data/) folder also includes datasets recorded during the project as well thermal data set provided by Flir. </em>

## Data labelling
After the data is sorted as per [Data Split](#Datasplit), we can now proceed to label the data. The most popular labelling formats used for object detection are Common Objects in Context (COCO) and Pascal Visual Object Classes(VOC) which are both suitable for this setup.COCO uses JSON format while Pascal VOC uses XML for the annotated data. The choice between the two is left to user discretion, since these annotated files are ultimately converted to a cross-platform and cross-language binary format(TFRecord) as shown in Figure 1. 
An example of annotation XML file for a image in a Pascal VOC format is shown below.
```
<object>
	<name>fig</name>
	<pose>Unspecified</pose>
	<truncated>0</truncated>
	<difficult>0</difficult>
	<bndbox>
		<xmin>256</xmin>
		<ymin>27</ymin>
		<xmax>381</xmax>
		<ymax>192</ymax>
	</bndbox>
</object>
```

While an example of annotation JSON file with data for one image in COCO format can be shown as follows.
```
{
  "type": "instances",
  "images": [
    {
      "file_name": "0.jpg",
      "height": 600,
      "width": 800,
      "id": 0
    }
  ]
  "categories": [
    {
      "supercategory": "none",
      "name": "date",
      "id": 0
    }
  ]
  "annotations": [
    {
      "id": 1,
      "bbox": [
        100,
        116,
        140,
        170
      ],
      "image_id": 0,
      "segmentation": [],
      "ignore": 0,
      "area": 23800,
      "iscrowd": 0,
      "category_id": 0
    }
  ]
}
```

As seen in the above examples, there is significant difference between the two formats as described below.

* Bounding boxes - 
Pascal VOC bounding box is the x and y co-ordinates of the top left and x and y co-ordinates of the bottom right edge of the rectangle.On the other hand, bounding box in COCO is the x and y co-ordinate of the top left and the height and width.
* Data storage - Annotations in COCO format generate a single JSON file for the whole dataset while Pascal VOC creates separate XML files per image.

Despite these differences, it should be noted that choosing either format does not impact model training.However it has  an impact on the tool you choose for labelling the data. For annotating the images in both the formats, several open source softwares are available. As an example [VGG Image Annotator](http://www.robots.ox.ac.uk/~vgg/software/via/) can be used for COCO annotations while [LabelImg](https://github.com/tzutalin/labelImg) can be used to annotate in PASCAL VOC format.   

It should be ensured that the images and their corresponding annotated files must have same names when using Pascal VOC format. The final folder for Pascal VOC should look like
```
data
 ├── Dummy_dataset
 │ ├── train
 │ │ ├── image_name_0.jpg
 │ │ ├── image_name_0.xml
 │ │ ├── ...
 │ │ ├── image_name_N.jpg
 │ │ ├── image_name_N.xml
 │ ├── test
 │ │ ├── image_name_0.jpg
 │ │ ├── image_name_0.xml
 │ │ ├── ...
 │ │ ├── image_name_N.jpg
 │ │ ├── image_name_N.xml
```

On the other hand, the final directory for datasets annotated in COCO format should look like 
```
data
 ├── Dummy_dataset
 │ ├── train
 │ │ ├── images_directory
 │ │ │ ├── image_name_0.jpg
 │ │ │ ├── ...
 │ │ │ ├── image_name_N.jpg
 │ │ ├── annotation_file.json
 │ ├── test
 │ │ ├── images_directory
 │ │ │ ├── image_name_0.jpg
 │ │ │ ├── ...
 │ │ │ ├── image_name_N.jpg
 │ │ ├── annotation_file.json
```

## Conversion to tfrecords
TFRecord is a binary cross-platform, cross-language format used for efficient serialization of structured data. On top of being cross-platform, tfrecords offers crucial performance benefits  (e.g. faster read speeds, less storage) and has ability to handle large datasets.As a result, tensorflow uses tfrecords as its only supported input format.More information about the format can be found at [TFRecord and tf.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord) and at [Tensorflow Records? What they are and how to use them](https://medium.com/mostly-ai/tensorflow-records-what-they-are-and-how-to-use-them-c46bc4bbb564) .

In order to convert the [annotated data](#Data%20labelling) from the earlier steps, open terminal /command prompt and navigate to the `tensorflow_training` folder in the repository. Write the following command to initialize virtual conda environment installed from the main [README.md](../).

```
$ conda activate tf1_12_gpu
```
Next, depending upon the labelling format, please follow the instructions either from `Only for the Pascal_VOC` section or from `Only for the COCO` section.

 `Only for the Pascal_VOC` format issue the following commend to generate tfrecord file for the annotated data. Please note that this command is an example which creates tfrecords for Dummy_dataset. The input path for your test and train directories needs to be configured before issuing this command.  

```
$  python supporting_scripts/xml_tfrecord.py --xml_input=data/Dummy_dataset/test/  --output_path=tfrecords/test_tfr/test.record

$  python supporting_scripts/xml_tfrecord.py --xml_input=data/Dummy_dataset/train/  --output_path=tfrecords/train_tfr/train.record
```

where,

`xml_input` = Relative path to test/ train directory containing images and corresponding XML files. 

`output_path`= This is the output path for the generated tfrecords file. User doesn't need to change this path.

The generated tfrecord files can be found inside [tfrecords](tfrecords/) folder. We can now proceed to the next section in order to create a [Label map](#Labelmap).

`Only for the COCO` format issue the following commend to generate tfrecord file for the annotated data.Please note that this command is an example which creates tfrecords for Flir dataset. The input path for your test and train directories needs to be configured before issuing this command. 

```
$  python json_tfrecord.py --input_image_dir=data/Flir/test/thermal_8_bit --input_annotations_file=data/Flir/test/thermal_annotations.json --output_dir=tfrecords/test_tfr/test.record

$  python json_tfrecord.py --input_image_dir=data/Flir/train/thermal_8_bit --input_annotations_file=data/Flir/train/thermal_annotations.json --output_dir=tfrecords/train_tfr/train.record
```

where,

`input_image` = Relative path to test/ train directory containing images.

`input_annotations_file`=  Relative path to test/ train directory containing JSON annotation file.

`output_dir`= This is the output path for the generated tfrecords file. User doesn't need to change this path.

The generated tfrecord files can be found inside [tfrecords](tfrecords/) folder. We can now proceed to the next section in order to create a [Label map](#Labe%20lmap)

## Label map

After [generating tfrecords](#Conversion%20to%20tfrecords) for test and train data, next step is to create a label map associated with the dataset.This label map defines a mapping from string class names to integer class Ids. It should include all the classes included in annotated data. As an important note, tensorflow can only read Label maps starting from id 1.
A sample label map is shows as follows.
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

These maps can be created and edited using any text editor. However they must be saved as .pbtxt file instead of .txt file. The map should be placed in [label_map](label_map/) folder.A sample file of the label map is provided in the same folder.

## Model configuration

As a next step we need to download the pre-trained models that we want to use as a base model for our training. Download links of all the supported models can be located at [pre-trained models for tensorflow](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). Once the model is downloaded, unzip the model and place it in the [pretrained_baseline_google_models](pretrained_baseline_google_models/) folder. As an example, a ssd_mobilenet_v2 model is shown below to illustrate the final outcome of this step.
```
pretrained_baseline_google_models
 ├── ssd_mobilenet_v2_coco_2018_03_29
 │ ├── saved_model
 │ ├── checkpoint
 │ ├── frozen_inference_graph.pb
 │ ├── model.ckpt.data-00000-of-00001
 │ ├── model.ckpt.index
 │ ├── model.ckpt.meta
 │ ├── pipeline.config
```

<em>**Note: For reference, [pretrained_baseline_google_models](pretrained_baseline_google_models/) folder already includes  base models for ssd_mobilenet_v2_coco and aster_rcnn_inception_v2_coco. You need to do this step only when you need to use different models other than stated.**</em>

To configure the training and evaluation process of the model discussed earlier, tensorflow object detection API uses a configuration file. At a high level, the configuration file is split into five parts:
* `model configuration` - This defines what type of model will be trained (ie. meta-architecture, feature extractor).
* `train_config` - This decides what parameters should be used to train model parameters (ie. Stochastic gradient descent  parameters, input preprocessing and feature extractor initialization values).
* `eval_config` - This determines what set of metrics will be reported for evaluation.
* `train_input_config` - This defines what dataset the model should be trained on.
* `eval_input_config` - This defines what dataset the model will be evaluated on. Typically this should be different than the training input dataset.


The skeleton of configuration file is shown below
```
model {
(... Add model config here...)
}

train_config : {
(... Add train_config here...)
}

train_input_reader: {
(... Add train_input configuration here...)
}

eval_config: {
}

eval_input_reader: {
(... Add eval_input configuration here...)
}
```

Depending on the model to be trained (e.g MobilenetV2, ResNET), a corresponding sample file for model configuration should be downloaded from [object detection sample configs](https://github.com/tensorflow/models/tree/v1.12.0/research/object_detection/samples/configs) and placed in [model_config](model_config/) folder.The configuration file has .config extension and can be edited with any simple text editor. Configuration file for ssd_mobilenet_v2_coco is already provided in the [model_config](model_config/) as an example.

This configuration file allows us to tweak several hyper-parameters of the model such as batch size, number of classes, number of epochs, optimizers, learning rate dropout and data augmentation.For transfer learning, `train_input_config`, `eval_config` and `eval_input_config` are essential since we need to provide relevant paths to tfrecords, label maps  and  base models in these sections. To elaborate further, aforementioned sections of a configuration file for SSD MobilenetV2 are shown below as an example. 

```
train_config: {
  batch_size: 24
  optimizer {
    rms_prop_optimizer: {
      learning_rate: {
        exponential_decay_learning_rate {
          initial_learning_rate: 0.004
          decay_steps: 800720
          decay_factor: 0.95
        }
      }
      momentum_optimizer_value: 0.9
      decay: 0.9
      epsilon: 1.0
    }
  }
  fine_tune_checkpoint: "PATH_TO_BE_CONFIGURED/model.ckpt"
  fine_tune_checkpoint_type:  "detection"
  # Note: The below line limits the training process to 200K steps, which we
  # empirically found to be sufficient enough to train the pets dataset. This
  # effectively bypasses the learning rate schedule (the learning rate will
  # never decay). Remove the below line to train indefinitely.
  num_steps: 200000
  data_augmentation_options {
    random_horizontal_flip {
    }
  }
  data_augmentation_options {
    ssd_random_crop {
    }
  }
}
```

For the above section, we need to add the absolute path to the model placed in [pretrained_baseline_google_models](pretrained_baseline_google_models/) folder to the following line:

fine_tune_checkpoint: "PATH_TO_BE_CONFIGURED/model.ckpt"

This allows the us to load a pre-trained model as a base for our training. Its important to know that most of this model are "frozen" in a sense that their weights wont change as we train the model with our data. Since layers only specific to a class such as feature extractor are getting trained while retaining the weights in frozen layers, this parameter allows us to fine tune the model to our use case.   

```
train_input_reader: {
  tf_record_input_reader {
    input_path: "PATH_TO_BE_CONFIGURED/tfrecords/train_tfr/train.record"
  }
  label_map_path: "PATH_TO_BE_CONFIGURED/label_map.pbtxt"
}
```

Furthermore we need to provide absolute path to the train tfrecord file located at [tfrecords](tfrecords/) folder to the `eval_input_reader` section shown above.

input_path: "PATH_TO_BE_CONFIGURED/tfrecords/train_tfr/train.record"

We also need add path to the label map file placed [label_map](label_map/) folder in this section of the configuration file.

label_map_path: "PATH_TO_BE_CONFIGURED/label_map.pbtxt"

```
eval_config: {
  num_examples: 8000
  # Note: The below line limits the evaluation process to 10 evaluations.
  # Remove the below line to evaluate indefinitely.
  max_evals: 10
}
eval_input_reader: {
  tf_record_input_reader {
    input_path: "PATH_TO_BE_CONFIGURED/tfrecords/test_tfr/test.record"
  }
  label_map_path: "PATH_TO_BE_CONFIGURED/label_map.pbtxt"
  shuffle: false
  num_readers: 1
}
```
In the `eval_config` section shown above, the parameter `num_examples` should be equal total number test images based on your [data split](#Data%20Split). Finally we need to provide absolute path to the test tfrecord file located at [tfrecords](tfrecords/) to the `eval_input_config` section shown above.

input_path: "PATH_TO_BE_CONFIGURED/tfrecords/train_tfr/train.record"

We also need add path to the same label map file used earlier located in [label_map](label_map/) folder.

label_map_path: "PATH_TO_BE_CONFIGURED/label_map.pbtxt"

After making all the changes above save the file and now we are ready to start training.

## Model training
Checklist
remove older frozen grpahs

## Model evaluation





* [model_evalulation](model_evalulation/)
* [model_frozen_inference_graph](model_frozen_inference_graph/)
* [model_training_checkpoints](model_training_checkpoints/)
* [supporting_scripts](supporting_scripts/)





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
