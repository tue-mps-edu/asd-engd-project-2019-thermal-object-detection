## Created on Fri Feb 14 10:20:44 2020
### This script is adopted from google object detection API demo repository hosted at: 
## https://medium.com/swlh/nvidia-jetson-nano-custom-object-detection-from-scratch-using-tensorflow-and-opencv-113fe4dba134

# Refer Dependicies_read.md file to see that you have all the prerequisites.

### Things to be edited before running the script:

# Path to directory for the test or train images change 'path'
# Section 1 is for resize and section 2 is for rename and section 3 is for converting xml to tfrecords

# In section 2 run change the format of file in "if file.endswith(".xml"):" to your requirements

# List of the strings that is used to add correct label for each box.
# PATH_TO_LABELS = os.path.join('Folder_name_for_model_configuration_file', 'Name_of_configeration_file.pbtxt')

# Setup test and train images path with test and train records

#PATH_TEST = "Path of the test data"
#PATH_RECORD_TEST = "do not change it"
#PATH_TRAIN = "Path of the train data"
#PATH_RECORD_TRAIN = "do not change it"

### Run each section individually

### @Authors: t.s.r.parvathaneni@tue.nl(Ram), s.m.patwardhan@tue.nl (Sukrut)

##+++++++++++++++++++++++++====================================++++++++++++++++++++++++++++++++++++++
from PIL import Image
import tensorflow as tf
import os

flags = tf.imagesort.flags
flags.DEFINE_string('xml_input', '', 'Path to the xml input')
FLAGS = flags.FLAGS



# SECTION 1 ========= Rename XML
def rename(path_input):
os.chdir(path_input)
dirs = os.listdir(path_input)
    i = 0
    for item in dirs:
        if os.path.isfile(path+item):
            file = (path+item)
            if file.endswith(".xml"):
                dst ="image_" + str(i) + ".xml"
                src = path + item
                os.rename(src, dst) 
                i=i+1
                print("done image " + str(i))
    return
rename()

## SECTION 2 ========= Rename JPEG
# def rename(path_input):
#     i = 0
#     for item in dirs:
#         if os.path.isfile(path+item):
#             file = (path+item)
#             if file.endswith(".xml"):
#                 dst ="image_" + str(i) + ".xml"
#                 src = path + item
#                 os.rename(src, dst) 
#                 i=i+1
#                 print("done image " + str(i))
#     return
# rename()

if __name__ == '__main__':
    tf.imagesort.run()