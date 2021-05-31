## 操作场景
腾讯云第五代次实例 S5、M5、C4、IT5、D3 全面采用第二代智能英特尔<sup>®</sup>至强<sup>®</sup>可扩展处理器 Cascade Lake，搭配 Intel Advanced Vector Extension (AVX-512) 指令集，提供高性能深度学习能力。本文以 S5、M5 实例为例，介绍如何在 CVM 上通过 AVX512 加速人工智能应用。

## 选型推荐[](id:RecommendedSelection)
云服务器的多种实例规格可用于多种应用开发，其中 [标准型 S5](https://cloud.tencent.com/document/product/213/11518#S5) 及 [内存型 M5](https://cloud.tencent.com/document/product/213/11518#M5) 适用于机器学习或深度学习。这些实例配备了第二代 Intel<sup>®</sup> Xeon<sup>®</sup> 处理器，适配 Intel<sup>®</sup> DL boost 学习能力。推荐配置如下表：
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
TensorFlow\* 是用于大规模机器学习及深度学习的热门框架之一。您可参考该示例，提升实例的训练及推理性能。更多框架部署相关信息，请参见 [Intel<sup>®</sup> Optimization for TensorFlow\* Installation Guide](https://software.intel.com/content/www/us/en/develop/articles/intel-optimization-for-tensorflow-installation-guide.html)。本文操作步骤如下：

#### 部署 TensorFlow\* 框架
1. 在云服务器中，安装 Python。本文以 Python 3.6.10 为例。
2. 执行以下命令，安装 Intel<sup>®</sup> 优化的 TensorFlow\* 版本 intel-tensorflow。
```
pip install intel-tensorflow
```
3. 执行以下命令，获取系统的物理核个数。
```
lscpu | grep "Core(s) per socket" | cut -d':' -f2 | xargs
```
4. 选择运行时参数优化方式。通常会使用以下两种运行接口，从而采取不同的优化设置。您可结合实际需求选择，更多参数优化配置说明请参见 [General Best Practices for Intel<sup>®</sup> Optimization for TensorFlow](https://github.com/IntelAI/models/blob/master/docs/general/tensorflow/GeneralBestPractices.md)。
 - **Batch inference**：设置 BatchSize >1，并测量每秒可以处理的输入张量总数。通常情况下，Batch Inference 方式可以通过使用同一个 CPU socket 上的所有物理核心来实现最佳性能。
 - **On-line Inference**（也称为实时推断）：设置 BS = 1，并测量处理单个输入张量（即一批大小为1）所需时间的度量。在实时推理方案中，可以通过多实例并发运行来获取最佳的 throughput。
5. 设置优化参数，可通过以下方式优化运行参数：
 - 设置环境运行参数。在环境变量文件中，添加以下配置：
``` 
export OMP_NUM_THREADS=physicalcores
export KMP_AFFINITY="granularity=fine,verbose,compact,1,0"
export KMP_BLOCKTIME=1
exportKMP_SETTINGS=1
```
 - 在代码中增加环境变化设置。在运行的 Python 代码中，加入以下环境变化配置：
```
import os
os.environ["KMP_BLOCKTIME"] = "1"
os.environ["KMP_SETTINGS"] = "1"
os.environ["KMP_AFFINITY"]= "granularity=fine,verbose,compact,1,0"
if FLAGS.num_intra_threads > 0:
    os.environ["OMP_NUM_THREADS"]= # <physical cores>
config = tf.ConfigProto()
config.intra_op_parallelism_threads = # <physical cores>
config.inter_op_parallelism_threads = 1
tf.Session(config=config)
```

#### 运行 TensorFlow\* 深度学习模型的推理
可参考 [Image Recognition with ResNet50, ResNet101 and InceptionV3](https://github.com/IntelAI/models/blob/master/docs/image_recognition/tensorflow/Tutorial.md) 运行其他机器学习/深度学习模型推理。本文介绍如何运行 ResNet50 的 inference benchmark，并以 benchmark 为例。详情请参见 [ResNet50 (v1.5)](https://github.com/IntelAI/models/blob/master/benchmarks/image_recognition/tensorflow/resnet50v1_5/README.md)。

#### 运行 TensorFlow\* 深度学习模型的训练
本文介绍如何运行 ResNet50 的 training benchmark，详情请参见 [FP32 Training Instructions](https://github.com/IntelAI/models/blob/master/benchmarks/image_recognition/tensorflow/resnet50v1_5/README.md#fp32-training-instructions)。
:::
::: 示例2：部署深度学习框架\sPyTorch*
#### 部署步骤
1. 在云服务器中，安装 Python3.6 或及以上版本。
2. 前往 [PyTorch 官网](https://pytorch.org/)，根据下图所示信息，选择 CPU 版本。
![](https://main.qcloudimg.com/raw/88725a10ecefb38afc760ac282c62ce2.png)
3. 执行以下命令，安装 PyTorch。
```shell
pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f
https://download.pytorch.org/whl/torch_stable.html
```

#### 运行 PyTorch* 深度学习模型的推理及训练优化建议
- 运行 CNN 类型的模型推理，建议使用 `to_mkldnn()` 进行加速。示例代码如下：
```
from torch.utils import mkldnn
...
net = mkldnn.to_mkldnn(net)
...
output = net(data.to_mkldnn())
```
- 推理及训练都可使用 jemalloc 来进行性能优化，详情请参见 [jemalloc](https://github.com/jemalloc/jemalloc/wiki) 及 [示例代码](https://github.com/mingfeima/op_bench-py/blob/master/run.sh)。
- 多 socket 的分布式训练示例，详情请参见 [示例代码](https://github.com/mingfeima/pssp/blob/master/pssp-transformer/dist_train_cpu.sh)。
:::
::: 示例3：使用\sIntel<sup>®</sup>AI\s量化工具加速
#### 支持版本
Intel<sup>®</sup> AI 量化工具支持 Intel<sup>®</sup> 优化的 TensorFlow* v1.15.0、v2.0.0 和 v2.1.0。

#### 量化方式
Intel<sup>®</sup> AI 量化工具旨在提供简单易用的工具，对模型进行量化，加速低精度模型在第二代 Intel<sup>®</sup> Xeon<sup>®</sup> 可扩展处理器平台上的推理性能。提供以下两种优化方式，更多工具介绍请参见 [IntelAI tools](https://github.com/IntelAI/tools/)。
 - [Quantization Python Programming API](https://github.com/IntelAI/tools/blob/master/api/README.md#quantization-python-programming-api-quick-start)：提供 Intel<sup>®</sup> 优化的 TensorFlow* 量化的 Python API。
 - [TensorFlow Quantization](https://github.com/IntelAI/tools/blob/master/tensorflow_quantization/README.md#quantization-tools)：对 post-training 的模型进行量化优化，减少模型大小，并提升推理性能。

主要流程步骤示意图如下：
![](https://main.qcloudimg.com/raw/cd4c741f44710166e41731657ed6bdc8.png)
:::
::: 示例4：使用\sIntel<sup>®</sup>\sDistribution\sof\sOpenVINO™\sToolkit\s进行推理加速
Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 是一个可以加快计算机视觉和深度学习应用开发的工具套件，它能够支持英特尔平台的各种加速器（包括 CPU、GPU、FPGA 以及 Movidius 的 VPU）来进行深度学习，同时能够直接支持异构的执行。

Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 工具套件旨在提高计算机视觉处理及深度学习推理解决方案的性能并缩短开发时间。包括计算机视觉和深度学习开发套件两部分，其中的深度学习部署工具套件 DLDT（Deep Learning Deployment Toolkit）是一个加速深度学习推理性能的跨平台工具，包括：
- 模型优化器（Model optimizer）：将 Caffe、TensorFlow 和 Mxnet 等多种框架训练的模型转换为中间表示（IR）。
- 推理引擎（Inference Engine）：将转换后的 IR 放在 CPU、GPU、FPGA 和 VPU 等硬件上执行，自动调用硬件的加速套件实现推理性能的加速。

您可前往 [Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 官网](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html) 或查阅 [在线文档](https://docs.openvinotoolkit.org/latest/index.html) 了解更多信息。

#### 工作流程
Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 工具套件工作流程示意图如下：
![](https://main.qcloudimg.com/raw/af868e9659e94f48027c51e90b8efec1.png)

#### 部署 Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit
详情请参见 [安装面向 Linux* 的 Intel<sup>®</sup> OpenVINO™ 工具套件分发版](https://docs.openvinotoolkit.org/downloads/cn/I03030-5-Install%20Intel_%20Distribution%20of%20OpenVINO_%20toolkit%20for%20Linux%20-%20OpenVINO_%20Toolkit.pdf)。
 
 #### 使用 Intel<sup>®</sup> Distribution of OpenVINO™ Toolkit 深度学习开发套件（DLDT）
 请参考以下资料：
- [Intel<sup>®</sup> 深度学习部署工具包简介](https://docs.openvinotoolkit.org/downloads/cn/I03030-9-Introduction%20to%20Intel_%20Deep%20Learning%20Deployment%20Toolkit%20-%20OpenVINO_%20Toolkit.pdf)
-  [图像分类 C++ 示例（异步模式）](https://docs.openvinotoolkit.org/downloads/cn/I03030-10-Image%20Classification%20Cpp%20Sample%20Async%20-%20OpenVINO_%20Toolkit.pdf)
-  [对象检测 C++ 示例（SSD）](https://docs.openvinotoolkit.org/downloads/cn/I03030-11-Object%20Detection%20Cpp%20Sample%20SSD%20-%20OpenVINO_%20Toolkit.pdf)
-  [自动语音识别 C++ 示例](https://docs.openvinotoolkit.org/downloads/cn/I03030-12-Automatic%20Speech%20Recognition%20Cpp%20%20Sample%20-%20OpenVINO_%20Toolkit.pdf)
-  [动作识别 Python* 演示](https://docs.openvinotoolkit.org/downloads/cn/I03030-13-Action%20Recognition%20Python%20Demo%20-%20OpenVINO_%20Toolkit.pdf)
-  [十字路口摄像头 C++ 演示](https://docs.openvinotoolkit.org/downloads/cn/I03030-14-Crossroad%20Camera%20Cpp%20%20Demo%20-%20OpenVINO_%20Toolkit.pdf)
-  [人姿估算 C++ 演示](https://docs.openvinotoolkit.org/downloads/cn/I03030-15-Human%20Pose%20Estimation%20Cpp%20Demo%20-%20OpenVINO_%20Toolkit.pdf)
-  [交互人脸检测 C++ 演示](https://docs.openvinotoolkit.org/downloads/cn/I03030-16-Interactive%20Face%20Detection%20Cpp%20%20Demo%20-%20OpenVINO_%20Toolkit.pdf)
:::
:::  示例5：使用\sIntel<sup>®</sup>\sDAAL\s加速机器学习
Intel<sup>®</sup> 数据分析加速库 DAAL（Data Analytics Acceleration Library）面向数据科学家，旨在加快数据分析和预测效率，尤其是海量数据。可充分利用向量化和多线程等优化技术，提升机器学习在 Intel 平台上的整体性能。Intel<sup>®</sup> DAAL 旨在帮助数据科学家和分析师快速建立从数据预处理到数据特征工程、数据建模和部署的一整套端到端软件方案。它提供了建立机器学习和分析所需的各种数据分析及算法所需的高性能构建模块。
 
 #### 安装 Intel<sup>®</sup> Distribution for Python* 及 Intel<sup>®</sup> DAAL
 您可通过以下方式进行安装：
 - 安装 Intel<sup>®</sup> Distribution for Python\*，其中已包含 Intel<sup>®</sup> DAAL。详情请参见 [Intel<sup>®</sup> Distribution for Python*](https://software.intel.com/en-us/distribution-for-python)。
 - 单独安装 Intel<sup>®</sup> DAAL ，详情请参见 [Intel<sup>®</sup> oneAPI Data Analytics Library](https://software.intel.com/en-us/daal)。您还可参考 [Intel<sup>®</sup> oneAPI Data Analytics Library Developer Guide and Reference](https://software.intel.com/en-us/daal-programming-guide)，了解更多信息。

#### 使用 Intel<sup>®</sup> DAAL
使用 Intel<sup>®</sup> DAAL 加速 scikit-learn，有以下两种方式：
 - 方式1：执行以下命令
 ```
 python -m daal4py <your-scikit-learn-script>
 ```
 - 方式2：在代码中加入以下内容
```
import daal4py.sklearn
daal4py.sklearn.patch_sklearn('kmeans')
```
::: 
::: 示例6：AI\s神经网络模型量化
#### 使用 Intel<sup>®</sup> AI Quantization Tools for TensorFlow*
Intel<sup>®</sup> AI Quantization Tools for TensorFlow* 是一个开源 Python 库，提供跨神经网络开发框架的统一的低精度量化 API 入口。旨在提供简单易用和以精度驱动的自动 tuning 工具，对模型进行量化，加速低精度模型在第二代 Intel<sup>®</sup> Xeon<sup>®</sup> 可扩展处理器平台上的推理性能。详情请参见 [intel Ipot](https://github.com/intel/lpot)。

#### 安装 Intel<sup>®</sup> AI Quantization Tools for TensorFlow* 
1. 执行以下命令，使用 anaconda 建立名为 lpot 的 python3.x 虚拟环境。本文以 python 3.7 为例。
```
conda create -n lpot python=3.7
``` ```
conda activate lpot
```
2. 安装 lpot，可通过以下两种方式：
 - 执行以下命令，从二进制文件安装。
 ```
 pip install lpot
 ```
 - 依次执行以下命令，从源码安装。
 ```
git clone https://github.com/intel/lpot.git
``` ```
cd lpot
``` ```
pip install –r requirements.txt
``` ```
python setup.py install
 ```

#### 运行 Intel<sup>®</sup> AI Quantization Tools for TensorFlow* 
本文以 ResNet50 v1.0 为例，介绍如何使用本工具进行量化。
1. 准备数据集。
   1. 依次执行以下命令，下载并解压 ImageNet validation 数据集。
```
mkdir –p img_raw/val && cd img_raw
``` ```shell
wget http://www.image-net.org/challenges/LSVRC/2012/dd31405981
ef5f776aa17412e1f0c112/ILSVRC2012_img_val.tar
``` ```
tar –xvf ILSVRC2012_img_val.tar -C val
```
   2. 依次执行以下命令，将 image 文件移入按 label 分类的子目录。
```
cd val
``` ```shell
wget -qO -https://raw.githubusercontent.com/soumith/
imagenetloader.torch/master/valprep.sh | bash
```
   3. 依次执行以下命令，使用脚本 [prepare_dataset.sh](https://github.com/intel/lpot/blob/master/examples/tensorflow/image_recognition/prepare_dataset.sh) 将原始数据转换为 TFrecord 格式。
```
cd examples/tensorflow/image_recognition
``` ```shell
bash prepare_dataset.sh --output_dir=./data --raw_dir=/PATH/TO/img_raw/val/ 
--subset=validation
``` 更多数据集相关信息，请参见 [Prepare Dataset](https://github.com/intel/lpot/tree/master/examples/tensorflow/image_recognition#2-prepare-dataset)。
2. 执行以下命令，准备模型。
```shell
 wget https://storage.googleapis.com/intel-optimized-tensorflow/
 models/v1_6/resnet50_fp32_pretrained_model.pb
```
3. 依次执行以下命令，运行 Tuning。
修改文件 `examples/tensorflow/image_recognition/resnet50_v1.yaml`，使 `quantization\calibration`、`evaluation\accuracy`、`evaluation\performance` 三部分的数据集路径指向用户本地实际路径，即数据集准备阶段生成的 TFrecord 数据所在位置。详情请参见 [ResNet50 V1.0](https://github.com/intel/lpot/tree/master/examples/tensorflow/image_recognition#1-resnet50-v10)。
```
cd examples/tensorflow/image_recognition
``` ```
bash run_tuning.sh --config=resnet50_v1.yaml \
--input_model=/PATH/TO/resnet50_fp32_pretrained_model.pb \
--output_model=./lpot_resnet50_v1.pb
```
4. 执行以下命令，运行 Benchmark。
```
bash run_benchmark.sh --input_model=./lpot_resnet50_v1.pb --config=resnet50_v1.yaml
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
</dx-accordion>

