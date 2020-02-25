TensorRT Optimization
====================================

This part of the repository is based on jkjung's [tensorrt](https://github.com/jkjung-avt/tensorrt_demos) repository.

TensorRT is an SDK for high-peformance deep learning inference. The workflow follows the picture below. Neural Network training is commonly done on the host, a high-performance PC, and afterwards the model is optimized for deployment on the target platform.



![TensorRT_workflow](docs/tensor_rt_workflow.jpeg)



It is important to mention that TensorRT performs platform specific optimizations to guarantee the highest performance during inference. **This means that a serialized engine optimized on the Jetson Xavier AGX is not portable between platforms (e.g. Jetson Nano).** 

Furthermore, TensorRT has a lot of dependencies with the software in which the Neural Network is trained. TensorRT optimization is not compatible with models trained in some Tensorflow versions. This is mainly due to the Tensorflow API, which renames nodes upon releases. This ultimately results in TensorRT not recognizing some of them during the optimization phase. This can be circumvented by using graphsurgeon to remove/rename nodes. Nevertheless, for simplicity, this project provides a fully contained environment with the right versions to guarantee a seamless process.

*Note: At the time of writing, UFF and ONNX parsers are supported by TensorRT. Nevertheless, at this point we'll only work with the UFF parser.*

## Setup

From here onwards we'll assume the [training phase](../tensorflow_training) is done using our provided environment with Tensorflow-gpu 1.12. Otherwise, successful optimization is not guaranteed. Furthermore, we'll assume the target platform is the NVIDIA Xavier AGX. 

Before proceeding with the optimization, you must ensure the latest Jetpack version is installed in the target platform. At the time of writing, the system was tested using Jetpack 4.3, which comes with all the necessary dependencies to get up and running in no time (Cuda, CuDNN, OpenCV). The steps for installation can be found on [NVIDIA's website](https://developer.nvidia.com/embedded/jetpack).

Once Jetpack is installed, go to the tensor_rt folder in this repository and run the install script. This script will add extra paths, dependencies and patches required to run the optimization process.

```
$ cd tensor_rt
$ ./install.sh
```



