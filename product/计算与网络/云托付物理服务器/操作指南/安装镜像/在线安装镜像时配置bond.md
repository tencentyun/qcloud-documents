## 操作场景
当您在进行 [在线安装镜像](https://cloud.tencent.com/document/product/1448/75935) 操作时，可参考本文配置 CHC 云服务器的“自定义数据”，实现在线安装镜像时配置 bond。

<dx-alert infotype="explain" title="">
本文仅适用于使用**公共镜像**和**自定义镜像**生产云主机时操作。
</dx-alert>




## 操作步骤
在“生产” CHC 云服务器实例时，若选择**公共镜像**或**自定义镜像**的镜像安装方式，则可通过填写“高级设置” > “自定义数据”，用于启动时的实例配置。您可根据具体的操作系统类型填写合适的脚本，以实现配置 bond 的功能。

示例如下：
本文以 CentOS7.6 为例，将以下代码填写至“自定义数据”并创建 CHC 云服务器，安装镜像时会自动配置 bond。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f81380f64236835371ba4b1656e9b5f6.png)
代码如下：
```
#!/bin/bash

mkdir -p /etc/sysconfig/network-scripts/backup
mv /etc/sysconfig/network-scripts/ifcfg-eth0 ../backup
echo "BOOTPROTO=none
DEVICE=eth0
ONBOOT=yes
TYPE=Ethernet
MASTER=bond0
SLAVE=yes" > /etc/sysconfig/network-scripts/ifcfg-eth0
echo "BOOTPROTO=none
DEVICE=eth1
ONBOOT=yes
TYPE=Ethernet
MASTER=bond0
SLAVE=yes" > /etc/sysconfig/network-scripts/ifcfg-eth1
echo "BOOTPROTO=dhcp
DEVICE=bond0
ONBOOT=yes
TYPE=Ethernet
BONDING_OPTS='mode=4 miimon=100 lacp_rate=fast xmit_hash_policy=2 broadcast_arp=1 broadcast_nd=1 periodic_na=1 periodic_na_interval=90'" > /etc/sysconfig/network-scripts/ifcfg-bond0
echo "network:
  config: disabled" > /etc/cloud/cloud.cfg.d/forbid_change_networkcfg.cfg

systemctl restart network
```
