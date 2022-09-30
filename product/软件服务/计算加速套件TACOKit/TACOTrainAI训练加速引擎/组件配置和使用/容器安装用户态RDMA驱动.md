## 操作场景
本文介绍如何为容器安装用户态 RDMA 驱动。


## 操作步骤

<dx-alert infotype="explain" title="">
本文以 Ubuntu 20.04 操作系统的机器为例。
</dx-alert>



1. 执行以下命令，下载对应容器中的 OS 版本的 MLNX OFED 驱动。
```plaintext
wget https://www.mellanox.com/downloads/ofed/MLNX_OFED-5.4-3.1.0.0/MLNX_OFED_LINUX-5.4-3.1.0.0-ubuntu20.04-x86_64.tgz
```
若您使用了其他版本操作系统，则请访问 [Linux InfiniBand Drivers](https://network.nvidia.com/products/infiniband-drivers/linux/mlnx_ofed/) 下载对应的版本。选择步骤如下图所示：
<dx-alert infotype="notice" title="">
OFED 版本选择`5.4-3.1.0.0`。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/ee47027a8c0e7a25e1ef29c69c4cc2ed.png" width="918px"/>
2. 依次执行以下命令，进行解压及安装。
```plaintext
tar xf MLNX_OFED_LINUX-5.4-3.1.0.0-ubuntu20.04-x86_64.tgz
```
```plaintext
cd MLNX_OFED_LINUX-5.4-3.1.0.0-ubuntu20.04-x86_64
```
```plaintext
./mlnxofedinstall --user-space-only --without-fw-update --force
```
安装过程中出现的红色 warning 信息可忽略，直至页面出现 “Installation passed successfully” 绿色字样，表示安装成功。

## 相关操作
若您在安装过程中出现如下图所示错误：
<img src="https://qcloudimg.tencent-cloud.cn/raw/02451f555785db6819bed7c6e3d43512.png" width="918px"/>
请参考以下步骤处理：
1. 由于 neohost 需要依赖 python2，执行以下命令，修改系统默认的 python 版本。
```plaintext
ln -sf /usr/bin/python2.7 /usr/bin/python
```
2. 执行以下命令，确认 python 版本。
```plaintext
python --version
```
如果提示找不到 python 命令，则需要安装 python2.7。
3. 执行以下命令，重新安装 ofed。
```plaintext
./mlnxofedinstall --user-space-only --without-fw-update --force
```
4. 执行以下命令，恢复 python3 作为默认 python 版本。
```plaintext
update-alternatives --install /usr/bin/python python /usr/bin/python3 1
```
