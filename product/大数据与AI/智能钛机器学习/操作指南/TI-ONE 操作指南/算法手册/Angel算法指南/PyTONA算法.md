## [Angel]LR on PyTONA

#### 算法简介
LogisticRegression（LR）算法是一种常见的分类算法，因其模型简单、可解释性强等特点在工程领域得到广泛应用。本算子是 LR 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明

- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的，以空格分隔；libffm 格式的 field 是从0开始的。

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye 为 predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数。
   - batchSize：训练用的 mini batch 大小。
   - actionType：训练或者预测任务 。  
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型。

用户需在自己本地安装 Pytorch（1.3.1版本），然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 lr.py，执行如下命令：

```
python lr.py --input_dim 148
```

其中，input_dim 为输入数据的特征的维度，执行完该命令后会生成用于分布式训练的 lr.pt 模型文件，用户需手动上传到自己的 cos 路径。

- 资源参数
    - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
    - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
    - drive 节点资源类型：请选择合适的 drive 节点机型。
    - executor 节点资源类型：请选择合适的 executor 节点机型。
    - master 节点资源类型：请选择合适的 master 节点机型。
    - ps 节点资源类型：请选择合适的 ps 节点机型。
    - spark conf 参数
      - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
      - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决二分类问题，训练的模型可用于做分类预测

- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练。
![](https://main.qcloudimg.com/raw/f03bee10b0f5667fddc33a28c3f6d72b.png)



## [Angel]FM on PyTONA

#### 算法简介
FactorizationMachine（FM）是一种基于矩阵分解的机器学习算法，它可对任意的实值向量进行预测。其主要优点包括：
（1）可用于高度稀疏数据场景。
（2）具有线性的计算复杂度。本算子是 FM 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明

- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的，以空格分隔；libffm 格式的 field 是从0开始的。

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye 为 predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数。
   - batchSize：训练用的 mini batch 大小。
   - actionType：训练或者预测任务。
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型。

用户需在自己本地安装 pytorch(1.3.1版本)，然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 fm.py，执行如下命令：

```
python fm.py --input_dim 148 --embedding_dim 10
```

其中，input_dim 为输入数据的特征的维度，embedding_dim 为特征 embedding 向量的长度，执行完该命令用户会生成用于分布式训练的 fm.pt 模型文件，用户需手动上传到自己的 COS 路径。

- 资源参数
    - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
    - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
    - drive 节点资源类型：请选择合适的 drive 节点机型。
    - executor 节点资源类型：请选择合适的 executor 节点机型。
    - master 节点资源类型：请选择合适的 master 节点机型。
    - ps 节点资源类型：请选择合适的 ps 节点机型。
    - spark conf 参数
      - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
      - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决二分类的问题，训练的模型可用于做分类预测

- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练。
![](https://main.qcloudimg.com/raw/2a63a74a1f6fa23d60b8cff83db6bcdd.png)

## [Angel]DeepFM on PyTONA

#### 算法简介
DeepFM 算法是在 FM（Factorization machine）的基础上加入深度层构成。 与 PNN，NFM 算法相比，它保留了 FM 的二阶隐式特征交叉的同时，又用深度网络来获取高阶特征交叉。本算子是 DeepFM 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明

- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的, 以空格分隔；libffm 格式的 field 是从0开始的

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye为predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数。
   - batchSize：训练用的 mini batch 大小。
   - actionType：训练或者预测任务。
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型。

用户需在自己本地安装 Pytorch（1.3.1版本），然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 deepfm.py，执行如下命令：

```
python deepfm.py --input_dim 148 --n_fields 13 --embedding_dim 10 --fc_dims 10 5 1
```

其中，input_dim 为输入数据的特征的维度，n_fields 为输入数据 field 的个数，embedding_dim 为特征 embedding 向量的长度，fc_dims为fc-layers 每层的节点数。执行完该命令会生成用于分布式训练的 deepfm.pt 模型文件，用户需手动上传到自己的 COS 路径。

- 资源参数
    - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
    - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
    - drive 节点资源类型：请选择合适的 drive 节点机型。
    - executor 节点资源类型：请选择合适的 executor 节点机型。
    - master 节点资源类型：请选择合适的 master 节点机型。
    - ps 节点资源类型：请选择合适的 ps 节点机型。
    - spark conf 参数
      - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
      - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决的是二分类的问题，训练的模型可用于做分类预测
- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练
![](https://main.qcloudimg.com/raw/459e96a4b4972c173e704853044f3740.png)

## [Angel]DeepAndWide on PyTONA 

#### 算法简介
DeepAndWide 算法是将 Embedding 的结果直接输入 DNN 进一步提取高阶特交叉，最后将一阶特征与高阶特征组合起来进行预测，本算子是 DeepAndWide 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明

- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的，以空格分隔；libffm 格式的 field 是从0开始的。

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye 为 predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数。
   - batchSize：训练用的 mini batch 大小。
   - actionType：训练或者预测任务。
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型。

用户需在自己本地安装 Pytorch（1.3.1版本），然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 deepandwide.py，执行如下命令：

```
python deepandwide.py --input_dim 148 --n_fields 13 --embedding_dim 10 --fc_dims 10 5 1
```

其中，input_dim 为输入数据的特征的维度，n_fields 为输入数据 field 的个数，embedding_dim 为特征 embedding 向量的长度，fc_dims为fc-layers 每层的节点数。执行该命令后会生成用于分布式训练的 deepandwide.pt 模型文件，用户需手动上传到自己的 COS 路径。

- 资源参数
    - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
    - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
    - drive 节点资源类型：请选择合适的 drive 节点机型。
    - executor 节点资源类型：请选择合适的 executor 节点机型。
    - master 节点资源类型：请选择合适的 master 节点机型。
    - ps 节点资源类型：请选择合适的 ps 节点机型。
    - spark conf 参数
      - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
      - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决的是二分类的问题，训练的模型可用于做分类预测

- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练。
![](https://main.qcloudimg.com/raw/459e96a4b4972c173e704853044f3740.png)

## [Angel]DCN on PyTONA 

#### 算法简介
DCN 由两个结构组成，一个是 cross network，一个是很基础的 deep network，而 stack layer 只是简单的拼接了 cross network 和  deep network 的输出结果。本算子是 DCN 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明
- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的，以空格分隔；libffm 格式的 field 是从0开始的。

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye 为 predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数。
   - batchSize：训练用的 mini batch 大小。
   - actionType：训练或者预测任务。
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型。

用户需在自己本地安装 pytorch（1.3.1版本），然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 dcn.py，执行如下命令：

```
python dcn.py --input_dim 148 --n_fields 13 --embedding_dim 10 --cross_depth 3 --fc_dims 10 5 5
```

其中，input_dim 为输入数据的特征的维度，n_fields 为输入数据 field 的个数，embedding_dim 为特征 embedding 向量的长度，cross_depth 为 cross 网络的深度，fc_dims为fc-layers 每层的节点数。执行该命令后会生成用于分布式训练的 dcn.pt 模型文件，用户需手动上传到自己的 COS 路径。

- 资源参数
    - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
    - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
    - drive 节点资源类型：请选择合适的 drive 节点机型。
    - executor 节点资源类型：请选择合适的 executor 节点机型。
    - master 节点资源类型：请选择合适的 master 节点机型。
    - ps 节点资源类型：请选择合适的 ps 节点机型。
    - spark conf 参数
      - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
      - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决的是二分类的问题，训练的模型可用于做分类预测

- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练。
![](https://main.qcloudimg.com/raw/459e96a4b4972c173e704853044f3740.png)



## [Angel]AttentionNet on PyTONA

#### 算法简介

Attention 给模型赋予了区分辨别的能力，例如，在机器翻译、语音识别应用中，为句子中的每个词赋予不同的权重，使神经网络模型的学习变得更加灵活（soft）本算子是 AttentionNet 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明

- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的，以空格分隔；libffm 格式的 field 是从0开始的。

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye 为 predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数。
   - batchSize：训练用的 mini batch 大小。
   - actionType：训练或者预测任务。   
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型。

用户需在自己本地安装pytorch（1.3.1版本），然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 attention_net.py，执行如下命令：

```
python attention_net.py --input_dim 148 --n_fields 13 --embedding_dim 10 --fc_dims 10 5 1
```

其中，input_dim 为输入数据的特征的维度，n_fields为输入数据 field 的个数，embedding_dim 为特征 embedding 向量的长度，fc_dims 为 fc-layers 每层的节点数，执行该命令后会生成用于分布式训练的 attention_net.pt 模型文件，用户需手动上传到自己的 COS 路径。

- 资源参数
    - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
    - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
    - drive 节点资源类型：请选择合适的 drive 节点机型。
    - executor 节点资源类型：请选择合适的 executor 节点机型。
    - master 节点资源类型：请选择合适的 master 节点机型。
    - ps 节点资源类型：请选择合适的 ps 节点机型。
    - spark conf 参数
      - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
      - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决的是二分类的问题，训练的模型可用于做分类预测

- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练。
![](https://main.qcloudimg.com/raw/459e96a4b4972c173e704853044f3740.png)



## [Angel]AttentionFM on PyTONA 

#### 算法简介
AttentionFM（Attentional Factorization Machine），和 NFM 是同一个作者。AFM 是在 FM 上的改进，它最大的特点就是使用一个 attention network 来学习不同组合特征的重要性
本算子是 AttentionFM 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明

- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的，以空格分隔；libffm 格式的 field 是从0开始的。

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye 为 predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数。
   - batchSize：训练用的 mini batch 大小。
   - actionType：训练或者预测任务。 
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型。
      
用户需在自己本地安装 pytorch（1.3.1版本），然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 attention_fm.py，执行如下命令：

```
python attention_fm.py --input_dim 148 --n_fields 13 --embedding_dim 10 --attention_dim 10
```

其中，input_dim 为输入数据的特征的维度，n_fields 为输入数据 field 的个数，embedding_dim 为特征 embedding 向量的长度，attention_dim为attention 的维度，执行该命令用户会生成用于分布式训练的 attention_fm.pt模型文件，用户需手动上传到自己的 COS 路径。

- 资源参数
    - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
    - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
    - drive 节点资源类型：请选择合适的 drive 节点机型。
    - executor 节点资源类型：请选择合适的 executor 节点机型。
    - master 节点资源类型：请选择合适的 master 节点机型。
    - ps 节点资源类型：请选择合适的 ps 节点机型。
    - spark conf 参数
      - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
      - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决的是二分类的问题，训练的模型可用于做分类预测

- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练。
![](https://main.qcloudimg.com/raw/459e96a4b4972c173e704853044f3740.png)



## [Angel]xDeepFM on PyTONA

#### 算法简介

为了实现自动学习显式的高阶特征交互，同时使得交互发生在向量级上，xDeepFM 提出了一种新的名为压缩交互网络（Compressed Interaction Network，简称 CIN）的神经模型。
本算子是 xDeepFM 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明

- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的, 以空格分隔；libffm 格式的 field 是从0开始的。

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye 为 predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数
   - batchSize：训练用的 mini batch 大小
   - actionType：训练或者预测任务   
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型

用户需在自己本地安装 pytorch（1.3.1版本），然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 xdeepfm.py，执行如下命令生成可用于分布式训练的 Pytorch 模型文件：

```
python xdeepfm.py --input_dim 148 --n_fields 13 --embedding_dim 10 --fc_dims 10 5 5 --cin_dims 5 5
```

其中，input_dim 为输入数据的特征的维度，n_fields 为输入数据 field 的个数，embedding_dim 为特征 embedding 向量的长度，fc_dims 为 fc-layers 每层的节点数，cin_dims 为 cin 网络每层的节点数。执行该命令后会生成用于分布式训练的 xdeepfm.pt 模型文件，用户需手动上传到自己的 cos 路径。

- 资源参数
    - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
    - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
    - drive 节点资源类型：请选择合适的 drive 节点机型。
    - executor 节点资源类型：请选择合适的 executor 节点机型。
    - master 节点资源类型：请选择合适的 master 节点机型。
    - ps 节点资源类型：请选择合适的 ps 节点机型。
    - spark conf 参数
      - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
      - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决二分类的问题，训练的模型可用于做分类预测

- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练。
![](https://main.qcloudimg.com/raw/459e96a4b4972c173e704853044f3740.png)



## [Angel]PNN on PyTONA

#### 算法简介
PNN（Product-Based Neural Networks）算法是在 Embedding 的基础上，对 Embedding 的结果进行两两内积或外积，然后将内/外积结果与原始的 Embedding 结果拼接起来输入 DNN 进一步提取高阶特交叉，值得注意的是，PNN 并没有放弃一阶特征，最后将一阶特征与高阶特征组合起来进行预测，本算子是 PNN 算法在 [Pyorch on Angel](https://github.com/Angel-ML/PyTorch-On-Angel) 的实现。

#### 参数说明

- **输入数据格式**
目前支持 libsvm、libffm 两种数据格式，分别如下所示：

```
libsvm格式: label index:value index:value index:value ......
libffm格式: label field:index:value field:index:value field:index:value ......
```

>!index 是从1开始的，以空格分隔；libffm 格式的 field 是从0开始的。

- **节点**
- 算法 IO 参数
   - 数据输入路径：训练数据输入路径。
   - 验证数据输入路径：actionTpye 为 train 时，该参数生效。
   - 模型保存路径：训练完后 angel 模型保存路径，可用于批量预测或增量训练。
   - 模型加载路径：actionTpye 为 train 时，表示增量训练预加载的模型路径，为 predict 是表示预测模型加载路径。
   - 预测结果输出路径：actionTpye 为 predict 时该参数生效，表示预测结果存储路径。
   - PyTorch 模型文件保存路径：训练好的 Pytorch 模型保存路径，可用于在线 serving。

- 算法参数  
   - numEpoch：训练总的迭代轮数。
   - batchSize：训练用的 mini batch 大小。
   - actionType：训练或者预测任务。   
   - PyTorch 模型文件：用户使用 Python 脚本生成的 Pytorch 脚本模型。

用户需在自己本地安装 pytorch（1.3.1版本），然后到 [python/recommendation](https://github.com/Angel-ML/PyTorch-On-Angel/tree/branch-0.2.0/python/recommendation) 下载算法文件 pnn.py，执行如下命令：

```
python pnn.py --input_dim 148 --n_fields 13 --embedding_dim 10 --fc_dims 10 5 1
```

其中，input_dim 为输入数据的特征的维度，n_fields 为输入数据 field 的个数，embedding_dim 为特征 embedding 向量的长度，fc_dims 为 fc-layers 每层的节点数。执行该命令后会生成用于分布式训练的 pnn.pt 模型文件，用户需手动上传到自己的 COS 路径。

- 资源参数
 - num-executors：任务启动的 spark executor 个数，可根据数据量来配置，一般训练数据量越大，需要的 worker 个数越多。
 - spark.ps.instances：Angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 PS 个数越多。
 - drive 节点资源类型：请选择合适的 drive 节点机型。
 - executor 节点资源类型：请选择合适的 executor 节点机型。
 - master 节点资源类型：请选择合适的 master 节点机型。
 - ps 节点资源类型：请选择合适的 ps 节点机型。
 - spark conf 参数
     - spark.angel.tmp.output.path.prefix：angel 临时目录的前缀路径，为 COS 路径。
     - saprk.angel.output.path.deleteonexist：为了防止误删除模型，默认不自动删除模型输出路径的文件。如果需要，可设置为 true。

#### 本算子主要解决的是二分类的问题，训练的模型可用于做分类预测
- 原始数据如下图所示：  
![](https://main.qcloudimg.com/raw/e7c8663c1b20e2de8625c7c58f3a71ad.png)
- 训练完成后会得到分类模型，可用于预测或再训练。
![](https://main.qcloudimg.com/raw/459e96a4b4972c173e704853044f3740.png)
