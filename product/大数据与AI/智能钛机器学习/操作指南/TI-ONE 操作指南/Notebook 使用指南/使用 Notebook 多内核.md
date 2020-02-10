## 操作场景
本文档将向您演示如何在 Notebook 中**切换多内核使用**、**查看已有依赖包**以及**安装第三方库**。

## 操作步骤
### 选择适合自己的 Notebook 多内核环境
目前平台提供了 9 种内核选择，包括
+ 纯净的 python 环境
- python3 : conda_python3
- python2 : conda_python2
+ TensorFlow 环境
- TensorFlow 1.14 + python3 : conda_tensorflow_py3
- TensorFlow 1.14 + python2 : conda_tensorflow_py2
- TensorFlow 2.0.0 + python3 : conda_tensorflow2_py3
+ PyTorch 环境
- Pytorch 1.2.0 + python3 : conda_pytorch_py3
- Pytorch 1.2.0 + python2 : conda_pytorch_py2
+ MxNet 环境
- MxNet 1.5.0 + python3 : conda_mxnet_py3
- MxNet 1.5.0 + python2 : conda_mxnet_py2

![](https://main.qcloudimg.com/raw/097aa1eb7127f31e2659ab89d2d18f8b.png)

### 查看已有依赖包
在对应内核的输入框中输入 !pip list，查看该内核已有的依赖包；

![](https://main.qcloudimg.com/raw/37bd8d81d32d3efbd90732a92e90591d.png)

### 安装外部依赖包
#### 依赖包在腾讯云 pip 源仓库中已有
如果您期望安装的依赖包及其对应版本可以在 http://mirrors.cloud.tencent.com/pypi/simple/ 中找到，则可以直接在对应内核的命令框中通过 !pip install 安装

![](https://main.qcloudimg.com/raw/60f0fd0320a0fc98b780637ea42bd493.png)

#### 依赖包不在腾讯云 pip 源仓库中
在默认情况下，Notebook 具有访问外网的权限。您可以通过外网下载第三方依赖包到本地，再在内核的命令框中通过的 !pip install 安装

如果您的 Notebook 额外配置了不带有 Internet 访问权限的子网时，可以考虑：
- 首先将所需的第三方依赖包从外部网络下载；
- 其次，上传依赖包，单击“上传文件”，将依赖包上传。上传大小限制300MB；

![](https://main.qcloudimg.com/raw/f7ef2e6f31e5a1e66d96cb2f8f9835ba.png)

- 最后，新建 notebook 文件，在对应内核的命令框中通过 pip install 命令安装上传的外部包；
- 上述步骤成功后，后续您才能通过 import 命令使用


###  注意事项
1. 安装完依赖包后，部分依赖包需要重启 kernel 才能进行 import 操作

![](https://main.qcloudimg.com/raw/3e72d7e56d4fcf96f44b4ea6163f1c19.png)

