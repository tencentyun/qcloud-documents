## 操作场景
腾讯云第六代实例 S6 及第五代实例 S5、M5、C4、IT5、D3 全面采用第二代智能英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cascade Lake。提供了更多的指令集和特性，可用于加速人工智能的应用，同时集成的大量硬件增强技术，其中 AVX-512（高级矢量扩展）能够为 AI 推理过程提供强劲的并行计算能力，使用户获得更好的深度学习效果。

本文以 S5、M5 实例为例，介绍如何在 CVM 上通过 AVX512 加速人工智能应用。

## 选型推荐[](id:RecommendedSelection)
云服务器的多种实例规格可用于多种应用开发，其中 [标准型 S6](https://cloud.tencent.com/document/product/213/11518#S6)、[标准型 S5](https://cloud.tencent.com/document/product/213/11518#S5) 及 [内存型 M5](https://cloud.tencent.com/document/product/213/11518#M5) 适用于机器学习或深度学习。这些实例配备了第二代 Intel<sup>®</sup> Xeon<sup>®</sup> 处理器，适配 Intel<sup>®</sup> DL boost 学习能力。推荐配置如下表：
<table>
<tr>
<th>平台类型</th><th>实例规格</th>
</tr>
<tr>
<td>深度学习训练平台</td>
<td> 84vCPU 的标准型 S5 实例或 48vCPU 的内存型 M5 实例。</td>
</tr>
<tr>
<td>深度学习推理平台</td>
<td>8/16/24/32/48vCPU 的标准型 S5 实例或内存型 M5 实例。 </td>
</tr>
<tr>
<td>机器学习训练或推理平台</td>
<td>48vCPU 的标准型 S5 实例或 24vCPU 的内存型 M5 实例。</td>
</tr>
</table>
 
 ## 具备优势
使用 Intel<sup>®</sup> Xeon<sup>®</sup> 可扩展处理器运行机器学习或深度学习工作负载时，具备以下优势：
- 适合处理大内存型工作负载、医学成像、GAN、地震分析、基因测序等场景中使用的 3D-CNN 拓扑。
- 支持使用简单的 `numactl` 命令进行灵活的核心控制，也适用小批量的实时推理。
- 强大的生态系统支持，可直接在大型集群上进行分布式训练，避免额外添加大容量存储和昂贵的缓存机制来进行规模化架构的训练。
- 可在同一个集群中支持多种工作负载（例如 HPC、BigData、AI 等），获取更优的 TCO。
- 通过 SIMD 加速，满足众多实际深度学习应用程序的计算要求。
- 同一套基础架构可直接用于训练及推理。
 
## 操作步骤
### 创建实例
创建云服务器实例，详情请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。其中，实例规格需根据 [选型推荐](#RecommendedSelection) 及实际业务场景进行选择。如下图所示：
![](https://main.qcloudimg.com/raw/787c6b14601fbed2b93970c39b71175f.png)
>?更多实例规格参数介绍，请参见 [实例规格](https://cloud.tencent.com/document/product/213/11518)。

### 登录实例
登录云服务器实例，详情请参见 [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。

### 部署示例
您可根据实际业务场景，参考以下示例部署人工智能平台，进行机器学习或深度学习任务：

<dx-accordion>
::: 示例1：使用\sIntel<sup>®</sup>优化深度学习框架\sTensorFlow*
在第二代智能英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cascade Lake 上 PyTorch 和 IPEX 会自动启用针对 AVX-512 指令集进行的优化，以尽可能提高运算性能。

TensorFlow\* 是用于大规模机器学习及深度学习的热门框架之一。您可参考该示例，提升实例的训练及推理性能。更多框架部署相关信息，请参见 [Intel<sup>®</sup> Optimization for TensorFlow\* Installation Guide](https://software.intel.com/content/www/us/en/develop/articles/intel-optimization-for-tensorflow-installation-guide.html)。操作步骤如下：

#### 部署 TensorFlow\* 框架
1. 在云服务器中，安装 Python。本文以 Python 3.7 为例。
2. 执行以下命令，安装 Intel<sup>®</sup> 优化的 TensorFlow\* 版本 intel-tensorflow。
<dx-alert infotype="explain" title="">
建议使用**2.4.0及以上版本**，以获得最新的功能与优化。
</dx-alert> ```
pip install intel-tensorflow
```

#### 设置运行时优化参数
选择运行时参数优化方式。通常会使用以下两种运行接口，从而采取不同的优化设置。您可结合实际需求选择，更多参数优化配置说明请参见 [General Best Practices for Intel<sup>®</sup> Optimization for TensorFlow](https://github.com/IntelAI/models/blob/master/docs/general/tensorflow/GeneralBestPractices.md)。
 - **Batch inference**：设置 BatchSize >1，并测量每秒可以处理的输入张量总数。通常情况下，Batch Inference 方式可以通过使用同一个 CPU socket 上的所有物理核心来实现最佳性能。
 - **On-line Inference**（也称为实时推断）：设置 BS = 1，并测量处理单个输入张量（即一批大小为1）所需时间的度量。在实时推理方案中，可以通过多实例并发运行来获取最佳的吞吐。

操作步骤如下：
1. 执行以下命令，获取系统的物理核个数。
```
lscpu | grep "Core(s) per socket" | cut -d':' -f2 | xargs
```
2. 设置优化参数，可选择以下任一方式：
 - 设置环境运行参数。在环境变量文件中，添加以下配置：
``` 
 export OMP_NUM_THREADS= # <physicalcores>
 export KMP_AFFINITY="granularity=fine,verbose,compact,1,0"
 export KMP_BLOCKTIME=1
 export KMP_SETTINGS=1
 export TF_NUM_INTRAOP_THREADS= # <physicalcores>
 export TF_NUM_INTEROP_THREADS=1
 export TF_ENABLE_MKL_NATIVE_FORMAT=0
```
 - 在代码中增加环境变量设置。在运行的 Python 代码中，加入以下环境变量配置：
```
import os
os.environ["KMP_BLOCKTIME"] = "1"
os.environ["KMP_SETTINGS"] = "1"
os.environ["KMP_AFFINITY"]= "granularity=fine,verbose,compact,1,0"
if FLAGS.num_intra_threads > 0:
    os.environ["OMP_NUM_THREADS"]= # <physical cores>
os.environ["TF_ENABLE_MKL_NATIVE_FORMAT"] = "0"
config = tf.ConfigProto()
config.intra_op_parallelism_threads = # <physical cores>
config.inter_op_parallelism_threads = 1
tf.Session(config=config)
```

#### 运行 TensorFlow\* 深度学习模型的推理
可参考 [Image Recognition with ResNet50, ResNet101 and InceptionV3](https://github.com/IntelAI/models/blob/master/docs/image_recognition/tensorflow/Tutorial.md) 运行其他机器学习/深度学习模型推理。本文以 benchmark 为例，介绍如何运行 ResNet50 的 inference benchmark。详情请参见 [ResNet50 (v1.5)](https://github.com/IntelAI/models/blob/master/benchmarks/image_recognition/tensorflow/resnet50v1_5/README.md)。

#### 运行 TensorFlow\* 深度学习模型的训练
本文介绍如何运行 ResNet50 的 training benchmark，详情请参见 [FP32 Training Instructions](https://github.com/IntelAI/models/blob/master/benchmarks/image_recognition/tensorflow/resnet50v1_5/README.md#fp32-training-instructions)。

#### TensorFlow 性能展示

性能数据可参见 [Improving TensorFlow* Inference Performance on Intel® Xeon® Processors](https://www.intel.com/content/www/us/en/artificial-intelligence/posts/improving-tensorflow-inference-performance-on-intel-xeon-processors.html)，根据实际模式、物理配置的不同，性能数据会有一定差别。以下性能数据仅供参考：
 - **延时性能**：
  通过测试，在 batch size 为1时选取适用于图像分类、目标检测的一些模型进行测试，会发现使用 AVX512 优化的版本相对于非优化版本所提供的推理性能有一些明显提升。例如在延迟上，优化后的 ResNet 50的延时降低为原来的45%。
 - **吞吐量性能**：
  通过设置增加 batch size 来测试吞吐性能，选取适用于图像分类、目标检测的一些模型进行测试，发现在吞吐的性能数据上也有明显提升，优化后 ResNet 50的性能提升为原来的1.98倍。

:::
::: 示例2：部署深度学习框架\sPyTorch*
#### 部署步骤
1. 在云服务器中，安装 Python3.6 或以上版本，本文以 Python 3.7 为例。
2. 前往 [Intel<sup>®</sup> Extension for PyTorch 官方github repo](https://github.com/intel/intel-extension-for-pytorch#installation)，根据安装指南中提供的信息，对 PyTorch 以及 Intel<sup>®</sup> Extension for PyTorch (IPEX) 进行编译以及安装。

#### 设置运行时优化参数

在第二代智能英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cascade Lake 上 PyTorch 和 IPEX 会自动启用针对 AVX-512 指令集进行的优化，以尽可能提高运算性能。

您可按照本步骤设置运行时参数优化方式，更多参数优化配置说明请参见 [Maximize Performance of Intel® Software Optimization for PyTorch* on CPU](https://software.intel.com/content/www/us/en/develop/articles/how-to-get-better-performance-on-pytorchcaffe2-with-intel-acceleration.html)。
 - **Batch inference**：设置 BatchSize > 1，并测量每秒可以处理的输入张量总数。通常情况下，Batch Inference 方式可以通过使用同一个 CPU socket 上的所有物理核心来实现最佳性能。
 - **On-line Inference**（也称为实时推断）：设置 BatchSize = 1，并测量处理单个输入张量（即一批大小为1）所需时间的度量。在实时推理方案中，可以通过多实例并发运行来获取最佳的吞吐量。

操作步骤如下：

1. 执行以下命令，获取系统的物理核个数。
```
lscpu | grep "Core(s) per socket" | cut -d':' -f2 | xargs
```
2. 设置优化参数，可选择以下任一方式：
 - 设置环境运行参数，使用 GNU OpenMP* Libraries。在环境变量文件中，添加以下配置：
``` 
export OMP_NUM_THREADS=physicalcores
export GOMP_CPU_AFFINITY="0-<physicalcores-1>"
export OMP_SCHEDULE=STATIC
export OMP_PROC_BIND=CLOSE
```
 - 设置环境运行参数，使用 Intel OpenMP* Libraries。在环境变量文件中，添加以下配置：
``` 
export OMP_NUM_THREADS=physicalcores
export LD_PRELOAD=<path_to_libiomp5.so>
export KMP_AFFINITY="granularity=fine,verbose,compact,1,0"
export KMP_BLOCKTIME=1
export KMP_SETTINGS=1
```


#### 运行 PyTorch* 深度学习模型的推理及训练优化建议

- 运行模型推理时，可使用 Intel<sup>®</sup> Extension for PyTorch 来获取性能提升。示例代码如下：
```
import intel_pytorch_extension
...
net = net.to('xpu')       # Move model to IPEX format
data = data.to('xpu')     # Move data  to IPEX format
...
output = net(data)        # Perform inference with IPEX
output = output.to('cpu') # Move output back to ATen format
```
- 推理及训练都可使用 jemalloc 来进行性能优化。jemalloc 是一个通用的 `malloc(3)` 实现，强调避免碎片化和可扩展的并发支持，旨在为系统提供的内存分配器。jemalloc 提供了许多超出标准分配器功能的内省、内存管理和调整功能。详情请参见 [jemalloc](https://github.com/jemalloc/jemalloc/wiki) 及 [示例代码](https://github.com/mingfeima/op_bench-py/blob/master/run.sh)。
- 关于多 socket 的分布式训练，详情请参见 [PSSP-Transformer 的分布式 CPU 训练脚本](https://github.com/mingfeima/pssp/blob/master/pssp-transformer/dist_train_cpu.sh)。

#### 性能结果

基于 Intel 第二代英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cascade Lake，在2*CPU（28核/CPU）及384G内存场景下，不同模型测试的性能数据可参见 [性能测试数据](https://software.intel.com/content/www/us/en/develop/articles/intel-and-facebook-collaborate-to-boost-pytorch-cpu-performance.html)。由于实际模型及物理配置不同，性能数据会有差别，本文提供的测试数据仅供参考。


:::
::: 示例3：使用\sIntel<sup>®</sup>AI\s低精度优化工具加速


Intel<sup>®</sup> 低精度优化工具是一个开源的 Python 库，旨在提供一个简单易用的、跨神经网络框架的低精度量化推理接口。用户可以通过对该接口的简单调用来对模型进行量化，提高生产力，从而加速低精度模型在第三代 Intel<sup>®</sup> Xeon<sup>®</sup> DL Boost 可扩展处理器平台上的推理性能。更多使用介绍请参见 [Intel<sup>®</sup> 低精度量化工具代码仓库](https://github.com/Intel/lpot/)。

#### 支持的神经网络框架版本
Intel<sup>®</sup>低精度优化工具支持：
Intel<sup>®</sup> 优化的 TensorFlow* `v1.15.0`、`v1.15.0up1`、`v1.15.0up2`、 `v2.0.0`、`v2.1.0`、`v2.2.0`、`v2.3.0`和`v2.4.0`。
Intel<sup>®</sup> 优化的 PyTorch `v1.5.0+cpu` 和 `v1.6.0+cpu`。
Intel<sup>®</sup> 优化的 MXNet `v1.6.0`、`v1.7.0`以及 ONNX-Runtime `v1.6.0`。

#### 实现框架
Intel<sup>®</sup> 低精度优化工具实现框架示意图如下：
![](https://main.qcloudimg.com/raw/6062f647b40e2900354fbc73d8a4248a.jpg)

#### 工作流程
Intel<sup>®</sup> 低精度优化工具工作流程示意图如下：
![](https://main.qcloudimg.com/raw/acbc366d69819b443064ba5df58608fc.png)

#### 量化模型性能与精度示例

部分由 Intel<sup>®</sup> 低精度优化工具量化的模型在 Intel 第二代英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cascade Lake 的获得的性能与精度如下：

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Framework</th>
    <th rowspan="2">Version</th>
    <th rowspan="2">Model</th>
    <th colspan="3">Accuracy</th>
    <th>Performance speed up</th>
  </tr>
  <tr>
    <td>INT8 Tuning Accuracy</td>
    <td>FP32 Accuracy Baseline</td>
    <td>Acc Ratio [(INT8-FP32)/FP32]</td>
    <td>Realtime Latency Ratio[FP32/INT8]</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>resnet50v1.5</td>
    <td>76.92%</td>
    <td>76.46%</td>
    <td>0.60%</td>
    <td>3.37x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>resnet101</td>
    <td>77.18%</td>
    <td>76.45%</td>
    <td>0.95%</td>
    <td>2.53x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>inception_v1</td>
    <td>70.41%</td>
    <td>69.74%</td>
    <td>0.96%</td>
    <td>1.89x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>inception_v2</td>
    <td>74.36%</td>
    <td>73.97%</td>
    <td>0.53%</td>
    <td>1.95x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>inception_v3</td>
    <td>77.28%</td>
    <td>76.75%</td>
    <td>0.69%</td>
    <td>2.37x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>inception_v4</td>
    <td>80.39%</td>
    <td>80.27%</td>
    <td>0.15%</td>
    <td>2.60x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>inception_resnet_v2</td>
    <td>80.38%</td>
    <td>80.40%</td>
    <td>-0.02%</td>
    <td>1.98x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>mobilenetv1</td>
    <td>73.29%</td>
    <td>70.96%</td>
    <td>3.28%</td>
    <td>2.93x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>ssd_resnet50_v1</td>
    <td>37.98%</td>
    <td>38.00%</td>
    <td>-0.05%</td>
    <td>2.99x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>mask_rcnn_inception_v2</td>
    <td>28.62%</td>
    <td>28.73%</td>
    <td>-0.38%</td>
    <td>2.96x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>vgg16</td>
    <td>72.11%</td>
    <td>70.89%</td>
    <td>1.72%</td>
    <td>3.76x</td>
  </tr>
  <tr>
    <td>tensorflow</td>
    <td>2.4.0</td>
    <td>vgg19</td>
    <td>72.36%</td>
    <td>71.01%</td>
    <td>1.90%</td>
    <td>3.85x</td>
  </tr>
</tbody>
</table>

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Framework</th>
    <th rowspan="2">Version</th>
    <th rowspan="2">Model</th>
    <th colspan="3">Accuracy</th>
    <th>Performance speed up</th>
  </tr>
  <tr>
    <td>INT8 Tuning Accuracy</td>
    <td>FP32 Accuracy Baseline</td>
    <td>Acc Ratio [(INT8-FP32)/FP32]</td>
    <td>Realtime Latency Ratio[FP32/INT8]</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>pytorch</td>
    <td>1.5.0+cpu</td>
    <td>resnet50</td>
    <td>75.96%</td>
    <td>76.13%</td>
    <td>-0.23%</td>
    <td>2.46x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.5.0+cpu</td>
    <td>resnext101_32x8d</td>
    <td>79.12%</td>
    <td>79.31%</td>
    <td>-0.24%</td>
    <td>2.63x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_base_mrpc</td>
    <td>88.90%</td>
    <td>88.73%</td>
    <td>0.19%</td>
    <td>2.10x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_base_cola</td>
    <td>59.06%</td>
    <td>58.84%</td>
    <td>0.37%</td>
    <td>2.23x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_base_sts-b</td>
    <td>88.40%</td>
    <td>89.27%</td>
    <td>-0.97%</td>
    <td>2.13x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_base_sst-2</td>
    <td>91.51%</td>
    <td>91.86%</td>
    <td>-0.37%</td>
    <td>2.32x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_base_rte</td>
    <td>69.31%</td>
    <td>69.68%</td>
    <td>-0.52%</td>
    <td>2.03x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_large_mrpc</td>
    <td>87.45%</td>
    <td>88.33%</td>
    <td>-0.99%</td>
    <td>2.65x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_large_squad</td>
    <td>92.85</td>
    <td>93.05</td>
    <td>-0.21%</td>
    <td>1.92x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_large_qnli</td>
    <td>91.20%</td>
    <td>91.82%</td>
    <td>-0.68%</td>
    <td>2.59x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_large_rte</td>
    <td>71.84%</td>
    <td>72.56%</td>
    <td>-0.99%</td>
    <td>1.34x</td>
  </tr>
  <tr>
    <td>pytorch</td>
    <td>1.6.0a0+24aac32</td>
    <td>bert_large_cola</td>
    <td>62.74%</td>
    <td>62.57%</td>
    <td>0.27%</td>
    <td>2.67x</td>
  </tr>
</tbody>
</table>

<dx-alert infotype="explain" title="">
表中的 PyTorch 和 Tensorflow 均指基于 Intel 优化后的框架，完整支持的量化模型列表请查阅 [在线文档](https://github.com/intel/lpot/blob/master/docs/full_model_list.md)。
</dx-alert>



#### Intel<sup>®</sup>低精度优化工具安装与使用示例 

1. 依次执行以下命令，使用 anaconda 建立名为 lpot 的 python3.x 虚拟环境。本文以 python 3.7 为例。
```plaintext
conda create -n lpot python=3.7
conda activate lpot
```
2. 安装 lpot，可通过以下两种方式：
    - 执行以下命令，从二进制文件安装。
``` plaintext
pip install lpot
```
    - 执行以下命令，从源码安装。
```plaintext
 git clone https://github.com/intel/lpot.git
 cd lpot
 pip install –r requirements.txt
 python setup.py install
```
3. 量化 TensorFlow ResNet50 v1.0。本文以 ResNet50 v1.0 为例，介绍如何使用本工具进行量化：
    1. 准备数据集。
执行以下命令，下载并解压 ImageNet validation 数据集。
```plaintext
mkdir –p img_raw/val && cd img_raw
wget http://www.image-net.org/challenges/LSVRC/2012/dd31405981
ef5f776aa17412e1f0c112/ILSVRC2012_img_val.tar
tar –xvf ILSVRC2012_img_val.tar -C val
``` 执行以下命令，将 image 文件移入按 label 分类的子目录。
```plaintext
cd val
wget -qO -https://raw.githubusercontent.com/soumith/
imagenetloader.torch/master/valprep.sh | bash
``` 执行以下命令，使用脚本 [prepare_dataset.sh](https://github.com/intel/lpot/blob/master/examples/tensorflow/image_recognition/prepare_dataset.sh) 将原始数据转换为 TFrecord 格式。
```plaintext
cd examples/tensorflow/image_recognition
bash prepare_dataset.sh --output_dir=./data --raw_dir=/PATH/TO/img_raw/val/ 
--subset=validation
``` 更多数据集相关信息，请参见 [Prepare Dataset](https://github.com/intel/lpot/tree/master/examples/tensorflow/image_recognition#2-prepare-dataset)。
    2. 执行以下命令，准备模型。
 ```plaintext
wget https://storage.googleapis.com/intel-optimized-tensorflow/
 models/v1_6/resnet50_fp32_pretrained_model.pb
```
    3. 执行以下命令，运行 Tuning。
修改文件 `examples/tensorflow/image_recognition/resnet50_v1.yaml`，使 `quantization\calibration`、`evaluation\accuracy`、`evaluation\performance` 三部分的数据集路径指向用户本地实际路径，即数据集准备阶段生成的 TFrecord 数据所在位置。详情请参见 [ResNet50 V1.0](https://github.com/intel/lpot/tree/master/examples/tensorflow/image_recognition#1-resnet50-v10)。
```plaintext
cd examples/tensorflow/image_recognition
bash run_tuning.sh --config=resnet50_v1.yaml \
--input_model=/PATH/TO/resnet50_fp32_pretrained_model.pb \
--output_model=./lpot_resnet50_v1.pb
```
    4. 执行以下命令，运行 Benchmark。
```plaintext
bash run_benchmark.sh --input_model=./lpot_resnet50_v1.pb
--config=resnet50_v1.yaml
``` 输出结果如下，其中性能数据仅供参考：
```shell
 accuracy mode benchmarkresult:
 Accuracy is 0.739
 Batch size = 32
 Latency: 1.341 ms
 Throughput: 745.631 images/sec
 performance mode benchmark result:
 Accuracy is 0.000
 Batch size = 32
 Latency: 1.300 ms
 Throughput: 769.302 images/sec
```
:::
::: 示例4：使用\sIntel<sup>®</sup>\sDistribution\sof\sOpenVINO™\sToolkit\s进行推理加速
Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 是一个可以加快计算机视觉及其他深度学习应用部署的工具套件，它能够支持英特尔平台的各种加速器（包括 CPU、GPU、FPGA 以及 Movidius 的 VPU）来进行深度学习，同时能直接支持异构硬件的执行。

Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 能够优化通过 TensorFlow\* 、PyTorch\* 等训练的模型, 它包括模型优化器、推理引擎、Open Model Zoo、训练后优化工具（Post-training Optimization Tool）等一整套部署工具，其中：

- **模型优化器（Model optimizer）**：将 Caffe\*、TensorFlow\* 、PyTorch\* 和 Mxnet\* 等多种框架训练的模型转换为中间表示（IR）。
- **推理引擎（Inference Engine）**：将转换后的 IR 放在 CPU、GPU、FPGA 和 VPU 等硬件上执行，自动调用硬件的加速套件实现推理性能的加速。

您可前往 [Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 官网](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html) 或查阅 [在线文档](https://docs.openvinotoolkit.org/latest/index.html) 了解更多信息。

#### 工作流程
Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 工具套件工作流程示意图如下：
![](https://main.qcloudimg.com/raw/98afcac361352773801fbe863d21b912.png)

#### Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 推理性能
The Intel® Distribution of OpenVINO™ 工具在多种英特尔处理器与加速硬件上提供了优化实现。在英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器平台上，它使用了Intel<sup>®</sup> DL Boost 与 AVX-512 指令集进行推理网络的加速。关于各平台的性能数据，请参见 [Intel<sup>®</sup> OpenVINO™ 工具套件基准性能数据](https://docs.openvinotoolkit.org/latest/openvino_docs_performance_benchmarks_openvino.html)。

 #### 使用 Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 深度学习开发套件（DLDT）
 请参考以下资料：
- [Intel<sup>®</sup> 深度学习部署工具包简介](https://docs.openvinotoolkit.org/downloads/cn/I03030-9-Introduction%20to%20Intel_%20Deep%20Learning%20Deployment%20Toolkit%20-%20OpenVINO_%20Toolkit.pdf)
-  [图像分类 C++ 示例（异步模式）](https://docs.openvinotoolkit.org/downloads/cn/I03030-10-Image%20Classification%20Cpp%20Sample%20Async%20-%20OpenVINO_%20Toolkit.pdf)
-  [对象检测 C++ 示例（SSD）](https://docs.openvinotoolkit.org/downloads/cn/I03030-11-Object%20Detection%20Cpp%20Sample%20SSD%20-%20OpenVINO_%20Toolkit.pdf)
-  [自动语音识别 C++ 示例](https://docs.openvinotoolkit.org/downloads/cn/I03030-12-Automatic%20Speech%20Recognition%20Cpp%20%20Sample%20-%20OpenVINO_%20Toolkit.pdf)
-  [动作识别 Python* 演示](https://docs.openvinotoolkit.org/downloads/cn/I03030-13-Action%20Recognition%20Python%20Demo%20-%20OpenVINO_%20Toolkit.pdf)
-  [十字路口摄像头 C++ 演示](https://docs.openvinotoolkit.org/downloads/cn/I03030-14-Crossroad%20Camera%20Cpp%20%20Demo%20-%20OpenVINO_%20Toolkit.pdf)
- [人姿估算 C++ 演示](https://docs.openvinotoolkit.org/downloads/cn/I03030-15-Human%20Pose%20Estimation%20Cpp%20Demo%20-%20OpenVINO_%20Toolkit.pdf)

#### Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 基准测试
详情请参见 [安装面向 Linux* 的 Intel<sup>®</sup> OpenVINO™ 工具套件分发版](https://docs.openvinotoolkit.org/downloads/cn/I03030-5-Install%20Intel_%20Distribution%20of%20OpenVINO_%20toolkit%20for%20Linux%20-%20OpenVINO_%20Toolkit.pdf)。

:::
</dx-accordion>

