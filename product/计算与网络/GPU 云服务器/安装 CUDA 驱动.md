CUDA（Compute Unified Device Architecture）是显卡厂商 NVIDIA 推出的运算平台。 CUDA™ 是一种由 NVIDIA 推出的通用并行计算架构，该架构使 GPU 能够解决复杂的计算问题。 它包含了 CUDA 指令集架构（ISA）以及 GPU 内部的并行计算引擎。 开发人员现在可以使用 C 语言, C++ , FORTRAN 来为 CUDA™ 架构编写程序，所编写出的程序可以在支持 CUDA™ 的处理器上以超高性能运行。
GPU 云服务器采用 NVIDIA 显卡，需要安装 CUDA 开发运行环境。以目前最常用的 CUDA 7.5 为例，可参照以下步骤进行安装。
## Linux 系统指引
1. 登录 [CUDA 驱动下载](https://developer.nvidia.com/cuda-75-downloads-archive) 或复制链接 https://developer.nvidia.com/cuda-75-downloads-archive 。
2. 选择操作系统和安装包。以 CentOS 7.2 64 位为例，可按如下方式进行选择：
![](//mc.qcloudimg.com/static/img/a69a79a2d6cbd1f442b58bfb423d8cca/image.jpg)
>!
>- Installer Type 推荐选择 rpm（network）。
>- network：网络安装包，安装包较小，需要在主机内联网下载实际的安装包。
>- local：本地安装包。安装包较大，包含每一个下载安装组件的安装包。

3. 右击【Download】-【复制链接地址】。
![](//mc.qcloudimg.com/static/img/3a2552b7e1637055bae0a1391520713b/image.png)
4. 登录 GPU 实例，使用 `wget` 命令， 粘贴上述步骤复制的链接地址下载安装包；或通过在本地系统下载 CUDA 安装包， 上传到 GPU 实例的服务器。
![](//mc.qcloudimg.com/static/img/e40ed1109aaed75d51b3781fe0045eb6/image.png)
5. 在 CUDA 安装包所在目录下运行如下命令：
`sudo rpm -i cuda-repo-rhel7-7.5-18.x86_64.rpm`
`sudo yum clean all`
`sudo yum install cuda`
6. 在	` /usr/local/cuda-7.5/samples/1_Utilities/deviceQuery ` 目录下，执行 `make` 命令，可以编译出 deviceQuery 程序。
7. 执行 deviceQuery 正常显示如下设备信息，此刻认为 CUDA 安装正确。
![](//mc.qcloudimg.com/static/img/d545951dc869591d83bf23e27831287a/image.jpg)

## Windows 系统指引
要在 Windows 实例上安装 CUDA ，请使用远程桌面以管理员的身份登录您的 Windows 实例。
1. 在 [CUDA 驱动官网](https://developer.nvidia.com/cuda-75-downloads-archive) 下载 CUDA 安装包。
2. 选择操作系统和安装包。以 Win Server 2012 R2 64 位为例，可按如下方式进行选择：
![](//mc.qcloudimg.com/static/img/ecf81426ceb95fd4ed549cf0bc627895/image.jpg)
![](//mc.qcloudimg.com/static/img/525b743130bda690a7223cbd5533ec75/image.jpg)
3. 启动安装程序，按提示进行安装，如果最后出现完成对话框，则安装成功。
![](//mc.qcloudimg.com/static/img/52aef97b2d048f884c467d8446fed003/image.jpg)



