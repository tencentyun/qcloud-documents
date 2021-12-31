

TensorFlow 是深度学习领域中应用最广泛的开源框架之一，腾讯云帆团队立足于腾讯丰富的 AI 场景，深度发掘编译优化、混合精度、高维动态稀疏支持等加速能力，基于开源 TensorFlow 版本1.15打造了深度优化的训练框架，致力于满足各个场景的业务需求。

目前 TencentTensorflow（简称 TTensorflow 或 TTF）已接入了腾讯内部众多业务场景，助力业务团队降本增效。为了更好的服务内外部客户，腾讯云决定将内部深度优化的 TTF 免费提供给公有云用户，协助广大用户提高 AI 产品迭代效率。


## 应用场景
TTF 目前支持但是不限于以下场景：
- **推荐系统**，例如 Wide&Deep 及 DeepFM 等。
- **自然语言处理**，例如 BERT 及 Transformer 等。
- **图像识别**，例如 ResNet、MobileNet 及 Inception 系列等。

## 主要优势

- [高维稀疏动态特征支持](#support1) 帮助用户在不需要重新训练的条件下，动态添加和删除特征。同时兼容原生的 TF API，且不存在 Hash 冲突问题。
- [混合精度](#support2) 在原有实现的基础上增加了调整精度的策略，根据 loss 的状态自动在全精度和半精度之间切换，避免精度损失。
- 针对特定业务场景的 [XLA 图优化](#support3) 和算子融合优化。
- NVIDIA 最新一代 [Ampere GPU 和 CUDA 11 支持](#support4)。
您可根据以下内容，了解优势详细分析。




### 高维稀疏动态特征支持[](id:support1)
推荐场景有以下两大特点：
- 用户及物品（内容）随时间快速变化：需要训练的特征参数也随之动态变化，流式数据+在线学习是常用的训练模式。
- 千人千面千亿特征：通常情况下，特征越丰富，模型表达能力越强，业务效果越好。为了保证训练效果，稀疏模型可能达到百GB级别，乃至数十TB量级。

#### 原生 TensorFlow


原生 TensorFlow 是面向处理稠密数据而设计的，其应用拓展到推荐、广告、搜索等高维稀疏数据场景时，一般通过 tf.Variable 的方式实现静态 Embedding 机制。“静态”指用于存储 Embedding 的 Variable 空间大小固定，不能在训练过程中根据用户、物品动态调整，这一机制在实际业务中暴露出很多弊端，例如：
- 不论是用户还是物品数量都非常庞大，往往达到过亿级别，特征维度高达上亿维。处理这种高维数据时，TensorFlow 需要提前将“特征 ID 化”，即强制将其映射到有限的 tf.Variable 空间中，这个过程会造成 Hash 冲突，即不同 ID 可能会取到相同 Embedding，直接影响业务效果。
- 用户与物品的增删非常频繁，导致高维特征的某个维度需要频繁地动态增删，而基于连续存储的 Variable 所实现的静态 Embedding 不能真正释放某一段内存，只能置0，不灵活且浪费内存资源。
- 稀疏模型达到 TB 量级时，为了保证线上推理效率，通常需要对模型进行裁剪、降低大小，但原生 TensorFlow 的连续存储方式无法实现删除特定维度，导致模型过大无法高效存储和加载，实用性受到限制。如下图所示：
<img src="https://main.qcloudimg.com/raw/c3213b7c12ed42155d431544c13873d9.png" width="50%"/>

#### TTF 动态 Embedding 机制
针对原生 TensorFlow 在高维稀疏数据场景的上述不足，腾讯云帆团队融合了内部各业务团队的一线实战经验，基于稀疏域隔离方案推出了动态 Embedding 机制，并针对稀疏场景进行了优化器（SparseAdam）的深度定制。

动态 Embedding 机制基于 HashTable 原理实现，并使 HashTable 在 TensorFlow 中可训练（Trainable），该方案没有 Hash 冲突，效果更好。内存动态伸缩，单机也能调高维模型，并与原生 TensorFlow 所有重要机制兼容，可在特征无 Hash 冲突的训练条件下，以经济的方式使用内存资源，从而实现超大规模特征的离线训练和模型上线。其原理如下图所示：
<img src="https://main.qcloudimg.com/raw/1cd0dd85f41658718e665289f79fa50d.png" width="50%"/>

在模型训练时，优化器通常选择 AdamOptimizer。对于稀疏数据场景，某一个 mini-batch 往往只涉及极其少量的 embedding 参数的更新，但是 AdamOptimizer 作为 momentum-based 的优化器，每次都会全局更新动量和参数，低效且非必需。因此基于 AdamOptimizer 提出了 LazyAdamOptimizer，每次只更新梯度不为0的 embedding 参数。LazyAdamOptimizer 虽然可以解决样本稀疏问题，但是当一个样本更新时，其参数的衰减却是由全局 step 计算的，该方式不合理且会影响模型的收敛精度。

为了解决这个问题，团队设计了 SparseAdamOptimizer。SparseAdamOptimizer 为每个参数记录了上一次更新到本次更新的步数，在做参数衰减更新时由 c 决定，其他步骤与 LazyAdamOptimizer 相同，这种衰减策略更合理。

使用 MLPerf 的 NCF 模型评估 SparseAdamOptimzer，结果如下图所示。可见在稀疏数据场景下，SparseAdam 相比于 Adam、LazyAdam 能提升模型精度。

<img src="https://main.qcloudimg.com/raw/344ac6c4d1a7f4d1377a77f9d0a02817.png" width="80%"/>

### 混合精度[](id:support2)

#### 原生 TensorFlow 训练模型
原生 TensorFlow 自1.14版本以后，已支持混合精度训练，可通过简单的开关进行控制使用。然而，在内部的部分业务实践过程中，仅使用混合精度训练存在着明显的精度损失。虽然可使用混合精度训练中穿插全精度训练的方式来弥补精度，但目前 tensorflow 不支持自动切换，需要用户手动停止训练、切换配置、再重新加载模型，极为不便，也不适合进行线上的长时间训练。

#### 混合进度训练的框架
基于上述问题，腾讯云帆团队设计了一套能进行灵活的混合进度训练的框架，实现无需手动对模型训练进行启停，同时可以实现更好地协调精度和时间的训练策略。
在 Python 部分开放了实现自定义策略接口，并在 C++ 部分对 tensorflow 源码进行了修改，增加了混合精度训练的运行时开关。设计框架主要为下图：
<img src="https://main.qcloudimg.com/raw/c4c59244e165dd1a2cfc456156350d45.png" width="60%"/>

在上述机制的基础上，我们设计了 TTensorflow 策略来进行灵活混合精度训练。该策略在 training 阶段采用混合精度计算的同时，检测学习率是否发生变化，若当前 step 的学习率改变，则在当前 step 后的 hold_step 内切换到全精度训练，hold_step 后在采用混合精度训练。如下图所示：
<img src="https://main.qcloudimg.com/raw/d763515fd557e0b080bfee3c4d076cd9.png" width="30%"/>

下图为使用 TTensorflow 策略在 imagenet 数据集上训练 resnet50 的 loss 曲线，可以明显的观察到在 learning rate 发生变化时进行了精度上的切换（蓝色区间是全精度计算，橙色是混合精度计算。横轴为迭代步，纵轴是 Loss）。如下图所示：
<img src="https://main.qcloudimg.com/raw/a657b9999b72c95de3d40cd773565ecf.png" width="50%"/>

通过灵活混合精度策略，我们成功解决了开启混合精度计算后的模型精度下降的问题。

### XLA 编译优化[](id:support3)

TTF 针对原生 TensorFlow 在模型编译优化上的不足，在 TensorFlow Grappler、XLA 上都结合一线业务场景进行了深度优化，并保持着对 MLIR 等新技术的跟进。具体包含以下几点：

- 在实际业务的复杂模型场景中，针对原生 XLA 在特定业务瓶颈算子上的不足进行了深度优化。例如，多机多卡通信算子、DiagPartOp、DeptwiseConv2D 等。在游戏 AI、视觉智能（人脸识别等）等业务场景的模型训练中取得了不错的效果。如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/0592b7fbacccfcb9c9571e43e47c3b5a.png" width="50%"/>
<img src="https://main.qcloudimg.com/raw/4b4495ddf76440ca0f75a64577d84fdb.png" width="50%"/>
- 针对原生 TensorFlow Grappler 的图优化丰富度不够，难以在实际业务中提升性能的问题，结合 TF-TRT 在云上 GPU 场景扩展了 TensorFlowGrappler 的图优化能力，在电商、直播、视频等云上客户的模型推理场景中取得了50% - 200%的提升。如下图所示：
<img src="https://main.qcloudimg.com/raw/e4831c9873fd68de652fd4a2c8b82aea.png" width="70%"/>
- 在开源 TensorFlow 版本中，开源编译模块没有根据运行时实际的信息划分出适当的编译区域，实际运行中会产生冗余重编译等性能问题。例如，在 TensorFLow 编译优化流程中会强依赖张量形状，额外编译时间占用运行时间，且编译形状变化的张量时会导致重编译。云帆 TTensorflow 提出自适应动态编译框架，在游戏 AI 王者监督模型上已取得超40%的加速比。如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/d28ebaf0c5dd5efd942f4e2c49598ffd.png" width="70%"/>

### Ampere 架构和 CUDA 11支持[](id:support4)

目前 NVIDIA Ampere 系列产品开始逐步上线，包括 A100，A30等，但开源 Tensorflow 1.15并未计划提供 Ampere 产品和 CUDA 11的支持，详情请参见 [TensorFlow GPU](https://www.tensorflow.org/install/source#gpu)。由于仍有很多用户在使用 Tensorflow 1.15的版本，我们对 TTF 加入了 CUDA 11的支持。

## 开始使用
您可参考 [部署及实践](https://cloud.tencent.com/document/product/560/59150) 开始使用 TTF。
>?TTF 本身免费，您只需要为业务执行过程中的相关腾讯云资源付费。
