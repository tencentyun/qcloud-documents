GPU 云服务器正常工作需安装正确的基础设施软件，对 NVIDIA 系列 GPU 而言，有两个层次的软件包需要安装：
- 驱动 GPU 工作的硬件驱动程序。
- 上层应用程序所需要的库。

若把 NVIDIA GPU 用作通用计算，需要安装 Tesla Driver + CUDA，本文仅介绍如何安装 Tesla Driver，如何安装 CUDA 请参考 [安装 CUDA 驱动指引](https://cloud.tencent.com/document/product/560/8064)。

为方便用户，用户可以再创建 GPU 云服务器时，在镜像市场里选择预装特定版本驱动和 CUDA 的镜像。

## Linux 驱动安装
Linux 驱动安装采用Shell 脚本安装， 适用于任何 Linux 发行版，包括 CentOS，Ubuntu 等。

NVIDIA Telsa GPU 的 Linux 驱动在安装过程中需要编译 kernel module，所以要求系统安装好了 gcc 和编译 Linux Kernel Module 所依赖的包，例如 kernel-devel-$(uname -r) 等。

1. 安装dkms。在安装dkms前，检查当前系统中是否已安装dkms：

   ```
   rpm -qa | grep -i dkms
   ```

   如果未安装dkms，则使用yum命令安装：

   ```
   sudo yum install -y dkms
   ```

   如果出现类似下图dkms信息，则表示dkms安装成功：

   ![](https://main.qcloudimg.com/raw/11632d28a44423d1b7d0429f2eac3491.png)

2. 登录 [NVIDIA 驱动下载](http://www.nvidia.com/Download/Find.aspx) 或打开链接 http://www.nvidia.com/Download/Find.aspx 。

3. 选择操作系统和安装包。以 V100 为例，搜寻驱动，然后选择要下载的驱动版本。
     ![](https://main.qcloudimg.com/raw/af853052cee77c7a8c6a41c7b3f38f77.png)

> **注意：**
操作系统选择 Linux 64-bit 代表下载的是 shell 安装文件，如果选择具体的发行版下载的文件则是对应的包安装文件。

4. 选择特定的版本跳转后，单击【DOWNLOAD】。
   ![](https://main.qcloudimg.com/raw/3a353c2242e060cbe56798dfc9e7b55c.png)

5. 再次跳转后，如有填写个人信息的页面可选择直接跳过，出现下面页面时，右击【AGREE&DOWNLOAD】，右键菜单里复制链接地址。
   ![](https://main.qcloudimg.com/raw/e343c0276071797f3bc1051e430758f5.png)

6. 登录 GPU 实例，使用 `wget` 命令， 粘贴上述步骤复制的链接地址下载安装包；或通过在本地系统下载 NVIDIA 安装包， 上传到 GPU 实例的服务器。
   ![](https://main.qcloudimg.com/raw/225740c30b0ff835ffbee6bbd85dbfc3.png)

7. 对安装包加执行权限。 例如，对文件名为 `NVIDIA-Linux-x86_64-418.126.02.run` 加执行权限：

   ```
   chmod +x NVIDIA-Linux-x86_64-418.126.02.run
   ```


8. 安装当前系统对应的 gcc 和 kernel-devel 包。在安装前，检查系统中是否已安装rpm包：

   ```
   rpm -qa | grep kernel-devel
   rpm -qa | grep gcc
   ```

   如果未安装，则需要手动安装：

   ```
   sudo yum install -y gcc kernel-devel
   ```

   如果出现类似下图信息，则表示gcc和kernel-devel安装成功：

   ![](https://main.qcloudimg.com/raw/59e94802c7d338e495b5c8d46d6170d4.png)

> **注意：**
> 如果升级了kernel版本，需要将kernel-devel升级至与kernel相同的版本。

9. 运行驱动安装程序后按提示进行后续操作。

   ```
   sudo sh NVIDIA-Linux-x86_64-418.126.02.run
   ```


10. 安装完成后， 运行`nvidia-smi`。如果有类似如下的 GPU 信息显示出来，说明驱动安装成功。
    ![](https://main.qcloudimg.com/raw/936b27301d91c55ec669d24cb23dcdab.png)



## Windows 驱动安装

1. 登录 [NVIDIA 驱动下载官网](http://www.nvidia.com/Download/Find.aspx)。
2. 选择操作系统和安装包。以 V100为例，选择如下驱动程序：
![](https://main.qcloudimg.com/raw/eea30a56007428750d0b750c3d6dbae7.png)
3. 打开下载驱动程序的文件夹，然后双击安装文件以启动它。按照说明安装驱动程序并根据需要重启实例。要验证 GPU 是否正常工作，请检查设备管理器。

## 安装失败原因
Linux 系统驱动安装失败表现为 nvidia-smi 无法工作，一般有下面几个常见原因：
1. 系统缺乏编译 kernel module 所需要的包，如 gcc，kernel-devel-xxx 等，导致无法编译，最终安装失败。
2. 系统里面存在多个版本的 kernel，由于 DKMS 的不正确配置，导致驱动编译为非当前版本 kernel 的 kernel moudule，导致 kernel module 安装失败。
3. 安装驱动后，升级了 kernel 版本导致原来的安装失效。
