## FPS Test Results

Both the non-optimized and optimized SSD MobileNet v2 network are implemented on the Jetson Xavier in order to analyse the frames per second (FPS). The optimization is done using TensorRT. Table 1 shows the minimum, maximum and average FPS of the networks. Note that these values are calculated after the Jetson Xavier was on for some time, because the first 30 seconds-1 minute the Jetson Xavier is heating up.

|             | Non-optimized Network | Optimized Network |
| ----------- | --------------------- | ----------------- |
| Average FPS | 24.83                 | 119.3             |
| Minimum FPS | 23.24                 | 101.1             |
| Maximum FPS | 30.13                 | 128.1             |

*Table 1: results of the FPS test for both the non-optimized and optimized network*

The non-optimized network shows an average FPS of almost 25. The average FPS of the optimized network is over 119, with a maximum FPS of 128. This is an increment of almost a factor of 5. The stakeholders' requirement was to have a FPS of at least 100, which is reached after optimization. The minimum FPS after optimization is 101.1, so we can even conclude that the FPS of the network is over 100 at all times when operating. 