## 操作场景
本文档将向您介绍如何使用 TI SDK 训练 Pytorch 模型。

## 操作步骤
使用 TI SDK 训练 Pytorch 模型只需要三步
1. 准备训练脚本
2. 构造一个 ti.pytorch.Pytorch Estimator
3. 调用 Estimator 的 fit 方法

TI 预置了1.1版本 Pytorch 镜像，用户也可以上传自定义镜像，自定义镜像的版本不受限制，只需要参考 TI 容器规范，参考 [使用自定义镜像](https://cloud.tencent.com/document/product/851/40126 )。

### 准备训练脚本
TI 中使用的训练脚本和标准的 Pytorch 脚本非常相似，只需少量的修改就可以将用户现有的 Pytorch 训练脚本适配到TI中。训练脚本可以直接读取注入的环境变量和超级参数。

可用的环境变量有：

- `TM_MODEL_DIR`：string 类型，表示容器中模型的输出路径
- `TM_NUM_GPUS`：整型，表示实例可用的 GPU 数
- `TM_OUTPUT_DATA_DIR`：string 类型，表示容器中输出数据（例如 checkpoints、图像或其他文件，但不包括生成的模型）的路径
- `TM_CHANNEL_XXXX`：string 类型，表示输入训练数据的路径，XXXX对应`fit`参数中通道的名字，如 train 和 test 两个通道对应的环境变量是`TM_CHANNEL_TRAIN` `TM_CHANNEL_TEST`.

一个典型训练脚本的工作流程是
1. 读取环境变量指定的路径加载数据
2. 读取超级参数用于训练（可选）
3. 训练完成后，将模型保存到约定的目录中

TI 会运行用户的训练脚本，建议将启动训练的入口代码放到 main 方法中（`if__name__== '__main__'`）

### 构造 Estimator

```python
estimator = PyTorch(entry_point='train.py',
                            role=role,
                            framework_version='1.1.0',
                            train_instance_count=1,
                            train_instance_type='TI.SMALL2.1core2g',
                            source_dir='path/to/code',
                            # available hyperparameters: emsize, nhid, nlayers, lr, clip, epochs, batch_size,
                            # bptt, dropout, tied, seed, log_interval
                            hyperparameters={
                                'epochs': 1,
                                'tied': True
                            })
```



### 调用 fit 方法

```python
estimator.fit({'training': 'cos://path/to/input'})
```

#### 必须参数
- inputs： 存储训练数据集的 COS 路径，可以采用以下两种数据结构
  - `str`：例如 `cos://my-bucket/my-training-data`，COS URI，表示数据集的路径
  - `dict[str, str]`：例如`{'train': 'cos://my-bucket/my-training-data/train', 'test': 'cos://my-bucket/my-training-data/test'}`，可以指定多个通道的数据集

#### 可选参数

- `wait (bool)`：默认为 True，是否阻塞直到训练完成。如果设置为 False，`fit`立即返回，训练任务后台异步执行，后面仍可通过`attach`方法附加。
- `logs (bool)`：默认为 True，是否打印训练任务产生的日志。只有在`wait`为 True 时才生效。
- `job_name (str)`：训练任务名称。如果未指定，则 Estimator 将根据训练镜像名和时间戳生成一个默认名字。

#### 工作流程
调用 fit 方法启动训练任务后，TI 后台会执行以下操作：
- 启动`train_instance_count`数量的`train_instance_type`对应的算力

在每台实例上，执行以下步骤

1. 拉取预置 Pytorch 镜像启动容器
2. 下载训练数据集
3. 设置训练相关的环境变量
4. 开始训练
