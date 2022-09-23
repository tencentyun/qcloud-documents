PyTorch 是一个基于 Python 为接口的深度学习框架，允许用户利用 GPU 资源对矩阵进行运算，类似 numpy 中 Array 的运算，更多详细介绍可参考 [PyTorch](https://pytorch.org/) 文档。

## 运行版本说明
PyTorch 组件中使用的 Python 版本和支持的第三方模块版本信息如下：
```
Python version is [3,6]
scipy version is [1.0.0]
numpy version is [1.14.3]
```

若有需求使用其他第三方的 lib，可使用 pip 在代码内安装，示例如下：
```
import pip
pip.main(['install', "package_name"])
```

## 使用阶段
![](https://main.qcloudimg.com/raw/147085da4b8e4f5c869897da30fa4366.gif)

1. 从左侧导航中选择【组件】>【深度学习】，拖拽出 PyTorch 节点至画布中。

2. 参数配置
脚本及依赖包文件上传  

     将任务脚本上传至 __程序脚本__ 框。如果需要依赖文件，则压缩为zip文件后通过 __依赖包文件__ 框上传。

   - 程序依赖：指定位于 COS 中的用户依赖文件路径，指定内容将被拷贝到程序脚本同一级目录下。支持目录或者文件，若有多个文件以英文逗号分割 。

   - 程序参数：指定运行任务脚本的参数。

   - 资源参数：选择运行工作流使用的 GPU、CPU 等资源配置。

     ![](https://main.qcloudimg.com/raw/5d8d93a7dc5f447317d4bc95ba862d50.png)

3. 单击【保存】并运行工作流。

4. 查看 PyTorch 控制台和日志。
   在 PyTorch 节点上单击右键菜单可查看任务状态和详细日志。
   ![](https://main.qcloudimg.com/raw/50f89dab5a2369de70b2fd8937eb3075.png)
   ![](https://main.qcloudimg.com/raw/a9f7d66a87ea43259165dc2c9fceb7f2.png)

## 示例
以下代码展示了如何在 PyTorch 框架中，调用`torch.nn`构建一个典型神经网络(nn)。
输入：
```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 5x5 square convolution
        # kernel
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # If the size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
print(net)
```

输出：
```
Net(
  (conv1): Conv2d(1, 6, kernel_size=(5, 5), stride=(1, 1))
  (conv2): Conv2d(6, 16, kernel_size=(5, 5), stride=(1, 1))
  (fc1): Linear(in_features=400, out_features=120, bias=True)
  (fc2): Linear(in_features=120, out_features=84, bias=True)
  (fc3): Linear(in_features=84, out_features=10, bias=True)
)
```

示例代码下载：[pytorch_nn_example.py](https://tio.cloud.tencent.com/gitbook/doc/manual/attachments/pytorch_nn_example.py)

