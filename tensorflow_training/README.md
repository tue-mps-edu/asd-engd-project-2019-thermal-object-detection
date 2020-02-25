TensorFlow Training
====================================

In order to exemplify the training process, we provide [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) annotated car [images](images) to test the training procedure. This process can be replicate with whichever dataset you wish, following the same steps. Annotation were made using [lblImage](https://github.com/tzutalin/labelImg).



Tensorflow requires the TFRecords format for training. Therefore, we must convert xml files to CSV, in order to finally create the records files for training.

```
$ python xml_to_csv.py
```

Afterwards, we convert the CSV files to records. This must be done for training and testing images.

```
$ python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=data/train.record --image_dir=images/

$ python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=data/test.record --image_dir=images/
```

...and so on