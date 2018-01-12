黑石官方支持的镜像默认不带GPU驱动，请依本文指引快速安装GPU驱动  


## 工具准备
Xshell,PuTTY 等远程登录工具

## 操作步骤
根据服务器型号和OS版本，选择安装脚本

登录服务器，新建文件粘贴脚本代码

运行脚本

检查是否安装成功

## 选择安装脚本
请根据OS版本、GPU 型号以及开发习惯选择 CUDA toolkit。Nvida官方提供的CUDA toolkit 和GPU卡的兼容列表，请参考
[Nvidia官网文档](http://www.nvidia.com/Download/index.aspx?lang=cn "Nvidia官网文档")

 

### CentOs6.5,CUDA toolkit 9

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

### CentO7.2,CUDA toolkit 9

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

### Ubuntu14、CUDA toolkit 8
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


### Ubuntu16、CUDA toolkit 8
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

## 运行脚本
修改脚本的可执行权限， chmod +x xxxxx.sh <br/>
执行脚本，如果提示：`cuda installed successfully` ，则表示安装成功。

## 检验是否安装成功
在 /usr/local/cuda/samples/1_Utilities/deviceQuery 目录下，执行 make 命令，可以编译出 deviceQuery 程序。<br/>
执行 deviceQuery 正常显示如下设备信息，此刻认为 CUDA 安装正确。

![](https://mc.qcloudimg.com/static/img/d545951dc869591d83bf23e27831287a/image.jpg)