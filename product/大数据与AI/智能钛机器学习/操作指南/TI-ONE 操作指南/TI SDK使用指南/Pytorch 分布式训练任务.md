## 操作场景
本文档将向您介绍如何使用 TI SDK 实现 Pytorch 分布式训练。

## 使用 Horovod 训练
Horovod 是一个基于 MPI 的分布式训练框架，容器内设置 MPI 环境并执行 mpirun 命令，可以运行任何 Horovod 训练脚本。

在 Estimator 中使用`distributions`表示这是一个分布式训练任务，支持的 mpi 参数有：  
- `enabled (bool)`：如果设置为 True，则设置 MPI 并执行 mpirun 命令。
- `processes_per_host (int)`：MPI 应在每台实例上启动的进程数。请注意，这个值需不大于实例上的 GPU 卡数。
- `custom_mpi_options (str)`：可以在此字段中传递任何 mpirun 支持的参数选项，TI 执行的 mpirun 时会附带此参数，以启动分布式 horovod 训练。

在下面的示例中，我们创建了一个使用2台单V100卡机器的分布式训练任务。
```python
ti_session = session.Session()

role = "TIONE_QCSRole"

inputs = ti_session.upload_data(path='distributed/data', key_prefix="data/pytorch_dist")
print(inputs)

estimator = PyTorch(role=role,
                    framework_version='1.1.0',
                    train_instance_count=2,
                    train_instance_type='TI.GN10X.2XLARGE40.1xV100',
                    source_dir='distributed/code',
                    entry_point="horovod_pytorch_example.py",
                    distributions={
                      'mpi': {
                        'enabled': True,
                        'processes_per_host': 1,
                        'custom_mpi_options': '--NCCL_DEBUG INFO'
                      }
                    })
estimator.fit({'training': inputs})
```
