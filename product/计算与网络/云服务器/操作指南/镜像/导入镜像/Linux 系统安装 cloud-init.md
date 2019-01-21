cloud-init 主要提供实例首次初始化时自定义配置的能力。如果导入的镜像没有安装 cloud-init 服务，基于该镜像启动的实例将无法被正常初始化，导致该镜像导入失败。
安装 cloud-init 有以下两种方式：
- 通过 [手工下载 cloud-init 源码包方式](#ManualDown) 
- 通过 [使用软件源上的 cloud-init 包方式](#SoftSources)

>! 在导入 Linux 系统镜像前，请确保您的镜像内部已正确安装了 cloud-init 服务。

<span id="ManualDown"></span>
## 手工下载 cloud-init 源码包方式

### 前提条件

安装 cloud-init 的服务器可正常访问外网。

### 下载 cloud-init 源码包
1. cloud-init 源码包：[点此获取](https://launchpad.net/cloud-init/+download)，建议选择 **cloud-init-17.1.tar.gz** 安装版本。
>?   cloud-init-17.1 版本与腾讯云的兼容性最佳。在正常安装的情况下，可以保证使用该镜像创建的云服务器的所有配置项都可以正常初始化。
2. 执行以下命令，下载 cloud-init 源码包。
```
wget https://launchpad.net/cloud-init/trunk/17.1/+download/cloud-init-17.1.tar.gz
```

### 安装 cloud-init
1. 执行以下命令，解压 cloud-init 安装包。
```
tar -zxvf cloud-init-17.1.tar.gz 
```
2. 执行以下命令，安装 Python-pip。
 ```
yum install python-pip -y
```
3. 执行以下命令，安装依赖包。
>!  cloud-init 依赖组件 requests 2.20.0版本后，已弃用 Python2.6。如果镜像环境的 Python 解释器为 Python2.6及以下，在安装 cloud-init 依赖包之前，请执行以下命令，安装 requests 2.20.0 版本以下的版本。
```
pip install 'requests<2.20.0'
```

 ```
pip install -r cloud-init-17.1/requirements.txt
```
4. 根据操作系统版本，安装 cloud-utils 组件。
 - Centos 6系列，执行以下命令：
```
yum install cloud-utils-growpart dracut-modules-growroot -y
dracut -f
```
 - Centos 7系列，执行以下命令：
```
yum install cloud-utils-growpart -y
```
 - Ubuntu 系列，执行以下命令：
```
apt-get install cloud-guest-utils -y
```
5. 执行以下命令，安装 cloud-init。
```
python setup.py build
python setup.py install --init-system systemd
```
>! --init-system 的可选参数有：(systemd, sysvinit,  sysvinit_deb, sysvinit_freebsd, sysvinit_openrc, sysvinit_suse, upstart)  [default: None]。请根据当前操作系统使用的自启动服务管理方式，进行选择。若选择错误，cloud-init 服务会无法开机自启动。本文以 systemd 自启动服务管理为例。

### 修改 cloud-init 配置文件

1. 根据不同操作系统，下载 cloud.cfg。
 - [ubuntu 操作系统的 cloud.cfg](http://cloudinit-1251783334.cosgz.myqcloud.com/ubuntu-cloud.cfg)
 - [centos 操作系统的 cloud.cfg](http://cloudinit-1251783334.cosgz.myqcloud.com/centos-cloud.cfg)
 - 其他操作系统待补充
2. 将 `/etc/cloud/cloud.cfg` 的内容替换为已下载的 cloud.cfg 文件内容。

### 添加 syslog 用户
执行以下命令，添加 syslog 用户。
```
useradd syslog
```

### 设置 cloud-init 服务开机自启动
- **若操作系统是 systemd 自启动管理服务，则执行以下命令进行设置。**
 1) **针对 ubuntu 或 debian 操作系统，需执行以下命令。**
```
 ln -s /usr/local/bin/cloud-init /usr/bin/cloud-init 
```
 2) **所有操作系统都需执行以下命令。**
```
systemctl enable cloud-init-local.service 
systemctl start cloud-init-local.service
systemctl enable cloud-init.service
systemctl start cloud-init.service
systemctl enable cloud-config.service
systemctl start cloud-config.service
systemctl enable cloud-final.service
systemctl start cloud-final.service
systemctl status cloud-init-local.service
systemctl status cloud-init.service
systemctl status cloud-config.service
systemctl status cloud-final.service
```
 3) **针对 centos 和 redhat 操作系统，需执行以下命令。**
 将 /lib/systemd/system/cloud-init-local.service 文件替换为如下内容：
```
[Unit]
Description=Initial cloud-init job (pre-networking)
Wants=network-pre.target
After=systemd-remount-fs.service
Before=NetworkManager.service
Before=network-pre.target
Before=shutdown.target
Conflicts=shutdown.target
RequiresMountsFor=/var/lib/cloud
[Service]
Type=oneshot
ExecStart=/usr/bin/cloud-init init --local
ExecStart=/bin/touch /run/cloud-init/network-config-ready
RemainAfterExit=yes
TimeoutSec=0
# Output needs to appear in instance console output
StandardOutput=journal+console
[Install]
WantedBy=cloud-init.target
```
将 /lib/systemd/system/cloud-init.service 文件替换为以下内容：
```
[Unit]
Description=Initial cloud-init job (metadata service crawler)
Wants=cloud-init-local.service
Wants=sshd-keygen.service
Wants=sshd.service
After=cloud-init-local.service
After=systemd-networkd-wait-online.service
After=networking.service
After=systemd-hostnamed.service
Before=network-online.target
Before=sshd-keygen.service
Before=sshd.service
Before=systemd-user-sessions.service
Conflicts=shutdown.target
[Service]
Type=oneshot
ExecStart=/usr/bin/cloud-init init
RemainAfterExit=yes
TimeoutSec=0
# Output needs to appear in instance console output
StandardOutput=journal+console
[Install]
WantedBy=cloud-init.target
```
- **若操作系统是 sysvinit 自启动管理服务，则执行以下命令进行设置。**
```
chkconfig --add cloud-init-local
chkconfig --add cloud-init
chkconfig --add cloud-config
chkconfig --add cloud-final
chkconfig cloud-init-local on 
chkconfig cloud-init on 
chkconfig cloud-config on 
chkconfig cloud-final on 
```

<span id="SoftSources"></span>
## 使用软件源上的 cloud-init 包方式

### 安装 cloud-init

执行以下命令，安装 cloud-init。
```
apt-get/yum install cloud-init
```
>? 通过 apt-get 或 yum 命令安装的 cloud-init 默认为当前操作系统配置的软件源中默认的 cloud-init 版本。使用该方式安装的镜像创建的实例可能会存在部分配置项初始化不符合预期的情况，建议使用 [手工下载 cloud-init 源码包方式]() 进行安装。

### 修改 cloud-init 配置文件
1. 根据不同操作系统，下载 cloud.cfg。
 - [ubuntu 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/ubuntu-cloud.cfg)
 - [centos 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/centos-cloud.cfg)
 - 其他操作系统待补充
2. 将 `/etc/cloud/cloud.cfg` 的内容替换为已下载的 cloud.cfg 文件内容。

## 安装 cloud-init 后的相关操作
>! 以下操作执行完成后，请勿重启服务器。否则需重新执行下以下操作。

1. 执行以下命令，检查 cloud-init 相关配置是否成功。
```
cloud-init init --local
rm -rf /var/lib/cloud
```
2. 针对 ubuntu 或 debian 操作系统，需执行以下命令。
```
rm -rf /etc/network/interfaces.d/50-cloud-init.cfg
```
3. 针对 ubuntu 或 debian 操作系统，需将 `/etc/network/interfaces` 修改为以下内容：
```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
source /etc/network/interfaces.d/*
```
