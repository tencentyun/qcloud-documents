
## 操作场景

Cloud-init 主要提供实例首次初始化时自定义配置的能力。如果导入的镜像没有安装 cloud-init 服务，基于该镜像启动的实例将无法被正常初始化，导致该镜像正常导入失败。本文档指导您安装 cloud-init 服务。
安装 cloud-init 推荐以下三种方式：
- 通过 [下载 cloud-init 二进制包](#binary)
- 通过 [手工下载 cloud-init 源码包方式](#ManualDown) 
- 通过 [使用软件源上的 cloud-init 包方式](#SoftSources)

## 前提条件
安装 cloud-init 的服务器可正常访问外网。

## 操作步骤
<dx-tabs>
::: 下载 cloud-init \s二进制包[](id:binary)
<dx-alert infotype="explain" title="">
- cloud-init 依赖于 qcloud-python, qcloud-python 是腾讯云重新编译打包的软件包，是单独的 python 环境，仅用于 cloud-init 运行环境，安装在 `/usr/local/qcloud/python` 目录下，与系统中默认的 python 不相冲突。
- cloud-init 是腾讯云基于社区20.1版本研发的，适配腾讯云运行环境的专属 cloud-init。
- cloud-init 二制包支持如下 OS:
</dx-alert>
<table>
<thead>
  <tr>
    <th rowspan="2">类型</th>
    <th rowspan="2">OS</th>
    <th rowspan="2">版本</th>
    <th colspan="2" style="text-align:center">x86_64</th>
    <th colspan="2" style="text-align:center">arm64</th>
  </tr>
  <tr>
    <th>qcloud-python</th>
    <th>cloud-init</th>
    <th>qcloud-python</th>
    <th>cloud-init</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="5">rpm</td>
    <td rowspan="2">CentOS</td>
    <td>7</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/centos7.6/qcloud-python-3.7.10-1.el7.x86_64.rpm">qcloud-python-3.7.10-1.el7.x86_64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/centos7.6/cloud-init-20.1.0011-1.el7.x86_64.rpm">cloud-init-20.1.0011-1.el7.x86_64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/centos7.4/aarch64/qcloud-python-3.7.10-1.el7.centos.aarch64.rpm">qcloud-python-3.7.10-1.el7.centos.aarch64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/centos7.4/aarch64/cloud-init-20.1.0011-3.el7.centos.aarch64.rpm">cloud-init-20.1.0011-3.el7.centos.aarch64.rpm</a></td>
  </tr>
  <tr>
    <td>8</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/centos8.2/x86_64/qcloud-python-3.7.10-1.el8.x86_64.rpm">qcloud-python-3.7.10-1.el8.x86_64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/centos8.2/x86_64/cloud-init-20.1.0011-1.el8.x86_64.rpm">cloud-init-20.1.0011-1.el8.x86_64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/centos8.2/aarch64/qcloud-python-3.7.10-1.el8.aarch64.rpm">qcloud-python-3.7.10-1.el8.aarch64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/centos8.2/aarch64/cloud-init-20.1.0011-3.el8.aarch64.rpm">cloud-init-20.1.0011-3.el8.aarch64.rpm</a></td>
  </tr>
  <tr>
    <td>Fedora</td>
    <td>36</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/fedora36/qcloud-python-3.7.10-2.fc36.x86_64.rpm">qcloud-python-3.7.10-2.fc36.x86_64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu20.04/cloud-init_20.1.0011-1_arm64.deb">cloud-init_20.1.0011-1_arm64.deb</a></td>
    <td>NA</td>
    <td>NA</td>
  </tr>
  <tr>
    <td>Kylin</td>
    <td>20sp1</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/kylin10sp1/x86_64/qcloud-python-3.7.10-1.ky10.x86_64.rpm">qcloud-python-3.7.10-1.ky10.x86_64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/kylin10sp1/x86_64/cloud-init-20.1.0011-2.ky10.x86_64.rpm">cloud-init-20.1.0011-2.ky10.x86_64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/kylin10sp1/aarch64/qcloud-python-3.7.10-1.ky10.aarch64.rpm">qcloud-python-3.7.10-1.ky10.aarch64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/kylin10sp1/aarch64/cloud-init-20.1.0011-1.ky10.aarch64.rpm">cloud-init-20.1.0011-1.ky10.aarch64.rpm</a></td>
  </tr>
  <tr>
    <td>openSUSE</td>
    <td>15.4</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/opensuse15.4/qcloud-python-3.7.10-2.x86_64.rpm">qcloud-python-3.7.10-2.x86_64.rpm</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/opensuse15.4/cloud-init-20.1.0011-2.x86_64.rpm">cloud-init-20.1.0011-2.x86_64.rpm</a></td>
    <td>NA</td>
    <td>NA</td>
  </tr>
  <tr>
    <td rowspan="8">deb</td>
    <td rowspan="4">Debian</td>
    <td>11</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian11/qcloud-python_3.7.10-1_amd64.deb">qcloud-python_3.7.10-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian11/cloud-init_20.1.0011-1_amd64.deb">cloud-init_20.1.0011-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian11/aarch64/qcloud-python_3.7.10-1_arm64.deb">qcloud-python_3.7.10-1_arm64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian11/aarch64/cloud-init_20.1.0011-1_arm64.deb">cloud-init_20.1.0011-1_arm64.deb</a></td>
  </tr>
  <tr>
    <td>10</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian10/qcloud-python_3.7.10-1_amd64.deb">qcloud-python_3.7.10-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian10/cloud-init_20.1.0011-1_amd64.deb">cloud-init_20.1.0011-1_amd64.deb</a></td>
    <td>NA</td>
    <td>NA</td>
  </tr>
  <tr>
    <td>9</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian9/qcloud-python_3.7.10-1_amd64.deb">qcloud-python_3.7.10-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian9/cloud-init_20.1.0011-1_amd64.deb">cloud-init_20.1.0011-1_amd64.deb</a></td>
    <td>NA</td>
    <td>NA</td>
  </tr>
  <tr>
    <td>8</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian8/qcloud-python_3.7.10-1_amd64.deb">qcloud-python_3.7.10-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/debian8/cloud-init_20.1.0011-1_amd64.deb">cloud-init_20.1.0011-1_amd64.deb</a></td>
    <td>NA</td>
    <td>NA</td>
  </tr>
  <tr>
    <td rowspan="4">Ubuntu</td>
    <td>22.04</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu22.04/qcloud-python_3.7.10-1_amd64.deb">qcloud-python_3.7.10-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu22.04/cloud-init_20.1.0011-1_amd64.deb">cloud-init_20.1.0011-1_amd64.deb</a></td>
    <td>NA</td>
    <td>NA</td>
  </tr>
  <tr>
    <td>20.04</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu20.04/x86_64/qcloud-python_3.7.10-1_amd64.deb">qcloud-python_3.7.10-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu20.04/x86_64/cloud-init_20.1.0011-1_amd64.deb">cloud-init_20.1.0011-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu20.04/qcloud-python_3.7.10-1_arm64.deb">qcloud-python_3.7.10-1_arm64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu20.04/cloud-init_20.1.0011-1_arm64.deb">cloud-init_20.1.0011-1_arm64.deb</a></td>
  </tr>
  <tr>
    <td>18.04</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu18.04/x86_64/qcloud-python_3.7.10-1%2Bubuntu18.04_amd64.deb">qcloud-python_3.7.10-1%2Bubuntu18.04_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu18.04/x86_64/cloud-init_20.1.0011-1%2Bubuntu18.04_amd64.deb">cloud-init_20.1.0011-1%2Bubuntu18.04_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu18.04/aarch64/qcloud-python_3.7.10-1_arm64.deb">qcloud-python_3.7.10-1_arm64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu18.04/aarch64/cloud-init_20.1.0011-1_arm64.deb">cloud-init_20.1.0011-1_arm64.deb</a></td>
  </tr>
  <tr>
    <td>16.04</td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu16.04/qcloud-python_3.7.10-1_amd64.deb">qcloud-python_3.7.10-1_amd64.deb</a></td>
    <td><a href="https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/packages/ubuntu16.04/cloud-init_20.1.0011-1_amd64.deb">cloud-init_20.1.0011-1_amd64.deb</a></td>
    <td>NA</td>
    <td>NA</td>
  </tr>
</tbody>
</table>

### 下载 cloud-init 二进制包[](id:binary)
1. 下载上述安装包。

2. 如果系统中已经有 cloud-init，请排查并执行如下命令，清理残留
```shellsession
rm -rf /var/lib/cloud
rm -rf /etc/cloud
rm -rf /usr/local/bin/cloud*
```
3. 根据操作系统，执行如下命令：
  - deb 系列，执行以下命令：
  ```shellsession
  dpkg -i *.deb
```
 - rpm 系列, 执行如下命令：
 ```shellsession
 rpm -ivh *.rpm
 ```
4. 查询版本是否正确安装
  ```shellsession
cloud-init qcloud -v
/usr/bin/cloud-init qcloud 0011
 ```
5.  重启后生效
:::
::: 手工下载\scloud-init\s源码包方式[](id:ManualDown)

### 下载 cloud-init 源码包

<dx-alert infotype="explain" title="">
- 在正常安装的情况下，cloud-init-20.1.0011 版本与腾讯云的兼容性最佳，可以保证使用该镜像创建的云服务器的所有配置项都可以正常初始化。建议选择 **cloud-init-20.1.0011.tar.gz** 安装版本。您也可以 [点此获取](https://launchpad.net/cloud-init/+download) 其他版本的 cloud-init 源码包。本文以 cloud-init-20.1.0011 版本为例。
</dx-alert>


执行以下命令，下载 cloud-init 源码包。
```shellsession
wget https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/src/cloud-init-20.1.0011.tar.gz
```

### 安装 cloud-init
1. 执行以下命令，解压 cloud-init 安装包。
<dx-alert infotype="explain" title="">
如果您使用的操作系统为 Ubuntu，请切换至 root 帐号。
</dx-alert>
```shellsession
tar -zxvf cloud-init-20.1.0011.tar.gz 
```
2. 执行以下命令，进入已解压的 cloud-init 安装包目录（即进入 cloud-init-20.1.0011 目录）。
```shellsession
cd cloud-init
```
3. 根据操作系统版本，安装 Python-pip。
  - CentOS 6/7系列，执行以下命令：
```shellsession
yum install python3-pip -y
```
  - Ubuntu 系列，执行以下命令：
```shellsession
apt-get -y install python3-pip
```
  - OpenSUSE / SUSE系列，执行以下命令：
```shellsession
zypper -n install python3-pip
```
若在安装时，出现无法安装或找不到安装包的错误，可参考 [解决无法安装 Python-pip 问题](#updateSoftware) 进行处理。
4. 执行以下命令，升级 pip。
```
python3 -m pip install --upgrade pip
```
5. 执行以下命令，安装依赖包。
<dx-alert infotype="notice" title="">
Cloud-init 依赖组件 requests 2.20.0版本后，已弃用 Python2.6。如果镜像环境的 Python 解释器为 Python2.6及以下，在安装 cloud-init 依赖包之前，请执行 `pip install 'requests&lt;2.20.0'` 命令，安装 requests 2.20.0 版本以下的版本。
</dx-alert>
```shellsession
pip3 install -r requirements.txt
```
5. 根据操作系统版本，安装 cloud-utils 组件。
  - CentOS 6系列，执行以下命令：
```shellsession
yum install cloud-utils-growpart dracut-modules-growroot -y
dracut -f
```
  - CentOS 7系列，执行以下命令：
```shellsession
yum install cloud-utils-growpart -y
```
  - Ubuntu 系列，执行以下命令：
```shellsession
apt-get install cloud-guest-utils -y
```
  - OpenSUSE / SUSE 系列，执行以下命令：
```shellsession
zypper install -y growpart
```
6. 执行以下命令，安装 cloud-init。
```shellsession
python3 setup.py build
```
```shellsession
python3 setup.py install --init-system systemd
``` <dx-alert infotype="notice" title="">
- --init-system 的可选参数有：(systemd, sysvinit, sysvinit_deb, sysvinit_freebsd, sysvinit_openrc, sysvinit_suse, upstart) [default: None]。请根据当前操作系统使用的自启动服务管理方式，进行选择。若选择错误，cloud-init 服务会无法开机自启动。
- centos6 及以下系统请选择 sysvinit，centos7 及以上系统请选择 systemd。本文以 systemd 自启动服务管理为例。
</dx-alert>


[](id:cloud-init)
### 修改 cloud-init 配置文件

1. 根据不同操作系统，下载 cloud.cfg。
  - [点此下载](https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/cfg/ubuntu/cloud.cfg) Ubuntu 操作系统的 cloud.cfg。
  - [点此下载](https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/cfg/centos/cloud.cfg) CentOS 操作系统的 cloud.cfg。
  - [点此下载](https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/cfg/sles/cloud.cfg) OpenSUSE / SUSE 操作系统的 cloud.cfg。
2. 将 `/etc/cloud/cloud.cfg` 的内容替换为已下载的 cloud.cfg 文件内容。


### 添加 syslog 用户
执行以下命令，添加 syslog 用户。
```shellsession
useradd syslog
```


### 设置 cloud-init 服务开机自启动
- **若操作系统是 systemd 自启动管理服务，则执行以下命令进行设置。**
<dx-alert infotype="explain" title="">
您可执行 `strings /sbin/init | grep "/lib/system"` 命令，若有返回信息，则操作系统是 systemd 自启动管理服务。
</dx-alert>
 1. **针对 Ubuntu 或 Debian 操作系统，需执行以下命令。**
```shellsession
 ln -s /usr/local/bin/cloud-init /usr/bin/cloud-init 
```
 2. **所有操作系统都需执行以下命令。**
```shellsession
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
```shellsession
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
```shellsession
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
```shellsession
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
```shellsession
apt-get/yum install cloud-init
```
<dx-alert infotype="explain" title="">
通过 apt-get 或 yum 命令安装的 cloud-init 默认为当前操作系统配置的软件源中默认的 cloud-init 版本。使用该方式安装的镜像创建的实例可能会存在部分配置项初始化不符合预期的情况，建议使用 [手工下载 cloud-init 源码包方式](#ManualDown) 进行安装。
</dx-alert>



### 修改 cloud-init 配置文件[](id:cloud-init)
1. 根据不同操作系统，下载 cloud.cfg。
 - [点此下载](https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/cfg/ubuntu/cloud.cfg) Ubuntu 操作系统的 cloud.cfg。
 - [点此下载](https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/cfg/centos/cloud.cfg) CentOS 操作系统的 cloud.cfg。
 - [点此下载](https://gerryguan-1306210569.cos.ap-chongqing.myqcloud.com/cloud-init/cfg/sles/cloud.cfg) OpenSUSE / SUSE 操作系统的 cloud.cfg。
2. 将 `/etc/cloud/cloud.cfg` 的内容替换为已下载的 cloud.cfg 文件内容。
:::
</dx-tabs>



## 相关操作


<dx-alert infotype="notice" title="">
以下操作执行完成后，请勿重启服务器，否则需重新执行下以下操作。
</dx-alert>


1. 执行以下命令，检查 cloud-init 相关配置是否成功。
```shellsession
cloud-init init --local
```
返回类似如下信息，则说明已成功配置 cloud-init。
```shellsession
Cloud-init v. 20.1.0011 running 'init-local' at Fri, 01 Apr 2022 01:26:11 +0000. Up 38.70 seconds.
```
2. 执行以下命令，删除 cloudinit 的缓存记录。
```shellsession
rm -rf /var/lib/cloud
```
3. 针对 Ubuntu 或 Debian 操作系统，需执行以下命令。
``` shellsession
rm -rf /etc/network/interfaces.d/50-cloud-init.cfg
```
4. 针对 Ubuntu 或 Debian 操作系统，需将 `/etc/network/interfaces` 修改为以下内容：
```shellsession
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
source /etc/network/interfaces.d/*
```

## 附录
[](id:updateSoftware)
### 解决无法安装 Python-pip 问题
若在安装 Python-pip 出现无此安装包或无法安装的错误，可对应实际使用的操作系统，参考以下步骤进行解决：
<dx-tabs>
::: CentOS\s6/7系列
  1. 执行以下命令，设置 EPEL 存储库。
```shellsession
yum install epel-release -y
```
  2. 执行以下命令，安装 Python-pip。
```shellsession
yum install python3-pip -y
```
:::
::: Ubuntu\s系列
  1. 执行以下命令，清除缓存。
```shellsession
apt-get clean all
```
  1. 执行以下命令，更新软件包列表。
```shellsession
apt-get update -y
```
  2. 执行以下命令，安装 Python-pip。
```shellsession
apt-get -y install python3-pip
```
:::
</dx-tabs>
