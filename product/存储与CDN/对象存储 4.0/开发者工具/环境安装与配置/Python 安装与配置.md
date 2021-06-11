本文档简要介绍在不同操作系统下，Python 开发环境的安装方法

## 通过官方网站提供的安装包安装

### 1. 下载：
进入 [Python官方网站](https://www.python.org/downloads/) ，根据自己使用的操作系统，选择合适的安装包下载。

> Python 官方已经与2020年1月1日停止了对 Python2 的维护，建议安装使用 Python3。

### 2. 安装：
下载安装包后，根据安装包的引导即可完成 Python 开发环境的安装。

### 3. 验证：
在终端中执行以下命令查看 Python 版本：
```shell
python -V
```
若终端输出 Python 版本号则证明安装成功。

> 在 Windows 系统中，若在执行以上命令时终端提示"不是内部或外部命令"，
> 请在【计算机】>【属性】>【高级系统设置】>【环境变量】>【系统变量(S)】中编辑"Path"，
> 增加 Python 和 pip 的安装路径

## 通过包管理器安装

### Mac OS:
使用 Mac OS 的用户可以先安装 [HomeBrew](https://brew.sh/index_zh-cn) ，然后通过 HomeBrew 来安装 Python ：
```shell
brew install python
```

### Ubuntu:
使用 Ubuntu 的用户可以使用 Ubuntu 自带的 apt（Advanced Packaging Tool） 包管理器来安装 Python：
```shell
sudo apt-get install python
```

### CentOS:
使用 CentOS 的用户可以使用 CentOS 自带的 yum（Yellow dog Updater, Modified） 包管理器来安装 Python：
```shell
sudo yum install -y python
```
