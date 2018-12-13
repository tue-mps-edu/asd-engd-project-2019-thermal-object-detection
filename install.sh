#!/bin/bash

INSTALL_PROTOC=$PWD/scripts/install_protoc.sh
MODELS_DIR=$PWD/third_party/models
PYTHON=python3

echo "Using $PYTHON"

# install protoc
echo "Downloading protoc"
source $INSTALL_PROTOC
PROTOC=$PWD/data/protoc/bin/protoc

# install tensorflow models
git submodule update --init

pushd $MODELS_DIR/research
echo $PWD
sed -i '516s/print num_classes, num_anchors/print(num_classes, num_anchors)/' \
       object_detection/meta_architectures/ssd_meta_arch_test.py
sed -i '147s/print /print(/' \
       object_detection/dataset_tools/oid_hierarchical_labels_expansion.py
sed -i '149s/labels_file"""$/[optional]labels_file""")/' \
       object_detection/dataset_tools/oid_hierarchical_labels_expansion.py
sed -i '281s/loss_tensor in losses_dict.itervalues()/_, loss_tensor in losses_dict.items()/' \
       object_detection/model_lib.py
sed -i '380s/category_index.values(),/list(category_index.values()),/' \
       object_detection/model_lib.py
sed -i '390s/iteritems()/items()/' \
       object_detection/model_lib.py
sed -i '168s/range(num_boundaries),/list(range(num_boundaries)),/' \
       object_detection/utils/learning_schedules.py
$ROOT_DIR/protoc-3.5.1/bin/protoc object_detection/protos/*.proto --python_out=.
echo "Installing object detection library"
echo $PROTOC
$PROTOC object_detection/protos/*.proto --python_out=.
$PYTHON setup.py install --user
popd

pushd $MODELS_DIR/research/slim
echo $PWD
echo "Installing slim library"
$PYTHON setup.py install --user
popd

echo "Installing tf_trt_models"
echo $PWD
$PYTHON setup.py install --user
