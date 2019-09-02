## 现象描述
使用 GPU 计算型实例的过程中，在系统内部使用 `nvidia-smi` 查看 GPU 状态时，可能遇到没有运行任何使用 GPU 的应用，但 GPU 使用率显示100%的情况。如下图所示：
![](//mc.qcloudimg.com/static/img/5a58bc996b38c28b94131105a3fbd000/image.png)
## 可能原因
实例加载 NVIDIA 驱动时，ECC Memory Scrubbing 机制造成。
## 解决思路
在实例系统内执行 `nvidia-smi -pm 1` 命令，让 GPU Driver 进入 Persistence 模式。
## 处理步骤
1. 登录 GPU 计算型实例，执行以下命令：
```
nvidia-smi -pm 1
```
![](//mc.qcloudimg.com/static/img/456d59df82aa68c243b6073bfe63f490/image.png)
2. 执行以下命令，检查 GPU 使用率：
```
nvidia-smi
```
GPU 使用率正常，如下图所示：
![](//mc.qcloudimg.com/static/img/460c515a0a7ac32b4c525b759e13c732/image.png)
