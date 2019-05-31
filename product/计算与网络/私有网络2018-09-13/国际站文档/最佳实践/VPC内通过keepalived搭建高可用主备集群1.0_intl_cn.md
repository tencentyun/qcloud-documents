本文将介绍如何在腾讯云VPC内通过keepalived搭建高可用主备集群。
## 基本原理
通常高可用主备集群包含2台服务器，一台主服务器处于某种业务的激活状态（即Active状态），另一台备服务器处于该业务的备用状态（即Standby状态)，它们共享同一个VIP（virtual IP），同一时刻VIP只在一台主设备上生效，当主服务器出现问题，备用服务器接管VIP继续提供服务。高可用主备模式有着广泛的应用，例如：mysql 主备切换、Ngnix web接入。
![](//mc.qcloudimg.com/static/img/a5aa34fb87508284d9e7a07898085728/1.png)

## 与物理网络的区别
在传统的物理网络中可以通过keepalived的VRRP协议协商主备状态，其原理是：主设备周期性发送免费ARP报文刷新上联交换机的MAC表或终端ARP表，触发VIP的迁移到主设备上。腾讯云VPC内支持部署keepalived来搭建主备高可用集群，与物理网络相比，主要有两个区别：
1)  暂不支持VRRP组播报文，需要将keepalived的vrrp instance配置为单播VRRP报文。
2)  暂不支持通过免费ARP报文做VIP的迁移，而是通过调用云API来绑定VIP到主设备上。

## 主要步骤
1.  申请VIP，该VIP仅支持在子网内迁移（因此需要保证主备服务器位于同一个子网）。
2.  主备服务器安装及配置keepalived(**1.2.8版本以上**)。
3.  使用keepalived的notify机制，调用云API进行主备切换。
4.  （可选）给VIP分配外网IP。
5.  验证主备倒换时VIP及外网IP是否正常切换。

## 详细步骤
### 步骤1.    申请VIP
在某个子网内申请VIP（VPC内用户主动申请的IP都可作为VIP），暂时仅支持云API，云API代码开发指引请参考第6步。由于VIP绑定于弹性网卡上，弹性网卡分为主网卡和辅助网卡，而VPC内每台CVM在创建时会默认分配一个主网卡，因此您可以选择在主服务器所绑定的主弹性网卡上申请VIP。
**具体操作：** 
1) 通过云`API:DescribeNetworkInterfaces`[点击查看API详情](https://cloud.tencent.com/doc/api/245/4814)得到云服务器的主网卡的`networkInterfaceId`（入参填写：**私有网络ID**和**云服务器的ID**即可）。
2) 通过云`API:AssignPrivateIpAddresses`[点击查看API详情](https://cloud.tencent.com/doc/api/245/4817)在弹性网卡上申请内网VIP的，申请VIP操作可参考以下python代码：

```
        
#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'vpc'
action = 'AssignPrivateIpAddresses'
config = {
    'Region': 'bj',
    'secretId': '您的secretId',
    'secretKey': '您的secretKey',
    'method': 'post'
}
params = {
    'vpcId': '您的vpcID',
    'networkInterfaceId': '您需要初次见ip绑定的弹性网卡ID',
    'secondaryPrivateIpAddressCount': '您需要申请IP地址的个数'
}

try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
       
```
        
### 步骤2. 主备子机安装keepalived（1.2.8版本以上）
以centos为例：`yum –y install keepalived`

### 步骤3.    keepalived.conf配置单播模式
编辑文件/etc/keepalived/keepalived.conf，除基本keepalived的vrrp配置外，注意需要配置单播模式，即指定对端设备的ip地址，在keepalived.conf的vrrp_instance项中指定单播模式：

```
vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    unicast_peer {
        10.0.0.1    #对端设备的ip地址，例如：10.0.0.1
    }
    virtual_ipaddress {
        10.100.0.27   #第一步申请的VIP
    }
    nopreempt
    garp_master_delay 1
    garp_master_refresh 5
}
```

### 步骤 4.（可选）给VIP分配外网IP
先在控制台申请EIP，再通过云API绑定到1中申请的内网IP，[点击查看具体调用方式](https://cloud.tencent.com/doc/api/229/1377)，python代码与步骤1类似。

### 步骤 5.   keepalived.conf 配置切换脚本
主备切换时，新切换为主的设备通过notify调用vip.py进行切换。

```
vrrp_sync_group G1 {
    group {
        E1
    }
    notify_master "/etc/keepalived/vip.py"
}

```
### 步骤 6. 验证主备倒换时VIP及外网IP是否正常切换
vip.py：通过云API开发主备切换程序，通过调用内网IP迁移的云API来进行IP地址的切换，以python为例：
1) 下载 Python SDK
- [转到 github 查看 Python SDK >>](https://github.com/QcloudApi/qcloudapi-sdk-python)
- [点击下载 Python SDK >>](https://mc.qcloudimg.com/static/archive/b61ee1ce734e7437530304152c20ee14/qcloudapi-sdk-python-master.zip)

请仔细阅读其中README.md，并将sdk下载到/etc/keepalived目录中，如：

2) 云API密钥获取：
![](//mc.qcloudimg.com/static/img/ffd379c9e886d0ae3de4fba34539aac7/2.png)
![](//mc.qcloudimg.com/static/img/900df050c3d619566a482ff4e1bd5433/4.png)
3) 基于sdk开发切换调用云API的程序vip.py，并将vip.py保存到/etc/keepalived目录，内网IP迁移云API：

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
step1: 下载python-sdk: https://github.com/QcloudApi/qcloudapi-sdk-python
step2: 将以下python代码保存成vip.py放到sdk的src同级目录,  具体参数参考: https://cloud.tencent.com/doc/api/245/1361
"""

from src.QcloudApi.qcloudapi import QcloudApi

module = 'vpc'
action = 'MigratePrivateIpAddress'
config = {
    'Region': 'bj',
    'secretId': '您的secretId',
    'secretKey': '您的secretKey',
    'method': 'post'
}
params = {
    'vpcId': 'vpc-2l52o5c2',
    'privateIpAddress': '10.100.0.27',
    'oldNetworkInterfaceId': 'IP迁移前所在的弹性网卡ID',
    'newNetworkInterfaceId': 'IP迁移后所在的弹性网卡ID'
}

try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
```

注意，主备设备上该vip.py中的迁移前后弹性网卡需要对调，需要给vip.py添加可执行属性:
`Chmod +x vip.py`
并手动执行vip.py检验,执行下面命令将触发ip地址迁移：
`/etc/keepalived/vip.py`
4)  启动keepalived：`/etc/init.d/keepalived start`
5)  验证主备切换容灾效果：通过重启keepalived进程、重启子机等方式模拟主机故障，检测VIP是否能迁移。

#### 附件：Keepalived.conf参考

```
! Configuration File for keepalived
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
}
vrrp_sync_group G1 {
    group {
        VI_1
    }
    notify_master "/etc/keepalived/vip.py"
}
vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    unicast_peer {
        10.0.0.1    #对端设备的ip地址，例如：10.0.0.1
    }
    virtual_ipaddress {
        10.100.0.27
    }
    nopreempt
    garp_master_delay 1
    garp_master_refresh 5
}
```
