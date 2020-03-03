
"cloud-init" allows users to customize configuration while initialing an instance. Please note that if the image used for creating an instance does not install "cloud-init", the image cannot be imported.
"cloud-init" can be installed by using one of the following solutions: [Manually Download cloud-init Source Code Package for Installation](/document/product/213/12587#.E4.B8.80.E3.80.81.E6.89.8B.E5.B7.A5.E4.B8.8B.E8.BD.BDcloud-init.E6.BA.90.E7.A0.81.E5.8C.85.E7.9A.84.E6.96.B9.E5.BC.8F.E5.AE.89.E8.A3.85) or [Directly Use cloud-init Package in Software Source](/document/product/213/12587#.E4.BA.8C.E3.80.81.E7.9B.B4.E6.8E.A5.E4.BD.BF.E7.94.A8.E8.BD.AF.E4.BB.B6.E6.BA.90.E4.B8.8A.E9.9D.A2.E7.9A.84-cloud-init-.E5.8C.85.E5.AE.89.E8.A3.85). Before importing the Linux system image, make sure that the cloud-init service has been properly installed in the image in one of the following ways:
## Downloading and Installing `cloud-init` Source Code Package Manually

### 1 Preconditions 

The server where cloud-init is installed can be connected to the public network


### 2 Download cloud-init Source Code Package
- Download URL: https://launchpad.net/cloud-init/+download
- Recommended version: cloud-init-17.1.tar.gz
>**Note:** "cloud-init-17.1" is best compatible with Tencent Cloud. Proper installation can guarantee all configurations of the CVM created through the image are normally initialized.

### 3 Install `cloud-init`
#### 3.1 Install `cloud-init` Dependencies
- setuptools
- jinja2
- prettytable
- oauthlib
- configobj
- pyyaml
- requests
- jsonpatch
- jsonschema
- six

#### 3.2 Decompress and Install
```
cd ./cloud-init-17.1
   python setup.py build
   python setup.py install --init-system systemd
```
>**Note:** --init-system has the following optional parameters: (systemd, sysvinit,  sysvinit_deb, sysvinit_freebsd, sysvinit_openrc, sysvinit_suse, upstart)  [default: None]. Your selection depends on how the auto-start service is managed in the current operating system. "cloud-init" service cannot be started automatically on boot in case of incorrect selection. Here, systemd auto-start service management is taken as an example.

#### 3.3 Modify cloud-init Configuration File
According to different operating systems, download cloud.cfg by clicking the links below to replace the content of /etc/cloud/cloud.cfg.
- [cloud.cfg for Ubuntu Operating System](http://cloudinit-1251740579.cosgz.myqcloud.com/ubuntu-cloud.cfg)
- [cloud.cfg for Centos Operating System](http://cloudinit-1251740579.cosgz.myqcloud.com/centos-cloud.cfg)
- Other operating systems will be available soon

#### 3.4 Add syslog User
`useradd syslog`

#### 3.5 Set Auto-start on Boot for cloud-init Service

**3.5.1 Auto-start management service for systemd operating system**
Execute the specific commands for Ubuntu or Debian operating system
` ln -s /usr/local/bin/cloud-init /usr/bin/cloud-init `

Execute the following commands for all operating systems
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
Execute the specific commands for Centos and Redhat operating systems
Replace the content in /lib/systemd/system/cloud-init-local.service file with following:
**Unit**   
```
Description=Initial cloud-init job (pre-networking)
Wants=network-pre.target
After=systemd-remount-fs.service
Before=NetworkManager.service
Before=network-pre.target
Before=shutdown.target
Conflicts=shutdown.target
RequiresMountsFor=/var/lib/cloud
```
**Service**
```
Type=oneshot
ExecStart=/usr/bin/cloud-init init --local
ExecStart=/bin/touch /run/cloud-init/network-config-ready
RemainAfterExit=yes
TimeoutSec=0
```
>**Note:** Output needs to appear in instance console output
StandardOutput=journal+console

**Install**
WantedBy=cloud-init.target


Replace the content in /lib/systemd/system/cloud-init.service file with following:
**Unit**
```
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
```
**Service**
```
Type=oneshot
ExecStart=/usr/bin/cloud-init init
RemainAfterExit=yes
TimeoutSec=0
```
>**Note:** Output needs to appear in instance console output
StandardOutput=journal+console

**Install**
WantedBy=cloud-init.target

**3.5.2 Auto-start management service for sysvinit operating system**
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

## Installing Using cloud-init Package in Software Source
Execute the following command for installation
`apt-get/yum install cloud-init`
 >**Note:** The version of cloud-init directly installed by executing apt-get or yum commands is the default cloud-init version in the software source configured in the current operating system. Generally, cloud-init 17.1 may be greatly different from other versions, so the initialization of some configuration items of the instance created through the image installed in this way may fail. "Manually Download cloud-init Source Code Package for Installation" is recommended.

**Modify cloud-init configuration file**
 According to different operating systems, download cloud.cfg by clicking the links below to replace the content of /etc/cloud/cloud.cfg.
- [cloud.cfg for Ubuntu Operating System](http://cloudinit-1251740579.cosgz.myqcloud.com/ubuntu-cloud.cfg)
- [cloud.cfg for Centos Operating System](http://cloudinit-1251740579.cosgz.myqcloud.com/centos-cloud.cfg)
- Other operating systems will be available soon


## Operations After Installation
>**Note:** Do not restart the server after the following operations are completed, otherwise you have to do it again.

```
cloud-init init --local
rm -rf /var/lib/cloud
```

Specific operations in Ubuntu or Debian operating systems
`rm -rf /etc/network/interfaces.d/50-cloud-init.cfg`

Modify /etc/network/interfaces to the following content:

This file describes the network interfaces available on your system and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/

