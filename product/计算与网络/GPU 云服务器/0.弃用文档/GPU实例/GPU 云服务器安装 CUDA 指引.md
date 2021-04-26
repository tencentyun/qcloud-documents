GPU 云服务器必须具备相应的 NVIDIA 驱动，必须针对您的编译您安装的 NVIDIA 驱动程序。
## Linux 安装驱动
1. 登录 [NVIDIA 驱动下载](http://www.nvidia.com/Download/Find.aspx) 或复制链接 http://www.nvidia.com/Download/Find.aspx 。
2. 选择操作系统和安装包。以 M40 为例，选择要下载的驱动版本：
![](//mc.qcloudimg.com/static/img/70da79038a0220191adc012fa8133b1b/image.png)
![](//mc.qcloudimg.com/static/img/8255f9b4f32528399fc4616df6feec68/image.png)
4. 跳转后，右击【DOWNLOAD】-【复制链接地址】。
![](//mc.qcloudimg.com/static/img/bb3b94d8c364948dd2b36ef893649a7e/image.png)
5. 登录 GPU 实例，使用 `wget` 命令， 粘贴上述步骤复制的链接地址下载安装包；或通过在本地系统下载 NVIDIA 安装包， 上传到 GPU 实例的服务器。
![](//mc.qcloudimg.com/static/img/7e712f47f709a4d978daf1fb09417cd1/image.png)
3. 对安装包加执行权限。 比如对文件名为 `NVIDIA-Linux-x86_64-352.99.run` 加执行权限
 ` chmod +x NVIDIA-Linux-x86_64-352.99.run`
4. 安装当前系统对应的 gcc 和 kernel-devel 包
  `sudo yum install -y gcc kernel-devel-xxx`
  `xxx `是内核版本号，可以通过 `uname -r` 查看。
5. 运行驱动安装程序 `sudo /bin/bash ./NVIDIA-Linux-x86_64-352.99.ru` 按提示进行后续操作。
6. 安装完成后， 运行 nvidia-smi 如果有类似如下的 GPU 信息显示出来，说明驱动安装成功。
![](//mc.qcloudimg.com/static/img/1c82b06999b15cc414a383d61961e528/image.jpg)

## Windows 安装驱动
1. 登录 [NVIDIA 驱动下载官网](http://www.nvidia.com/Download/Find.aspx)。
2. 选择操作系统和安装包。以 M40 为例，选择如下驱动程序：
![](//mc.qcloudimg.com/static/img/ba82ef3631369d12b995b6cb2a94b14c/image.png)
3. 打开下载驱动程序的文件夹，然后双击安装文件以启动它。按照说明安装驱动程序并根据需要重启实例。要验证 GPU 是否正常工作，请检查设备管理器。






