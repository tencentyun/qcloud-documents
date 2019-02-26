GPU 云服务器正常工作需安装正确的基础设施软件，对NVIDIA系列GPU而言，有两个层次的软件包需要安装：
1. 驱动GPU工作的硬件驱动程序
2. 上层应用程序所需要的库

如果把NVIDIA GPU用作通用计算，需要安装Tesla Driver + CUDA，本篇内容仅介绍如何安装Tesla Driver。

腾讯云为用户提供了更好的便利性，用户可以创建GPU云服务器的时候，在镜像市场里选择预装特定版本驱动和CUDA的镜像

## Linux 安装驱动
Linux驱动安装有2种方式：
1. Shell脚本安装， 适应于任何Linux发行版，包括CentOS，Ubuntu等
2. 针对不同Linux发行版的对应的包安装方式，例如，DEB包安装， RPM包安装等

不管哪种安装方式，NVIDIA Telsa GPU的Linux驱动在安装过程种需要编译kernel module，所以要求系统安装好了gcc和编译Linux Kernel Module所依赖的包，例如kernel-devel-$(uname -r)等。

### Shell脚本安装
1. 登录 [NVIDIA 驱动下载](http://www.nvidia.com/Download/Find.aspx) 或打开链接 http://www.nvidia.com/Download/Find.aspx 。
2. 选择操作系统和安装包。以 P40 为例，搜寻驱动，然后选择要下载的驱动版本：（**注意: 操作系统选择Linux 64-bit代表下载的是shell安装文件，如果选择具体的发行版下载的文件则是对应的包安装文件**）
![](https://main.qcloudimg.com/raw/42f815083c1ee87a98a13595c69bd496.png)
3. 选择特定的版本跳转后，点击【DOWNLOAD】
![](https://main.qcloudimg.com/raw/95ada99ab6bcc84decfef4caf1905f62.png)
4. 再次跳转后，如有填写个人信息的页面可选择直接点击跳过，出现下面页面时，右击【AGREE&DOWNLOAD】，右键菜单里复制链接地址
![](https://main.qcloudimg.com/raw/e343c0276071797f3bc1051e430758f5.png)
5. 登录 GPU 实例，使用 `wget` 命令， 粘贴上述步骤复制的链接地址下载安装包；或通过在本地系统下载 NVIDIA 安装包， 上传到 GPU 实例的服务器。
![](https://main.qcloudimg.com/raw/e8648c2802a0c31bf557b056ce084911.png)
3. 对安装包加执行权限。 比如对文件名为 `NVIDIA-Linux-x86_64-396.44.run` 加执行权限
 ` chmod +x NVIDIA-Linux-x86_64-396.44.run`
4. 安装当前系统对应的 gcc 和 kernel-devel 包
  `sudo yum install -y gcc kernel-devel-xxx`
  `xxx `是内核版本号，可以通过 `uname -r` 查看。
5. 运行驱动安装程序 `sudo /bin/bash ./NVIDIA-Linux-x86_64-396.44.run` 按提示进行后续操作。
6. 安装完成后， 运行 nvidia-smi 如果有类似如下的 GPU 信息显示出来，说明驱动安装成功。
![](https://main.qcloudimg.com/raw/b5877169c7012d20e7de02754d43cedc.png)

### DEB/RPM包安装
#### DEB包安装方式
1. 按照上面的方式选择对应的支持Deb包的操作系统，例如：ubuntu 16.04，得到下载链接：`wget http://us.download.nvidia.com/tesla/396.44/nvidia-diag-driver-local-repo-ubuntu1604-396.44_1.0-1_amd64.deb`
2. `dpkg -i nvidia-diag-driver-local-repo-ubuntu1604-396.44_1.0-1_amd64.deb`
3. `apt-get update`
4. `apt-get install cuda-drivers`
5. `reboot`
6. 运行nvidia-smi能输出正确信息代表驱动安装成功
 
#### RPM包安装方式
1. 按照下面的方式选择对应支持RPM包的操作系统，例如：rhel 7.x， 得到下载链接：`wget http://us.download.nvidia.com/tesla/396.44/nvidia-diag-driver-local-repo-rhel7-396.44-1.0-1.x86_64.rpm`
2. `rpm -i nvidia-diag-driver-local-repo-rhel7-396.44-1.0-1.x86_64.rpm`
3. `yum clean all`
4. `yum install cuda-drivers`
5. `reboot`
6. 运行nvidia-smi能输出正确信息代表驱动安装成功

## Windows 安装驱动
1. 登录 [NVIDIA 驱动下载官网](http://www.nvidia.com/Download/Find.aspx)。
2. 选择操作系统和安装包。以 M40 为例，选择如下驱动程序：
![](//mc.qcloudimg.com/static/img/ba82ef3631369d12b995b6cb2a94b14c/image.png)
3. 打开下载驱动程序的文件夹，然后双击安装文件以启动它。按照说明安装驱动程序并根据需要重启实例。要验证 GPU 是否正常工作，请检查设备管理器。

## 安装失败原因
Linux系统驱动安装失败表现为nvidia-smi无法工作，一般有下面几个常见原因：
1. 系统缺乏编译kernel module所需要的包，如gcc，kernel-devel-xxx等，导致无法编译，最终安装失败
2. 系统里面存在多个版本的kernel，由于DKMS的不正确配置，导致驱动编译为非当前版本kernel的kernel moudule，导致kernel module安装失败
3. 安装驱动后，升级了kernel版本导致原来的安装失效

