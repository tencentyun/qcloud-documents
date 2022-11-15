## 操作场景

本文介绍如何在服务器上安装 TACO Infer。TACO Infer 的安装包包括 Python Wheel 包和推理 SDK 包两个部分。Python Wheel 包用于在具有目标加速芯片的机器环境中对模型进行优化，SDK 则用于 C++开发模型推理部署。


## 使用环境要求[](id:requirements)

<table>
<tr>
<th>具体项</th>
<th>说明</th>
</tr>
<tr>
<td width="15%">操作系统</td>
<td>TACO Infer 针对 CentOS 7.9进行了全面的测试，建议您优先选用 CentOS 7.9进行 TACO Infer 的使用和部署。目前仅支持 Linux 操作系统，如使用其他版本 Linux 操作系统遇到问题，欢迎 <a href="https://cloud.tencent.com/document/product/1573/74094">联系我们</a> 获取支持。</td>
</tr>
<tr>
<td>计算设备</td>
<td>TACO Infer 目前开放测试的版本支持 Intel 和 AMD 系列的 CPU 优化，后续会支持更多优化目标硬件，请您关注产品动态。<br>
目前腾讯云上的畅销高性能 CPU 计算机型包括：
<ul style="margin-bottom:0px">
<li>云服务器 CVM：标准型 S6，SA3 等。更多实例信息请参见 <a href="https://cloud.tencent.com/document/product/213/11518">云服务器实例规格</a>。</li>
<li>裸金属服务器：高 IO 型 BMI5，标准型 BMSA2 等。更多实例信息请参见 <a href="https://cloud.tencent.com/document/product/386/63404">裸金属服务器实例规格</a>。</li>
</ul>
</td>
</tr>
<tr>
<td>ABI 版本</td>
<td>TACO Infer 支持 CXX11 ABI。</td>
</tr>
<tr>
<td>Python 版本</td>
<td>TACO Infer 支持 Python 3.6及以上版本，建议您安装支持版本的 Python环境。</td>
</tr>
<tr>
<td>框架版本</td>
<td>TACO Infer 目前开放测试的版本支持 TensorFlow 模型优化，对 TF 1.14和1.15两个主要版本进行了全面的测试。<br>后续会支持更多框架，请您关注产品动态。如使用其他版本遇到任何问题，欢迎联系我们获取支持。</td>
</tr>
</table>


## 操作步骤[](id:steps)


### 安装 TensorFlow
使用 TACO Infer 时，需要您的 Python 运行环境中已安装 TensorFlow。TACO Infer 目前可支持 TensorFlow 1.14 和 1.15，如果您在使用其他版本的过程中遇到问题，可以 [联系我们](https://cloud.tencent.com/document/product/1573/74094) 获取支持。

TensorFlow 1.14 安装命令如下：
```bash
pip install tensorflow==1.14
```
 


### 依赖安装

Taco Infer 依赖 libcurl、openssl、libuuid。您可以通过以下命令检查是否已经安装这些组件：
```bash
yum list installed | grep ${package}
```
若未安装，请通过以下命令安装。
- libcurl
```bash
yum install libcurl-devel
```
- openssl
```bash
yum install openssl-devel
```
- libuuid
```bash
yum install libuuid-devel
```


### 获取 Wheel 包及 SDK 包[](id:getWheelSDK)
填写 [TACO Infer 调查问卷](https://wj.qq.com/s2/10076022/0280/)，即可获得 TACO Infer Python Wheel 包和 SDK 安装包。目前支持计算环境和框架请参见 [使用环境要求](https://cloud.tencent.com/document/product/1573/74091#requirements)，若有其他版本需要可以 [联系我们](https://cloud.tencent.com/document/product/1573/74094)。


### 安装 Wheel 包
通过 pip 命令，即可安装 Taco python 包：
```bash
pip install ${path/to/wheel_package}
```

### 获取 SDK 包
 建议将解压后的库文件拷贝到 `/usr/local/lib` 下，以便 ld 程序能够找到 Taco 动态链接库进行链接。

SDK 包中存在三个动态链接库和一个可执行文件：
- libtaco_tf.so
- libtidy_ops.so
- libomp-1fdec59b.so
- tidy_vm
