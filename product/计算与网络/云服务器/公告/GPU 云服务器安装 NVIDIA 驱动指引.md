## Linux GPU 云服务器安装 NVIDIA 驱动指引
1. 要在 Linux 实例上安装 NVIDIA 驱动程序，您可以从 http://www.nvidia.com/Download/Find.aspx 下载 NVIDIA 驱动程序。以M40为例，选择如下的驱动程序。
![](//mc.qcloudimg.com/static/img/772ea4a736d7a9b00c77f15f08beb2eb/image.jpg)
2. 下载后的驱动文件， 比如文件名为 `NVIDIA-Linux-x86_64-352.99.run`加执行权限
 ` chmod +x NVIDIA-Linux-x86_64-352.99.run`
3. 安装当前系统对应的gcc 和 kernel-devel 包
  `sudo yum install -y gcc kernel-devel-xxx`
  `xxx `是内核版本号，可以通过 `uname -r` 查看。
4. 运行驱动安装程序 `sudo /bin/bash ./NVIDIA-Linux-x86_64-352.99.ru` 按提示进行后续操作。
5. 安装完成后， 运行 nvidia-smi 如果有类似如下的GPU信息显示出来，说明驱动安装成功。
![](//mc.qcloudimg.com/static/img/1c82b06999b15cc414a383d61961e528/image.jpg)

## Windows GPU 云服务器安装 NVIDIA 驱动指引
1. 要在 Windows 实例上安装 NVIDIA 驱动程序，请使用远程桌面以管理员身份登录您的 Windows 实例。您可以从 http://www.nvidia.com/Download/Find.aspx 下载 NVIDIA 驱动程序,以M40为例，选择如下的驱动程序。
![](//mc.qcloudimg.com/static/img/c3925ced580cc85a74b7e636b726fa17/image.jpg)
2. 打开在其中下载驱动程序的文件夹，然后双击安装文件以启动它。按照说明安装驱动程序并根据需要重启实例。要验证 GPU 是否正常工作，请检查设备管理器。






