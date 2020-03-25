#!/bin/bash

set -e

#Set the paths to .bashrc
if ! grep 'cuda/bin' ${HOME}/.bashrc > /dev/null ; then
  echo "** Add CUDA stuffs into ~/.bashrc"
  echo >> ${HOME}/.bashrc
  echo "export PATH=/usr/local/cuda/bin:\${PATH}" >> ${HOME}/.bashrc
  echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:\${LD_LIBRARY_PATH}" >> ${HOME}/.bashrc
fi

source ~/.bashrc

#Install Tensorflow

sudo apt-get update
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev
sudo apt-get install python3-pip
sudo pip3 install -U pip testresources setuptools
sudo pip3 install -U numpy==1.16.1 future==0.17.1 mock==3.0.5 h5py==2.9.0 keras_preprocessing==1.0.5 keras_applications==1.0.8 gast==0.2.2 enum34 futures protobuf

sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v43 tensorflow-gpu==1.15.0+nv19.12

#sudo pip3 install cython
# install pycuda if necessary
source ~/.bashrc

if ! python3 -c "import pycuda" > /dev/null 2>&1; then
  echo "installing pycuda..."
  scripts/install_pycuda.sh
fi

echo "** Patch 'graphsurgeon.py' in TensorRT"

script_path=$(realpath $0)
gs_path=$(ls /usr/lib/python3.?/dist-packages/graphsurgeon/node_manipulation.py)
patch_path=$(dirname $script_path)/graphsurgeon.patch

if head -30 ${gs_path} | tail -1 | grep -q NodeDef; then
  # This is for JetPack-4.2
  sudo patch -N -p1 -r - ${gs_path} ${patch_path}-4.2 && echo
fi
if head -22 ${gs_path} | tail -1 | grep -q update_node; then
  # This is for JetPack-4.2.2
  sudo patch -N -p1 -r - ${gs_path} ${patch_path}-4.2.2 && echo
fi

echo "** Making symbolic link of libflattenconcat.so"

trt_version=$(echo /usr/lib/aarch64-linux-gnu/libnvinfer.so.? | cut -d '.' -f 3)
ln -sf libflattenconcat.so.${trt_version} libflattenconcat.so

echo "** Installation done"
