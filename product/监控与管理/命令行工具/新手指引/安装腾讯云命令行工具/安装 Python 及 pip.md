Python 环境是腾讯云命令行工具运行时的必要环境。因此，请用户在使用命令行工具前确认是否本地计算机上已经安装了 Python 环境及 Pip 工具。

## Windows环境下安装 Python 和 Pip
登录 [Python 官方网站](https://www.python.org/downloads/)，下载 Python 2.7.x 版本，依照安装向导进行安装。

>!在安装 Python 时，请开启 pip，否则将无法进行腾讯云命令行工具的安装。

## Linux/Unix/MacOS环境下安装 Python 和 Pip
### 方法一：系统安装
1. Ubuntu 类系统使用以下命令安装。
```
$ sudo apt-get install python python-pip
```
2. CentOS、Redhat 类系统使用以下命令安装。
```
$ sudo yum install python python-pip
```

### 方法二：源码安装
1. 安装 Python。
```
$ wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
$ tar -zxvf Python-2.7.12.tgz
$ cd Python-2.7.12
$ ./configure
$ make
$ sudo make install
```
2. 安装 pip 工具。
```
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "pip-install.py"
$ sudo python pip-install.py
```
