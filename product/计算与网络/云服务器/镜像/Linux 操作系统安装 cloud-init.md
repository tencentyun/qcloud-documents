
cloud-init 主要提供了一个实例首次初始化时的自定义配置的能力，如果导入的镜像没有安装cloud-init服务，通过该镜像启动的实例就不会被正常初始化，因此该镜像就会导入失败。
安装cloud-init的方式有两种，[手工下载cloud-init源码包的方式安装](/document/product/213/12587#.E4.B8.80.E3.80.81.E6.89.8B.E5.B7.A5.E4.B8.8B.E8.BD.BDcloud-init.E6.BA.90.E7.A0.81.E5.8C.85.E7.9A.84.E6.96.B9.E5.BC.8F.E5.AE.89.E8.A3.85) 和 [直接使用软件源上面的 cloud-init 包安装](/document/product/213/12587#.E4.BA.8C.E3.80.81.E7.9B.B4.E6.8E.A5.E4.BD.BF.E7.94.A8.E8.BD.AF.E4.BB.B6.E6.BA.90.E4.B8.8A.E9.9D.A2.E7.9A.84-cloud-init-.E5.8C.85.E5.AE.89.E8.A3.85)。在导入Linux系统镜像前，请确保您的镜像内部已经按照如下方式之一正确安装了cloud-init服务。
## 一、手工下载cloud-init源码包的方式安装

### 1、前提条件

* 安装cloud-init的服务器外网能通


### 2、下载cloud-init源码包
> 1）下载地址： https://launchpad.net/cloud-init/+download
> 2）建议安装版本： cloud-init-17.1.tar.gz  （<font color="#FF0000">*注： cloud-init-17.1 版本与腾讯云的兼容性最好，在正常安装的情况下可以保证使用该镜像创建出来的云服务器所有配置项都能够正常初始化。*</font>）

### 3、安装cloud-init
#### 3.1、安装cloud-init 依赖包
>setuptools
>jinja2
prettytable
oauthlib
configobj
pyyaml
requests
jsonpatch
jsonschema
six

#### 3.2、解压并安装
>cd ./cloud-init-17.1
   python setup.py build
   python setup.py install --init-system systemd
  <br> <font color="#FF0000">*注：--init-system的可选参数 有：(systemd, sysvinit,  sysvinit_deb, sysvinit_freebsd, sysvinit_openrc, sysvinit_suse, upstart)  [default: None]，需要根据当前操作系统使用的自启动服务管理方式是什么进行选择，如果选择出错则cloud-init 服务无法开机自启动，本例以systemd自启动服务管理为例。*</font>

#### 3.3、修改cloud-init 配置文件
> 根据不同操作系统，从以下链接下载 cloud.cfg 将 /etc/cloud/cloud.cfg 的内容进行替换。
> * [ubuntu 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/ubuntu-cloud.cfg)
> * [centos 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/centos-cloud.cfg)
> * 其他操作系统待补充

#### 3.4、添加 syslog 用户
>useradd syslog

#### 3.5、设置 cloud-init 服务开机自启动

**3.5.1 、若操作系统是systemd自启动管理服务**
<br>**ubuntu 或 debian 操作系统特殊执行**
> ln -s /usr/local/bin/cloud-init /usr/bin/cloud-init 

**所有操作系统都执行**
>systemctl enable cloud-init-local.service 
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

**centos 和 redhat 操作系统特殊执行**
>**将 /lib/systemd/system/cloud-init-local.service 文件内容替换为如下：**
[Unit]
Description=Initial cloud-init job (pre-networking)
Wants=network-pre.target
After=systemd-remount-fs.service
Before=NetworkManager.service
Before=network-pre.target
Before=shutdown.target
Conflicts=shutdown.target
RequiresMountsFor=/var/lib/cloud

>[Service]
Type=oneshot
ExecStart=/usr/bin/cloud-init init --local
ExecStart=/bin/touch /run/cloud-init/network-config-ready
RemainAfterExit=yes
TimeoutSec=0

>\# Output needs to appear in instance console output
StandardOutput=journal+console

>[Install]
WantedBy=cloud-init.target


>**将 /lib/systemd/system/cloud-init.service 文件内容替换为如下：**
>[Unit]
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

>[Service]
Type=oneshot
ExecStart=/usr/bin/cloud-init init
RemainAfterExit=yes
TimeoutSec=0

>\# Output needs to appear in instance console output
StandardOutput=journal+console

>[Install]
WantedBy=cloud-init.target

**3.5.2 、若操作系统是sysvinit自启动管理服务**

>chkconfig --add cloud-init-local
chkconfig --add cloud-init
chkconfig --add cloud-config
chkconfig --add cloud-final

>chkconfig cloud-init-local on 
chkconfig cloud-init on 
chkconfig cloud-config on 
chkconfig cloud-final on 


## 二、直接使用软件源上面的 cloud-init 包安装
**执行以下安装命令安装**
>apt-get/yum install cloud-init
 <br><font color="#FF0000">*注： 直接通过apt-get 或 yum 命令安装的cloud-init 版本默认为当前操作系统配置的软件源里面默认的cloud-init版本，通常情况下和cloud-init 17.1 版本存会存在比较大的差异，使用这种方式安装的镜像创建出来的实例可能会存在部分配置项初始化不符合预期的情况，建议使用方案一：手工下载cloud-init源码包的方式进行安装。*</font>

**修改cloud-init 配置文件**
> 根据不同操作系统，从以下链接下载 cloud.cfg 将 /etc/cloud/cloud.cfg 的内容进行替换。
> * [ubuntu 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/ubuntu-cloud.cfg)
> * [centos 操作系统的 cloud.cfg](http://cloudinit-1251740579.cosgz.myqcloud.com/centos-cloud.cfg)
> * 其他操作系统待补充


## 三、安装完之后的操作
<font color="#FF0000">*注：以下操作执行完成后请勿重启服务器，否则需重新执行下以下操作。*</font>
>cloud-init init --local
>rm -rf /var/lib/cloud

**ubuntu 或 debian 操作系统特殊操作**
>rm -rf /etc/network/interfaces.d/50-cloud-init.cfg

>修改 /etc/network/interfaces 为如下内容：

>\# This file describes the network interfaces available on your system
\# and how to activate them. For more information, see interfaces(5).
>
source /etc/network/interfaces.d/*
