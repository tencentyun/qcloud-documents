## 操作场景
GPU 云服务器正常工作需提前安装正确的基础设施软件，对 NVIDIA 系列 GPU 而言，有以下两个层次的软件包需要安装：
- 驱动 GPU 工作的硬件驱动程序。
- 上层应用程序所需要的库。

若把 NVIDIA GPU 用作通用计算，则需安装 Tesla Driver + CUDA。本文以 CentOS 操作系统为例，介绍如何安装 Tesla Driver，如何安装 CUDA 请参考 [安装 CUDA 驱动指引](https://cloud.tencent.com/document/product/560/8064)。

>?为方便用户，用户可以在创建 GPU 云服务器时，在服务市场里选择预装特定版本驱动和 CUDA 的镜像。详情请参见 [选择镜像](https://cloud.tencent.com/document/product/560/30211#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E9.80.89.E6.8B.A9.E9.95.9C.E5.83.8F)。


## 操作步骤
### Linux 驱动安装
Linux 驱动安装采用 Shell 脚本安装方式，适用于任何 Linux 发行版，包括 CentOS，Ubuntu 等。

NVIDIA Telsa GPU 的 Linux 驱动在安装过程中需要编译 kernel module，系统需提前安装 gcc 和编译 Linux Kernel Module 所依赖的包，例如 `kernel-devel-$(uname -r)` 等。

1. 执行以下命令，检查当前系统中是否已安装 dkms。
```
rpm -qa | grep -i dkms
```
返回结果如下图，则表示已安装 dkms。
![](https://main.qcloudimg.com/raw/ada786e81334e5a88f8c95e54ff42f18.png)
如未安装 dkms，则执行以下命令进行安装。
```
sudo yum install -y dkms
```
2. 登录 [NVIDIA 驱动下载](http://www.nvidia.com/Download/Find.aspx) 或访问 `http://www.nvidia.com/Download/Find.aspx`。
3. 选择操作系统和安装包，并单击【SEARCH】搜寻驱动，选择要下载的驱动版本。本文以 V100 为例，如下图所示：
>!操作系统（Operating System）选择 Linux 64-bit 即表示下载 shell 安装文件。如果选择具体的发行版，则下载的文件是对应的包安装文件。
>
![](https://main.qcloudimg.com/raw/296039c584039388c7988c22fb0227a4.png)
4. 选择特定的版本进入下载页面，单击【DOWNLOAD】。如下图所示：
![](https://main.qcloudimg.com/raw/2d933595a3a21e89f64a6463b14f3bd3.png)
5. <span id="Step5"></span>如有填写个人信息的页面可选择直接跳过，当出现以下页面时，右键单击【AGREE&DOWNLOAD】并选择菜单中的【复制链接地址】。如下图所示：
![](https://main.qcloudimg.com/raw/e0412e1a06eb06ad9f98e7f6a2d5a026.png)
6. 参考 [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录 GPU 实例。您也可以根据实际操作习惯，选择其他不同的登录方式：
	- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
	- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)
7. 使用 `wget` 命令， 粘贴 [步骤5](#Step5) 中已获取的链接地址，下载安装包。如下图所示：
![](https://main.qcloudimg.com/raw/cbbb80409d43052061ba638d7ae622e5.png)
或者您可在本地系统下载 NVIDIA 安装包，再上传到 GPU 实例的服务器。
8. 执行以下命令，对安装包添加执行权限。 例如，对文件名为 `NVIDIA-Linux-x86_64-418.126.02.run` 添加执行权限。
```
chmod +x NVIDIA-Linux-x86_64-418.126.02.run
```
9. 依次执行以下命令，检查当前系统中是否已安装 gcc 和 kernel-devel 包。
```
rpm -qa | grep kernel-devel
```
```
rpm -qa | grep gcc
```
返回结果如下，则表示已安装 gcc 和 kernel-devel。
![](https://main.qcloudimg.com/raw/0a9d385944669528d49544eb0bd6b8eb.png)
如未安装，则请执行以下命令进行安装。
```
sudo yum install -y gcc kernel-devel
```
>!如升级了 kernel 版本，则需要将 kernel-devel 升级至与 kernel 相同的版本。
>
9. 执行以下命令，运行驱动安装程序，并按提示进行后续操作。
```
sudo sh NVIDIA-Linux-x86_64-418.126.02.run
```
10. 安装完成后，执行以下命令进行验证。
```
nvidia-smi
```
如返回信息类似下图中的 GPU 信息，则说明驱动安装成功。
![](https://main.qcloudimg.com/raw/94cbceaa09720cd7edba76961f2763d8.png)



### Windows 驱动安装
1. 参考 [使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)，登录 GPU 实例。
1. 访问 [NVIDIA 驱动下载](http://www.nvidia.com/Download/Find.aspx) 官网。
2. 选择操作系统和安装包，并选择对应驱动程序。本文以 V100 为例，如下图所示：
![](https://main.qcloudimg.com/raw/222b7f9fa96b269a9c6c0b6b5781d048.png)
3. 打开下载驱动程序所在的文件夹，双击安装文件开始安装，按照界面上的提示安装驱动程序并根据需要重启实例。
安装完成后，如需验证 GPU 是否正常工作，请查看设备管理器。


## 安装失败原因
Linux 系统驱动安装失败表现为 nvidia-smi 无法工作，通常原因如下：
1. 系统缺乏编译 kernel module 所需要的包，如 gcc，kernel-devel-xxx 等，导致无法编译，最终安装失败。
2. 系统里面存在多个版本的 kernel，由于 DKMS 的不正确配置，导致驱动编译为非当前版本 kernel 的 kernel moudule，导致 kernel module 安装失败。
3. 安装驱动后，升级了 kernel 版本导致原来的安装失效。
