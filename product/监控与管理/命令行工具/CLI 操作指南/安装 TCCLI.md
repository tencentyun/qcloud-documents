## 操作场景
本文指导您如何安装 TCCLI。


## 前提条件
安装 Python 环境和 pip 工具，安装命令行工具前请确保您的系统已经安装了 Python 环境和 pip 工具。

>!python 版本必须为2.7及以上版本，更多内容请参考 [python](https://www.python.org/) 主页 和 [pip](https://pypi.org/project/pip/) 主页。

## 相关说明
TCCLI 依赖于 TencentCloudApi Python SDK，如果 TencentCloudApi Python SDK 的版本号小于要安装 TCCLI 版本号，在安装 TCCLI 时会自动升级 TencentCloudApi Python SDK。


## 操作步骤
1. 安装 TCCLI，执行以下命令：
```
pip install tccli
```
2. 安装完成之后，执行 tccli version 检测是否安装成功。
>?如果您的环境是 linux 环境，您可以通过以下命令启动自动补全功能：
`complete -C 'tccli_completer' tccli`
