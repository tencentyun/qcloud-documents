## 操作场景
本文介绍如何部署及使用 TensorFlow。


## 操作步骤

### 准备环境
1. 购买云服务器 CVM 实例或高性能计算集群，详情请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855) 或 [购买高性能计算集群实例](https://cloud.tencent.com/document/product/386/63434)。
<dx-alert infotype="explain" title="">
建议创建实例时，选择**公共镜像**并勾选“后台自动安装GPU驱动”，实例将在系统启动后预装对应版本驱动。若您选择**自定义镜像**，则请手动安装 GPU 驱动。
</dx-alert>
2. 执行以下命令，安装 docker。
```plaintext
curl -s -L http://mirrors.tencent.com/install/GPU/taco/get-docker.sh | sudo bash
```
若您无法通过该命令安装，请尝试多次执行命令，或参考 Docker 官方文档 [Install Docker Engine](https://docs.docker.com/engine/install/) 进行安装。
3. 执行以下命令，安装 nvidia-docker2。
```plaintext
curl -s -L http://mirrors.tencent.com/install/GPU/taco/get-nvidia-docker2.sh | sudo bash
```
若您无法通过该命令安装，请尝试多次执行命令，或参考 NVIDIA 官方文档 [Installation Guide & mdash](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) 进行安装。

### 下载 docker 镜像
执行以下命令，下载 docker 镜像。
```plaintext
docker pull ccr.ccs.tencentyun.com/qcloud/taco-train:ttf115-cu112-cvm-0.4.1
```

### 启动 docker 镜像
执行以下命令，启动 docker 镜像。
```plaintext
docker run -it --rm --gpus all --shm-size=32g --ulimit memlock=-1 --ulimit stack=67108864 --name ttf1.15-gpu ccr.ccs.tencentyun.com/qcloud/taco-train:ttf115-cu112-cvm-0.4.1
```
启动后，您可执行以下命令查看 TTF 版本。
```plaintext
pip show ttensorflow
```


### 模型适配

#### 动态 embedding
TF 原生的静态 Embedding 及 TTF 提供的动态 Embedding 代码如下：
<dx-tabs>
::: TF 原生的静态 embedding

```
deep_dynamic_variables = tf.get_variable(
    name="deep_dynamic_embeddings",
    initializer=tf.compat.v1.random_normal_initializer(0, 0.005),
    shape=[100000000, self.embedding_size])
    
deep_sparse_weights = tf.nn.embedding_lookup(
    params=deep_dynamic_variables,
    ids=ft_sparse_val,
    name="deep_sparse_weights")
    
deep_embedding = tf.gather(deep_sparse_weights, ft_sparse_idx)
deep_embedding = tf.reshape(
    deep_embedding,
    shape=[self.batch_size, self.feature_num * self.embedding_size])
```


:::
::: TTF 提供的动态 embedding

```
deep_dynamic_variables = tf.dynamic_embedding.get_variable(       
    name="deep_dynamic_embeddings",                               
    initializer=tf.compat.v1.random_normal_initializer(0, 0.005), 
    dim=self.embedding_size,                                      
    devices=["/{}:0".format(FLAGS.device)],                       
    init_size=100000000)                                           
deep_sparse_weights = tf.dynamic_embedding.embedding_lookup(      
    params=deep_dynamic_variables,                                
    ids=ft_sparse_val,                                            
    name="deep_sparse_weights")   
       
deep_embedding = tf.gather(deep_sparse_weights, ft_sparse_idx)    
deep_embedding = tf.reshape(
    deep_embedding,
    shape=[self.batch_size, self.feature_num * self.embedding_size])
```

:::
</dx-tabs>

TTF 仅对以下两部分进行替换，使用非常便利：
-  embedding 使用 [`tf.dynamic_embedding.get_variable()`](https://github.com/tensorflow/recommenders-addons/blob/master/docs/api_docs/tfra/dynamic_embedding/get_variable.md)。
- lookup 使用 [`tf.dynamic_embedding.embedding_lookup()`](https://github.com/tensorflow/recommenders-addons/blob/master/docs/api_docs/tfra/dynamic_embedding/embedding_lookup.md)。
详细的 API 使用说明文档请参见 [Module: tfra.dynamic_embedding](https://github.com/tensorflow/recommenders-addons/blob/master/docs/api_docs/tfra/dynamic_embedding.md)。

#### 混合精度

混合精度既可以通过代码对优化器进行重写，也可通过修改环境变量实现。如下所示：
- 代码修改的方式
<dx-codeblock>
:::  shell
opt = tf.train.experimental.enable_mixed_precision_graph_rewrite(opt)
:::
</dx-codeblock>
- 环境变量方式
<dx-codeblock>
:::  shell
export TF_ENABLE_AUTO_MIXED_PRECISION=1
:::
</dx-codeblock>

#### XLA
XLA 既可以通过代码进行配置，也可通过修改环境变量实现。如下所示：
- 代码修改的方式
<dx-codeblock>
:::  shell
config = tf.ConfigProto()
config.graph_options.optimizer_options.global_jit_level = tf.OptimizerOptions.ON_1
sess = tf.Session(config=config)
:::
</dx-codeblock>
- 环境变量的方式
<dx-codeblock>
:::  shell
TF_XLA_FLAGS=--tf_xla_auto_jit=1
:::
</dx-codeblock>


## Demo
在运行 Demo 前：
1. 执行以下命令，在实例中创建一个固定的位置存放数据集。
<dx-codeblock>
:::  shell
cd /ttensorflow/dynamic-embedding-demo
:::
</dx-codeblock>
2. 执行以下命令，下载数据集。
<dx-codeblock>
:::  shell
bash download_dataset.sh 
:::
</dx-codeblock>
您可根据以下 Demo，快速了解并使用 TTF。

### benchmark
该 Demo 用于对比测试动态 embedding 和原生静态 embedding 的性能。可依次执行以下命令，运行 Demo：
<dx-codeblock>
:::  shell
cd benchmark
// 按照默认配置运行
python train.py

// 每次修改batch size，需要将本地数据集缓存文件删掉
rm -f .index .data-00000-of-00001
python train.py --batch_size=16384

// 分别使用静态embedding和动态embedding进行DeepFM模型训练
python train.py --batch_size=16384 --is_dynamic=False
python train.py --batch_size=16384 --is_dynamic=True

// 调整Deep部分的fc层数
python train.py --batch_size=16384 --dnn_layer_num=12
:::
</dx-codeblock>

### ps
该 Demo 展示如何在 ps 模式下使用动态 embedding。可执行以下命令，运行 Demo：
<dx-codeblock>
:::  shell
cd ps && bash start.sh
:::
</dx-codeblock>

### Estimator
该 Demo 展示如何在 Estimator 模式下使用动态 embedding。可执行以下命令，运行 Demo：
<dx-codeblock>
:::  shell
cd estimator && bash start.sh
:::
</dx-codeblock>




