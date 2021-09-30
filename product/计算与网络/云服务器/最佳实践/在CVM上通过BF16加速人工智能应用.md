## 操作场景
腾讯云第五代次实例 C5、S5、BMS5、M5采用第三代智能英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cooper Lake。其中，英特尔<sup>®</sup> DL Boost 深度学习加速采用 BF16，可使人工智能性能性能提升1.93倍。

本文以 C5 实例为例，介绍如何在 CVM 上通过 BF16 加速人工智能应用。

## 原理说明
### BF16

BF16（也称 bfloat16 或 Brain Float 16）由 Google 发明。Intel 在第三代英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cooper Lake-SP 所包含的深度学习加速技术（英特尔<sup>®</sup> DL Boost）中全新集成了 BF16 功能。

<dx-accordion>
::: 数据格式[](id:RecommendedSelection)
BF16 提供和 FP32 相同的宽度，但精度损失很少，非常适合应用于对精度要求较高的场景。许多模型在使用 BF16时，可实现与使用32位浮点数值时相同的准确率，部分模型在使用 BF16 时甚至表现出准确率的提升。BF16 可使内存需求减半，并且由于 BF16 以一半的位数完成任务，因此 BF16 理论上计算性能可以翻倍。
BF16 浮点数格式如下图所示：
<img src="https://main.qcloudimg.com/raw/254d7f71a76454503669c56e2477696e.png" width="65%"/>
精度如下图所示：
![](https://main.qcloudimg.com/raw/8642ad31bfabd6a0d77cd2fbd22fb6c6.png)
:::
::: 准确率[](id:RecommendedSelection)
BF16 能达到近似 FP32 的准确率。在 PyTorch v1.7.0上，以 Resnet50 为例，采用相同的模型，FP32 和 BF16 的精度如下图所示：
<img src="https://main.qcloudimg.com/raw/973015246928705055cac697552c13b7.png" width="65%"/>
:::
</dx-accordion>


### 在 PyTorch 和 Tensorflow 中使用 FP32 和 BF16 混精方式进行推理[](id:RecommendedSelection)

<dx-accordion>
::: PyTorch 模型
英特尔<sup>®</sup>开发的 IPEX（Intel Extension for PyTorch）是 PyTorch 的 Python 扩展，利用 IPEX 可以方便地将 PyTorch 模型中的算子在运行过程中动态地转化为 BF16 算子。仅需在 Python 脚本中将 IPEX 的 `auto_mixed_precision` 设置为 BF16，再将数据和模型添加到 IPEX 中即可。如下图所示：
<img src="https://main.qcloudimg.com/raw/f3624d7cfd49a993618d80027dfa7bdb.png" alt="pytorch-enabling" width="65%;"><br>
>?
>- 如需了解英特尔 IPEX 安装方法，请前往 [Intel<sup>®</sup> Extension for PyTorch官方github repo](https://github.com/intel/intel-extension-for-pytorch#installation)，根据安装指南中提供的信息，对 PyTorch 以及 Intel<sup>®</sup> Extension for PyTorch (IPEX) 进行编译以及安装。
>- 如需了解英特尔 IPEX 更多信息，请参见 [intel-extension-for-pytorch](https://github.com/intel/intel-extension-for-pytorch)。
>
:::
::: Tensorflow 模型
在 Tensorflow 中可以通过设置 AutoMixedPrecision 方便地使用 BF16，在脚本中只需修改两处。步骤如下：
1. 打开 AutoMixedPrecision 代码。如下图所示：
![](https://main.qcloudimg.com/raw/49bbab553c05843b52e83a76c178543f.png)
2. 添加需要使用 BF16的算子列表。如下图所示：
<img src="https://main.qcloudimg.com/raw/8938cf97afd333ecc5ec2f133117a94a.png" width="80%;"><br>
如需了解具体支持的转换算子列表，请参见 [auto_mixed_precision_lists.h](https://github.com/reedwm/tensorflow/blob/auto_mp_mkl/tensorflow/core/grappler/optimizers/auto_mixed_precision_lists.h#L343-L454)。
:::
</dx-accordion>

## 操作步骤

### 使用云市场镜像创建实例
英特尔<sup>®</sup>向腾讯云镜像市场提供了免费的 BF16 的镜像。该镜像中已经设置好使用 BF16 数据格式的环境，支持 PyTorch 和 Tensorflow 两种机器学习库。用户登录运行的镜像后，不需要设置任何环境，可以直接运行各种不同模型的推理运算，体验 BF16带来的性能提升。步骤如下：
1. 前往 [Intel BF16 优化工具 ](https://market.cloud.tencent.com/products/28521) 镜像页面，勾选“ 同意 《云市场商品服务协议》 与 《腾讯云云市场用户协议》”后，单击【立即购买】。
2. 创建云服务器实例，详情请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。
其中，如需获取 BF16 的支持，**实例**请选择处理器型号为 Intel Xeon Cooper Lake 机型。本文以使用 [计算型 C5](https://cloud.tencent.com/document/product/213/11518#C5) 为例，实例其他规格请按需选择。如下图所示：
![](https://main.qcloudimg.com/raw/b25b6c612565dbd6473dd23d81899967.png)
>?更多实例规格参数介绍，请参见 [实例规格](https://cloud.tencent.com/document/product/213/11518)。
>


###  通过实例测试 BF16 性能加速[](id:RecommendedSelection)
1. 登录实例，详情请参见 [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，确认 CPU 是否支持 BF16。 
```
lscpu | grep "avx512_bf16"
``` 返回如下目录结构：
```
miniconda  pkgs  run-pt.py  run-pt.sh  run-tf.sh  tf1.15
``` 各文件内容如下：
 - **miniconda**：miniconda 的安装目录。镜像中依赖库通过 miniconda 安装。
 - **pkgs**：为了省去用户通过源代码编译安装的麻烦，此目录中已包含 Pytorch、Tensorflow、IPEX 的 wheel 文件和 miniconda 的安装文件。
 - **run-pt.py & run-pt.sh**：运行 PyTorch 模型的 Python 脚本和 Shell 脚本文件。
 - **run-tf.sh**：运行 Tensorflow 的 Shell 脚本文件。
 - **tf1.15**：包含 Tensorflow 的多种模型。
3. 可使用以下命令运行不同的模型：
 - **模型介绍**：
<table>
<thead>
<tr>
<th>模型</th>
<th>简介</th>
</tr>
</thead>
<tbody><tr>
<td>alexnet</td>
<td>是一种卷积神经网络（CNN），首次在大规模图像数据集实现了深层卷积神经网络结构。</td>
</tr>
<tr>
<td>densenet121</td>
<td>是一种拥有较深层数的卷积神经网络。</td>
</tr>
<tr>
<td>googlenet</td>
<td>是一种卷积神经网络模型，能更高效的利用计算资源，在相同的计算量下能提取到更多的特征，从而提升训练结果。</td>
</tr>
<tr>
<td>resnet50</td>
<td>残差网络（Residual Network），广泛用于目标分类等领域以及作为计算机视觉任务主干经典神经网络的一部分。</td>
</tr>
<tr>
<td>inceptionv3</td>
<td>GoogleNet 改进后的版本。</td>
</tr>
<tr>
<td>mnasnet</td>
<td>一种移动端 CNN 模型的自动神经结构搜索方法</td>
</tr>
<tr>
<td>mobilenet</td>
<td>专注于移动端或者嵌入式设备中的轻量级 CNN 网络。</td>
</tr>
<tr>
<td>squeezenet</td>
<td>一种轻量且高效的 CNN 模型，参数比 AlexNet 少50倍，但模型正确率与 AlexNet 接近。</td>
</tr>
<tr>
<td>vgg16</td>
<td>一种有16层网络结构的神经网络模型。</td>
</tr>
<tr>
<td>large-bert</td>
<td>BERT（Bidirectional Enoceder Representations from  Transformers），即双向的 Transformers  的 Encoder。是 Google 于2018年10月提出的用于自然语言处理（NLP）的预训练技术，网络结构主要分为 Base 和 Large 两种。</td>
</tr>
<tr>
<td>ssd-mobilenet</td>
<td>前端网络设为 MobileNet，后端算法为 SSD（Sing-Shot Detection，一种 one-stage 检测算法）的目标检测模型。</td>
</tr>
</tbody></table>
<table>
<thead>  - **PyTorch 模型**：
<tr>
<th>PyTorch 模型</th>
<th><strong>未优化</strong></th>
<th>使用 IPEX FP32优化</th>
<th>使用 IPEX BF16优化</th>
</tr>
</thead>
<tbody><tr>
<td>alexnet</td>
<td>./run-pt.sh alexnet none none jit</td>
<td>./run-pt.sh alexnet ipex fp32 jit</td>
<td>./run-pt.sh alexnet ipex bf16 jit</td>
</tr>
<tr>
<td>densenet121</td>
<td>./run-pt.sh densenet121 none none jit</td>
<td>./run-pt.sh densenet121 ipex fp32 jit</td>
<td>./run-pt.sh densenet121 ipex  bf16 jit</td>
</tr>
<tr>
<td>googlenet</td>
<td>./run-pt.sh googlenet none none jit</td>
<td>./run-pt.sh googlenet ipex fp32</td>
<td>./run-pt.sh googlenet ipex bf16</td>
</tr>
<tr>
<td>resnet50</td>
<td>./run-pt.sh resnet50 none none jit</td>
<td>./run-pt.sh resnet50 ipex fp32 jit</td>
<td>./run-pt.sh resnet50 ipex bf16 jit</td>
</tr>
<tr>
<td>inceptionv3</td>
<td>./run-pt.sh inception_v3 none none jit</td>
<td>./run-pt.sh inceptionv3 ipex fp32</td>
<td>./run-pt.sh inceptionv3 ipex bf16</td>
</tr>
<tr>
<td>mnasnet0_5</td>
<td>./run-pt.sh mnasnet0_5 none none jit</td>
<td>./run-pt.sh mnasnet0_5 ipex fp32 jit</td>
<td>./run-pt.sh mnasnet0_5 ipex bf16 jit</td>
</tr>
<tr>
<td>mobilenetv2</td>
<td>./run-pt.sh mobilenet_v2 none none jit</td>
<td>./run-pt.sh mobilenetv2 ipex fp32 jit</td>
<td>./run-pt.sh mobilenetv2 ipex bf16 jit</td>
</tr>
<tr>
<td>squeezenet1_0</td>
<td>./run-pt.sh squeezenet1_0 none none jit</td>
<td>./run-pt.sh squeezenet1_0 ipex fp32 jit</td>
<td>./run-pt.sh squeezenet1_0 ipex bf16 jit</td>
</tr>
<tr>
<td>vgg16</td>
<td>./run-pt.sh vgg16 none none jit</td>
<td>./run-pt.sh vgg16 ipex fp32 jit</td>
<td>./run-pt.sh vgg16 ipex bf16 jit</td>
</tr>
</tbody></table>
 - **Tensorflow 模型**：
<table>
<thead>
<tr>
<th>Tensorflow 模型</th>
<th><strong>未优化</strong></th>
<th>使用 BF16优化</th>
</tr>
</thead>
<tbody><tr>
<td>resnet50</td>
<td>./run-tf.sh resnet50</td>
<td>./run-tf.sh resnet50 bf16</td>
</tr>
<tr>
<td>mobilenetv1</td>
<td>./run-tf.sh mobilenetv1</td>
<td>./run-tf.sh mobilenetv1 bf16</td>
</tr>
<tr>
<td>large-bert</td>
<td>./run-tf.sh large-bert</td>
<td>./run-tf.sh large-bert bf16</td>
</tr>
<tr>
<td>ssd-mobilenet</td>
<td>./run-tf.sh ssdmobilenet</td>
<td>./run-tf.sh ssdmobilenet bf16  登录实例</td>
</tr>
</tbody></table>


###  获取 BF16 性能测试数据 [](id:RecommendedSelection)

基于 Intel 第三代英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cooper Lake，在云服务器8核32G内存场景，基于不同模型下测试的性能数据如下：
>?由于实际模型及物理配置不同，性能数据会有一定差别，本文提供数据仅供参考。

#### PyTorch 模型
利用 FP32 + BF16 的混合精度方式，运行多个 PyTorch 模型，配置信息和标准化的性能提升如下图所示：
![](https://main.qcloudimg.com/raw/40017f30e1c345597d4e759479a6bcb1.png)
性能数值如下表：  
<table>
<thead>
<tr>
<th>Pytorch</th>
<th>优化前</th>
<th>IPEX 优化后 FP32</th>
<th>IPEX 优化后 BF16</th>
</tr>
</thead>
<tbody><tr>
<td>alexnet</td>
<td>110.71</td>
<td>140.18</td>
<td>251.48</td>
</tr>
<tr>
<td>densenet121</td>
<td>29.39</td>
<td>44.83</td>
<td>59.3</td>
</tr>
<tr>
<td>googlenet</td>
<td>31.89</td>
<td>80.09</td>
<td>106.76</td>
</tr>
<tr>
<td>resnet50</td>
<td>27.61</td>
<td>56.74</td>
<td>98.35</td>
</tr>
<tr>
<td>inception_v3</td>
<td>30.41</td>
<td>47.33</td>
<td>64.59</td>
</tr>
<tr>
<td>mnasnet0_5</td>
<td>174.51</td>
<td>584.65</td>
<td>633.84</td>
</tr>
<tr>
<td>mobilenet_v2</td>
<td>93.6</td>
<td>355.76</td>
<td>474.96</td>
</tr>
<tr>
<td>squeezenet1_0</td>
<td>70.52</td>
<td>240.29</td>
<td>340.88</td>
</tr>
<tr>
<td>vgg16</td>
<td>10.28</td>
<td>15.06</td>
<td>25.42</td>
</tr>
</tbody></table>

#### TensorFlow 模型

利用 FP32 + BF16 的混合精度方式，运行多个 Tensorflow 模型，配置信息和标准化的性能提升如下图所示：
![](https://main.qcloudimg.com/raw/172fa14e0b35038e0a684dd51ddbd706.png)
性能数值如下表：
<table>
<thead>
<tr>
<th>TensorFlow</th>
<th>优化前</th>
<th>BF16优化后</th>
</tr>
</thead>
<tbody><tr>
<td>resnet50</td>
<td>56.89</td>
<td>95.38</td>
</tr>
<tr>
<td>mobilenetv1</td>
<td>91.41</td>
<td>161.48</td>
</tr>
<tr>
<td>large-bert</td>
<td>0.77</td>
<td>1.85</td>
</tr>
<tr>
<td>ssd-mobilenet</td>
<td>25.86</td>
<td>38.38</td>
</tr>
</tbody></table>

