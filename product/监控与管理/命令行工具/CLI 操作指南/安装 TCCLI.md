本文指导您如何安装 TCCLI。

## 前提条件

安装 Python 环境和 pip 工具，安装命令行工具前请确保您的系统已经安装了 Python 环境和 pip 工具。

>! Python 版本必须为2.7及以上版本，更多内容请参考 [Python](https://www.python.org/) 和 [pip](https://pypi.org/project/pip/) 官网文档。



## 操作步骤

1. 安装 TCCLI，执行以下命令：
```sh
pip install tccli
```
>!如果您是从3.0.252.3以下版本进行升级，需要执行以下命令：
> ```bash
> sudo pip uninstall tccli jmespath
> sudo pip install tccli
> ```

2. 安装完成之后，执行以下命令，检测是否安装成功。
```bash
tccli --version
```

#### 命令补全

如果您的环境是 Linux 环境，您可以通过以下命令启动自动补全功能：
```plaintext
complete -C 'tccli_completer' tccli
```
也可以将该命令加入环境变量（`/etc/profile`）中，使自动补全功能一直有效。
