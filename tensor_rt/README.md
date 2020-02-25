TensorRT Optimization
====================================



TensorRT is an SDK for high-peformance deep learning inference. The workflow follows the picture below. Neural Network training is commonly done on the host, a high-performance PC, and afterwards the model is optimized for deployment on the target platform.



![TensorRT_workflow](docs/tensor_rt_workflow.jpeg)



It is important to mention that the TensorRT optimizer performs platform specific optimizations to guarantee the highest peformance during inference. This means that a serialized engine optimized on the Jetson Xavier AGX is not portable for other platforms (e.g. Jetson Nano). 

Furthermore, TensorRT has a lot of dependencies on the base software in which the Neural Network is trained. TensorRT optimization is not compatible with models trained in some Tensorflow versions. This is mainly due to the Tensorflow API, which renames layers upon releases, leading to TensorRT not to recognize this changes during the optimization phase. This can be circumvented by using graphsurgeon. Nevertheless, for simplicity, this project provides a fully contained environment with the right versions to guarantee a seamless process.



## Setup

 From here onwards we'll assume training is done using our provided environment using Tensorflow-gpu 1.12. Otherwise, successful optimization is not guaranteed.

