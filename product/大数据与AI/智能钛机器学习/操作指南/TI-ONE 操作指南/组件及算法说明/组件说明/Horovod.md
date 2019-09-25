Horovod，它的名字来自于俄国传统民间舞蹈，舞者手牵手围成一个圈跳舞，与分布式 TensorFlow 流程使用 Horovod 互相通信的场景很像。Horovod 是 Uber（优步）开源的又一个深度学习工，Horovod 在2017年10月，Uber 以 Apache 2.0授权许可开源发布。Horovod 是优步跨多台机器的分布式训练框架，现已加入开源计划 LF Deep Learning Foundation。目前智能钛支持 TensorFlow 和 PyTorch 的 horovod 加速框架。
#### 位置
在【框架】>【深度学习】>【horovod】
![img](https://main.qcloudimg.com/raw/28d9734a48723aa1bc4f7f8ecca5fb85.png)

## 参数
#### 组件参数
组件参数与普通的 TensorFlow \ PyTorch 组件类似，目前智能钛提供了  TensorFlow 1.12 和 PyTorch 的联合镜像，可以选择 py2 和 py3 两个版本。
![img](https://main.qcloudimg.com/raw/989b979be4eb12c8c9d56a10a5de26e0.png)

#### 资源参数
配置多机多卡的资源，worker_num 数量即机器数，例如下图就代表了一个2机16卡的资源配置情况 （1机8卡  * 2）
![img](https://main.qcloudimg.com/raw/5dc6e5ef3c3f65e5ef8b344eb5127fa2.png)


## 代码示例
利用 horovod 框架，需要对原有的 TensorFlow 和 PyTorch 代码进行改造。
将一个只支持单机单卡的训练脚本修改为支持多机多卡的训练脚本，以 TensorFlow 为例，只需要做如下改动：

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
