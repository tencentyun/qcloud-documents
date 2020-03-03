
本文档以 Python 2.7 版本为例，详细介绍在 Windows 和 Linux 系统下， Python 的安装与环境配置过程。

## Windows 
#### 1. 下载
进入 [ Python 官网](https://www.python.org/downloads/) 选择合适的版本下载，本示例中我们选择下载 [Python 2.7.13](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi) 版本。

#### 2. 安装
下载好 Python 安装包后，双击 Python 安装包，按照默认提示，一步步进行安装。

#### 3. 环境变量配置
安装完成后，右键单击【计算机】>【属性】>【高级系统设置】>【环境变量】>【系统变量(S)】 找到 “Path” （若无该变量，则新建），并在“变量值”末尾添加 Python 的安装路径：`;C:\Python27`（请更改为您实际的安装路径），单击【确定】保存。
![161709](//mc.qcloudimg.com/static/img/b5784ed03d0f2fd07195c9c3ae1e5075/image.png)

#### 4. 测试配置是否成功
单击【开始】（或快捷键：Win+R）>【运行】（输入 cmd）>【确定】（或者按 Enter 键），在弹出的窗口中输入命令 Python 并回车。若出现如图信息，则说明 Python 2.7 安装成功：
![152355](//mc.qcloudimg.com/static/img/026d7738b234171b285a98f0e751038a/image.png)

## Linux
#### 1. 查看 Python 版本 
Linux 的 yum 自带 Python，首先查看默认 Python 版本。
```sh
python -V
``` 
若已经是 Python 2.7 及以上版本，则忽略以下步骤，否则（此处假设现有版本为 Python 2.6.6），输入以下命令：
```sh
yum groupinstall "Development tools"
```

#### 2. 安装编译 Python 需要的组件
```sh
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel
```

#### 3. 下载并解压 Python 2.7 
```sh
wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz
tar xf Python-2.7.12.tar.xz
```

#### 4. 编译与安装 Python
```
cd Python-2.7.12 //进入目录
./configure -prefix=/usr/local
make && make install  //安装
make clean 
make distclean
```

#### 5. 将系统 Python 命令指向 Python 2.7
```shell
mv /usr/bin/python /usr/bin/python2.6.6
ln -s /usr/local/bin/python2.7 /usr/bin/python
```

#### 6. 测试配置是否成功
```sh
python
```
若出现如图信息，则说明 Python 2.7 安装成功：
![112046](//mc.qcloudimg.com/static/img/0eb560566c1f67e302e75b1dcb515d98/image.png)

>!如果出现权限的问题，建议在命令前添加 sudo 尝试解决。
