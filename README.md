Thermal Camera Detection
====================================

This repository is based on NVIDIA's [tf_trt_models](https://github.com/NVIDIA-Jetson/tf_trt_models) and [jkjung's](https://github.com/jkjung-avt/tf_trt_models) fork of NVIDIA's repository. Below, you will find an index of the contents of this repository so you can use them based on your needs. However, to fully understand the pipeline, we advice you to follow them in order. Also, be sure to first follow the setup process for the scripts to work properly.

* [Project Description](docs/)
* [Training](tensorflow_training/)
* [TensorRT optimization](tensor_rt/)
* [Camera Integration and Deployment]()

<a name="setup"></a>

## Setup

In order to use this repository, you must first make sure that the host computer has the latest NVIDIA drivers installed. Afterwards, you will need Anaconda3 to make use setup a virtual environment using the yml file provided in the repository.



Refer to these links to install the prerequisites:

- [NVIDIA drivers](http://www.linuxandubuntu.com/home/how-to-install-latest-nvidia-drivers-in-linux)

- [Anaconda Install](https://www.anaconda.com/distribution/)

  

Once these prerequisites have been met, clone this repository

```
$ git clone https://github.com/Hrayo712/tf_trt_models
```

<em>Note: The repository includes tensorflow object detection API submodules under the third_party folder. These can be cloned automatically by adding the --recursive flag to the clone command. Otherwise, the install script will do it for you.</em>



After cloning the repository, setup the conda environment with the given <em>yml</em> file to create the virtual environment with all the required dependencies. This process can take a while.

```
$ cd tf_trt_models
$ conda env create -f environment/tf1_12_gpu.yml
```



Afterwards, run the installation script. This bash script will update the submodules, pulling the tensorflow models from a particular commit, and install the object detection API to facilitate training and development. 

```
$ conda activate tf1_12_gpu

$ ./install.sh
```

if everything goes smoothly, you should be able to seamlessly execute the scripts provided in this repository.

