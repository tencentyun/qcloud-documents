Caffe（Convolutional Architecture for Fast Embedding）是一个高效的深度学习框架，具有易上手、速度快、效率高、社区好等优势。
## 版本说明
Pycaffe 组件内核是 Caffe 1.0 版本。
Pycaffe 组件中使用的 Python 版本和支持的第三方模块信息如下：

- Python 2.7.12
- SciPy 0.17.0
- NumPy 1.11.0

如果您需要使用其他第三方的 lib，可使用 pip 在代码内安装，示例如下：
```
import pip
pip.main(['install', "package_name"])
```

 
## 操作步骤

1. **添加组件**
从左侧菜单栏中，选择**框架**>**深度学习**列表下的 **PyCaffe** 节点，将其拖拽至画布中。                                          
2. **配置参数**
 - 脚本及依赖包文件上传：
    将任务脚本上传至程序脚本框。如果需要依赖文件，则压缩为 zip 文件后通过依赖包文件框上传。
 - 程序依赖：
    指定位于 COS 中的用户依赖文件路径，指定内容将被拷贝到程序脚本同一级目录下。支持目录或者文件依赖，若指定多个文件则以英文逗号分隔 。
 - 程序参数：
    指定运行任务脚本的参数。
3. **配置资源**
 在**资源参数**列表框中配置任务的资源参数。
4. **运行**
单击**保存**并运行工作流。
5. **查看 PyCaffe 控制台和日志**
在 PyCaffe 节点上单击右键，可查看任务状态和详细日志。

## 代码示例

以下代码将向您展示，在 PyCaffe 框架中训练 mnist 手写数字识别的方法。

```
import os
import argparse

import caffe
from caffe import layers as L, params as P
from caffe.proto import caffe_pb2

parser = argparse.ArgumentParser()
parser.add_argument("--save_dir", type=str, default="/cos_person",
                    help="Directory to save the trained model.")
parser.add_argument("--data_dir", type=str, default=None,
                    help="Directory which contains two subdirs: "
                         "`mnist_train_lmdb` and `mnist_test_lmdb`")
parser.add_argument("--max_iter", type=int, default=10000,
                    help="Number of training steps.")
args = parser.parse_args()


def lenet(lmdb, batch_size, include_accuracy=False, deploy=False):
    # our version of LeNet: a series of linear and simple nonlinear
    # transformations
    n = caffe.NetSpec()
    if not deploy:
        n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB,
                                 source=lmdb,
                                 transform_param=dict(scale=1. / 255), ntop=2)
    else:
        n.data = L.Input(
            input_param={'shape': {'dim': [batch_size, 1, 28, 28]}})

    n.conv1 = L.Convolution(n.data, kernel_size=5, num_output=20,
                            weight_filler=dict(type='xavier'))
    n.pool1 = L.Pooling(n.conv1, kernel_size=2, stride=2, pool=P.Pooling.MAX)
    n.conv2 = L.Convolution(n.pool1, kernel_size=5, num_output=50,
                            weight_filler=dict(type='xavier'))
    n.pool2 = L.Pooling(n.conv2, kernel_size=2, stride=2, pool=P.Pooling.MAX)
    n.fc1 = L.InnerProduct(n.pool2, num_output=500,
                           weight_filler=dict(type='xavier'))
    n.relu1 = L.ReLU(n.fc1, in_place=True)
    n.score = L.InnerProduct(n.relu1, num_output=10,
                             weight_filler=dict(type='xavier'))
    if not deploy:
        if include_accuracy:
            n.accuracy = L.Accuracy(n.score, n.label)
        n.loss = L.SoftmaxWithLoss(n.score, n.label)

    return n.to_proto()


def train():
    # Define paths
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)
    save_path = args.save_dir
    train_net_path = '{}/lenet_train.prototxt'.format(save_path)
    test_net_path = '{}/lenet_test.prototxt'.format(save_path)
    deploy_net_path = '{}/lenet_deploy.prototxt'.format(save_path)
    solver_file = '{}/lenet_solver.prototxt'.format(save_path)

    lmdb_data_path = args.data_dir
    train_lmdb_path = '{}/mnist_train_lmdb'.format(lmdb_data_path)
    test_lmdb_path = '{}/mnist_test_lmdb'.format(lmdb_data_path)

    lenet_snapshot_prefix = '{}/lenet'.format(save_path)

    # Generate net prototxt files
    with open(train_net_path, 'w') as f:
        f.write(str(lenet(train_lmdb_path, 64)))
    with open(test_net_path, 'w') as f:
        f.write(str(lenet(test_lmdb_path, 100, include_accuracy=True)))
    with open(deploy_net_path, 'w') as f:
        f.write(str(lenet(None, 1, deploy=True)))

    # Generate solver prototxt file
    s = caffe_pb2.SolverParameter()
    # Set a seed for reproducible experiments:
    # this controls for randomization in training.
    s.random_seed = 0xCAFFE
    # Specify locations of the train and (maybe) test networks.
    s.train_net = train_net_path
    s.test_net.append(test_net_path)
    s.test_interval = 500  # Test after every 500 training iterations.
    s.test_iter.append(100)  # Test on 100 batches each time we test.
    s.max_iter = args.max_iter  # no. of times to update the net (training iterations)
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


if __name__ == '__main__':
    train()
```

