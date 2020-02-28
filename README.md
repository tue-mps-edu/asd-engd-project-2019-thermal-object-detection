Thermal Camera Detection
====================================

This repository is based on NVIDIA's [tf_trt_models](https://github.com/NVIDIA-Jetson/tf_trt_models) and [jkjung's](https://github.com/jkjung-avt/tf_trt_models) fork of NVIDIA's repository, along with the [TensorRT](https://github.com/jkjung-avt/tensorrt_demos) repository. Below, you will find an index of the contents of this repository so you can use them based on your needs. However, to fully understand the pipeline, we advice you to follow them in order. Also, be sure to first follow the setup process for the scripts to work properly.

* [Project Description](docs/)
* [Training](tensorflow_training/)
* [TensorRT optimization](tensorrt/)
* [Camera Integration and Deployment](src/)



## Setup

In order to run the code in this repository, it is necessary that the host computer used for training, as well as the target platform used for online inference have the necessary software already installed. To facilitate this process, we provide a set of installation scripts. Please refer to the following sections to setup each accordingly.

- [Host Setup](#Host Setup) 
  - Lenovo Thinkpad P1 (Intel Core i7 8750H @2.20 GHz), Nvidia Quadro P1000 Graphics.
- [Target Platform Setup](#Target Platform Setup)
  - Nvidia Jetson Xavier AGX

<a name="Host Setup"></a>

## Host Setup

In order to use this repository, you must first make sure that the host computer has the latest NVIDIA drivers installed. Afterwards, you will need Anaconda3 to a virtual environment (conda) using the *yml* file provided in the repository.



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

<em>Note: Be sure to restart the terminal before attempting to create the new conda environment. This is to allow conda to initialize the base environment via the .bashrc file on the home directory </em>



Afterwards, run the installation script. This bash script will update the submodules, pulling the tensorflow models from a particular commit, and install the object detection API to facilitate training and development. 

```
$ conda activate tf1_12_gpu

$ ./install.sh
```



If everything goes smoothly, you should be able to seamlessly execute the scripts provided in this repository. 

```
$ cd tensorflow_training

$ python model_builder_test.py
```



This script verifies the installation of the setup, along with its dependencies. You should see the following output.

```
..................
----------------------------------------------------------------------
Ran 18 tests in 0.062s

OK
```



<a name="Target Platform Setup"></a>

## Target Platform Setup

In order to perform inference on the NVIDIA Xavier AGX , you must ensure the latest Jetpack version is installed in the target platform. At the time of writing, the system was tested using Jetpack 4.3, which comes with all the necessary dependencies to get up and running in no time (Cuda, CuDNN, OpenCV). The steps for installation can be found on [NVIDIA's website](https://developer.nvidia.com/embedded/jetpack).

Once Jetpack is installed, run the install script located in this folder. This script will add extra paths, dependencies and patches required to run the optimization process.

```
$ cd tensorrt
$ ./install.sh
```

Furthermore, in case the built-in memory of the Jetson Xavier AGX is not enough for some models, you can run the following to allocate extra swap memory.

```
$ scripts/installSwapfile.sh
```

*Note: This step is optional. However, if you decide to go ahead, be sure to reboot your system for all changes to apply.*

