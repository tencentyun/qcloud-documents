Caffe 是一个清晰而高效的深度学习框架，具有上手快、速度快、模块化、开放性和社区好等优势。

## 运行版本说明
Pycaffe 组件内核是 Caffe 1.0 版本。
Pycaffe 组件中使用的 Python 版本和支持的第三方模块信息如下：
```
Python version is [2.7.12]
scipy version is [0.17.0]
numpy version is [1.11.0]
```

若有需求使用其他第三方的 lib，可使用 pip 在代码内安装，示例如下：
```
 import pip
 pip.main(['install', "package_name"])
```

## 使用阶段

1. 从左边栏中，组件>深度学习 列表下拖拽出 PyCaffe 节点至画布中。
  ![](https://main.qcloudimg.com/raw/a20d4c6aa9c28c9351fe9c419fc69548.png)                                            

2. 参数配置（脚本及依赖包文件上传）
将任务脚本上传至 **程序脚本** 框。如果需要依赖文件，则压缩为 zip 文件后通过 **依赖包文件** 框上传。

 程序依赖：指定位于 COS 中的用户依赖文件路径，指定内容将被拷贝到程序脚本同一级目录下。支持目录或者文件，若有多个文件以英文逗号分割 。
 程序参数：指定运行任务脚本的参数。
 资源参数：选择运行工作流使用的 GPU、CPU 等资源配置。
![](https://main.qcloudimg.com/raw/04724a4733197f8aeac095a167aad56f.png)

3. 单击【保存】并运行工作流。

4. 查看 PyCaffe 控制台和日志
在 PyCaffe 节点上单击右键菜单可查看任务状态和详细日志。
   ![](https://main.qcloudimg.com/raw/e885bde8cb51c74927127b5ac3c1fb97.png)
   ![](https://main.qcloudimg.com/raw/4eb6a08b1ab47025901a205013eb48fd.png)

## 示例

以下代码展示了如何在 PyCaffe 框架中，构建一个卷积神经网络(Lenet)：
```python
import os
import sys
import shlex
import subprocess
caffe_root="/caffe"
os.chdir(caffe_root)
sys.path.insert(0, os.path.join(caffe_root,"python"))
import caffe

# transform data into lmdb form
os.system('bash %s/create_mnist.sh' % 'cos_path_to_shell_scripts')

save_path = '/cos_person/cos_path_to_output_model'
train_net_path = '%s/lenet_train.prototxt' % save_path
test_net_path = '%s/lenet_test.prototxt' % save_path
deploy_net_path = '%s/lenet_deploy.prototxt' % save_path
solver_file= '%s/lenet_solver.prototxt' % save_path

lmdb_data_path = 'path_to_lenet_lmdb' # better not in cos for now
train_lmdb_path = '%s/mnist_train_lmdb' % lmdb_data_path
test_lmdb_path = '%s/mnist_test_lmdb' % lmdb_data_path

lenet_snapshot_prefix = '%s/lenet' % save_path

from caffe import layers as L, params as P

def lenet(lmdb, batch_size):
    # our version of LeNet: a series of linear and simple nonlinear transformations
    n = caffe.NetSpec()
    
    n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, source=lmdb,
                             transform_param=dict(scale=1./255), ntop=2)
    
    n.conv1 = L.Convolution(n.data, kernel_size=5, num_output=20, weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=2, stride=2, pool=P.Pooling.MAX)
    n.conv2 = L.Convolution(n.pool1, kernel_size=5, num_output=50, weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=2, stride=2, pool=P.Pooling.MAX)
    n.fc1 =   L.InnerProduct(n.pool2, num_output=500, weight_filler=dict(type='xavier'))
    n.relu1 = L.ReLU(n.fc1, in_place=True)
    n.score = L.InnerProduct(n.relu1, num_output=10, weight_filler=dict(type='xavier'))
    n.loss =  L.SoftmaxWithLoss(n.score, n.label)
    
    return n.to_proto()
    
with open(train_net_path, 'w') as f:
    f.write(str(lenet(train_lmdb_path, 64)))    
with open(test_net_path, 'w') as f:
    f.write(str(lenet(test_lmdb_path, 100)))

deploy_net = lenet(test_lmdb_path, 100)
del deploy_net.layer[0]
with open(deploy_net_path, 'w') as f:
    f.write(str(deploy_net))    

from caffe.proto import caffe_pb2
s = caffe_pb2.SolverParameter()

# Set a seed for reproducible experiments:
# this controls for randomization in training.
s.random_seed = 0xCAFFE

# Specify locations of the train and (maybe) test networks.
s.train_net = train_net_path
s.test_net.append(test_net_path)
s.test_interval = 500  # Test after every 500 training iterations.
s.test_iter.append(100) # Test on 100 batches each time we test.

s.max_iter = 10000     # no. of times to update the net (training iterations)

# EDIT HERE to try different solvers
# solver types include "SGD", "Adam", and "Nesterov" among others.
s.type = "SGD"

# Set the initial learning rate for SGD.
s.base_lr = 0.01  # EDIT HERE to try different learning rates
# Set momentum to accelerate learning by
# taking weighted average of current and previous updates.
s.momentum = 0.9
# Set weight decay to regularize and prevent overfitting
s.weight_decay = 5e-4

# Set `lr_policy` to define how the learning rate changes during training.
# This is the same policy as our default LeNet.
s.lr_policy = 'inv'
s.gamma = 0.0001
s.power = 0.75
# EDIT HERE to try the fixed rate (and compare with adaptive solvers)
# `fixed` is the simplest policy that keeps the learning rate constant.
# s.lr_policy = 'fixed'

# Display the current training loss and accuracy every 1000 iterations.
s.display = 1000

# Snapshots are files used to store networks we've trained.
# We'll snapshot every 5K iterations -- twice during training.
s.snapshot = 5000
s.snapshot_prefix = lenet_snapshot_prefix

# Train on the GPU
s.solver_mode = caffe_pb2.SolverParameter.GPU

# Write the solver to a file.
with open(solver_file, 'w') as f:
    f.write(str(s))

# Train
caffe.set_device(0)
caffe.set_mode_gpu()
solver = caffe.SGDSolver(solver_file)
solver.solve()
```

示例代码下载：[PyCaffe_LenetTrain.py](https://tio.cloud.tencent.com/gitbook/doc/manual/attachments/PyCaffe_LenetTrain.py)
