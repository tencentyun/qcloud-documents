## 操作场景
TI Containers 是一个帮助用户构建镜像的软件包，用户可以使用 TI Containers 来方便地创建一个可以在 TI 环境中运行的容器，目前 TI 预置的 Tensorflow、Pytorch 镜像都是利用 TI Containers 构建的。本文档将向您提供利用 TI Containers 构建容器以及可用环境变量的相关介绍。


## 利用 TI Containers 构建容器
### 构建过程
- Dockerfile
以下是一个 DockerFile 例子，构建一个可以在 TI 中运行的容器，并定义了一个入口`train.py`

```dockerfile
FROM tensorflow/tensorflow:2.0.0a0

RUN pip install ti-containers

# Copies the training code inside the container
COPY train.py /opt/ml/code/train.py

# Defines train.py as script entry point
ENV TI_PROGRAM train.py
```

- build docker
```shell
docker build -t tf-2.0 .
```

### 执行过程

训练脚本必须放在容器内`/opt/ml/code`下，可以通过环境变量 TI_PROGRAM 访问该目录
训练脚本支持 Python(.py) 和 shell 两种语言
训练开始时，会执行以下语句

```shell
python train.py
```

### 使用超级参数

超级参数可以以启动参数的形式被传递给训练脚本
举例，有以下 JSON 格式的超级参数
```json
{
  "HyperParameters": 
  {
    "batch-size": 256, 
    "learning-rate": 0.0001, 
    "communicator": "pure_nccl"
  }
}
```

当执行用户自定义脚本时，作为启动参数一部分

```shell
./user_script.sh --batch-size 256 --learning_rate 0.0001 --communicator pure_nccl
```

### 使用环境变量
除了使用超级参数外，训练脚本还可以通过环境变量，举例，以下的例子使用了`training`和`testing`两个通道的输入数据
```ython
from ti.pytorch import PyTorch

estimator = PyTorch(entry_point='train.py', ...)

estimator.fit({'training': 'cos://bucket/path/to/training/data',
               'testing': 'cos://bucket/path/to/testing/data'})
```

用户的训练脚本可以使用 TM_CHANNEL_{channel_name} 来获取路径信息

```python
import argparse
import os

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  ...

  # reads input channels training and testing from the environment variables
  parser.add_argument('--training', type=str, default=os.environ['TM_CHANNEL_TRAINING'])
  parser.add_argument('--testing', type=str, default=os.environ['TM_CHANNEL_TESTING'])

  args = parser.parse_args()
  ...
```



## 可用环境变量
- TM_MODEL_DIR：模型输出目录
```shell
TM_MODEL_DIR=/opt/ml/model
```
- TM_CHANNELS：输入数据通道名
```shell
TM_CHANNELS='["testing","training"]'
```
- TM_CHANNEL_{channel_name}
```shell
# 举例
TM_CHANNEL_TRAINING='/opt/ml/input/data/training'
TM_CHANNEL_TESTING='/opt/ml/input/data/testing'
```

- TM_HPS：超级参数字典
```shell
#超参，举例
TM_HPS='{"batch-size": "256", "learning-rate": "0.0001","communicator": "pure_nccl"}'
```
TM_HP_{hyperparameter_name}：具体的超级参数值

```
# 超参，举例
TM_HP_LEARNING-RATE=0.0001
TM_HP_BATCH-SIZE=10000
TM_HP_COMMUNICATOR=pure_nccl
```

使用方法举例
```python
learning_rate = float(os.environ['TM_HP_LEARNING-RATE'])
batch_size = int(os.environ['TM_HP_BATCH-SIZE'])
comminicator = os.environ['TM_HP_COMMUNICATOR']
```

- TM_CURRENT_HOST：当前 Host
- TM_HOSTS：所有 Host
- TM_NUM_GPUS：GPU 卡数
- TM_NUM_CPUS：CPU 核数
- TM_LOG_LEVEL：日志登记
- TM_USER_ARGS：用户自定义参数
- TM_INPUT_DIR：输入目录

```shell
TM_INPUT_DIR=/opt/ml/input/
```

TM_INPUT_CONFIG_DIR：输入配置目录

```shell
TM_INPUT_CONFIG_DIR=/opt/ml/input/config
```
TI 启动任务时会在`TM_INPUT_CONFIG_DIR`创建以下三个文件：
	`hyperparameters.json`：超级参数
	`inputdataconfig.json`：输入数据
	`resourceconfig.json`：资源配置



