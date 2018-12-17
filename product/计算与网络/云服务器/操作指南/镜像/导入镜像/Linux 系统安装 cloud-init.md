cloud-init 主要提供实例首次初始化时自定义配置的能力。如果导入的镜像没有安装 cloud-init 服务，基于该镜像启动的实例将无法被正常初始化，导致该镜像导入失败。
安装 cloud-init 的方式有两种，包括 **手工下载 cloud-init 源码包安装** 和 **直接使用软件源 cloud-init 包安装**。
在导入 Linux 系统镜像前，请确保您的镜像内部已正确安装了 cloud-init 服务。
## 手工下载 cloud-init 源码包安装
### 一. 前提条件
安装 cloud-init 的云服务器能访问外网。

### 二. 下载 cloud-init 源码包
使用以下命令下载 cloud-init 源码包，官网下载地址：https://launchpad.net/cloud-init/+download
```
wget https://launchpad.net/cloud-init/trunk/17.1/+download/cloud-init-17.1.tar.gz
```
> **注意：**
> 建议安装版本： cloud-init-17.1.tar.gz
> cloud-init-17.1 版本与腾讯云的兼容性最好，在正常安装的情况下可以保证使用该镜像创建出来的云服务器所有配置项都能够正常初始化。


### 三. 安装 cloud-init
#### 3.1 安装 cloud-init 依赖包
cloud-init 依赖包如下：
```
setuptools  
jinja2  
prettytable  
oauthlib  
configobj  
pyyaml  
requests  
jsonpatch  
jsonschema  
six
```
- Python-pip 安装命令，推荐使用 Python-pip 安装以上依赖包：
```
yum install python-pip -y
```
- 使用 pip 安装依赖包：
```
pip install setuptools jinja2 prettytable oauthlib pyyaml requests jsonpatch jsonschema six
```

#### 3.2 解压并安装
运行以下命令：
```
tar -zxvf cloud-init-17.1.tar.gz 
cd ./cloud-init-17.1
python setup.py build
python setup.py install --init-system systemd
```
其中，--init-system 的可选参数有：(systemd，sysvinit，sysvinit_deb，sysvinit_freebsd，sysvinit_openrc，sysvinit_suse，upstart)；[default: None]，需要根据当前操作系统使用的自启动服务管理方式是什么进行选择，**如果选择出错则 cloud-init 服务无法开机自启动**，本例以 systemd 自启动服务管理为例。

#### 3.3 修改 cloud-init 配置文件
根据不同操作系统，从以下链接下载 cloud.cfg，将`/etc/cloud/cloud.cfg`的内容进行替换。
> * [Ubuntu 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/ubuntu-cloud.cfg)
> * [CentOS 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/centos-cloud.cfg)
> * 其他操作系统待补充

#### 3.4 添加 syslog 用户
```
useradd syslog
```

#### 3.5 设置 cloud-init 服务开机自启动
**若操作系统是 systemd 自启动管理服务：**
- Ubuntu 或 Debian 操作系统特殊执行：
```
ln -s /usr/local/bin/cloud-init /usr/bin/cloud-init 
```
- 所有操作系统都执行：
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
- CentOS 和 Red Hat 操作系统特殊执行：
将`/lib/systemd/system/cloud-init-local.service`文件内容替换为如下：

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
将`/lib/systemd/system/cloud-init.service`文件内容替换为如下：
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
**若操作系统是 sysvinit 自启动管理服务：**
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

## 直接使用软件源 cloud-init 包安装
1. 执行以下安装命令进行安装：
```
apt-get/yum install cloud-init
```
> **注意：**
>  直接通过 apt-get 或 yum 命令安装的 cloud-init 为当前操作系统配置的软件源默认的 cloud-init 版本。通常情况下和 cloud-init 17.1 版本存会存在比较大的差异，使用这种方式安装的镜像创建出来的实例可能会存在部分配置项初始化不符合预期的情况，**因此建议使用：手工下载 cloud-init 源码包安装**。</font>

2. 修改 cloud-init 配置文件
根据不同操作系统，从以下链接下载 cloud.cfg 将`/etc/cloud/cloud.cfg`的内容进行替换。
>- [Ubuntu 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/ubuntu-cloud.cfg)
>-  [CentOS 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/centos-cloud.cfg)
>- 其他操作系统待补充


## 安装后的操作
> **注意：**
以下操作执行完成后请勿重启服务器，否则需重新执行以下操作。

```
cloud-init init --local
rm -rf /var/lib/cloud
```

#### Ubuntu 或 Debian 操作系统特殊操作：
```
rm -rf /etc/network/interfaces.d/50-cloud-init.cfg
```

修改`/etc/network/interfaces`为如下内容：
```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
source /etc/network/interfaces.d/*
```
