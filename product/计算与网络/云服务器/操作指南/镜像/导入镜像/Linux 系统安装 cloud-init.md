## 操作场景

Cloud-init 主要提供实例首次初始化时自定义配置的能力。如果导入的镜像没有安装 cloud-init 服务，基于该镜像启动的实例将无法被正常初始化，导致该镜像导入失败。本文档指导您安装 cloud-init 服务。
安装 cloud-init 推荐以下两种方式：
- 通过 [手工下载 cloud-init 源码包方式](#ManualDown) 
- 通过 [使用软件源上的 cloud-init 包方式](#SoftSources)

## 注意事项
在导入 Linux 系统镜像前，请确保您的镜像内部已正确安装了 cloud-init 服务。

## 前提条件
安装 cloud-init 的服务器可正常访问外网。

## 操作步骤
<dx-tabs>
::: 手工下载\scloud-init\s源码包方式[](id:ManualDown)

### 下载 cloud-init 源码包



<dx-alert infotype="explain" title="">
- 在正常安装的情况下，cloud-init-17.1 版本与腾讯云的兼容性最佳，可以保证使用该镜像创建的云服务器的所有配置项都可以正常初始化。建议选择 **cloud-init-17.1.tar.gz** 安装版本。您也可以 [点此获取](https://launchpad.net/cloud-init/+download) 其他版本的 cloud-init 源码包。本文以 cloud-init-17.1 版本为例。
- 如使用 cloud-init-17.1 或其他版本的 cloud-init 源码包安装不成功，您还可以通过 [手工下载绿色版 cloud-init 包方式](#greeninitCloudInit) 进行安装。
</dx-alert>


执行以下命令，下载 cloud-init 源码包。
```
wget https://launchpad.net/cloud-init/trunk/17.1/+download/cloud-init-17.1.tar.gz
```

### 安装 cloud-init
1. 执行以下命令，解压 cloud-init 安装包。
<dx-alert infotype="explain" title="">
如果您使用的操作系统为 Ubuntu，请切换至 root 帐号。
</dx-alert>
```
tar -zxvf cloud-init-17.1.tar.gz 
```
2. 执行以下命令，进入已解压的 cloud-init 安装包目录（即进入 cloud-init-17.1 目录）。
```
cd cloud-init-17.1
```
3. 根据操作系统版本，安装 Python-pip。
  - CentOS 6/7系列，执行以下命令：
```
yum install python-pip -y
```
  - Ubuntu 系列，执行以下命令：
```
apt-get install python-pip -y
```
若在安装时，出现无法安装或找不到安装包的错误，可参考 [解决无法安装 Python-pip 问题](#updateSoftware) 进行处理。
4. 执行以下命令，安装依赖包。
<dx-alert infotype="notice" title="">
Cloud-init 依赖组件 requests 2.20.0版本后，已弃用 Python2.6。如果镜像环境的 Python 解释器为 Python2.6及以下，在安装 cloud-init 依赖包之前，请执行 `pip install 'requests&lt;2.20.0'` 命令，安装 requests 2.20.0 版本以下的版本。
</dx-alert>
```
pip install -r requirements.txt
```
5. 根据操作系统版本，安装 cloud-utils 组件。
  - CentOS 6系列，执行以下命令：
```
yum install cloud-utils-growpart dracut-modules-growroot -y
dracut -f
```
  - CentOS 7系列，执行以下命令：
```
yum install cloud-utils-growpart -y
```
  - Ubuntu 系列，执行以下命令：
```
apt-get install cloud-guest-utils -y
```
6. 执行以下命令，安装 cloud-init。
```
python setup.py build
python setup.py install --init-system systemd
``` <dx-alert infotype="notice" title="">
--init-system 的可选参数有：(systemd, sysvinit,  sysvinit_deb, sysvinit_freebsd, sysvinit_openrc, sysvinit_suse, upstart)  [default: None]。请根据当前操作系统使用的自启动服务管理方式，进行选择。若选择错误，cloud-init 服务会无法开机自启动。本文以 systemd 自启动服务管理为例。
</dx-alert>


### 修改 cloud-init 配置文件

1. 根据不同操作系统，下载 cloud.cfg。
  - [点此下载](https://cloudinit-1251783334.cos.ap-guangzhou.myqcloud.com/ubuntu/cloud.cfg) Ubuntu 操作系统的 cloud.cfg。
  - [点此下载](https://cloudinit-1251783334.cos.ap-guangzhou.myqcloud.com/centos/cloud.cfg) CentOS 操作系统的 cloud.cfg。
2. 将 `/etc/cloud/cloud.cfg` 的内容替换为已下载的 cloud.cfg 文件内容。


### 添加 syslog 用户
执行以下命令，添加 syslog 用户。
```
useradd syslog
```


### 设置 cloud-init 服务开机自启动
- **若操作系统是 systemd 自启动管理服务，则执行以下命令进行设置。**
<dx-alert infotype="explain" title="">
您可执行 `strings /sbin/init | grep "/lib/system"` 命令，若有返回信息，则操作系统是 systemd 自启动管理服务。
</dx-alert>
 1. **针对 Ubuntu 或 Debian 操作系统，需执行以下命令。**
```
 ln -s /usr/local/bin/cloud-init /usr/bin/cloud-init 
```
 2. **所有操作系统都需执行以下命令。**
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
 3. **针对 CentOS 和 Redhat 操作系统，需执行以下命令。**
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
<dx-alert infotype="explain" title="">
您可执行 `strings /sbin/init | grep "sysvinit"` 命令，若有返回信息，则操作系统是 sysvinit 自启动管理服务。
</dx-alert>
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
:::
::: 使用软件源上的\scloud-init\s包方式[](id:SoftSources)
### 安装 cloud-init

执行以下命令，安装 cloud-init。
```
apt-get/yum install cloud-init
```
<dx-alert infotype="explain" title="">
通过 apt-get 或 yum 命令安装的 cloud-init 默认为当前操作系统配置的软件源中默认的 cloud-init 版本。使用该方式安装的镜像创建的实例可能会存在部分配置项初始化不符合预期的情况，建议使用 [手工下载 cloud-init 源码包方式](#ManualDown) 进行安装。
</dx-alert>



### 修改 cloud-init 配置文件
1. 根据不同操作系统，下载 cloud.cfg。
 - [点此下载](https://cloudinit-1251783334.cos.ap-guangzhou.myqcloud.com/ubuntu/cloud.cfg) Ubuntu 操作系统的 cloud.cfg。
 - [点此下载](https://cloudinit-1251783334.cos.ap-guangzhou.myqcloud.com/centos/cloud.cfg) CentOS 操作系统的 cloud.cfg。
2. 将 `/etc/cloud/cloud.cfg` 的内容替换为已下载的 cloud.cfg 文件内容。
:::
</dx-tabs>



## 相关操作


<dx-alert infotype="notice" title="">
以下操作执行完成后，请勿重启服务器，否则需重新执行下以下操作。
</dx-alert>


1. 执行以下命令，检查 cloud-init 相关配置是否成功。
```
cloud-init init --local
rm -rf /var/lib/cloud
```
2. 针对 Ubuntu 或 Debian 操作系统，需执行以下命令。
```
rm -rf /etc/network/interfaces.d/50-cloud-init.cfg
```
3. 针对 Ubuntu 或 Debian 操作系统，需将 `/etc/network/interfaces` 修改为以下内容：
```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
source /etc/network/interfaces.d/*
```

## 附录

### 手工下载绿色版 cloud-init 包方式[](id:greeninitCloudInit)
若通过 [手工下载 cloud-init 源码包方式](#ManualDown) 安装不成功，可通过以下操作进行安装：
1. [点此获取](https://image-tools-1251783334.cos.ap-guangzhou.myqcloud.com/greeninit-x64-beta.tgz) 绿色版 cloud-init 包。
2. 执行以下命令，解压绿色版 cloud-init 包。
```
tar xvf greeninit-x64-beta.tgz 
```
3. 执行以下命令，进入已解压的绿色版 cloud-init 包目录（即进入 greeninit 目录）。
```
cd greeninit
```
4. 执行以下命令，安装 cloud-init。
```
sh install.sh 
```

### 解决无法安装 Python-pip 问题[](id:updateSoftware)
若在安装 Python-pip 出现无此安装包或无法安装的错误，可对应实际使用的操作系统，参考以下步骤进行解决：
<dx-tabs>
::: CentOS\s6/7系列
  1. 执行以下命令，设置 EPEL 存储库。
```
yum install epel-release -y
```
  2. 执行以下命令，安装 Python-pip。
```
yum install python-pip -y
```
:::
::: Ubuntu\s系列
  1. 执行以下命令，更新软件包列表。
```
apt-get update -y
```
  2. 执行以下命令，安装 Python-pip。
```
apt-get install python-pip -y
```
:::
</dx-tabs>
