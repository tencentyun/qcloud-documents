本文将介绍如何在腾讯云 VPC 内通过 keepalived 搭建高可用主备集群。
## 基本原理
通常高可用主备集群包含 2 台服务器，一台主服务器处于某种业务的激活状态（即 Active 状态），另一台备服务器处于该业务的备用状态（即 Standby 状态)，它们共享同一个 VIP（Virtual IP），同一时刻 VIP 只在一台主设备上生效，当主服务器出现问题，备用服务器接管 VIP 继续提供服务。高可用主备模式有着广泛的应用，例如：MySQL 主备切换、Ngnix Web 接入。
<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/a5aa34fb87508284d9e7a07898085728/1.png)

</div>
## 与物理网络的区别
在传统的物理网络中可以通过 keepalived 的 VRRP 协议协商主备状态，其原理是：主设备周期性发送免费 ARP 报文刷新上联交换机的 MAC 表或终端 ARP 表，触发 VIP 的迁移到主设备上。腾讯云 VPC 内支持部署 keepalived 来搭建主备高可用集群，与物理网络相比，主要有两个区别：
1)  暂不支持 VRRP 组播报文，需要将 keepalived 的 VRRP Instance 配置为单播 VRRP 报文。
2)  暂不支持通过免费 ARP 报文做 VIP 的迁移，而是通过调用云 API来绑定 VIP 到主设备上。

## 主要步骤
1.  申请 VIP，该 VIP 仅支持在子网内迁移（因此需要保证主备服务器位于同一个子网）。
2.  主备服务器安装及配置 keepalived (**1.2.8版本以上**)。
3.  使用 keepalived 的 notify 机制，调用云 API 进行主备切换。
4.  给 VIP 分配外网 IP。**（可选）**
5.  验证主备倒换时 VIP 及外网 IP 是否正常切换。

## 详细步骤

### 步骤1.    申请VIP
在某个子网内申请VIP（VPC内用户主动申请的IP都可作为VIP），**控制台 或 云API**均可申请，由于VIP绑定于弹性网卡上，弹性网卡分为主网卡和辅助网卡，而VPC内每台CVM在创建时会默认分配一个主网卡，因此您可以选择在主服务器所绑定的主弹性网卡上申请VIP :


