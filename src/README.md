System Integration
====================================

By this point, we'll assume a Neural Network model has been already [trained](../tensorflow_training/) and [optimized](../tensorrt/). However, before running the python script to perform online inference with the [Tau2 camera](../CAD/), we need to install a kernel module to the Jetson Xavier to interface with the camera as a regular device (/dev/video0).

First, we must install the libraries of the TeAx's Thermal Grabber. For this, run the installation script provided in this folder. This script will install some dependencies (if needed), and then compile the necessary libraries to interface with the Tau2. 

```
$ ./install.sh
```

Then, we load the kernel module. 

```
$ sudo modprobe v4l2loopback
```

Finally, we run the daemon to connect the module to the camera via TeAx's library.

```
$ sudo LD_PRELOAD=TCG_SDK_2018_02_14/libthermalgrabber/lib/libthermalgrabber.so ./TCGrabberUSBV4L2d
```

After running this, you should see communication with the Tau2 camera. Some features are not enabled by default, nevertheless, communication is still possible as long as the daemon is running.



Finally, we open a new terminal and run the inference.

```
$ python3 trt_ssd.py --model ssd_mobilenet_v2_coco --vid 0 --usb
```



If everything goes well, you should be able to see online inference with the thermal camera feed on screen.