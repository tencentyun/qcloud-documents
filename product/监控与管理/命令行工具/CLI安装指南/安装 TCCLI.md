本文指导您如何安装 TCCLI。

## 前提条件

安装 Python 环境和 pip 工具，安装命令行工具前请确保您的系统已经安装了 Python 环境和 pip 工具。

>!
>- Python 版本必须为2.7及以上版本，更多内容请参考 [Python](https://www.python.org/) 和 [pip](https://pypi.org/project/pip/) 官网文档。
>- TCCLI 依赖于 TencentCloudApi Python SDK，如果 TencentCloudApi Python SDK 的版本号小于要安装 TCCLI 版本号，在安装 TCCLI 时会自动升级 TencentCloudApi Python SDK。
>



## 操作步骤

### 方式一：使用pip工具进行安装（推荐）

1. Windows 系统按 Win+R 打开运行窗口输入 cmd 并单击【确定】，本文以 Linux 为例。
2. 在命令行窗口中，执行以下命令进行 TCCLI 安装。
```bash
pip install tccli
```
 >!如果您是从3.0.252.3以下版本进行升级，需要执行以下命令：
>```bash
sudo pip uninstall tccli jmespath
sudo pip install tccli
```
3. 安装完成之后，执行以下命令，检测是否安装成功。
```bash
tccli --version
```
### 方式二：使用源码进行安装

在[Github](https://github.com/TencentCloud/tencentcloud-cli)仓库中下载TCCLI项目，执行setup.py脚本进行安装
```bash
git clone https://github.com/TencentCloud/tencentcloud-cli.git
cd tencentcloud-cli
python setup.py install
```

### 方式三：使用Homebrew进行安装

>! 该方法只适用于 mac OS 系统。您需要先安装homebrew，可以参考[homebrew官网](https://brew.sh/index_zh-cn)进行安装。

使用如下命令安装TCCLI：
```bash
brew install tccli
```
您可以使用如下命令对TCCLI进行更新：
```bash
brew upgrade
```