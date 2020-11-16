

## 参数
#### 组件参数
组件参数与普通的 TensorFlow \ PyTorch 组件类似，目前智能钛提供了  TensorFlow 1.12 和 PyTorch 的联合镜像，可以选择 py2 和 py3 两个版本。

#### 资源参数
配置多机多卡的资源，worker_num 数量即机器数。


## 代码示例
用户想要利用 horovod 框架，需要对原有的 TensorFlow 和 PyTorch 代码进行改造。
如果您想将一个只支持单机单卡的训练脚本修改为支持多机多卡的训练脚本，以 TensorFlow 为例，只需要做如下改动：

```
import tensorflow as tf
import horovod.tensorflow as hvd


# Initialize Horovod
hvd.init()

# Pin GPU to be used to process local rank (one GPU per process)
config = tf.ConfigProto()
config.gpu_options.visible_device_list = str(hvd.local_rank())

# Build model...
loss = ...
opt = tf.train.AdagradOptimizer(0.01 * hvd.size())

# Add Horovod Distributed Optimizer
opt = hvd.DistributedOptimizer(opt)

# Add hook to broadcast variables from rank 0 to all other processes during
# initialization.
hooks = [hvd.BroadcastGlobalVariablesHook(0)]

# Make training operation
train_op = opt.minimize(loss)

# Save checkpoints only on worker 0 to prevent other workers from corrupting them.
checkpoint_dir = '/tmp/train_logs' if hvd.rank() == 0 else None

# The MonitoredTrainingSession takes care of session initialization,
# restoring from a checkpoint, saving to a checkpoint, and closing when done
# or an error occurs.
with tf.train.MonitoredTrainingSession(checkpoint_dir=checkpoint_dir,
                                       config=config,
                                       hooks=hooks) as mon_sess:
  while not mon_sess.should_stop():
    # Perform synchronous training.
    mon_sess.run(train_op)

```

以上代码仅为示例说明， 需要用户自行定义 loss，仅供参考。
