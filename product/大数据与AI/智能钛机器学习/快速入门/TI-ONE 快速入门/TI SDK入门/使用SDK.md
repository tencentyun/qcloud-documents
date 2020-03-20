## 操作场景
本文档向您介绍如何使用 TI SDK 训练模型。

在 Notebook 中内置了 TI SDK 的案例，您可以通过典型案例快速上手，详情请参考 [使用内置案例](https://cloud.tencent.com/document/product/851/40074)。

## 操作步骤
TI SDK 使用以下几个核心类实现 TI 的模型训练
- Estimators： 对训练任务的抽象。
- Session：使用 TI 资源的方法集合。

使用 TI SDK 训练模型需要以下三个步骤：
1. 准备一个训练脚本。
2. 构造一个 Estimator。
3. 调用 Estimator 的 fit 方法。

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

#### 使用 Estimator 提交训练任务
Estimator 是对一个训练任务的高级抽象，包含训练镜像、算力资源、安全权限、算法参数、输入输出等一次训练依赖的所有参数。TI 针对 Tensorflow、PyTorch 等多种流行的机器学习框架分别封装了 Estimator 的具体实现。

以下例子展示了一个简单的 Tensorflow Estimator 使用：

```
tf_estimator = TensorFlow(role=role,
                          train_instance_count=1,
                          train_instance_type='TI.SMALL2.1core2g',
                          py_version='py3',
                          script_mode=True,
                          framework_version='1.14.0',
                          entry_point='train.py',
                          source_dir='gpu/code')

tf_estimator.fit('cos://bucket/path/to/training/data')
```

参数
- `role`：str 用户在云控制台创建的角色，需要传递角色给 TI，授权 TI 服务访问用户的云资源。
- `train_instance_count`：int 创建的算力实例数量。
- `train_instance_type`：str 创建的算力类型，目前支持的类型有。

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
- `hyperparameters`：dict 超级参数，将传递到训练容器中。
- `train_max_run`：int 最大运行时间，单位秒，超过设定时间若训练未完成，TI 会终止训练任务（默认值：24 * 60 * 60）。
- `input_mode`：输入类型，默认 File。
- `base_job_name`：str fit()方法启动的训练任务名称前缀，如果没有指定，会使用镜像名和时间戳生成默认任务名。
- `output_path`：用于保存模型和输出文件的 COS 路径，如果未指定，会生成默认的存储桶。
- `subnet_id`：str 子网 ID，如果未指定，将在没有 VPC 配置的情况下创建任务。
- `security_group_ids`：（list [ str ]）安全组 ID 列表，如果未指定，将在没有 VPC 配置的情况下创建任务。

更多的参数意义请参考 EstimatorBase 类 （ ti-python-sdk/src/ti/EstimatorBase.py）。


#### 调用 fit 方法
>!fit(inputs=None、wait=True、logs=True、job_name=None)
fit 方法会创建并启动一个训练任务

参数
- `inputs`： 存储训练数据集的 COS 路径，可以采用以下两种数据结构。
  - `str`：例如：`cos://my-bucket/my-training-data`，COS URI，表示数据集的路径。
  - `dict[str, str]`：例如`{'train': 'cos://my-bucket/my-training-data/train', 'test': 'cos://my-bucket/my-training-data/test'}`，可以指定多个通道的数据集
- `wait (bool)`：默认为 True，是否在阻塞直到训练完成。如果设置为 False，fit 立即返回，训练任务后台异步执行，后面仍可通过 attach 方法附加。
- `logs (bool)`：默认为 True，是否打印训练任务产生的日志。只有在 wait 为 True 时才生效。
- `job_name (str)`：训练任务名称。如果未指定，则 Estimator 将根据训练镜像名和时间戳生成默认名字。




