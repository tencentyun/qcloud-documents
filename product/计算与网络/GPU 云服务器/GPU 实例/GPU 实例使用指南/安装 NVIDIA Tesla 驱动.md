GPU 云服务器正常工作需安装正确的基础设施软件，对 NVIDIA 系列 GPU 而言，有两个层次的软件包需要安装：
- 驱动 GPU 工作的硬件驱动程序。
- 上层应用程序所需要的库。

若把 NVIDIA GPU 用作通用计算，需要安装 Tesla Driver + CUDA，本文仅介绍如何安装 Tesla Driver，如何安装 CUDA 请参考 [安装 CUDA 驱动指引](https://cloud.tencent.com/document/product/560/8064)。

为方便用户，用户可以再创建 GPU 云服务器时，在镜像市场里选择预装特定版本驱动和 CUDA 的镜像。

## Linux 驱动安装
Linux 驱动安装有2种方式：
- Shell 脚本安装， 适用于任何 Linux 发行版，包括 CentOS，Ubuntu 等；
- 包安装，适用于不同 Linux 发行版，例如 DEB 包安装， RPM 包安装等。

不管哪种安装方式，NVIDIA Telsa GPU 的 Linux 驱动在安装过程种需要编译 kernel module，所以要求系统安装好了 gcc 和编译 Linux Kernel Module 所依赖的包，例如 kernel-devel-$(uname -r) 等。

### Shell 脚本安装
1. 登录 [NVIDIA 驱动下载](http://www.nvidia.com/Download/Find.aspx) 或打开链接 http://www.nvidia.com/Download/Find.aspx 。

2. 选择操作系统和安装包。以 P40 为例，搜寻驱动，然后选择要下载的驱动版本。
![](https://main.qcloudimg.com/raw/42f815083c1ee87a98a13595c69bd496.png)
> **注意：**
操作系统选择 Linux 64-bit 代表下载的是 shell 安装文件，如果选择具体的发行版下载的文件则是对应的包安装文件。

3. 选择特定的版本跳转后，单击【DOWNLOAD】。
![](https://main.qcloudimg.com/raw/95ada99ab6bcc84decfef4caf1905f62.png)

4. 再次跳转后，如有填写个人信息的页面可选择直接跳过，出现下面页面时，右击【AGREE&DOWNLOAD】，右键菜单里复制链接地址。
![](https://main.qcloudimg.com/raw/e343c0276071797f3bc1051e430758f5.png)

5. 登录 GPU 实例，使用 `wget` 命令， 粘贴上述步骤复制的链接地址下载安装包；或通过在本地系统下载 NVIDIA 安装包， 上传到 GPU 实例的服务器。
![](https://main.qcloudimg.com/raw/e8648c2802a0c31bf557b056ce084911.png)

6. 对安装包加执行权限。 例如，对文件名为 `NVIDIA-Linux-x86_64-396.44.run` 加执行权限：
```
chmod +x NVIDIA-Linux-x86_64-396.44.run
```

7. 安装当前系统对应的 gcc 和 kernel-devel 包
```
sudo yum install -y gcc kernel-devel-xxx
```
`xxx`是内核版本号，可以通过 `uname -r` 查看。

8. 运行驱动安装程序后按提示进行后续操作。
```
sudo /bin/bash ./NVIDIA-Linux-x86_64-396.44.run
```

9. 安装完成后， 运行`nvidia-smi`。如果有类似如下的 GPU 信息显示出来，说明驱动安装成功。
![](https://main.qcloudimg.com/raw/b5877169c7012d20e7de02754d43cedc.png)

### DEB/RPM 包安装
#### DEB 包安装方式
1. 登录 [NVIDIA 驱动下载](http://www.nvidia.com/Download/Find.aspx) 或打开链接 http://www.nvidia.com/Download/Find.aspx 。
2. 选择对应的支持 DEB 包的操作系统，例如：Ubuntu 16.04，得到下载链接：`wget http://us.download.nvidia.com/tesla/396.44/nvidia-diag-driver-local-repo-ubuntu1604-396.44_1.0-1_amd64.deb`
2. 运行安装软件包命令。
```
dpkg -i nvidia-diag-driver-local-repo-ubuntu1604-396.44_1.0-1_amd64.deb
```
3. 使用`apt-get`命令更新软件包。
```
apt-get update
```
4. 运行`apt-get`命令安装驱动。
```
apt-get install cuda-drivers
```
5. 运行`reboot`命令重启。
6. 运行`nvidia-smi`能输出正确信息代表驱动安装成功。

#### RPM 包安装方式
1. 登录 [NVIDIA 驱动下载](http://www.nvidia.com/Download/Find.aspx) 或打开链接 http://www.nvidia.com/Download/Find.aspx 。
2. 选择支持 RPM 包的操作系统，并获取该 RPM 包的下载链接。例如：选择 CentOS 7.x， 得到下载链接：
`wget http://us.download.nvidia.com/tesla/396.44/nvidia-diag-driver-local-repo-rhel7-396.44-1.0-1.x86_64.rpm`
3. 使用`rpm`命令安装 rpm 包。
```
rpm -i nvidia-diag-driver-local-repo-rhel7-396.44-1.0-1.x86_64.rpm
```
4. 使用`yum`命令清除缓存。
 ```
 yum clean all
 ```
5. 使用`yum`命令安装驱动。
```
yum install cuda-drivers
```
6. 运行`reboot`命令重启。
7. 运行`nvidia-smi`能输出正确信息代表驱动安装成功。

## Windows 驱动安装
1. 登录 [NVIDIA 驱动下载官网](http://www.nvidia.com/Download/Find.aspx)。
2. 选择操作系统和安装包。以 M40 为例，选择如下驱动程序：
![](//mc.qcloudimg.com/static/img/ba82ef3631369d12b995b6cb2a94b14c/image.png)
3. 打开下载驱动程序的文件夹，然后双击安装文件以启动它。按照说明安装驱动程序并根据需要重启实例。要验证 GPU 是否正常工作，请检查设备管理器。

## 安装失败原因
Linux 系统驱动安装失败表现为 nvidia-smi 无法工作，一般有下面几个常见原因：
1. 系统缺乏编译 kernel module 所需要的包，如 gcc，kernel-devel-xxx 等，导致无法编译，最终安装失败。
2. 系统里面存在多个版本的 kernel，由于 DKMS 的不正确配置，导致驱动编译为非当前版本 kernel 的 kernel moudule，导致 kernel module 安装失败。
3. 安装驱动后，升级了 kernel 版本导致原来的安装失效。
