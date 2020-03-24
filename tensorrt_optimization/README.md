TensorRT Optimization
====================================



This part of the repository is based on jkjung's [TensorRT](https://github.com/jkjung-avt/tensorrt_demos) repository. This setup enables the seamless optimization of the SSD Mobilenet model trained on TensorFlow-GPU version 1.12. Before you can run the scripts in this folder, be sure to follow the installation instructions for the target platform located in the main [README.md](../).



## Background

TensorRT is an SDK for high-performance Deep Learning inference. The TensorRT workflow is shown in Figure1. Models trained on AI development platforms such as TensorFlow, Pytorch, etc. are imported by the TensorRT Optimizer to perform ***target-specific*** [optimizations](http://on-demand.gputechconf.com/gtcdc/2017/presentation/dc7172-shashank-prasanna-deep-learning-deployment-with-nvidia-tensorrt.pdf). Afterward, a serialized engine (binary file) with optimal execution speed is generated, enabling it to be easily deployed on production.



![TensorRT_workflow](docs/tensor_rt_workflow.jpeg)

*Figure 1: [TensorRT worfkflow](https://docs.nvidia.com/deeplearning/sdk/tensorrt-developer-guide/index.html).*

**IMPORTANT:** TensorRT performs platform specific optimizations to guarantee the highest performance during inference. **This means that serialized engines are not portable across platforms.** 

Furthermore, as TensorRT performs optimizations on models trained on different frameworks (and versions of these), some dependencies and intricacies should be taken into account when using TensorRT. For example, TensorRT is not compatible *out-of-the-box* with models trained in some Tensorflow versions. This is mainly due to the Tensorflow API, which renames nodes upon releases. This ultimately results in TensorRT not recognizing some of them during the optimization phase. This can be circumvented by using [GraphSurgeon](https://docs.nvidia.com/deeplearning/sdk/tensorrt-api/python_api/graphsurgeon/graphsurgeon.html) to remove/rename nodes. Nevertheless, this requires in-depth knowledge of each Neural Network model. Therefore, for simplicity, this project provides a fully contained environment with the right versions to guarantee a seamless process. More specifically, [model training](../tensorflow_training/) is done using TensorFlow-GPU version 1.12, and TensorRT 6.0.1 (included in [Jetpack](https://developer.nvidia.com/embedded/jetpack)).



##  Running the Optimization

From here onwards, it is assumed that [model training](../tensorflow_training) is done using the training environment provided by this repository. Otherwise, successful optimization is not guaranteed.

To perform TensorRT optimization, the first step is to convert frozen graph models (.pb files) to a format that can be consumed by TensorRT. To do this, TensorRT provides a set of parsers, out of which we will use [UFF](https://docs.nvidia.com/deeplearning/sdk/tensorrt-api/python_api/uff/uff.html). The parser will output a *.uff* file which will be used to build the Engine. To facilitate this process, the *build_engine.py* script performs these steps altogether creating a *.bin* file as the output engine. Moreover, a *.pbtxt* file is saved for debugging purposes in case an error occurs during the optimization process.

The given build engine script is already setup to out-of-the-box optimize the frozen graph included in this folder (ssd_mobilenet_v2_thermal.pb). Nevertheless, in case you need to modify the script to accommodate different requirements, some changes would be required on the MODEL_SPECS definition inside the script.

```
MODEL_SPECS = {

    'ssd_mobilenet_v2_thermal': {
        'input_pb':   os.path.abspath(os.path.join(
                          DIR_NAME, 'ssd_mobilenet_v2_thermal.pb')),
        'tmp_uff':    os.path.abspath(os.path.join(
                          DIR_NAME, 'ssd_mobilenet_v2_thermal.uff')),
        'output_bin': os.path.abspath(os.path.join(
                          DIR_NAME, 'TRT_ssd_mobilenet_v2_thermal.bin')),
        'num_classes': 4,
        'min_size': 0.2,
        'max_size': 0.95,
        'input_order': [0, 2, 1],  # order of loc_data, conf_data, priorbox_data
    },
}
```

First,  *num_classes* must match the number of classes of the given model, plus an additional one (to account for the background). Furthermore, the *min_size* and *max_size* parameters should match the *min_scale* and *max_scale* parameters on the model configuration file used for training. Additionally, DIR_NAME is by default the directory in which the script is executed, therefore, the frozen graph file should be in the same directory. 

Finally, the *input_order* parameter should be configured in a trial and error manner. The advice is to follow the [0, 2, 1] pattern. If this fails, you should verify the generated *.pbtxt* and look for the following lines. 

```
graphs {
	id: "main"
	nodes {
		id: "NMS"
		inputs: "squeeze"
		inputs: "concat_priorbox"
		inputs: "concat_box_conf"
		operation: "_NMS_TRT"
		fields {
		key: "backgroundLabelId_u_int"
		value {
			i: 1
.
.
.
```

The logic is the following: 

*input_order* lists the order in which *loc_data*, *conf_data* and *priorbox_data* appear in the *.pbtxt* file. *loc_data* appears first (squeeze), therefore, it is on index 0. *conf_data* appears last, therefore it is on index 2. Finally priorbox_data is index 1, thus, creating [0, 2, 1].



Finally, run the following command to optimize the model.

```
$ python3 build_engine.py ssd_mobilenet_v2_thermal
```

*Note: This process might take a while depending on the target platform.*

If everything went smoothly, you should see no errors on the screen. The engine is now the *.bin file.