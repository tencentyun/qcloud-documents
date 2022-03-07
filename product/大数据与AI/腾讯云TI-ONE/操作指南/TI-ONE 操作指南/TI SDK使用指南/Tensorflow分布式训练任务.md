## 操作场景
本文档将向您介绍如何使用 TI SDK 实现 Tensorflow 分布式训练。

TI 支持**参数服务器**和 **Horovod** 两种类型的分布式训练框架。使用`distributions`参数配置分布式训练策略。



## 使用参数服务器训练

如果指定 parameter_server 作为 distributions 参数的值，容器会在训练集群上启动参数服务器。

以下例子中创建了一个使用2台实例的参数服务器训练任务   

```python
tf_estimator = TensorFlow(role=role,
                          train_instance_count=2,
                          train_instance_type='TI.SMALL2.1core2g',
                          py_version='py3',
                          framework_version='1.14.0',
                          entry_point='train.py',
                          source_dir='path/code',
                          distributions={
                            'parameter_server': {'enabled': True}
                          }
                          )
tf_estimator.fit(inputs)
```



## 使用 Horovod 训练
Horovod 是一个基于 MPI 的分布式训练框架。 使用 Horovod 需要使用1.12以上版本的 Tensorflow（TI 预置镜像是1.14.0和2.0.0）
容器内设置 MPI 环境并执行`mpirun`命令，可以运行任何 Horovod 训练脚本

`distributions`支持的`mpi`参数有
- `enabled (bool)`：如果设置为 True，则设置 MPI 并执行 mpirun 命令。
- `processes_per_host (int)`：MPI 应在每台实例上启动的进程数。请注意，这个值需不大于实例上的 GPU 卡数
- `custom_mpi_options (str)`：可以在此字段中传递任何 mpirun 支持的参数选项，TI 执行的 mpirun 时会附带此参数，以启动分布式 horovod 训练。

以下例子中创建了一个使用2台单V100卡机器的分布式训练任务
```python
tf_estimator = TensorFlow(role=role,
                          train_instance_count=2,
                          train_instance_type='TI.GN10X.2XLARGE40.1xV100',
                          py_version='py3',
                          hyperparameters=hyperparameters,
                          framework_version='1.14.0',
                          entry_point='train.py',
                          source_dir='path/code',
                          distributions={
                            'mpi': {
                              'enabled': True,
                              'processes_per_host': 1,
                              'custom_mpi_options': '--NCCL_DEBUG INFO'
                            }
                          }
                         )
tf_estimator.fit(inputs)
```
