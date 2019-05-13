## 检查驱动安装情况

1. 输入命令`lsmod |grep nvidia`，确认 NVIDIA Driver 模块被加载；
![](//mc.qcloudimg.com/static/img/e1bac33437709c20a69a352550239110/image.png)
2. 执行 `nvidia-smi` ,如果可以正确显示GPU信息，则表示驱动安装正常。

![](//mc.qcloudimg.com/static/img/6c6ae379b4c6b804509b7753941aca76/image.jpg)



## 检查 CUDA 环境

1. 您可以在 CUDA 例子程序目录下 `/usr/local/cuda-7.5/samples/` 选择您想测试的程序，本章节选用`1_Utilities`目录下的 deviceQuery;
![](//mc.qcloudimg.com/static/img/dd34da0f42b641771c7a0ea15fd24d1c/image.png)
2. 输入命令 `make` 进行编译，是否可以正常运行，如显示以下信息则表明正常运行。
![](//mc.qcloudimg.com/static/img/65bf6ded7468950d3c2b261487511364/image.png)

