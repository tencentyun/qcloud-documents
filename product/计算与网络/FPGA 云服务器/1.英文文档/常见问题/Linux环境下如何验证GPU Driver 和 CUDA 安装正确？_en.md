## Checking Driver Installation

1. Enter the command `lsmod |grep nvidia` to confirm that the NVIDIA Driver module is loaded;
![](//mc.qcloudimg.com/static/img/e1bac33437709c20a69a352550239110/image.png)
2. Execute `nvidia-smi`. If the GPU information is correctly displayed, the driver is properly installed.

![](//mc.qcloudimg.com/static/img/6c6ae379b4c6b804509b7753941aca76/image.jpg)



## Checking CUDA environment

1. You can select a program to test under the CUDA sample program directory `/usr/local/cuda-7.5/samples/`. This chapter selects the deviceQuery under `1_Utilities` directory.
![](//mc.qcloudimg.com/static/img/dd34da0f42b641771c7a0ea15fd24d1c/image.png)
2. Enter the command `make` to compile, and see whether it can run normally. If the following information is displayed, it indicates normal operation.
![](//mc.qcloudimg.com/static/img/65bf6ded7468950d3c2b261487511364/image.png)


