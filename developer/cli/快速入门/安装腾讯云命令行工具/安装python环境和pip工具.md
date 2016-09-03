##安装python环境和pip工具
###windows环境
登录到Python 官方网站（https://www.python.org/downloads/，下载 Python 2.7.x 版本，依照安装向导进行安装。
注意：在安装 Python 时，请开启 pip，否则将无法进行腾讯云命令行工具的安装。
###Linux Unix MacOS环境
####方法一，直接安装
1.ubuntu类系统使用以下命令安装
```
$ sudo apt-get install python python-pip
```
2.centos、redhat类系统使用以下命令安装
```
$ sudo yum install python python-pip
```
####方法二,源码安装
1.安装python
```
$ wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
$ tar -zxvf Python-2.7.12.tgz
$ cd Python-2.7.12
$ ./configure
$ make
$ sudo make install
```
2.安装pip工具
```
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "pip-install.py"
$ sudo python pip-install.py
``