
<dx-alert infotype="explain" title="">
本文来自 [GPU 云服务器用户实践征文](https://cloud.tencent.com/document/product/855/71869)，仅供学习和参考。
</dx-alert>


## 操作场景
本文介绍如何使用 Windows GPU 云服务器，通过云服务器控制台搭建深度学习环境。


## 实例环境[](id:exampleEnv)
- **实例类型**：[GN8.LARGE56](https://cloud.tencent.com/document/product/560/19700#GN8)
- **操作系统**：Windows Server 2019 数据中心版 64位 中文版
- **CPU**：Intel(R) Xeon(R) CPU E5-2680 v4 @2.40GHz 2.40GHz * 6vCPUs
- **RAM**：56GB
- **GPU**：Tesla P40 * 1
- **驱动及相关库、软件版本**：CUDA 10.2、Python 3.7、Pytorch 1.8.1、Tensorflow_gpu_2.2.0


## 选择驱动及相关库、软件版本
在安装驱动前，您需大致了解 CUDA、cuDNN、Pytorch、TensorFlow 及 Python 版本对应关系，以便根据实际配置选择适配版本，免除后续出现版本不匹配等问题。

<dx-accordion>
::: 选择 CUDA 驱动版本
CUDA（Compute Unified Device Architecture），是显卡厂商 NVIDIA 推出的运算平台。CUDA™ 是一种由 NVIDIA 推出的通用并行计算架构，该架构使 GPU 能够解决复杂的计算问题。其包含了 CUDA 指令集架构（ISA）以及 GPU 内部的并行计算引擎。

#### 1. 查看显卡算力
在选择 CUDA 驱动版本时，需先了解本文使用（Tesla P40）显卡的算力。可通过 [NVIDIA 官网](https://developer.nvidia.com/zh-cn/cuda-gpus) 查询 Tesla P40 显卡算力为6.1。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8782c2508f744fd6d99fde997ef4037d.png)

#### 2. 选择 CUDA 版本 
如下图所示 CUDA 版本与显卡算力的关系，Tesla P40 显卡应选择8.0以上的 CUDA 版本。如需了解更多算力与 CUDA 版本信息，请参见 [Application Compatibility on the NVIDIA Ampere GPU Architecture](https://docs.nvidia.com/cuda/ampere-compatibility-guide/index.html#application-compatibility-on-ampere)。
![](https://qcloudimg.tencent-cloud.cn/raw/f4c05882b8077bc67c067e22350ca5b5.png)


:::
::: 选择显卡驱动版本
确定 CUDA 版本后，再选择显卡驱动版本。您可参考如下图所示 CUDA 与驱动对应关系图进行选择。如需了解更多信息，请参见 [cuda-toolkit-driver-versions](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-major-component-versions__table-cuda-toolkit-driver-versions)。
![](https://qcloudimg.tencent-cloud.cn/raw/698eb46e57f014573c48fe17b27036dd.png)



:::
::: 选择 cuDNN 版本
NVIDIA cuDNN 是用于深度神经网络的 GPU 加速库。其强调性能、易用性和低内存开销。NVIDIA cuDNN 可以集成到更高级别的机器学习框架中，例如谷歌的 Tensorflow、加州大学伯克利分校的流行 caffe 软件。简单的插入式设计可以让开发人员专注于设计和实现神经网络模型，而不是简单调整性能，同时还可以在 GPU 上实现高性能现代并行计算。

cuDNN 是基于 CUDA 的深度学习 GPU 加速库，有它才能在 GPU 上完成深度学习的计算。如需在 CUDA 上运行深度神经网络，需安装 cuDNN，才能使 GPU 进行深度神经网络的工作，工作速度相较 CPU 快很多。cuDNN 版本与 CUDA 版本的对应关系请参见 [cuDNN Archive](https://developer.nvidia.com/rdp/cudnn-archive)。


:::
::: 选择 Pytorch 版本

您需根据 CUDA 版本，选择对应的 Pytorch 版本，匹配版本信息请参见 [previous-versions](https://pytorch.org/get-started/previous-versions)。

<dx-alert infotype="notice" title="">
CUDA 及 Pytorch 最新版本不一定是最佳选择，可能出现适配问题。建议在查阅版本适配信息后，选择合适的版本后再安装对应驱动。
</dx-alert>


:::
::: 选择 TensorFlow 版本

Tensorflow 较 Pytorch 稍复杂，它还需要 Python、编译器的版本支持。CPU、GPU 版本与 Python、CUDA、cuDNN 的版本对应关系如下：
- [基于 CPU 版本的 TensorFlow 版本](https://tensorflow.google.cn/install/source_windows#cpu)
- [基于 GPU 版本的 TensorFlow 版本](https://tensorflow.google.cn/install/source_windows#gpu)


:::
</dx-accordion>


## 操作步骤

### 创建实例
参考 [购买 NVIDIA GPU 实例](https://cloud.tencent.com/document/product/560/30211)，创建 GPU 云服务器实例。
若您已具备 GPU 云服务器实例，则可参考 [重装系统](https://cloud.tencent.com/document/product/213/4933)，重置已有实例的操作系统。



### 安装驱动、CUDA 及 cuDNN

#### 安装显卡驱动
1. 参考 [使用标准方式登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/57778)，登录已创建的 GPU 云服务器。
2. 使用浏览器访问 [NVIDIA 官网](https://www.nvidia.com/download/index.aspx?lang=en-us)，并选择显卡的驱动版本。本文选择配置如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/97d4245fca1fab786cac7f273d24c870.png)
3. 选择 **SEARCH** 进入下载页面，单击**下载**即可。
若您想通过下载至本地，再通过 FTP 上传至 GPU 云服务器，可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
4. 下载完成后，请双击安装包，根据页面提示完成安装。


#### 安装 CUDA
1. 进入 [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive)，选择对应版本。本文以下载10.2版本为例，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0abcdcd228f7473630056793d9751a49.png)
2. 进入 “CUDA Toolkit 10.2 Download” 页面，选择对应系统配置。本文选择配置如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/468af37966a75b3f2a8d437fe88c88d7.png)
3. 单击 **Download**，开始下载。
4. 下载完成后，请双击安装包，并根据页面提示进行安装。其中，请注意以下步骤：
 - 在弹出的 “CUDA Setup Package” 窗口中，Extraction path 为暂时存放地址，无需修改，保持默认并单击 **OK**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6d651817a59ad13fd908088b1add4b36.png)
 - 在“许可协议”步骤中，选择“自定义”并单击**下一步**。如下图所示：
 ![](https://qcloudimg.tencent-cloud.cn/raw/727857dfa0ce1ffce9c3548ee2db24ee.png)
 根据实际需求选择安装组件，并单击**下一步**。如下图所示：
 ![](https://qcloudimg.tencent-cloud.cn/raw/1fc07d6706a932dab471c411bf9391a3.png)
 其余选项请根据页面提示，及实际需求进行选择，直至安装完毕。


#### 配置环境变量
1. 在操作系统界面，右键单击左下角的 <img src="https://qcloudimg.tencent-cloud.cn/raw/0cfefcbe7474bf6b532a589c53314d5b.png" style="margin:-3px 0px">，在弹出菜单中选择**运行**。
2. 在“运行”窗口中输入 `sysdm.cpl`，并单击**确定**。
3. 在打开的“系统属性”窗口中，选择**高级**页签，并单击**环境变量**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e1a875e3d5bb1aa54d704707413f6e68.png)
4. 选择“系统变量”中的 “Path”，单击**编辑**。
5. 在弹出的“编辑环境变量”窗口中，新建并输入如下环境变量配置。
```shellsession
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2 
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\bin 
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\lib\x64
C:\Program Files\NVIDIA Corporation\NVSMI
```
编辑完成后如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9543533dfdd020e240f5e320ac81e1f6.png)
6. 连续单击3次**确定**，保存设置。


#### 检查显卡驱动及 CUDA
1. 在操作系统界面，右键单击左下角的 <img src="https://qcloudimg.tencent-cloud.cn/raw/0cfefcbe7474bf6b532a589c53314d5b.png" style="margin:-3px 0px">，在弹出菜单中选择**运行**。
2. 在“运行”窗口中输入 `cmd`，并单击**确定**。
3. 在 cmd 窗口中：
 - 执行以下命令，检查显卡驱动是否安装成功。
```shellsession
nvidia-smi
```
返回如下图所示界面表示显卡驱动安装成功。下图为正在运行中的 GPU，在 GPU 运行时，该命令可查看 GPU 的使用情况。
![](https://qcloudimg.tencent-cloud.cn/raw/f99dbdf7c0bc316f974a614d08f64000.png)
 - 执行以下命令，检查 CUDA 是否安装成功。
```shellsession
nvcc -V
```
返回如下图所示界面表示 CUDA 安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/bf0e3e94af63bb2fa2c982d4b73e6000.png)


#### 安装 cuDNN
1. 前往 [cuDNN Download](https://developer.nvidia.com/rdp/cudnn-download) 页面，单击 **Archived cuDNN Releases** 查看更多版本。
2. 找到所需 cuDNN 版本，并下载。
3. 解压 cuDNN 压缩包，并将 `bin`、`include` 及 `lib` 文件夹拷贝至 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2` 目录下。
4. 至此已完成 cuDNN 安装。


### 安装深度学习库

#### 安装 Anaconda 

建议通过 [Anaconda](https://link.zhihu.com/?target=https%3A//www.anaconda.com/download/%23macos) 创建的虚拟环境安装 Pytorch 和 Tensorflow。通过 Anaconda，可便捷获取包并对包进行管理，同时可统一管理环境。Anaconda 包含了 conda、Python 在内的超过180个科学包及其依赖项，安装过程简单，能高性能使用 Python 和 R 语言，且有免费的社区支持。

1. 前往 [Anaconda 官网](https://www.anaconda.com/distribution/)，拉至页面底部，选择 **archive** 查看更多版本。
2. 在页面中下载所需版本，本文以下载 `Anaconda3-2019.03-Windows-x86_64` 为例。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cccbeb4a460836ad734b170f96ec357e.png)
3. 请双击安装包，并根据页面提示进行安装。其中，请注意以下步骤：
 - 在 “Choose Install Location” 步骤中，更改默认安装路径。因默认安装路径 C 盘中的 ProgramData 文件夹为隐藏文件夹，为了方便管理，建议安装在其他文件夹。下图所示为默认安装路径：
![](https://qcloudimg.tencent-cloud.cn/raw/80133f6cde9dc874a505a44f31936e27.png)
 - 在 “Advanced Installation Options” 步骤中，勾选全部选项，表示将 Anaconda 安装路径添加至环境变量，并将 Python 3.7 作为解释器。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e1e700f9f3d0e439f95ab358a47fd434.png)
4. 单击 **Install** 等待完成安装。


#### 配置 Anaconda
1. 在操作系统界面，单击左下角的 <img src="https://qcloudimg.tencent-cloud.cn/raw/0cfefcbe7474bf6b532a589c53314d5b.png" style="margin:-3px 0px">，在弹出菜单中选择 **Anaconda Prompt**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dc8be81800a9b339bfbae2e0463532bb.png)
2. 在打开的 “Anaconda Prompt” 命令行窗口中，执行以下命令，创建虚拟环境。
```shellsession
conda create -n xxx_env python=3.7
```
<dx-alert infotype="explain" title="">
`xxx_env` 为环境名，`python=3.7` 为 Python 版本，您可根据实际需求进行修改。
</dx-alert>
创建成功即如下图所示：
<br><img src="https://qcloudimg.tencent-cloud.cn/raw/e24c8a11cd8db38b3b5a38ce9083f073.png"/>
<br>
您可使用以下命令进入或退出已创建的虚拟环境。进入虚拟环境后，即可按照实际需求安装包。
```shellsession
#激活命令
conda activate xxx_env
#退出命令
conda deactivate
```



#### 安装 Pytorch
前往 [Pytorch 官网](https://pytorch.org/get-started/previous-versions/)，使用官网推荐的安装代码。
本文已安装 CUDA 版本为10.2，并选择 pip 安装方式，则在已创建的 `xxx_env` 虚拟环境中执行如下命令进行安装：
```shellsession
# CUDA 10.2
pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```
可通过替换源，加快安装速度，替换为清华源后则执行如下命令：
```shellsession
# CUDA 10.2
pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html -i https://pypi.tuna.tsinghua.edu.cn/simple
```


#### 安装 Tensorflow
执行以下命令，安装 Tensorflow_gpu_2.2.0。
```shellsession
pip install tensorflow-gpu==2.2.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```
执行以下命令，安装 keras。
```shellsession
pip install keras -i https://pypi.tuna.tsinghua.edu.cn/simple
```

至此，已完成了基本深度学习库的安装。您可参考本文方法安装更多所需要的包，并利用 Anaconda 自带的 jupyter notebook、Spyder 具或者安装 PyCharm 等工具开始代码学习！








