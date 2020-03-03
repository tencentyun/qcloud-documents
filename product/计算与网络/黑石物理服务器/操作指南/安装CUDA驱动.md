黑石官方镜像默认不带 GPU 驱动，请参考本文指引快速安装 GPU 驱动。  

## Linux 系列安装指引
### 操作步骤
1. 下载并运行安装脚本。
2. 检查是否安装成功。

### 工具准备
Xshell、PuTTY 等远程登录工具。

### 下载和运行安装脚本
Nvidia 官方的 CUDA toolkit 和 GPU 卡的兼容列表，请参考 [Nvidia 官网文档](http://www.nvidia.com/Download/index.aspx?lang=cn "Nvidia官网文档")。

请使用以下命令下载和运行安装脚本
```
wget http://mirrors.tencentyun.com/install/monitor_bm/install_gpu_driver.sh;chmod +x ./install_gpu_driver.sh ;./install_gpu_driver.sh 
```

执行结束后，有如下提示，说明安装成功：

```
Driver:   Installed 
```

```
Toolkit:  Installed in /usr/local/cuda-10.0
```

### 检验驱动是否安装成功
在`/usr/local/cuda/samples/1_Utilities/deviceQuery`目录下，执行 make 命令，可以编译出 deviceQuery 程序。
执行 deviceQuery 正常，则显示如下设备信息，表示 CUDA 安装正确。
![](https://mc.qcloudimg.com/static/img/d545951dc869591d83bf23e27831287a/image.jpg)

## Windows 系列安装指引
本教程适用于以下条件下的安装：
- 机型：PG103v2
- 操作系统版本： Windows Server 2012 R2
- CUDA 版本：CUDA_9.1.85

其他条件下的安装请参考 [Nvdia 官网](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)。  

### 工具准备
高于 2012 版本的 Visual Studio。

### 运行脚本下载驱动
新建 POWERSHELL 脚本，键入以下代码。右键 RUN WITH POWERSHELL 执行：

```
$client = new-object System.Net.WebClient
$client.DownloadFile('http://mirrors.tencentyun.com/install/monitor_bm/cuda_9.1.85_windows.exe','.\cuda_9.1.85_windows.exe')
$client.DownloadFile('http://mirrors.tencentyun.com/install/monitor_bm/cuda_9.1.85.1_windows.exe','.\cuda_9.1.85.1_windows.exe')
$client.DownloadFile('http://mirrors.tencentyun.com/install/monitor_bm/cuda_9.1.85.2_windows.exe','.\cuda_9.1.85.2_windows.exe')
$client.DownloadFile('http://mirrors.tencentyun.com/install/monitor_bm/cuda_9.1.85.3_windows.exe','.\cuda_9.1.85.3_windows.exe')
```

### 安装 CUDA 驱动
安装需要访问外网，请提前绑定好弹性公网 IP。以下文件请依次安装，CUDA_9.1.85 为主要安装程序，其余为补丁
- cuda\_9.1.85\_windows.exe
- cuda\_9.1.85.1\_windows.exe
- cuda\_9.1.85.2\_windows.exe
- cuda\_9.1.85.3\_windows.exe

### 验证是否安装成功
1. 进入目录

```
c:\ProgramData\NVIDIA Corporation\CUDA Samples\v9.1\1_Utilities\deviceQuery
```

2. 打开文件夹内的 Visual Studio 工程。

3. 编译运行后，出现如下图示现象，即证明安装成功。
![]( https://main.qcloudimg.com/raw/813fe93e57615ebf0d42bda71fdc0c86.jpg)
