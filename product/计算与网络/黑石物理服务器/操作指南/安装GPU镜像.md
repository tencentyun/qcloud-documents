黑石官方支持的镜像默认不带GPU驱动，当你拿到黑石GPU服务器时,请依本文指引快速安装GPU驱动
  


## 工具准备
Xshell,PuTTY 等远程登录工具

## 操作步骤
根据服务器型号和OS版本，确定安装脚本

登录服务器，新建文件保存脚本代码

运行脚本

校验是否能查看到GPU卡

## 安装脚本

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

\# for cuda env
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