- 控制台：点击查看[在弹性网卡上  分配内网IP（Qcloud控制台）](https://cloud.tencent.com/document/product/215/6513#.E5.88.86.E9.85.8D.E5.86.85.E7.BD.91ip.EF.BC.88qcloud.E6.8E.A7.E5.88.B6.E5.8F.B0.EF.BC.8910)

- 云API：**通过云 API 分配 申请VIP 具体操作(云API代码开发指引请参考第6步)：** 


> 注意：您在 `/etc/init.d/keepalived start` 或 `service network restart`执行后** 可在主服务器内看到该内网IP（参见第三步）.或者，您在分配内网IP后，在云服务器内配置该内网IP，**点击查看[分配内网IP（云服务器系统内）](https://cloud.tencent.com/document/product/215/6513#.E5.88.86.E9.85.8D.E5.86.85.E7.BD.91ip.EF.BC.88.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E7.B3.BB.E7.BB.9F.E5.86.85.EF.BC.8911)

1) 通过云`API:DescribeNetworkInterfaces`得到云服务器的主网卡的`networkInterfaceId`（入参填写：**私有网络 ID**和**云服务器的 ID**即可）。[点击查看 API 详情](https://cloud.tencent.com/doc/api/245/4814)
2) 通过云`API:AssignPrivateIpAddresses`在弹性网卡上申请内网 VIP 的，申请 VIP 操作可参考以下  Python 代码：[点击查看 API 详情](https://cloud.tencent.com/doc/api/245/4817)
```
        
#!/usr/bin/python
# -*- coding: utf-8 -*-

#以下两行根据SDK的安装方式选一
#     具体参考步骤6第3点中的代码注释
#from QcloudApi.qcloudapi import QcloudApi 
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
    'networkInterfaceId': '您的主服务器的主网卡ID',
    'secondaryPrivateIpAddressCount': '您需要申请IP地址的个数'

}

try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
       
```
        
### 步骤2. 主备子机安装 keepalived（1.2.8 版本以上）
以 CentOS 为例：
`yum –y install keepalived`

### 步骤3.    keepalived.conf 配置单播模式
编辑文件```/etc/keepalived/keepalived.conf```，除基本 keepalived 的 VRRP 配置外，注意需要配置单播模式，即指定对端设备的 IP 地址，在 keepalived.conf 的 vrrp_instance 项中指定单播模式：

```
vrrp_instance VI_1 {
    #注意主备参数选择
    state MASTER  #主
	#state BACKUP  #备
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    unicast_peer {
        10.0.0.1    #对端设备的 IP 地址，例如：10.0.0.1
    }
    virtual_ipaddress {
        10.100.0.27   #第一步申请的 VIP
    }
    nopreempt
    garp_master_delay 1
    garp_master_refresh 5
}
```

### 步骤 4.（可选）给 VIP 分配外网 IP
有两种控制台操作和云API操作两种方式：
- 控制台：先在控制台申请 EIP，绑定到**步骤 1** 中申请的内网 VIP，操作步骤 1 类似。
- 云API：[点击查看具体调用方式](https://cloud.tencent.com/doc/api/229/1377)。

### 步骤 5.   keepalived.conf 配置切换脚本
主备切换时，新切换为主的设备通过 notify 调用 vip.py 进行切换。

```
vrrp_sync_group G1 {
    group {
        VI_1
    }
    notify_master "/etc/keepalived/vip.py"
}

```
### 步骤 6. 验证主备倒换时 VIP 及外网 IP 是否正常切换
vip.py：通过云 API 开发主备切换程序，通过调用内网 IP 迁移的云 API 来进行 IP 地址的切换，以 Python 为例：

1) 下载 Python SDK
- [转到 github 查看 Python SDK >>](https://github.com/QcloudApi/qcloudapi-sdk-python)
- [点击下载 Python SDK >>](https://mc.qcloudimg.com/static/archive/b61ee1ce734e7437530304152c20ee14/qcloudapi-sdk-python-master.zip)

请仔细阅读其中 ```README.md```，并将 SDK 下载到```/etc/keepalived```目录中.

2) 云 API 密钥获取：

<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/ffd379c9e886d0ae3de4fba34539aac7/2.png)

</div>
<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/900df050c3d619566a482ff4e1bd5433/4.png)

</div>
3) 基于 SDK 开发切换调用云 API 的程序 vip.py，并将 vip.py 保存到```/etc/keepalived```目录，内网 IP 迁移云 API：

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pip安装使用方式：
	安装好python后执行如下步骤：
step1: yum install python-pip
step2: pip install qcloudapi-sdk-python
step3: 将代码中“from src.QcloudApi.qcloudapi import QcloudApi”改为“from QcloudApi.qcloudapi import QcloudApi”
step4: 编辑好代码并保存在/etc/keepalived试用

下载SDK源码直接使用方式：
	安装好python后执行如下步骤：
step1: 下载python-sdk: 网页操作https://github.com/QcloudApi/qcloudapi-sdk-python 
	或 linux执行"wget https://github.com/QcloudApi/qcloudapi-sdk-python/archive/master.zip"
step2: 将下载的sdk包放在/etc/keepalived并解压。修改解压后的文件夹名称为src，并在src文件夹下创建名为__init__.py的空白文件
step3: 将以下python代码保存成vip.py放到sdk的src同级目录, 编辑好内容试用 

具体参数参考: https://cloud.tencent.com/doc/api/245/1361
"""


#pip安装使用方式使用
from QcloudApi.qcloudapi import QcloudApi 

#SDK源码直接使用方式使用
#from src.QcloudApi.qcloudapi import QcloudApi


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

注意，主备设备上该 vip.py 中的迁移前后弹性网卡需要对调，需要给 vip.py 添加可执行属性:
`Chmod +x vip.py`
并手动执行 vip.py 检验,执行下面命令将触发 IP 地址迁移：
`/etc/keepalived/vip.py`

4)  启动 keepalived：`/etc/init.d/keepalived start`

5)  验证主备切换容灾效果：通过重启 keepalived 进程、重启子机等方式模拟主机故障，检测 VIP 是否能迁移。

#### 附件：keepalived.conf参考

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
    #注意主备参数选择
    state MASTER #主
	#state BACKUP #备
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    unicast_peer {
        10.0.0.1    #对端设备的IP地址，例如：10.0.0.1
    }
    virtual_ipaddress {
        10.100.0.27  #第一步申请的 VIP
    }
    nopreempt
    garp_master_delay 1
    garp_master_refresh 5
}
```
