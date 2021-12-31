## 操作场景
CUDA（Compute Unified Device Architecture）是显卡厂商 NVIDIA 推出的运算平台。CUDA™ 是一种由 NVIDIA 推出的通用并行计算架构，该架构使 GPU 能够解决复杂的计算问题。它包含了 CUDA 指令集架构（ISA）以及 GPU 内部的并行计算引擎。 开发人员目前可使用 C 语言、C++ 及 FORTRAN 来为 CUDA™ 架构编写程序，所编写出的程序可在支持 CUDA™ 的处理器上以超高性能运行。

GPU 云服务器采用 NVIDIA 显卡，则需要安装 CUDA 开发运行环境。本文以目前最常用的 CUDA 10.1 为例，您可参考以下步骤进行安装。


## 操作步骤
### Linux 系统指引
1. 前往 [CUDA 驱动下载](https://developer.nvidia.com/cuda-toolkit-archive) 页面或访问 `https://developer.nvidia.com/cuda-toolkit-archive`。
2. 选择对应的 CUDA 版本，本文以 CUDA Toolkit 10.1 为例。如下图所示：
![](https://main.qcloudimg.com/raw/1bff72aeaceb4ad6a930861c5a5d74f0.png)
3. 按照页面上的提示，依次选择操作系统和安装包。本文选择方式如下图所示：
>!Installer Type：推荐选择 runfile（local）。
> - network：网络安装包，安装包较小，需要在主机内联网下载实际的安装包。
> - local：本地安装包。安装包较大，包含每一个下载安装组件的安装包。
> 
![](https://main.qcloudimg.com/raw/acadac8128996daf65731875ae8aec3e.png)
4. <span id="Step4"></span>选择完成出现以下信息时，右键单击【Download】并选择菜单中的【复制链接地址】。如下图所示：
![](https://main.qcloudimg.com/raw/bb8f8fcf69d70efb702a5ece2e167db5.png)
5. 参考 [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录 GPU 实例。您也可以根据实际操作习惯，选择其他不同的登录方式：
	- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
	- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)
6. 使用 `wget` 命令， 粘贴 [步骤4](#Step4) 中已获取的链接，下载安装包。如下图所示：
![](https://main.qcloudimg.com/raw/0301e9615259750e5ce9f6fbe6874238.png)
或者您可在本地系统下载 CUDA 安装包，再上传到 GPU 实例的服务器。
7. 依次执行以下命令，对安装包添加执行权限。例如，对文件名为 `cuda_10.1.105_418.39_linux.run` 添加执行权限。
```
 sudo chmod +x cuda_10.1.105_418.39_linux.run
```
```
./cuda_10.1.105_418.39_linux.run --toolkit --samples --silent
```
8. 重启系统。
9. 依次执行以下命令，配置环境变量。
```
echo 'export PATH=/usr/local/cuda/bin:$PATH' | sudo tee /etc/profile.d/cuda.sh
```
```
source /etc/profile
```
10. [](id:Step10)依次执行以下命令，验证 CUDA 安装是否成功。
```
cd /usr/local/cuda-10.1/samples/1_Utilities/deviceQuery
```
```
make
```
```
./deviceQuery
```
如返回结果显示 Result=PASS，则表示 CUDA 安装成功。
若执行 `make` 命令后，出现如下图所示错误。
![](https://main.qcloudimg.com/raw/416e1e50a4226925af6debb6cb26f0c8.png)
则执行以下命令，安装对应的 gcc 包即可。
```
yum install -y gcc-c++
```
安装完成后，再次执行 [步骤10](#Step10) 进行验证即可。


### Windows 系统指引
1. 参考 [使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)，登录 GPU 实例。
2. 访问 [CUDA 驱动](https://developer.nvidia.com/cuda-toolkit-archive) 官网。
3. 选择对应的 CUDA 版本，本文以 CUDA Toolkit 10.1 为例。如下图所示：
![](https://main.qcloudimg.com/raw/1bff72aeaceb4ad6a930861c5a5d74f0.png)
4. 按照页面上的提示，依次选择操作系统和安装包。本文选择方式如下图所示：
![](https://main.qcloudimg.com/raw/9c25375680dcad463e8d758d3bbb0977.png)
5. 打开下载驱动程序所在的文件夹，双击安装文件开始安装，按照界面上的提示安装驱动程序并根据需要重启实例。
若最后出现完成对话框，则表示安装成功。如下图所示：
![](https://main.qcloudimg.com/raw/22bd8237582f4552d3cce662f58ebf2a.png)

