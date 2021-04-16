## 操作场景
本文以使用 TencentOS Server 2.4 的云服务器为例，提供多个常用软件的安装步骤，您可参考本文进行相关软件安装。


## 操作步骤
<dx-alert infotype="explain" title="">
TencentOS Server 2 默认安装 tlinux-release 及 epel-release，其分别包含 tlinux.repo 和 epel.repo。
</dx-alert>

### 安装 docker-ce
1. 执行以下命令，安装 docker-ce 的源 tlinux-docker-ce.repo。
```
yum install tlinux-release-docker-ce
```
2. 执行以下命令，安装 docker-ce。
```
yum install docker-ce
```
如在安装过程中遇到以下问题，可按照对应方法进行处理：
 - 安装过程中遇到冲突，则需删除旧版本。请执行以下命令：
```
yum remove docker docker-client docker-engine docker-client-latest docker-latest
```
 - 安装完成后启动时遇到如下错误：
```
Error starting daemon:Error initializing network controller: list bridge addresses failed: no available network
```
则请依次执行以下命令后，重新启动 docker 即可。
```
sudo ip link add name docker0 type bridge
```
```
sudo ip addr add dev docker0 172.17.42.1/16
```

### 安装 gcc
1. 执行以下命令，安装 gcc updates 的源 tlinux-gcc-update.repo。
```
yum install tlinux-release-gcc-update
```
2. 依次执行以下命令，安装 gcc。
```
yum remove tlinux12-compat compat-gcc-44-c++
```
```
yum update gcc
```

### 安装 SCL（高版本软件）
1. 执行以下命令，安装 scl 的源 tlinux-sclo.repo。
```
yum install tlinux-release-scl
```
2. 本文以安装 gcc 为例，使用高版本软件仓库。请依次执行以下命令：
<dx-alert infotype="explain" title="">
安装路径为 `/opt/rh`。
</dx-alert>
```
yum install devtoolset-8-gcc
```
```
yum install devtoolset-8-gcc-c++
```
```
scl enable devtoolset-8 bash
```

### 安装 openresty
1. 执行以下命令，安装源 tlinux-openresty.repo。
```
yum install tlinux-release-openresty
```
2. 执行以下命令，安装 openresty。
```
yum install openresty
```

### 安装 pypi
1. 执行以下命令，安装 python-pip。
```
yum install python-pip 或 python2-pip 或 python3-pip
```
2. 将以下内容输入 `/etc/pip.conf` 配置文件中，即可使用腾讯软件源加速 pip。
```
[global]
index-url = https://mirrors.tencent.com/pypi/simple1. 
```

### 安装 ceph-fuse
1. 执行以下命令，安装源 tlinux-ceph.repo。
```
yum install tlinux-release-ceph
```
2. 执行以下命令，安装 ceph-fuse。
```
yum install ceph-fuse
```

### 安装 PostgreSQL
1. 执行以下命令，安装源 tlinux-pgdg.repo。
```
yum install tlinux-release-pgdg
```
2. 执行以下命令，安装 PostgreSQL。
```
yum install postgresql12
```

### 安装 Kubernetes
1. 创建 `/etc/yum.repos.d/kubernetes.repo` 文件，并执行以下命令。
```
cat << EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.tencent.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
EOF
```
2. 依次执行以下命令，即可安装 Kubernetes。
```
yum clean all
```
```
yum makecache
```
```
yum -y install kubelet kubeadm kubectl kubernetes-cni
```
```
systemctl enable kubelet && systemctl start kubelet
```

### 安装 Glusterfs-7
1. 执行以下命令，安装源文 tlinux-Gluster-7.repo。
```
yum install tlinux-release-gluster7
```
2. 执行以下命令，安装 glusterfs-server。
```
yum install glusterfs-server
```

### 安装 git-2.19
通过 tlinux-testing 源仓库可安装高版本软件包。本文以安装 git 2.19版本为例，适用于 TencentOS Server 2 for x86_64 和 arm64。执行以下命令，即可安装 git-2.19。
```
yum --enablerepo=tlinux-testing install git
```
