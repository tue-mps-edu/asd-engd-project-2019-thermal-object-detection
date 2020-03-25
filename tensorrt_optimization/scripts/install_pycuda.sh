#!/bin/bash
#
# Reference for installing 'pycuda': https://wiki.tiker.net/PyCuda/Installation/Linux/Ubuntu

set -e

if ! which nvcc > /dev/null; then
  echo "ERROR: nvcc not found"
  exit
fi

echo "** Install requirements"
sudo apt-get install -y build-essential python3-dev
sudo apt-get install -y libboost-python-dev libboost-thread-dev

pip3 install pycuda --user

popd

python3 -c "import pycuda; print('pycuda version:', pycuda.VERSION)"
