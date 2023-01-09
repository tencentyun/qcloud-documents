
<dx-alert infotype="explain" title="">
本文来自 [GPU 云服务器用户实践征文](https://cloud.tencent.com/document/product/855/71869)，仅供学习和参考。
</dx-alert>

## 操作场景
本文介绍如何使用 GPU 云服务器进行 ViT 模型离线训练，完成简单的图像分类任务。


## ViT 模型简介
ViT 全称 Vision Transformer，该模型由 Alexey Dosovitskiy 等人提出，在多个任务上取得 SoTA 结果。示意图如下：
![](https://qcloudimg.tencent-cloud.cn/raw/118faac2352673dcd4a207dfb3c79a51.png)


对于一幅输入的图像，ViT 将其划分为多个子图像 patch，每个 patch 拼接 position embedding 后，和类别标签一起作为 Transfomer Encoder 的一组输入。而类别标签位置对应的输出层结果通过一个网络后，即得到 ViT 的输出。在预训练状态下，该结果对应的 ground truth 可以使用掩码的某个 patch 作为替代。


## 示例环境
- **实例类型**：本文可选实例为 [GN7](https://cloud.tencent.com/document/product/560/19700#GN7) 与 [GN8](https://cloud.tencent.com/document/product/560/19700#GN8)，结合 [Technical](https://technical.city/en/video/Tesla-P40-vs-Tesla-T4) 提供的 GPU 对比，Turing 架构的 T4 性能优于 Pascal 架构的 P40。本文最终选用 GN7.5XLARGE80。
- **所在地域**：由于可能需上传一些尺寸较大的数据集，需优先选择延迟最低的地域。本文使用 [在线 Ping](https://cloud.feitsui.com/tencent) 工具测试，所在位置到提供 GN7 的重庆区域延迟最小，因此选择重庆区域。
- **系统盘**：100GB 高性能云硬盘。
- **操作系统**：Ubuntu 18.04
- **带宽**：5M
- **本地操作系统**：MacOS


## 操作步骤

### 设置实例免密登录（可选）

1. （可选）您可在本机 `~/.ssh/config` 中，配置服务器的别名。本文创建别名为 `tcg`。
2. 通过 `ssh-copy-id` 命令，将本机 SSH 公钥复制至 GPU 云服务器。
3. 在 GPU 云服务器中执行以下命令，关闭密码登录以增强安全性。
```shellsession
echo 'PasswordAuthentication no' | sudo tee -a /etc/ssh/ssh\_config
```
4. 执行以下命令，重启 SSH 服务。
```shellsession
sudo systemctl restart sshd
```


### PyTorch-GPU 开发环境配置
若使用 GPU 版本的 PyTorch 进行开发，则需要进行一些环境配置。步骤如下：

1. 安装 Nvidia 显卡驱动
执行以下命令，安装 Nvidia 显卡驱动。
```shellsession
sudo apt install nvidia-driver-418
```
安装完成后执行如下命令，查看是否安装成功。
```shellsession
nvidia-smi
```
返回结果如下图所示，表示已安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/b8faab7af92e4a7c58930a970aa69325.png)
2. 配置 conda 环境
依次执行以下命令，配置 conda 环境。
```shellsession
wget https://repo.anaconda.com/miniconda/Miniconda3-py39\_4.11.0-Linux-x86\_64.sh
```
```shellsession
chmod +x Miniconda3-py39\_4.11.0-Linux-x86\_64.sh
```
```shellsession
./Miniconda3-py39\_4.11.0-Linux-x86\_64.sh
```
```shellsession
rm Miniconda3-py39\_4.11.0-Linux-x86\_64.sh
```
3. 编辑 `~/.condarc` 文件，加入以下软件源信息，将 conda 的软件源替换为清华源。
```shellsession
channels:

  - defaults

show\_channel\_urls: true

default\_channels:

  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main

  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r

  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2

custom\_channels:

  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
4. 执行以下命令，设置 pip 源为腾讯云镜像源。
```shellsession
pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple
```
5. 安装 PyTorch
执行以下命令，安装 PyTorch。
```shellsession
conda install pytorch torchvision cudatoolkit=11.4 -c pytorch --yes
```
依次执行以下命令，查看 PyTorch 是否安装成功。
```shellsession
python
```
```shellsession
import torch
```
```shellsession
print(torch.cuda.is_avaliable())
```
返回结果如下图所示，表示 PyTorch 已安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/12b5f76946fd80ff46a4e4dfa9aed2cd.png)



### 准备实验数据
本次训练的测试任务是图像分类任务，使用了腾讯云在线文档中用到的 [花朵图像分类](https://cloud.tencent.com/document/product/851/19547?from=10680) 数据集。该数据集包含5类花朵，数据大小为218M。数据集抽样展示如下：（各类别下花朵照片示例）
![](https://main.qcloudimg.com/raw/cb16186fcf4cf98a6764face437a59ca.png)

原始数据集中的各个分类数据分别存放在类名对应的文件夹下。首先需将其转化为 imagenet 对应的标准格式。按4：1划分训练和验证集，使用以下代码进行格式转换：
```python
# split data into train set and validation set, train:val=scale

import shutil

import os

import math

scale = 4

data\_path = '../raw'

data\_dst = '../train\_val'

#create imagenet directory structure

os.mkdir(data\_dst)

os.mkdir(os.path.join(data\_dst, 'train'))

os.mkdir(os.path.join(data\_dst, 'validation'))

for item in os.listdir(data\_path):

    item\_path = os.path.join(data\_path, item)

 if os.path.isdir(item\_path):

        train\_dst = os.path.join(data\_dst, 'train', item)

        val\_dst = os.path.join(data\_dst, 'validation', item)

        os.mkdir(train\_dst)

        os.mkdir(val\_dst)

        files = os.listdir(item\_path)

 print(f'Class {item}:\n\t Total sample count is {len(files)}')

        split\_idx = math.floor(len(files) \* scale / ( 1 + scale ))

 print(f'\t Train sample count is {split\_idx}')

 print(f'\t Val sample count is {len(files) - split\_idx}\n')

 for idx, file in enumerate(files):

            file\_path = os.path.join(item\_path, file)

 if idx <= split\_idx:

                shutil.copy(file\_path, train\_dst)

 else:

                shutil.copy(file\_path, val\_dst)

print(f'Split Complete. File path: {data\_dst}')
```
数据集概览如下：
```shellsession
Class roses:

     Total sample count is 641

     Train sample count is 512

     Validation sample count is 129

Class sunflowers:

     Total sample count is 699

     Train sample count is 559

     Validation sample count is 140

Class tulips:

     Total sample count is 799

     Train sample count is 639

     Validation sample count is 160

Class daisy:

     Total sample count is 633

     Train sample count is 506

     Validation sample count is 127

Class dandelion:

     Total sample count is 898

     Train sample count is 718

     Validation sample count is 180
```

为了加速训练过程，我们进一步将数据集转换为 Nvidia-DALI 这种 GPU 友好的格式。DALI 全称 Data Loading Library，该库可以通过使用 GPU 替代 CPU 来加速数据预处理过程。在已有 imagenet 格式数据的前提下，使用 DALI 只需运行以下命令即可：
```shellsession
git clone https://github.com/ver217/imagenet-tools.git

cd imagenet-tools && python3 make\_tfrecords.py \

  --raw\_data\_dir="../train\_val" \

  --local\_scratch\_dir="../train\_val\_tfrecord" && \

python3 make\_idx.py --tfrecord\_root="../train\_val\_tfrecord"  
```


### 模型训练结果
为了便于后续训练分布式大规模模型，本文在分布式训练框架 [Colossal-AI](https://colossalai.org/) 的基础上进行模型训练和开发。Colossal-AI 提供了一组便捷的接口，通过这组接口能方便地实现数据并行、模型并行、流水线并行或者混合并行。
参考 Colossal-AI 提供的 demo，本文使用 [pytorch-image-models](https://github.com/rwightman/pytorch-image-models) 库所集成的 ViT 实现，选择最小的 `vit\_tiny\_patch16\_224` 模型，该模型的分辨率为224\*224, 每个样本被划分为16个 `patch`。
1. 根据 [版本选择页面](https://colossalai.org/download) 通过以下命令，安装 Colossal-AI 和 pytorch-image-models：
```shellsession
pip install colossalai==0.1.5+torch1.11cu11.3 -f https://release.colossalai.org
```
```shellsession
pip install timm
```
2. 参考 Colossal-AI 提供的 [demo](https://github.com/hpcaitech/ColossalAI-Examples)，编写模型训练代码如下：
```python
from pathlib import Path

from colossalai.logging import get\_dist\_logger

import colossalai

import torch

import os

from colossalai.core import global\_context as gpc

from colossalai.utils import get\_dataloader, MultiTimer

from colossalai.trainer import Trainer, hooks

from colossalai.nn.metric import Accuracy

from torchvision import transforms

from colossalai.nn.lr\_scheduler import CosineAnnealingLR

from tqdm import tqdm

from titans.utils import barrier\_context

from colossalai.nn.lr\_scheduler import LinearWarmupLR

from timm.models import vit\_tiny\_patch16\_224

from titans.dataloader.imagenet import build\_dali\_imagenet

from mixup import MixupAccuracy, MixupLoss

def main():

    parser = colossalai.get\_default\_parser()

    args = parser.parse\_args()

    colossalai.launch\_from\_torch(config='./config.py')

    logger = get\_dist\_logger()

 # build model

    model = vit\_tiny\_patch16\_224(num\_classes=5, drop\_rate=0.1)

 # build dataloader

    root = os.environ.get('DATA', '../train\_val\_tfrecord')

    train\_dataloader, test\_dataloader = build\_dali\_imagenet(

        root, rand\_augment=True)

 # build criterion

    criterion = MixupLoss(loss\_fn\_cls=torch.nn.CrossEntropyLoss)

 # optimizer

    optimizer = torch.optim.SGD(

        model.parameters(), lr=0.1, momentum=0.9, weight\_decay=5e-4)

 # lr\_scheduler

    lr\_scheduler = CosineAnnealingLR(

       optimizer, total\_steps=gpc.config.NUM\_EPOCHS)

    engine, train\_dataloader, test\_dataloader, \_ = colossalai.initialize(

        model,

        optimizer,

        criterion,

        train\_dataloader,

        test\_dataloader,

    )

 # build a timer to measure time

    timer = MultiTimer()

 # create a trainer object

    trainer = Trainer(engine=engine, timer=timer, logger=logger)

 # define the hooks to attach to the trainer

    hook\_list = [

        hooks.LossHook(),

        hooks.LRSchedulerHook(lr\_scheduler=lr\_scheduler, by\_epoch=True),

        hooks.AccuracyHook(accuracy\_func=MixupAccuracy()),

        hooks.LogMetricByEpochHook(logger),

        hooks.LogMemoryByEpochHook(logger),

        hooks.LogTimingByEpochHook(timer, logger),

        hooks.TensorboardHook(log\_dir='./tb\_logs', ranks=[0]),

        hooks.SaveCheckpointHook(checkpoint\_dir='./ckpt')

    ]

 # start training

    trainer.fit(train\_dataloader=train\_dataloader,

                epochs=gpc.config.NUM\_EPOCHS,

                test\_dataloader=test\_dataloader,

                test\_interval=1,

                hooks=hook\_list,

                display\_progress=True)

if \_\_name\_\_ == '\_\_main\_\_':

    main()
```
模型的具体配置如下所示：
```shellsession
from colossalai.amp import AMP\_TYPE

BATCH\_SIZE = 128

DROP\_RATE = 0.1

NUM\_EPOCHS = 200 

CONFIG = dict(fp16=dict(mode=AMP\_TYPE.TORCH))

gradient\_accumulation = 16

clip\_grad\_norm = 1.0

dali = dict(

    gpu\_aug=True,

    mixup\_alpha=0.2

)
```
模型运行过程如下图所示， 单个 epoch 的时间在20s以内：
![](https://qcloudimg.tencent-cloud.cn/raw/0b9d0c91d5a05acd5808b8e71211e4a8.png)
结果显示模型在验证集上达到的最佳准确率为66.62%。


## 总结
本次使用过程中遇到的最大的问题是从 GitHub 克隆非常缓慢，为了解决该问题，尝试使用了 tunnel 和 proxychains 工具进行提速。但该行为违反了云服务器使用规则，导致了一段时间的云服务器不可用，最终通过删除代理并提交工单的方式才得以解决。
借此也提醒其他用户，进行外网代理不符合云服务器使用规范，为了保证您服务的稳定运行，切勿违反规定。


## 参考
[1] Dosovitskiy, Alexey, et al. "An image is worth 16x16 words: Transformers for image recognition at scale." arXiv preprint arXiv:2010.11929 (2020).
[2] [NVIDIA/DALI](https://github.com/NVIDIA/DALI)
[3] Bian, Zhengda, et al. "Colossal-AI: A Unified Deep Learning System For Large-Scale Parallel Training." arXiv preprint arXiv:2110.14883 (2021).
