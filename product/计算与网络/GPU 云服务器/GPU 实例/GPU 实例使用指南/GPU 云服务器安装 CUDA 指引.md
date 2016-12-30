
> CUDA®(Compute Unified Device Architecture)是显卡厂商NVIDIA推出的运算平台。 CUDA™是一种由NVIDIA推出的通用并行计算架构，该架构使GPU能够解决复杂的计算问题。 它包含了CUDA指令集架构（ISA）以及GPU内部的并行计算引擎。 开发人员现在可以使用C语言,C++,FORTRAN来为CUDA™架构编写程序,所编写出的程序于是就可以在支持CUDA™的处理器上以超高性能运行。

GPU 云服务器采用NVIDIA显卡，需要安装CUDA开发运行环境。以目前最常用的CUDA7.5为例，可参照以下步骤进行安装：

## Linux GPU 云服务器安装 CUDA 指引
1. 需要在 Linux 实例上安装 CUDA，可以从 https://developer.nvidia.com/cuda-75-downloads-archive 下载 CUDA 安装包。
2. 操作系统和安装包选择。
以 CentOS 7.2 64位为例，可按如下方式进行选择
![](//mc.qcloudimg.com/static/img/366bbd6ca9af49f77dda91036cf533bc/image.jpg)
>  注：Installer Type 推荐选择rpm（network）。
> network：网络安装包，安装包较小，需要在主机内联网下载实际的安装包。
> local：本地安装包。安装包较大，包含每一个下载安装组件的安装包。

3. 安装
![](//mc.qcloudimg.com/static/img/0dd00b1bbdc9d025109e38825be8ed71/image.jpg)
按照如上安装指引即可安装

4. 验证是否安装成功

- 在	` /usr/local/cuda-7.5/samples/1_Utilities/deviceQuery ` 目录下，执行 `make` 命令，可以编译出 deviceQuery 程序。
- 执行 deviceQuery 正常显示如下设备信息，此刻认为 CUDA 安装正确。

![](//mc.qcloudimg.com/static/img/d545951dc869591d83bf23e27831287a/image.jpg)


## Windows GPU 云服务器安装 CUDA 指引
1. 要在 Windows 实例上安装 CUDA，请使用远程桌面以管理员的身份登录您的 Windows 实例。可以从 https://developer.nvidia.com/cuda-75-downloads-archive 下载 CUDA 安装包。
2. 操作系统和安装包选择。
以 Win Server 2012 R2 64位为例，可按如下方式进行选择
![](//mc.qcloudimg.com/static/img/e8e76622c35b0013cf7be9eb4bfed1d8/image.jpg)
![](//mc.qcloudimg.com/static/img/4c4e34608a54cd98b8fc7535548aeea7/image.jpg)
3. 启动安装程序，按提示进行安装，如果最后出现完成对话框，则安装成功。
![](//mc.qcloudimg.com/static/img/52aef97b2d048f884c467d8446fed003/image.jpg)



