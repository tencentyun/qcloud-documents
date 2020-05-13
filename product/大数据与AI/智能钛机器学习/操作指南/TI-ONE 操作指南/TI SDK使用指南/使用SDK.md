## 操作场景
本文档向您介绍如何使用 TI SDK 训练模型。

### 在 Notebook 中使用 TI SDK
我们在 Notebook 中内置了 TI SDK 的案例，您可以通过典型案例快速上手，详情请参考 [使用内置案例](https://cloud.tencent.com/document/product/851/40074)。

### 在本地环境使用 TI SDK
若您的 TI SDK 环境为非腾讯云 Jupyter Notebook 环境时，您需要先配置 TI SDK 环境。
TI SDK 配置的环境目录为 ~/.ti/config.yaml，用户需要提供的配置信息如下：
1. region：训练任务提交的腾讯云资源的地域，目前支持 ap-guangzhou，ap-shanghai
2. uin：腾讯云账号 ID，可在腾讯云控制台-账号信息中查看
3. app_id：腾讯云账号 AppID，可在腾讯云控制台-账号信息中查看
4. secret_id：腾讯云账号 API 密钥 ID，可在腾讯云控制台 > 访问管理 > 用户详情中查看
5. secret_key：腾讯云账号 API 密钥 KEY，可在腾讯云控制台 > 访问管理 > 用户详情中查看

示例如下：

```python
# ~/.ti/config.yaml的内容格式如下：
basic:
    region: 你的腾讯云地域
    uin: 你的uin
    app_id:  你的appid
    secret_id:  你的secret_id
    secret_key:  你的secret_key
```



## 操作步骤
TI SDK 使用以下几个核心类实现 TI 的模型训练
- Estimators： 对训练任务的抽象。
- Session：使用 TI 资源的方法集合。

使用 TI SDK 训练模型需要以下四个步骤：
1. 准备一个训练脚本。
2. 上传训练数据集。
3. 构造一个 Estimator。
4. 调用 Estimator 的 fit 方法。

#### 准备训练脚本
训练脚本必须在 Python2.7 或3.6环境下执行。TI 提供了很高的兼容性，只需要少部分改动就可以将外部环境运行的训练脚本适配到 TI 中，同时 TI 提供了许多环境变量定义训练环境各种资源和参数，在训练脚本中可以直接访问这些环境变量获取相关属性，包括：
- `TM_MODEL_DIR`：string 类型，表示容器中模型的输出路径，设置为`/opt/ml/model`。
- `TM_NUM_GPUS`：整型，表示实例可用的 GPU 数。
- `TM_OUTPUT_DATA_DIR`：string 类型，表示容器中输出数据（例如 checkpoints、图像或其他文件，但不包括生成的模型）的路径。
- `TM_CHANNEL_XXXX`：string 类型，表示输入训练数据的路径，XXXX对应`fit`参数中通道的名字，如 train 和 test 两个通道对应的环境变量是`TM_CHANNEL_TRAIN` `TM_CHANNEL_TEST`
- `TM_HPS`：json 格式的超级参数。

一个典型的训练脚本处理流程如下：
1. 从输入通道加载训练数据。
2. 读取超参数配置。
3. 开始训练模型。
4. 保存模型。

TI 会运行用户的训练脚本，建议将启动训练的入口代码放到 main 方法中（`if__name__== '__main__'`）

#### 上传训练数据集

- TI SDK 任务采用 COS 对象存储数据源或 CFS 文件存储数据源作为训练脚本的输入源。
- 当您采用 CFS 文件存储数据源作为输入源时，您需要提前将数据集拷贝至文件系统目录，详见 [使用文件系统提交训练任务](https://cloud.tencent.com/document/product/851/41053)。
- 当您采用 COS 对象存储数据源作为输入源时，您需要将本地数据集上传至目标 COS 中。

以下例子展示了一个简单的本地数据上传 COS 的使用：

```python
from ti import session
ti_session = session.Session()

bucket = "your bucket"
key_prefix = "train-data"
path = "train-data"

inputs = ti_session.upload_data(bucket=bucket, path=path, key_prefix=key_prefix)
```

参数

- `bucket`：str 用户 COS 对象存储桶名称。
- `path`：str 用户数据集的本地目录路径。
- `key_prefix`：str 用户数据集 COS 桶下的存储路径。

#### 使用 Estimator 提交训练任务
Estimator 是对一个训练任务的高级抽象，包含训练镜像、算力资源、安全权限、算法参数、输入输出等一次训练依赖的所有参数。TI 针对 Tensorflow、PyTorch 等多种流行的机器学习框架分别封装了 Estimator 的具体实现。

以下例子展示了一个简单的 Tensorflow Estimator 使用：

```python
tf_estimator = TensorFlow(role=role,
                          train_instance_count=1,
                          train_instance_type='TI.SMALL2.1core2g',
                          py_version='py3',
                          script_mode=True,
                          framework_version='1.14.0',
                          entry_point='train.py',
                          source_dir='gpu/code')

tf_estimator.fit(inputs)
```

参数
- `role`：str 用户在云控制台创建的角色，需要传递角色给 TI，授权 TI 服务访问用户的云资源。
- `train_instance_count`：int 创建的算力实例数量。
- `train_instance_type`：str 创建的算力类型，目前支持的类型有：

CPU 算力

| 类型                      |
| ------------------------- |
| TI.SMALL2.1core2g         |
| TI.SMALL4.1core4g         |
| TI.MEDIUM4.2core4g        |
| TI.MEDIUM8.2core8g        |
| TI.LARGE8.4core8g         |
| TI.LARGE16.4core16g       |
| TI.2XLARGE16.8core16g     |
| TI.2XLARGE32.8core32g     |
| TI.3XLARGE24.12core24g    |
| TI.3XLARGE48.12core48g    |
| TI.4XLARGE32.16core32g    |
| TI.4XLARGE64.16core64g    |
| TI.6XLARGE48.24core48g    |
| TI.6XLARGE96.24core96g    |
| TI.8XLARGE64.32core64g    |
| TI.8XLARGE128.32core128g  |
| TI.12XLARGE96.48core96g   |
| TI.12XLARGE192.48core192g |
| TI.16XLARGE128.64core128g |
| TI.16XLARGE256.64core256g |
| TI.20XLARGE320.80core320g |

GPU 算力（V100）

| 类型         |
| ------------ |
| TI.GN10X.2XLARGE40.1xV100 |
| TI.GN10X.4XLARGE80.2xV100 |
| TI.GN10X.9XLARGE160.4xV100 |
| TI.GN10X.18XLARGE320.8xV100 |

- `train_volume_size`：int 附加的云硬盘大小，单位 GB。

- `entry_point`：str 训练任务的执行入口点名称。例如下面的代码路径中，mnist.py 为训练任务执行入口点，而 np_convert.py 和 image_convert.py 分别为依赖的代码。

```
├── code
│   ├── np_convert.py
│   ├── image_convert.py
│   └── mnist.py
```

- `source_dir`：str 训练任务的代码路径，将会统一压缩代码路径上传至用户 COS 中。

- `hyperparameters`：dict 超级参数，将传递到训练容器中。
- `train_max_run`：int 最大运行时间，单位秒，超过设定时间若训练未完成，TI 会终止训练任务（默认值：24 * 60 * 60）。
- `input_mode`：输入类型，默认 File。
- `base_job_name`：str fit()方法启动的训练任务名称前缀，如果没有指定，会使用镜像名和时间戳生成默认任务名。
- `output_path`：用于保存模型和输出文件的 COS 路径，如果未指定，会生成默认的存储桶。
- `subnet_id`：str 子网 ID，如果未指定，将在没有 VPC 配置的情况下创建任务。
- `image_name`：str 训练任务镜像名称，用户可传入 TKE 镜像仓库中自定义训练镜像。

更多的参数意义请参考 EstimatorBase 类 （ ti-python-sdk/src/ti/EstimatorBase.py）。


#### 调用 fit 方法
>!fit(inputs=None、wait=True、logs=True、job_name=None)
fit 方法会创建并启动一个训练任务

参数

- `inputs`： 存储训练数据集的 COS 路径或 CFS 文件系统信息，可以采用以下多种数据结构。
  - `str`：例如：`cos://my-bucket/my-training-data`，COS URI，表示数据集的路径。
  - `dict[str, str]`：例如`{'train': 'cos://my-bucket/my-training-data/train', 'test': 'cos://my-bucket/my-training-data/test'}`，可以指定多个通道的数据集。
  - `FileSystemInput`：表示 CFS 数据集的数据结构，详见 [使用文件系统提交训练任务](https://cloud.tencent.com/document/product/851/41053)。
  - `dict[str, FileSystemInput]`：例如{'train': TrainFileSystemInput, 'test': TestFileSystemInput}，可以指定多个 CFS 数据集的字典结构。

- `logs (bool)`：默认为 False，是否打印训练任务产生的日志。如果设置为 True，将输出训练的任务日志。
- `wait (bool)`：默认为 True，是否等待直到训练完成。如果设置为 False，fit 立即返回，训练任务后台异步执行。
- `job_name (str)`：训练任务名称。如果未指定，则 Estimator 将根据训练镜像名和时间戳生成默认名字。


