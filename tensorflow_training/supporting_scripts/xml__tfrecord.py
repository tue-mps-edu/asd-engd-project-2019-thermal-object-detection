#Created on Fri Feb 14 10:20:44 2020
# This script is adopted from google object detection API demo at:
# https://medium.com/swlh/nvidia-jetson-nano-custom-object-detection-from-scratch-using-tensorflow-and-opencv-113fe4dba134
# Refer Dependicies_read.md file to see that you have all the prerequisites.
#@Authors: t.s.r.parvathaneni@tue.nl(Ram), s.m.patwardhan@tue.nl (Sukrut)

## SECTION 1 ========= XML to TFRecords

  # Importing all necessary libraries
import xml.etree.ElementTree as ET
import tensorflow as tf
from object_detection.utils import dataset_util
import os
# This are the path to the datasets and to the output files.
# NEED TO BE UPDATED IN CASE THE DATASET CHANGES

flags = tf.app.flags
flags.DEFINE_string('xml_input', '', 'Path to the xml input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')

FLAGS = flags.FLAGS



IMAGE_EXT = ".jpg"
IMAGE_FORMAT = b'jpg'

# This function defines the different classes the dataset has and return a different number per each.
# NEED TO BE UPDATED IN CASE THE DATASET CHANGES
def class_text_to_int(row_label):
    if row_label == 'car':
        return 1
    print('car')


# Reads the xml and the images, and create the tf records files.
def xml_to_tf(path_input, path_output):
    xml_list = []
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

    writer = tf.python_io.TFRecordWriter(path_output)

    files = os.listdir(path_input)
    for file in files:
        if file.endswith(".xml"):
            xmlFile = path_input + file

            tree = ET.parse(xmlFile)
            root = tree.getroot()

            filename = root[1].text #+ IMAGE_EXT
            width = int(root[4][0].text)
            height = int(root[4][1].text)

            xmins = []
            xmaxs = []
            ymins = []
            ymaxs = []
            classes_text = []
            classes = []


            for member in root.findall('object'):
                car = member[0].text
                xmin = int(member[4][0].text)
                ymin = int(member[4][1].text)
                xmax = int(member[4][2].text)
                ymax = int(member[4][3].text)

                xmins.append(xmin/width)
                xmaxs.append(xmax/width)
                ymins.append(ymin/height)
                ymaxs.append(ymax/height)
                classes_text.append(car.encode('utf8'))
                classes.append(class_text_to_int(car))

            with tf.gfile.GFile(os.path.join(path_input, '{}'.format(filename)), 'rb') as fid:
                encoded_jpg = fid.read()
            tf_example = tf.train.Example(features=tf.train.Features(feature={
                'image/height': dataset_util.int64_feature(height),
                'image/width': dataset_util.int64_feature(width),
                'image/filename': dataset_util.bytes_feature(filename.encode('utf8')),
                'image/source_id': dataset_util.bytes_feature(filename.encode('utf8')),
                'image/encoded': dataset_util.bytes_feature(encoded_jpg),
                'image/format': dataset_util.bytes_feature(IMAGE_FORMAT),
                'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
                'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
                'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
                'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
                'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
                'image/object/class/label': dataset_util.int64_list_feature(classes),
            }))
            return tf_example



def main(_):
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)

    tf_example = xml_to_tf(FLAGS.xml_input, FLAGS.output_path)
    writer.write(tf_example.SerializeToString())
    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))

if __name__ == '__main__':
    tf.app.run()
