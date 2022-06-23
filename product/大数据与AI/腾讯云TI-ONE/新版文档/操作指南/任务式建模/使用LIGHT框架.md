## (必须)Light 初始化
在使用 Light 镜像，或者安装 Light 软件包后，只需添加3行代码即可初始化 Light 加速能力。	

| 修改点           | 修改内容                                                     |
| ---------------- | ------------------------------------------------------------ |
| 导入light包      | 在模块引入部分加入`from light import light, light_init`      |
| 填写加速信息字段 | 在字典中填写训练框架、是否启用加速及训练场景等信息     </br>params = {     "training_framework": "pytorch_ddp", # 【必填】     </br>"enable_optimizations": True, # 【选填】</br>默认值：True     "application_scenario": "Torch-NLP" # 【选填】</br>默认值："default"     }    </br> 参数：      "training_framework"：训练框架类型，可选填"tensorflow"、"tensorflow_keras"、"pytorch"、"pytorch_ddp"    </br> "enable_optimizations"：是否启用加速，可选填True、False;     </br>"application_scenario"：应用细分领域，可选填"TF-CV"、"TF-NLP"、"Torch-CV"、"Torch-NLP"、"TF-GAN"、"Torch-GAN"、"default";|
| 主函数加装饰器   | 在主函数或训练运行函数加上装饰器`@light_init(params=params)` |

下面通过例子展示将程序修改为 light 加速任务的具体方法：



```
import ...

## 修改点1：导入light包
from light import light, light_init

# 模型定义
class Net(nn.Module):
    ...

# 模型训练
def train(args, model, train_loader, optimizer, epoch):
    ...

## 修改点2：主函数加装饰器
@light_init(params={"training_framework": "pytorch_ddp", "application_scenario": "Torch-NLP"})
def main():
     ...

if __name__ == "__main__":
    main()
```

## （可选）使用 Light IO 加速能力

IO 操作是深度学习程序中很关键的一个步骤，在数据量比较大的情况下如果没有做好 IO 和计算的 overlap 会严重影响程序性能。如果您觉得您的程序花费太多时间在数据拷贝或者数据预处理阶段，不妨试试 Light IO 的加速能力。
Light目前支持 Tensorflow 和 Pytorch 框架下，使用 Light 数据 IO 能力加速训练，具体如下：

| Light  IO加速能力 | 数据预取                                              | 数据分片                                         | 数据缓存                         |
| ----------------- | ----------------------------------------------------- | ------------------------------------------------ | -------------------------------- |
| Tensorflow        | [2.2.2.1.1 light.io.get_iterator](http://light.io/)   | [2.2.2.2 light.io.files_shard](http://light.io/) | \                                |
| Pytorch           | [2.2.2.1.2 light.io.get_dataloader](http://light.io/) | \                                                | 2.2.2.3  缓存原文件/缓存解码数据 |

### Light 数据预取（支持 Tensorflow、Pytorch 框架）

目前 Light 支持在 Tensorflow、Pytorch 框架下数据预取的 IO 加速，可以在训练过程中预取数据到指定的 GPU 设备。
在 Tensorflow 框架下，Light 实现了优化版本的 tf.data.Dataset 迭代器；
在 Pytorch 框架下，Light 实现了优化版本的 torch.utils.data.Dataloader，具体API如下：

#### light.io.get_iterator（支持 Tensorflow 框架）

- API：
```
  light.io.get_iterator(
  dataset, prefetch_to_gpu=True
  )	
```
- 功能：优化版本的tf.data.Dataset，为dataset初始化创建迭代器，若prefetch_to_gpu为True，先将数据dataset预取到GPU	

- 参数：	

| 参数            | 说明                                                         |
  | --------------- | ------------------------------------------------------------ |
  | dataset         | tf.data.Dataset：该接口操作的数据集对象                      |
  | prefetch_to_gpu | bool：默认值True；取值True：将数据集dataset，预取到给定GPU设备（默认GPU 0号卡）；取值False：为数据集dataset初始化创建一个迭代器（类型为tf.data.Iterator） |

- 返回值:  dataset迭代器	

####  light.io.get_data_loader（支持Pytorch框架）

- API：
 ```
	light.io.get_data_loader(
  dataset, num_replicas, rank, batch_size=1, shuffle=False,
  sampler=None, batch_sampler=None, num_workers=0,`
  collate_fn=None, pin_memory=True, drop_last=False, timeout=0,
  worker_init_fn=None, multiprocessing_context=None, generator=None
  )
```	
  
- 功能：

  优化版本的torch.utils.data.Dataloader，类似Pytorch原生的Dataloader，但是会自动进行从cpu至gpu的预取操作，从而使cpu至gpu的数据拷贝可以与计算部分并行	

- 参数：

  相较原生Pytorch Dataloader，light.io.get_data_loader新增2个参数，分别是：1）num_replicas：Light分布式训练的进程总数，建议设置为light.cc.size( )；2）rank：Light分布式训练中本进程的编号，建议设置为light.cc.rank( )	


| 参数                    | 说明                                                         |
| ----------------------- | ------------------------------------------------------------ |
| dataset                 | Dataset：需要加载的数据集                                    |
| num_replicas            | [int：分布式训练的进程总数，建议设置为light.cc.size( )](http://light.cc/) |
| rank                    | [int：分布式训练中的本进程的编号，建议设置为light.cc.rank( )](http://light.cc/) |
| batch_size              | int：批处理大小                                              |
| shuffle                 | bool：是否随机打乱数据，默认为False                          |
| sampler                 | Sampler：抽取样本用的采样器，默认使用DistributedSampler进行默认分布式采样 |
| batch_sampler           | Sampler：类似于sampler，只是每次采样一个batch，默认为空      |
| collate_fn              | callable：用于将样本融合为batch                              |
| pin_memory              | bool：是否使用锁页内存分配数据                               |
| drop_last               | bool：在划分batch时，是否丢掉最后一个大小不足的batch         |
| timeout                 | int：如果为正，则会在提取超时时返回，必须为非负整数          |
| worker_init_fn          | callable：初始化底层加载进程的额外函数                       |
| multiprocessing_context | string：调节分配新加载进程的机制                             |

- 返回值：
  在2.2.1 Light初始化中，如果enable_optimization为True，返回LightDataLoader类型对象，其为Light针对IO进行自动优化后的Dataloader，为False时，返回Pytorch原生的Dataloader	

#### Light 数据分片（支持 Tensorflow 框架）
  目前Light支持Tensorflow框架下数据分片的方法。
- API：
 ```
	light.io.files_shard(
  `data_files_list, size, rank, drop_last=False`
  )
```	
  
- 功能：

  为当前Light进程（进程id为rank），分配1/size的数据文件列表；若总数据文件数小于总进程数，则不进行分配，直接返回总数据文件列表	

- 参数：	

| 参数            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| data_files_list | list：数据文件列表                                           |
| size            | int：当前分布式程序的Light进程数量                           |
| rank            | int：当前进程id                                              |
| drop_last       | bool： 默认值False。数据文件如果不能平均分配到每个进程，则该参数用来控制多余的部分是否需要丢弃 |

- 返回值:  

  list：当前进程分配到的数据文件列表	

#### Light数据缓存（支持Pytorch框架）

目前Light支持Pytorch框架下，将远端ceph训练数据原文件缓存至本地的能力，使训练数据供给更快，消除因高频访问ceph带来的性能毛刺，有2种使用方式，分别是缓存原文件和缓存解码后数据。

- 缓存原文件

| 修改点                                                       | 修改内容                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| __init__添加数据集列表                                       | 在自定义CustomDataset类的初始化过程中，传入并声明`self.files_path_list`变量 |
| 注意：`self.files_path_list`变量名不可修改，如果没有此变量，则没有使用缓存功能 |                                                              |
| __getitem__读取缓存                                          | [在自定义CustomDataset类__getitem__类方法中，使用`light.io.get_file( )`从缓存中读取文件](http://light.io/) |
| 添加数据集列表参数                                           | 在调用CustomDataset类时，添加`files_path_list`参数           |
| 替换dataloader                                               | [使用`light.io.get_data_loader(   )`替换`torch.utils.data.Dataloader( )`](http://light.io/) |

   下面通过一个伪代码例子展示具体的使用方法：

```

  class CustomDataset(torch.utils.data.Dataset):

    ## 修改点1：传入files_path_list参数，并声明类变量self.files_path_list

    def __init__(self, transform, files_path_list...):
        self.transform = transform
        self.files_path_list = files_path_list
         
    def __getitem__(self, index):
        ## 修改点2：使用light.io.get_file()从缓存中读取文件
        sample_path = light.io.get_file(get_sample_path(index))  # 原代码：sample_path = get_sample_path(index)
        sample = get_sample(sample_path)
        sample = self.transform(sample)
        return sample

## 修改点3：创建CustomDataset实例时，添加files_path_list参数
dataset = CustomDataset(transform, files_path_list, ...)
## 修改点4：用light.io.get_data_loader替换torch.utils.data.Dataloader
dataset = light.io.get_data_loader(dataset, batchsize, num_replicas=light.cc.size(), rank=light.cc.rank())  # 原代码：dataloader = torch.utils.data.DataLoader(dataset, batch_size)

```

- 缓存解码数据

目前Light支持Pytorch框架下，将解码后的数据缓存至内存、硬盘的能力，相较于缓存原文件的方式，缓存解码后的数据有3个优点：

1）可以缓存单个样本，不受限于原文件大小；

2）缓存支持多级存储，更加灵活，鲁棒性更高；

3）某些场景下可以减少数据预处理的耗时。

缓存解码后数据的使用方法有2种，分别针对 torch.utils.data.Dataset 和 torchvision.datasets.folder.DatasetFolder 的使用场景，具体使用方法如下：

**A.基于 torch.utils.data.Dataset 使用缓存解码数据能力**

| 修改点                                  | 修改内容                                                     |
| --------------------------------------- | ------------------------------------------------------------ |
| 继承LightDataset                        | 将自定义CustomDataset的父类，由`torch.utils.data.Dataset`替换为`LightDataset` |
| 调用LightDataset                        | 调用父类的__init__函数`super(CustomDataset,  self).__init__(self, cache_type='auto', transforms=None)`；     need_cache：是否需要cache，默认为 True；     cache_type：cache的类型，可支持'memory'，'disk',  'auto'三种，默认为内存缓存；     cache_dir：cache类型使用'disk'和'auto'类型时的缓存文件位置，若不设置，则默认为使用 '/dockerdata/cachedata'     cache_size：cache类型使用'disk'和'auto'类型时的缓存的大小，若不设置，则默认为 20G     transforms：缓存后执行的transform函数，可支持不同的格式 |
| （可选）由LightDataset执行transform函数 | 数据预处理transform可由LightDataset执行，也可放在自定义CustomDataset类中执行 |

下面通过2个伪代码例子展示具体的使用方法。
缓存原始数据例子：将 transform 传到父类 LightDataset 中，先缓存再处理数据：

```

## 修改点1：替换父类torch.utils.data.Dataset为LightDataset

class CustomDataset(LightDataset):  # 原代码：class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, filename, transform):
        ## 修改点2：调用父类LightDataset的方法，由父类进行transform
        super(CustomDataset, self).__init__(cache_type='auto', transforms=transform)

    def __getitem__(self, index):
        ## 修改点3：去掉原有的transform函数
        sample = get_sample(index)
        return sample
     
dataset = CustomDataset(filename, transform)
dataloader = Dataloader(dataset, batch_size)

```
缓存经过预处理的数据例子：
```
## 修改点1：替换父类torch.utils.data.Dataset为LightDataset
class CustomDataset(LightDataset):
    def __init__(self, filename, transform):
        self.transform = transform
        ## 修改点2：调用父类LightDataset的方法，不需要传transform
        super(CustomDataset, self).__init__(cache_type='auto')

    def __getitem__(self, index):
        sample = get_sample(index)
        sample = self.transform(sample)
        return sample

dataset = CustomDataset(filename, transform)
dataloader = Dataloader(dataset, batch_size)

```
B. 如果您的代码使用了torchvision的 ImageFolder 来进行数据读取，可以通过如下方式来使用light cache
```
# 导入light ImageFolder
from light.pytorch.datasets.folder import ImageFolder

# 修改前
dataset = torchvision.datasets.ImageFolder(
    traindir,
    transform=transform
)

# 修改后，这里使用light的ImageFolder
dataset = ImageFolder(
    traindir,
    transform=transform,   
    # cache_transform为True时，缓存transform之后的数据，为False时，缓存Transform之后的数据，默认为False。
    cache_transform=True
```

## （可选）使用 Light 计算加速能力

Light 目前支持 Tensorflow 和 Pytorch 框架下，使用 Light 计算能力加速训练，具体如下：

| Light IO 加速能力 | 数据预取                                              | 数据分片                                         | 数据缓存                        |
| ----------------- | ----------------------------------------------------- | ------------------------------------------------ | ------------------------------- |
| Tensorflow        | [2.2.2.1.1 light.io.get_iterator](http://light.io/)   | [2.2.2.2 light.io.files_shard](http://light.io/) | \                               |
| Pytorch           | [2.2.2.1.2 light.io.get_dataloader](http://light.io/) | \                                                | 2.2.2.3 缓存原文件/缓存解码数据 |

###  Light 混合精度（支持 Tensorflow、Pytorch 框架）

目前 Light 目前支持 Tensorflow、Pytorch 框架下，使用混合精度、XLA 优化和Cudnn AutoTune 加速计算的能力，可以在不影响模型精度的情况下，提升训练速度。
在 Tensorflow 框架下，Light 实现了优化版本的 tf.train.experimental.enable_mixed_precision_graph_rewrite；
在 Pytorch 框架下，Light 实现了优化版本的 NVIDIA Apex amp 和 Pytorch amp（注意，如果要让混合精度训练产生效果，需要硬件中有Tensor Cores支持。如果要使用 Apex，需要在 Light 镜像中增量安装 Apex，安装方法请参考 NVIDIA apex QuickStart，注意本地物理机的 GPU 卡型号，必须和用来训练任务的容器所使用的GPU卡型号相同，否则会报错），具体如下：

#### light.calc.get_mixed_precision_optimizer（支持 Tensorflow 框架）
- API：
  ```
	light.calc.get_mixed_precision_optimizer(
       opt
  )
```
- 功能：
优化版本的tf.train.experimental.enable_mixed_precision_graph_rewrite，将优化器扩展成混合精度	
- 参数:	

| 参数 | 说明   |
| ---- | ------ |
| opt  | 优化器 |

- 返回值: 
  具有混合精度的优化器	

#### 单机场景使用Apex（支持Pytorch框架）
```
from apex import amp

...
model = ...
...
optimizer = ...
...
model, optimizer = amp.initialize(model, optimizer, opt_level='O1')  # 注意这里是"O1"，而不是"01"
...
optimizer.zero_grad()
output = model(...)
loss = ...
...
with amp.scale_loss(loss, optimizer) as scaled_loss:
    scaled_loss.backward()  # 梯度自动缩放
optimizer.step() # 优化器更新梯度
...
```
####  Light 分布式场景使用 Apex（支持 Pytorch 框架）

注意：1）Apex 的初始化需要在 light.cc.get_distributed_optimizer( )之后；2）在每次 optimizer.step( )之前，需要先运行 optimizer.synchronize( )，然后在optimizer.step( )前面套一个 skip_synchronize( )。

```
from light import light, light_init
from apex import amp

...
model = ...
...
optimizer = ...
...
optimizer = light.cc.get_distributed_optimizer(optimizer)
model, optimizer = amp.initialize(model, optimizer, opt_level='O1')  # 注意这里是"O1"，而不是"01"
...
# train one step
optimizer.zero_grad()
output = model(...)
loss = ...
...
with amp.scale_loss(loss, optimizer)  as scaled_loss:
    scaled_loss.backward()  # 梯度自动缩放
    optimizer.synchronize()  # 优化器梯度同步
with optimizer.skip_synchronize():
    optimizer.step()  # 优化器更新梯度
```
详细例子可参考源码实例 Pytorch-Resnet50-Apex-demo 。

#### 单机场景使用 amp（支持 Pytorch 框架）

```
from torch.cuda.amp import autocast, GradScaler

...
model = ... # create model, default dtype: torch.FloatTensor
optimizer = ...
...
scaler = GradScaler() # Instantiate an GradScaler object
...
for epoch in epochs:
    for input, target in data:
        optimizer.zero_grad()
        # forward: model & loss turn on autocast
        with autocast():
            output = model(input)
            loss = ...
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
...
```
#### Light 分布式场景使用 amp（支持 Pytorch 框架）

注意：1）在每次 scaler.step(optimizer) 之前，需要先运行 optimizer.synchronize( )，然后在 scaler.step(optimizer) 和 scaler.update( ) 前面套一个skip_synchronize( ) 。

```
from light import light, light_init
from torch.cuda.amp import autocast, GradScaler

...
model = ... # create model, default dtype: torch.FloatTensor
optimizer = ...
optimizer = light.cc.get_distributed_optimizer(optimizer)
...
scaler = GradScaler() # Instantiate an GradScaler object
...
for epoch in epochs:
    for input, target in data:
        optimizer.zero_grad()
        #forward: model & loss turn on autocast
        with autocast():
            output = model(input)
            loss = ...
        scaler.scale(loss).backward()
        optimizer.synchronize()
        with optimizer.skip_synchronize():
            scaler.step(optimizer)
            scaler.update()
...

```
详细例子可参考 Pytorch-Resnet50-amp-demo 。

### Light XLA 优化（支持 Tensorflow 框架）

- API：
```
light.calc.set_xla_optimization(
      level=2
)
```
- 功能：
为 tensorflow 模型启用 xla 优化	
- 参数：	

| 参数  | 说明            |
| ----- | --------------- |
| level | int：默认值为 2 |

- 返回值: 
  无	

###  Light Cudnn 优化（支持 Pytorch 框架）

- API：
```
light.calc.set_cudnn_autotune( )
```
- 功能：
该接口会在前几个迭代步尝试变换卷积、矩阵乘法等运算的cudnn算法，从而在后续训练中得到速度最快的选择。
注意，该功能可能会使前几个迭代步的训练速度降低。	
- 参数: 无	
- 返回值: 无 	
###  Fused Optimizer 优化（支持 Pytorch 框架）
Fused Optimizer 的本质是 kernel fusion，通过聚合参数存储空间来减少 optimizer.step() 过程中的 kernel launch次数。Light Fused Optimizer 支持 pytorch 所有官方的 optimizer 。
Fused Optimizer 的效果与使用的 Optimizer 有关，更新逻辑越复杂， 加速效果越明显。

```
from light.pytorch.trainer_calc import FusedOptimizer

# 使用 FusedOptimizer 封装pytorch的optimizer即可
optimizer = FusedOptimizer(optimizer)
# 注意，FusedOptimizer的参数初始化需要在model.to() / model.cuda()调用之后执行，因为to操作会出发参数重新分配。

# 我们在FusedOptimizer中封装了torch原生optimizer中的如下方法，可以直接调用：
optimizer.zero_grad()
optimizer.step()
optimizer.state_dict()
optimizer.load_state_dict()

# 如果您要查看参数或者梯度的具体值，则可以调用FusedOptimizer的origin_optimizer成员。
optimizer.origin_optimizer.param_groups[0]['params']
```
## （可选）使用 Light 通信加速能力

目前 Light 支持 LightCC (Horovod) 优化版本，支持多机多卡分层通信、梯度压缩等功能）和 Pytorch-DDP（易用性优化，支持在 chief 节点直接启动多机多卡任务）的通信加速能力，具体如下：

| Light 通信加速能力 | LightCC                                                      | Pytorch-DDP           |
| ----------------- | ------------------------------------------------------------ | --------------------- |
| Tensorflow        | 2.2.4.1.1~2.2.4.1.22  size、rank、分布式优化器、allgather、allreduce、broadcast等 | \                     |
| Pytorch           | 2.2.4.1.1~2.2.4.6  size、rank、梯度规约、梯度压缩等；     2.2.4.1.22~2.2.4.1.25 broadcast_variable、allgather、allreduce等 | 2.2.4.2 DDP易用性优化 |


### 2.2.4.1 Light 分布式场景使用 LightCC 通信模式（支持 Tensorflow、Pytorch 框架）

LightCC 是 Horovod 的优化版本，已经默认安装于 Light 标准镜像中，如果训练代码中调用 Horovod 接口，会自动替换为 LightCC ，无需修改代码即可享受通信加速的能力。
如果需要使用 LightCC 所提供的的梯度规约、分层通信及多流通信等通信加速能力，请参考下面提供 Tensorflow 及 Pytorch 框架下的 LightCC API。

####  light.cc.size（支持 Tensorflow、Pytorch 框架）

- API：
```
  light.cc.size()
```

- 功能：
  获取分布式训练程序中Light进程数量

- 参数: 无

- 返回值: 
  int：Light进程数量

####  light.cc.local_size（支持 Tensorflow、Pytorch 框架）

- API：
```
  light.cc.local_size()
```
- 功能：
  获取一个机器节点上的Light进程数量，调用该函数的进程运行在此机器节点上
- 参数: 无
- 返回值: 
  int：Light进程数量

####  light.cc.rank（支持 Tensorflow、Pytorch 框架）

- API：
```
  light.cc.rank()
```
- 功能：
  获取当前Light进程在分布式训练中的rank
- 参数: 无
- 返回值: 
  int：Light进程rank值

####  light.cc.local_rank（支持Tensorflow、Pytorch框架）
- API：
  `light.cc.local_rank()`
- 功能：
  获取一个机器节点上当前Light进程的本地编号rank
- 参数: 无
- 返回值: 
  int：Light进程rank值

#### light.cc.Compression（支持 Tensorflow、Pytorch 框架）
- API：
```
  light.cc.Compression
```
- 功能：
  梯度压缩算法：none 或者 fp16
  用法：light.cc.Compression.none / light.cc.Compression.fp16

#### light.cc.reduction_op_values（支持 Tensorflow、Pytorch 框架）
- API：
```
 light.cc.Average / light.cc.Sum / light.cc.Adasum
```
- 功能：
  梯度规约op

####  light.cc.get_distributed_optimizer（支持 Tensorflow 框架）
- API：
  ```
	light.cc.get_distributed_optimizer(
        optimizer, name=None, use_locking=False, device_dense='',
        device_sparse='', compression=light.cc.Compression.none,
        sparse_as_dense=False, backward_passes_per_step=1,
        op=light.cc.Average, allreduce_type='fusion',
        fusion_type='auto_fusion', auto_fusion_threshold=67108864,
        piecewise_fusion_schedule='0', scopewise_fusion_schedule=''
  )
```	
- 功能：
  将 Tensorflow 单进程优化器 optimizer 扩展成分布式优化器，并自动加入了梯度规约的功能。并支持了不同的通信方式。	
- 参数:	

| 参数                      | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| optimizer                 | Optimizer: 准备进行分布式处理的单机 optimizer                |
| name                      | string:应用梯度时创建op操作的可选名称前缀，默认值为None      |
| use_locking               | bool:更新变量时是否使用locking，默认值为False                |
| device_dense              | string:用于dense  tensor的设备。如果使用HOROVOD_GPU_OPERATIONS构建，则默认使用GPU |
| device_sparse             | string:用于sparse  tensor的设备。如果使用HOROVOD_GPU_OPERATIONS构建，则默认使用GPU |
| compression               | 压缩算法类型：默认不使用。使用allreduce的时候压缩算法可以减少每个参数更新step中发送的数据量。可选值： |
|                           | [light.cc.Compression.none：不进行梯度压缩](http://light.cc/) |
|                           | [light.cc.Compression.fp16：将所有32bit浮点数梯度压缩为16bit](http://light.cc/) |
| sparse_as_dense           | bool:默认值为False。将所有的sparse tensor视为dense  tensor.如果原始的稀疏梯度具有较高的密度，则可以有效的帮助提高性能和内存利用率。 |
| backward_passes_per_step  | [int:默认值为1。使用light.cc.allreduce之前要执行反向传播的次数。这允许在reduce计算和更新梯度之前累计多个mini-batches的梯度。](http://light.cc/) |
| op                        | [默认值为light.cc.Average.当组合不同Light进程的梯度时，使用的规约操作.](http://light.cc/) |
|                           | 可选值：light.cc.Adasum / light.cc.Sum / light.cc.Average    |
| allreduce_type            | 支持"normal"和"fusion"两种方式，默认为"fusion"，表示调用ltfusion_allreduce，"normal"表示调用ltallreduce |
| fusion_type               | 默认为使用"auto_fusion"，可选：                              |
|                           | "piecewise_fusion"/"scopewise_fusion"、"xlascope_fusion"和"auto_fusion"四种模式，默认为"auto_fusion"。 |
|                           | 使用"piecewise_fusion"模式会根据用户设置的piecewise_fusion_schedule参数进行分层融合； |
|                           | 使用"scopewise_fusion"模式会根据用户设置的scopewise_fusion_schedule参数进行分层融合； |
|                           | 使用"xlascope_fusion"模式会根据模型中设置的jit_scope自动识别同一scope下的梯度进行融合； |
|                           | 使用"auto_fusion"模式会根据用户设置的auto_fusion_threshold参数进行分层融合。 |
| auto_fusion_threshold     | 使用"auto_fusion"时的合并阈值，单位为字节，默认为67108864，表示合并之后的层大小不超过67108864字节 |
| piecewise_fusion_schedule | 使用"piecewise_fusion"时的融合边界，以";"分隔，每个数字表示融合的分界线，例如"2;6"代表融合成3段，前2层(0,1)进行融合，接着4层(2-5)进行融合通信，最后6层及以后进行融合通信。默认为"0"，即将所有的梯度融合为1段进行通信 |
| scopewise_fusion_schedule | 使用"scopewise_fusion"时的融合边界，以";"分隔，每个字符串表示该variable_scope下的参数融合到一起，余下未被任何scope匹配的参数会另外融合为1段。默认为""，即将所有的梯度融合为1段进行通信 |

- 返回值: 
  加上了梯度规约的分布式优化器	

#### light.cc.get_distributed_gradient_tape（支持 Tensorflow 框架）
- API：
```
  light.cc.get_distributed_gradient_tape(
        gradtape, device_dense='', device_sparse='',
        compression=light.cc.Compression.none, sparse_as_dense=False,
        op=light.cc.Average
  )	
```

- 功能：
  将 gradtape 扩展具有分布式能力	
- 参数:	
  
- 返回值: 
  具有分布式能力的 gradtape	
####  light.cc.allreduce（支持 Tensorflow 框架）
- API：
 ```
	light.cc.allreduce(
        tensor, average=None, device_dense='', device_sparse='',
        compression=light.cc.Compression.none, op=None`
  )
```	
- 功能：
  对指定 Tensor 进行 allreduce 操作：
  对输入张量执行 ring-allreduce 的带宽规约操作。如果输入的 tensor 类型为tf.IndexedSlices，该函数将对值和索引执行 allgather 操作，从而对其表示的张量有效的执行 allreduce 规约操作。	
- 参数:	

| 参数          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| tensor        | tf.Tensor / tf.Variable /  tf.IndexedSlices可用于规约的类型,该张量的shape在Light的每个进程中必须保持相同 |
| average       | deprecatred,请使用op                                         |
| device_dense  | string:用于dense  tensor的设备。如果使用HOROVOD_GPU_OPERATIONS构建，则默认使用GPU |
| device_sparse | string:用于sparse  tensor的设备。如果使用HOROVOD_GPU_OPERATIONS构建，则默认使用GPU |
| compression   | 压缩算法类型：默认不使用。使用allreduce的时候压缩算法可以减少每个参数更新step中发送的数据量。可选值： |
|               | [light.cc.Compression.none：不进行梯度压缩](http://light.cc/) |
|               | light.cc.Compression.fp16：将所有32bit浮点数梯度压缩为16bit  |
| op            | [默认值为light.cc.Average.当组合不同Light进程的梯度时，使用的规约操作.](http://light.cc/) |
|               | 可选值：light.cc.Adasum / light.cc.Sum / light.cc.Average    |

- 返回值: 
  allreduce 操作后的 tensor	

#### light.cc.fusion_allreduce（支持 Tensorflow 框架）
- API：
 ```
	light.cc.fusion_allreduce(
        grads_and_vars, average=None, device_dense='', device_sparse='',
        compression=light.cc.Compression.none, op=None,`
        fusion_type="auto_fusion", auto_fusion_threshold=67108864,
        piecewise_fusion_schedule="0",`
        scopewise_fusion_schedule="scope0;scope1"
  )
```	
- 功能：
  对需要通信的梯度进行融合通信，可支持"piecewise_fusion"、"scopewise_fusion"、"xlascope_fusion"和"auto_fusion"四种模式;
  如果，不进行梯度融合通信，则对列表中的每个梯度进行allreduce规约操作。	
- 参数:	

| 参数                      | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| grads_and_vars            | 模型中 (gradient,  variable) 对的列表。为保证能处理特殊梯度（例如无Shape属性），必须传入一一对应的的梯度参数对 |
| average                   | deprecatred,请使用 op                                         |
| device_dense              | string:用于 dense  tensor 的设备。如果使用HOROVOD_GPU_OPERATIONS构建，则默认使用GPU |
| device_sparse             | string:用于 sparse  tensor 的设备。如果使用HOROVOD_GPU_OPERATIONS构建，则默认使用GPU |
| compression               | 压缩算法类型：默认不使用。使用 allreduce 的时候压缩算法可以减少每个参数更新 step 中发送的数据量。可选值： |
|                           | [light.cc.Compression.none：不进行梯度压缩](http://light.cc/) |
|                           | [light.cc.Compression.fp16：将所有32bit浮点数梯度压缩为16bit](http://light.cc/) |
| op                        | [默认值为light.cc.Average.当组合不同Light进程的梯度时，使用的规约操作. 可选值：](http://light.cc/) |
|                           | light.cc.Adasum  / light.cc.Sum  / light.cc.Average          |
| fusion_type               | 默认为使用"auto_fusion"，可选：                              |
|                           | "piecewise_fusion"/"scopewise_fusion"、"xlascope_fusion"和"auto_fusion"四种模式，默认为"auto_fusion"。 |
|                           | 使用"piecewise_fusion"模式会根据用户设置的piecewise_fusion_schedule参数进行分层融合； |
|                           | 使用"scopewise_fusion"模式会根据用户设置的scopewise_fusion_schedule参数进行分层融合； |
|                           | 使用"xlascope_fusion"模式会根据模型中设置的jit_scope自动识别同一scope下的梯度进行融合； |
|                           | 使用"auto_fusion"模式会根据用户设置的auto_fusion_threshold参数进行分层融合。 |
| auto_fusion_threshold     | 使用"auto_fusion"时的合并阈值，单位为字节，默认为67108864，表示合并之后的层大小不超过67108864字节 |
| piecewise_fusion_schedule | 使用"piecewise_fusion"时的融合边界，以";"分隔，每个数字表示融合的分界线，例如"2;6"代表融合成3段，前2层(0,1)进行融合，接着4层(2-5)进行融合通信，最后6层及以后进行融合通信。默认为"0"，即将所有的梯度融合为1段进行通信 |
| scopewise_fusion_schedule | 使用"scopewise_fusion"时的融合边界，以";"分隔，每个字符串表示该variable_scope下的参数融合到一起，余下未被任何scope匹配的参数会另外融合为1段。默认为""，即将所有的梯度融合为1段进行通信 |

- 返回值: 
  梯度规约后(gradient, variable)对的列表	

####  light.cc.allgather（支持 Tensorflow 框架）
- API：
  ```
	light.cc.allgather(
        tensor, name=None
  )
```	
- 功能：
  将所有 Light 程序上输入的 tensor 拼接在一起。
  拼接是在 tensor 的第一个维度上完成的，因此除第一个维度允许不同之外，不同进程上的输入 tensor 必须具有相同的 rank 和 shape	
- 参数:	

| 参数   | 说明                        |
| ------ | --------------------------- |
| tensor | Tensor: allgather操作的对象 |
| name   | string                      |

- 返回值: 
  allgather 操作的结果,为各个进程的 tensor 副本在第一维上进行合并后的结果。	

####  light.cc.broadcast（支持 Tensorflow框 架）
- API：
```
 light.cc.broadcast(
        inp_tensor, root_rank=0, name=None
 )
```	
	
- 功能：
  将输入的张量从 root_rank 进程上广播到所有 Light 进程，保证各进程一致。	
- 参数:	

| 参数       | 说明                            |
| ---------- | ------------------------------- |
| inp_tensor | tf.Tensor: 该接口操作的输入张量 |
| root_rank  | int:执行广播操作的Light进程id   |
| name       | string                          |

- 返回值: 
  无	

#### light.cc.broadcast_variables（支持 Tensorflow 框架）
- API：
```
	light.cc.broadcast_variables(
        variables, root_rank=0
 )
```	
- 功能：
  将输入的变量从 root_rank 进程上广播到所有 Light 进程，保证各进程一致。	
- 参数:	
| 参数      | 说明                          |
| --------- | ----------------------------- |
| variables | 需要进行广播的variables       |
| root_rank | int:执行广播操作的Light进程id |

- 返回值: 
  无	

#### light.cc.broadcast_global_variables（支持 Tensorflow 框架）
- API：
 ```
	light.cc.broadcast_global_variables(
        root_rank=0
  )
```	
- 功能：
  将全局变量从 root_rank 进程上广播到所有 Light 进程，保证各进程一致。	
- 参数:	
  root_rank	int:执行广播操作的 Light 进程 id
- 返回值: 
  无	
#### light.cc.get_broadcast_variable_hook（支持 Tensorflow 框架）
- API：
 ```
	light.cc.get_broadcast_variable_hook(`
        `root_rank=0`
  )
```	
- 功能：
  SessionRunHook 在初始化期间,将全局变量从 root_rank 进程上广播到所有 Light 进程，保证各进程一致。	
- 参数:	
  root_rank	int:执行广播操作的 Light 进程 id
- 返回值: 
  无	

####  light.cc.get_broadcast_variable_callback（支持 Tensorflow 框架）
- API：
 ```
	light.cc.get_broadcast_variable_callback(`
        `root_rank=0`
  )
```	
- 功能：
  keras callback 在初始化期间,将全局变量从 root_rank 进程上广播到所有 Light 进程，保证各进程一致。	
- 参数:	
  root_rank	int:执行广播操作的 Light 进程id
- 返回值: 
  无	

####  light.cc.get_metric_average_callback（支持 Tensorflow 框架）
- API：
```
	light.cc.get_metric_average_callback(
        device=''
  )
```	
- 功能：
  keras callback 会在每个 epoch 的最后,对所有的 Light 进程执行 average metric 操作。	
- 参数:	
  device	string:用于allreduce操作的设备。 如果 Light 使用 HOROVOD_GPU_ALLREDUCE 构建，则默认情况下使用 GPU。
- 返回值: 
  无	

#### light.cc.get_lr_schedule_callback（支持 Tensorflow 框架）
- API：
 ```
	light.cc.get_lr_schedule_callback(
        multiplier, start_epoch=0, end_epoch=None,
       staircase=True, momentum_correction=True,
        steps_per_epoch=None
  )
```	
- 功能：
  keras callback 将学习率从 start_epoch 时的 initial_lr 变为 end_epoch 时的 initial_lr*multiplier。
  如果 multiplier 是函数乘子，且 staircase=True ：调整学习率将在每个 epoch 的开始时进行，并且每个 epoch 传递给函数乘子的是一个整数；
  如果 multiplier 是函数乘子，且 staircase=False ：调整学习率将在每个 batch 的开始时进行，并且每个 epoch 传递给函数乘子的是一个浮点数 epoch=epoch+batch/steps_per_epoch。对于平滑学习率 (smooth Learning Rate) 调整很有用。
  其中：initial_lr 是训练初始时优化器的学习率。	
- 参数:	

| 参数                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| multiplier          | 常数乘子或者一个函数乘子，形如f(epoch)=lr                    |
| start_epoch         | int:默认值为0.开始学习率调整的第一个epoch                    |
| end_epoch           | int:默认值为None.结束学习率调整的epoch                       |
| staircase           | bool:默认值为True. staircase=True:是否调整学习率在开始的epoch; staircase=False:是否调整学习率在每一个开始的batch |
| momentum_correction | bool:默认值为True. 是否对带有动量的优化器进行动量修正        |
| steps_per_epoch     | int:每个epoch的batch的数量。keras version  大于等于2.0.0，会自动获取该值。否则，需手动补齐。 |

- 返回值: 
  无	

####  light.cc.get_lr_warmup_callback（支持 Tensorflow 框架）
- API：
 ```
	light.cc.get_lr_warmup_callback(
        warmup_epoch=5, momentum_correction=True,
        steps_per_epoch=None, verbose=0
  )
```	
- 功能：
  学习率预热(warmup)
  `lr = initial_lr / light.cc.size()` ---> `lr = initial_lr`
  其中：initial_lr 是训练初始时优化器的学习率。	
- 参数:	

| 参数                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| warmup_epoch        | int:默认值为5. 学习率预热的epoch数量                         |
| momentum_correction | bool:默认值为True. 是否对带有动量的优化器进行动量修正        |
| steps_per_epoch     | int:每个epoch的batch的数量。keras version  大于等于2.0.0，会自动获取该值。否则，需手动补齐。 |
| verbose             | 默认值为0，verbosity模式，取值 0 或 1                        |

- 返回值: 
  无	

####  light.cc.allgather_object（支持 Tensorflow 框架）
- API：
```
	light.cc.allgather_object(
        obj, session=None, name=None
  )
```	
- 功能：
  收集所有进程的可序列化 obj	
- 参数:	

| 参数    | 说明                               |
| ------- | ---------------------------------- |
| obj     | 一个没有丢失上下文可以序列化的对象 |
| session | TF1.x 兼容会话                     |
| name    | 默认None                           |

- 返回值: 
  list：从所有进程收集的obj列表	

#### light.cc.broadcast_object（支持 Tensorflow 框架）
- API：
 ```
	light.cc.broadcast_object(
        obj, root_rank=0, session=None, name=None
  )
```	
- 功能：
  广播可序列化obj	
- 参数:	

| 参数      | 说明                               |
| --------- | ---------------------------------- |
| obj       | 一个没有丢失上下文可以序列化的对象 |
| root_rank | 广播进程                           |
| session   | TF1.x 兼容会话                     |
| name      | 默认None                           |

- 返回值: 
  被广播的 obj	

#### light.cc.broadcast_variable（支持 Pytorch 框架）
- API：
 ```
	light.cc.broadcast_variable(
        inp, root_rank=0, name=None
  )
```	
- 功能：
  在分布式训练前广播参数，从而保证各个进程的初始参数一致	
- 参数:	

| 参数      | 说明                                                       |
| --------- | ---------------------------------------------------------- |
| inp       | Tensor/Optimizer/dict/list: 需要进行广播同步的参数或优化器 |
| root_rank | int:发起广播的进程编号                                     |
| name      | string                                                     |

- 返回值: 
  无	

####  light.cc.allreduce（支持 Pytorch 框架）
- API：
  ```
	light.cc.allreduce(
        tensor, average=None, name=None,
        compression=light.cc.Compression.none, op=None
  )
```	
- 功能：
  对指定 Tensor 进行all reduce操作	
- 参数:	

| 参数        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| tensor      | Tensor: allrduce操作的对象                                   |
| average     | deprecatred，请使用op                                        |
| name        | string                                                       |
| compression | 进行梯度压缩的算法，默认为不进行压缩。注意，梯度压缩可能会影响精度 |
| op          | 如何进行规约，默认为取平均                                   |

- 返回值: 
  allreduce操作的结果	

####  light.cc.allgather（支持 Pytorch 框架）
- API：
 ```
	light.cc.allgather(
        tensor, name=None
  )
```	
- 功能：
  对指定 Tensor 进行allgather操作	
- 参数:	

| 参数   | 说明                        |
| ------ | --------------------------- |
| tensor | Tensor: allgather操作的对象 |
| name   | string                      |

- 返回值: 
  allgather操作的结果,为各个进程的tensor副本在第一维上进行合并后的结果。	

####  light.cc.get_distributed_optimizer（支持 Pytorch 框架）
- API：
 ```
	light.cc.get_distributed_optimizer(
        optimizer, named_parameters=None,
        compression=light.cc.Compression.none,
        backward_passes_per_step=1, op=light.cc.Average
  )
```	
- 功能：
  将单进程优化器 optimizer 扩展成分布式优化器，并自动加入了梯度规约的功能。	
- 参数:	

| 参数                     | 说明                                                         |
| ------------------------ | ------------------------------------------------------------ |
| optimizer                | Optimizer: 准备进行分布式处理的单机optimizer                |
| name_parameters          | dict: 需要进行优化的优化器参数，一般只需要调用 model.named_parameters() |
| compression              | 进行梯度压缩的方法，默认为不进行梯度压缩                     |
| backward_passes_per_step | int: 设置每多少步进行一次规约，用于梯度累计。注意在使用时需要在不进行规约的迭代步跳过  optimizer.step() 与 optimizer.zero_grad() 以保证正确性 |
| op                       | [梯度规约方式，默认为light.cc.Average](http://light.cc/)     |

- 返回值: 
  DistributedOptimizer，用于进行分布式训练用的 optimizer	

### Light 分布式场景使用 Pytorch DDP 通信模式（支持 Pytorch 框架）
 为用户更方便使用 Light，Light 支持了 Pytorch DDP 的任务，不需要登录到多台机器上执行多机多卡命令，Light 对易用性做了优化。只需要少量修改即可使用 Light-ddp 模型多机多卡训练，具体修改分3步。
 首先是代码修改，训练代码保持不变，只需要加上 light_init的装饰器，Light 后端已经初始化了通信环境，因此训练代码里不需要再去调用`dist.init_process_group`（Light默认使用 NCCL）。
```
  from light import light_init                              # 修改点1：导入light初始化
  @light_init(params={"training_framework": "pytorch_ddp"}) # 修改点2：训练框架选择“pytorch_ddp”模式
  def main():

    # 修改点3：删除dist.init_process_group(backend="nccl", init_method='env://')
    model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[self.local_rank])
    ...
     
# please surround your entry function with
#
#   if __name__ == "__main__":
#
# otherwise, some multiprocess issues may be triggered.
if __name__ == "__main__":
    main()

```
然后是启动命令（start.sh）修改，原始DDP运行方式需要每台机器执行指定 nnodes、node_rank、nproc_per_node、master_addr、master_port 等参数，且需要配置不同的 node_rank ，命令复杂难在平台上使用。Light 简化了启动方式，以上参数均由 Light 后台自动配置，无需用户手动指定。
```
#!/bin/bash
sleep 200  # sleep for jizhi prepare env
export NCCL_DEBUG=INFO
# 部分机器硬件环境不支持IB，会导致通信异常，故这里关掉IB
# 若机器环境没问题，正确设置NCCL IB相关参数，打开IB可加速通信
export NCCL_IB_DISABLE=1

python3 -u -m light.pytorch.launch trainer.py

```
最后是配置（config.json）修改，客户端启动任务时，加上以下4行设置（application_scenario根据业务具体领域而定，参考【Light初始化】）。
```
{
  "exec_start_in_all_mpi_pods": true,
  "accelerate_params": {
    "enable_optimizations": true,
    "application_scenario" : "Torch-NLP"
  }
}
```
