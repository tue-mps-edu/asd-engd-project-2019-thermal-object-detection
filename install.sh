#!/bin/bash

ROOT_DIR=$PWD
THIRD_PARTY_DIR=$ROOT_DIR/third_party
MODELS_DIR=$THIRD_PARTY_DIR/models

PYTHON=python3

if [ $# -eq 1 ]; then
  PYTHON=$1
fi

echo "Using $PYTHON"

# install protoc
(
source scripts/install_protoc.sh
)

# install tensorflow models
(
git submodule update --init
cd $MODELS_DIR
cd research
sed -i '516s/print num_classes, num_anchors/print(num_classes, num_anchors)/' object_detection/meta_architectures/ssd_meta_arch_test.py
sed -i '147s/print /print(/' object_detection/dataset_tools/oid_hierarchical_labels_expansion.py
sed -i '149s/labels_file"""$/[optional]labels_file""")/' object_detection/dataset_tools/oid_hierarchical_labels_expansion.py
protoc object_detection/protos/*.proto --python_out=.
sudo $PYTHON setup.py install
cd slim
sudo $PYTHON setup.py install
cd $ROOT_DIR
)

# install this project
(
sudo $PYTHON setup.py install
)
