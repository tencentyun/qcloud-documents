PyTorch 是一种基于 Python 为接口的深度学习框架，允许用户利用 GPU 资源对矩阵进行运算，类似 numpy 中 Array 的运算，更多详细介绍可参考 [PyTorch 文档](https://pytorch.org/)。

## 版本说明
PyTorch 组件中使用的 Python 版本和支持的第三方模块版本信息如下：
- Python 3.6
- SciPy 1.0.0
- NumPy 1.14.3

如果您需要使用其他第三方的 lib，可使用 pip 在代码内安装，示例如下：
```
import pip
pip.main(['install', "package_name"])
```

## 操作步骤
1. **添加组件**
从左侧菜单栏中，选择【组件】>【深度学习】列表下的 PyTorch 节点，将其拖拽至画布中。
2. **配置参数**
- 脚本及依赖包文件上传：
  将任务脚本上传至程序脚本框。如果需要依赖文件，则压缩为 zip 文件后通过 依赖包文件 框上传。
![](https://main.qcloudimg.com/raw/f502e40c73117cfddef50af122cec760.png)
- 程序依赖：
指定位于 COS 中的用户依赖文件路径，指定内容将被拷贝到程序脚本同一级目录下。支持目录或者文件依赖，若存在多个文件则以英文逗号分隔 。
- 程序参数：
指定运行任务脚本的参数。
![](https://main.qcloudimg.com/raw/274c8424f7cd3c1c77917039890a2119.png)
3. **配置资源**
在【资源参数】列表框配置任务的资源参数。
![](https://main.qcloudimg.com/raw/3c14b0568ea191bcdf63219619b07c73.png)
4. **运行**
单击【保存】并运行工作流。
5. **查看 PyTorch 控制台和日志**
在 PyTorch 节点上单击右键菜单可查看任务状态和详细日志。
![](https://main.qcloudimg.com/raw/8624254d83e02991dcf1cb3e1ff47367.png)
详细日志如下：
![](https://main.qcloudimg.com/raw/d9339d4a8d678627a8ebf1dbc0275b4e.png)
>?stdout.log 为全部日志，stderr.log 为错误日志。



## 示例
以下代码展示了在 PyTorch 框架中，调用 torch.nn 构建一个典型神经网络（NN）的方法。
输入：
```
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




