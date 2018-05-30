黑石官方镜像默认不带 GPU 驱动，请参考本文指引快速安装 GPU 驱动。  

## Linux 系列安装指引
#### 操作步骤：
1. 根据服务器型号和 OS 版本，选择安装脚本。

2. 登录服务器，新建文件粘贴脚本代码。

3. 运行脚本。

4. 检查是否安装成功。

### 工具准备
Xshell、PuTTY 等远程登录工具。

### 选择安装脚本
请根据 OS 版本、GPU 型号以及开发习惯选择 CUDA toolkit。Nvida 官方提供的 CUDA toolkit 和 GPU 卡的兼容列表，请参考 [Nvidia 官网文档](http://www.nvidia.com/Download/index.aspx?lang=cn "Nvidia官网文档")。

#### CentOS 6.5，CUDA toolkit 9

```
#!/bin/bash
# install m40 cuda for centos6
# version 0.1: haleyhuang
# result
#       0       OK
#       1       install fail

date

wget http://mirrors.tencentyun.com/install/monitor_bm/cuda-repo-rhel6-9-0-local-9.0.176-1.x86_64.rpm && \
wget http://mirrors.tencentyun.com/install/monitor_bm/kernel-devel-2.6.32-573.18.1.el6.x86_64.rpm && \
wget http://mirrors.tencentyun.com/install/monitor_bm/kernel-headers-2.6.32-573.18.1.el6.x86_64.rpm
if [ $? -ne 0 ]; then
    echo "can't wget cuda!!!"
    exit 1
fi

yum remove -y kernel-headers && yum remove -y kernel-devel

rpm -i kernel-headers-2.6.32-573.18.1.el6.x86_64.rpm && \
rpm -i kernel-devel-2.6.32-573.18.1.el6.x86_64.rpm && \
rpm -i cuda-repo-rhel6-9-0-local-9.0.176-1.x86_64.rpm && \
yum clean all && \
yum install -y cuda
if [ $? -ne 0 ]; then
    echo "cuda install fail!!!"
    exit 1
fi

# for cuda env
echo $PATH | grep cuda
if [ $? -ne 0 ]; then
    echo 'export PATH=/usr/local/cuda/bin:$PATH' >> /etc/profile
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> /etc/profile
fi

rm -f cuda-repo-rhel6-9-0-local-9.0.176-1.x86_64.rpm
rm -f kernel-headers-2.6.32-573.18.1.el6.x86_64.rpm
rm -f kernel-devel-2.6.32-573.18.1.el6.x86_64.rpm

sync
sync

echo "cuda installed successfully"
echo "cuda installed successfully"
exit 0

```

#### CentOS 7.2，CUDA toolkit 9

```
#!/bin/bash
# install m40 cuda for centos7
# version 0.1: haleyhuang
# result
#       0       OK
#       1       install fail

lsmod | grep mlx4_en
if [ $? -eq 0 ]; then
    echo 'install igb modprobe mlx4_en; modprobe --ignore-install igb' > /etc/modprobe.d/mlx4_en.conf
fi

wget http://mirrors.tencentyun.com/install/monitor_bm/cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64.rpm && \
wget http://mirrors.tencentyun.com/install/monitor_bm/kernel-devel-3.10.0-327.el7.x86_64.rpm
if [ $? -ne 0 ]; then
    echo "can't wget cuda!!!"
    exit 1
fi

rpm -i kernel-devel-3.10.0-327.el7.x86_64.rpm && \
rpm -i cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64.rpm && \
yum clean all && \
yum install -y cuda
if [ $? -ne 0 ]; then
    echo "cuda install fail!!!"
    exit 1
fi

# for cuda env
echo $PATH | grep cuda
if [ $? -ne 0 ]; then
    echo 'export PATH=/usr/local/cuda/bin:$PATH' >> /etc/profile
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> /etc/profile
fi

rm -f cuda-repo-rhel7-9-0-local-9.0.176-1.x86_64.rpm
rm -f kernel-devel-3.10.0-327.el7.x86_64.rpm

sync
sync

echo "cuda installed successfully"
echo "cuda installed successfully"
exit 0
```

#### Ubuntu 14，CUDA toolkit 8

```
#!/bin/bash
# install m40 cuda for ubuntu14
# version 0.1: haleyhuang
# result
#       0       OK
#       1       install fail

date
# fixed grub bug
sed -i 's/set -e$/set -e;exit 0/g'  /var/lib/dpkg/info/grub-efi-amd64.postinst

apt-get update

dpkg --configure -a
apt-get -f -y install

lsmod | grep mlx4_en
if [ $? -eq 0 ]; then
    echo 'install igb modprobe mlx4_en; modprobe --ignore-install igb' > /etc/modprobe.d/mlx4_en.conf
fi

wget http://mirrors.tencentyun.com/install/monitor_bm/cuda-repo-ubuntu1404-8-0-local-ga2_8.0.61-1_amd64.deb
if [ $? -ne 0 ]; then
    echo "can't wget cuda!!!"
    exit 1
fi

wget http://mirrors.tencentyun.com/install/monitor_bm/cuda-repo-ubuntu1404-8-0-local-cublas-performance-update_8.0.61-1_amd64.deb
if [ $? -ne 0 ]; then
    echo "can't wget cuda patch!!!"
    exit 1
fi
 
dpkg -i cuda-repo-ubuntu1404-8-0-local-ga2_8.0.61-1_amd64.deb && \
apt-get update && apt-get install -y cuda && \
dpkg -i cuda-repo-ubuntu1404-8-0-local-cublas-performance-update_8.0.61-1_amd64.deb
if [ $? -ne 0 ]; then
    echo "cuda install fail!!!"
    exit 1
fi

# for cuda env
echo $PATH | grep cuda
if [ $? -ne 0 ]; then
    echo 'export PATH=/usr/local/cuda/bin:$PATH' >> /etc/profile
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> /etc/profile
fi

rm -f cuda-repo-ubuntu1404-8-0-local-ga2_8.0.61-1_amd64.deb
rm -f cuda-repo-ubuntu1404-8-0-local-cublas-performance-update_8.0.61-1_amd64.deb

sync
sync

echo "cuda installed successfully"
echo "cuda installed successfully"
exit 0
```

#### Ubuntu 16，CUDA toolkit 8

```
#!/bin/bash
# install p40 cuda for ubuntu16
# version 0.1: haleyhuang
# result
#       0       OK
#       1       install fail
#       2       configure fail
#       3       others

date

apt-get update
dpkg --configure -a
apt-get -f -y install

lsmod | grep mlx4_en
if [ $? -eq 0 ]; then
    echo 'install igb modprobe mlx4_en; modprobe --ignore-install igb' > /etc/modprobe.d/mlx4_en.conf
fi

wget http://mirrors.tencentyun.com/install/monitor_bm/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
if [ $? -ne 0 ]; then
    echo "can't wget cuda!!!"
    exit 1
fi

wget http://mirrors.tencentyun.com/install/monitor_bm/cuda-repo-ubuntu1604-8-0-local-cublas-performance-update_8.0.61-1_amd64.deb
if [ $? -ne 0 ]; then
    echo "can't wget cuda patch!!!"
    exit 1
fi
 
dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb && \
apt-get update && apt-get install -y cuda && \
dpkg -i cuda-repo-ubuntu1604-8-0-local-cublas-performance-update_8.0.61-1_amd64.deb
if [ $? -ne 0 ]; then
    echo "cuda install fail!!!"
    exit 1
fi

# for cuda env
echo $PATH | grep cuda
if [ $? -ne 0 ]; then
    echo 'export PATH=/usr/local/cuda/bin:$PATH' >> /etc/profile
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> /etc/profile
fi

rm -f cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
rm -f cuda-repo-ubuntu1604-8-0-local-cublas-performance-update_8.0.61-1_amd64.deb

sync
sync

echo "cuda installed successfully"

exit 0
```

### 运行脚本
修改脚本的可执行权限：
```
chmod +x xxxxx.sh
```
执行脚本，若出现以下提示，则表示脚本安装成功：
```
cuda installed successfully
```

### 检验驱动是否安装成功
在`/usr/local/cuda/samples/1_Utilities/deviceQuery`目录下，执行 make 命令，可以编译出 deviceQuery 程序。
执行 deviceQuery 正常，则显示如下设备信息，表示 CUDA 安装正确。
![](https://mc.qcloudimg.com/static/img/d545951dc869591d83bf23e27831287a/image.jpg)

## Windows 系列安装指引
本教程适用于以下条件下的安装：
- 机型：PG103v2
- 操作系统版本： Windwos SERVER 2012 R2
- CUDA 版本：CUDA_9.1.85

其他条件下的安装请参考 [Nvdia 官网](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)。  

### 工具准备
高于 2012 版本的 Visual Studio。

### 运行脚本下载驱动
新建 POWERSHELL 脚本，键入以下代码。右键 RUN WITH POWERSHELL 执行：
```
$client = new-object System.Net.WebClient
$client.DownloadFile('http://mirrors.tencentyun.com/install/monitor_bm/cuda_9.1.85_windows.exe','.\cuda_9.1.85_windows.exe')
$client.DownloadFile('http://mirrors.tencentyun.com/install/monitor_bm/cuda_9.1.85.1_windows.exe','.\cuda_9.1.85.1_windows.exe')
$client.DownloadFile('http://mirrors.tencentyun.com/install/monitor_bm/cuda_9.1.85.2_windows.exe','.\cuda_9.1.85.2_windows.exe')
$client.DownloadFile('http://mirrors.tencentyun.com/install/monitor_bm/cuda_9.1.85.3_windows.exe','.\cuda_9.1.85.3_windows.exe')
```

### 安装 CUDA 驱动
安装需要访问外网，请提前绑定好弹性公网 IP。以下文件请依次安装，CUDA_9.1.85 为主要安装程序，其余为补丁
- cuda\_9.1.85\_windows.exe
- cuda\_9.1.85.1\_windows.exe
- cuda\_9.1.85.2\_windows.exe
- cuda\_9.1.85.3\_windows.exe

### 验证是否安装成功
1. 进入目录
```
c:\ProgramData\NVIDIA Corporation\CUDA Samples\v9.1\1_Utilities\deviceQuery
```

2. 打开文件夹内的 Visual Studio 工程。

3. 编译运行后，出现如下图示现象，即证明安装成功。
![]( https://main.qcloudimg.com/raw/813fe93e57615ebf0d42bda71fdc0c86.jpg)
