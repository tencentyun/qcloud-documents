本文将介绍如何在腾讯云 VPC 内通过 keepalived 搭建高可用主备集群。

## 本文小引
为了更清晰地阐述 keepalived 如何在腾讯云主机上实践，本文：
- 首先对 keepalived 简述，并说明其在云主机的应用与物理网络的区别。
- 然后开始阐述如何通过何种步骤，达到两种使用模式：
 * 无常主模式，即双机选举主设备的优先级相同；
 * 常主常备模式，即需要让其中一台设备在无故障时尽量当主的场景。  常主常备模式较无常主模式增加了主备倒换次数， 推荐使用无常主模式（非常主常备模式）
- 本文通过给出若干 `keepalived 配置和脚本文件` + `不同场景配置方法`的形式，帮助用户在云主机上作本次实践。
- 本文主要介绍 keepalived 的 VRRP Instance 配置为单播 VRRP 报文的用法。

## 基本原理
通常高可用主备集群包含 2 台服务器，一台主服务器处于某种业务的激活状态（即 Active 状态），另一台备服务器处于该业务的备用状态（即 Standby 状态)，它们共享同一个 VIP（Virtual IP），同一时刻 VIP 只在一台主设备上生效，当主服务器出现问题，备用服务器接管 VIP 继续提供服务。高可用主备模式有着广泛的应用，例如：MySQL 主备切换、Ngnix Web 接入。
<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/a5aa34fb87508284d9e7a07898085728/1.png)

</div>
## 与物理网络的区别
在传统的物理网络中可以通过 keepalived 的 VRRP 协议协商主备状态，其原理是：主设备周期性发送免费 ARP 报文刷新上联交换机的 MAC 表或终端 ARP 表，触发 VIP 的迁移到主设备上。腾讯云 VPC 内支持部署 keepalived 来搭建主备高可用集群，与物理网络相比，主要区别是：
- 暂不支持通过免费 ARP 报文做 VIP 的迁移，而是通过调用云 API来绑定 VIP 到主设备上。


## 本文步骤预览
1.  申请 VIP，该 VIP 仅支持在子网内迁移（因此需要保证主备服务器位于同一个子网）。
2.  主备服务器安装及配置 keepalived (**1.3.5版本以上**)，并修改配置文件。**主备本机主 IP 仅有内网 IP 时，需要参考步骤 9 修改 SDK host**。
3.  编辑使用 keepalived  的 notify 机制，借助 notify_action.sh 和 vip.py，调用云 API 进行主备切换。
4.  编辑使用 keepalived 的 track_script 机制，借助 check_self.sh 和 vip.py，周期性执行检查脚本增强可用性。
5.  给 VIP 分配外网 IP。**（可选）**
6.  验证主备倒换时 VIP 及外网 IP 是否正常切换。

说明：由于本文给出了数个配置和脚本文件，为了更清晰地说明，**本节先给出各脚本的详细修改步骤**。然后您可以根据后文解决各步骤可能遇到的困难，如云 API 的使用，VIP 的申请等。**修改步骤预览如下：**

```
/etc/keepalived/
|-- check_self.sh
|-- keepalived.conf
|-- notify_action.sh
|-- README
`-- vip.py


常主常备用法使用步骤： 
主机操作： (常主)
    1. 安装 keepalived，给主网卡分配外网 IP 或弹性公网 IP。
    2. 在 keepalived 使用的配置目录/etc/keepalived/中，将本目录文件移入，并添加可执行权限 chmod +x /etc/keepalived/*.sh; chmod -x /etc/keepalived/keepalived.conf 
    3. 修改 keepalived.conf: 
        0) state            初始角色，主机填 MASTER, 备机填 BACKUP
        1) interface        改成本机网卡名 例如 eth0
        2) priority         主机值高于备，如：主 50 备 30 
        3) unicast_src_ip   改成本机内网 IP
        4) unicast_peer     改成对端机器内网 IP
        5) virtual_ipaddress    改成内网 vip 
        6) track_interface  改成本机网卡名 例如 eth0
    4. 修改 vip.py
        1) 第12行   interface   改成本机内网 IP，该 IP 要有外网 IP，否则步骤 9 修改 SDK host
        2) 第13行   vip         改成您的 VIP      
        3) 第14行   thisNetworkInterfaceId         改成本机的主机网卡 ID      
        4) 第15行   thatNetworkInterfaceId         改成对端机器的主机网卡 ID      
        5) 第16行   vpcId         改成您的 vpc ID      
        6) 第19-22行            填写您的 secretId 和您的 secretKey
    5. 修改 check_self.sh:
        1) 第3行    vip           改成内网 vip
        2) 第4行    interface     改成本机网卡名
        
备机操作：(常备)
    与主机操作类似

===================================================================================================================================

stable 用法使用步骤：(两台设备选举主机优先权相同, 非常主常备) (推荐！)
双机操作相同：
    1. 安装 keepalived，给主网卡分配外网IP或弹性公网IP
    2. 在 keepalived 使用的配置目录 /etc/keepalived/ 中，将本目录文件移入，并修改权限 chmod 744 /etc/keepalived/*.sh; chmod 644 /etc/keepalived/keepalived.conf 
    3. 修改 keepalived.conf: 
        0) state            初始角色，均填写 BACKUP
        1) interface        改成本机网卡名 例如 eth0
        2) priority         两台设备配置大小相同的整数，如 50
        3) unicast_src_ip   改成本机内网 IP
        4) unicast_peer     改成对端机器内网 IP
        5) virtual_ipaddress    改成内网 VIP 
        6) track_interface  改成本机网卡名 例如 eth0
    4. 修改 vip.py
        1) 第12行   interface   改成本机内网 IP，该IP要有外网 IP，否则步骤 9 修改 SDK host
        2) 第13行   vip         改成您的 vip      
        3) 第14行   thisNetworkInterfaceId         改成本机的主机网卡 ID      
        4) 第15行   thatNetworkInterfaceId         改成对端机器的主机网卡 ID      
        5) 第16行   vpcId         改成您的 vpc ID      
        6) 第19-22行            填写您的 secretId 和您的 secretKey
    5. 修改 check_self.sh:
        1) 第3行    vip           改成内网 VIP
        2) 第4行    interface     改成本机网卡名
        

注意：
    1. 脚本日志将会写到/var/log/keealived.log中。日志会占用您的磁盘空间。您可以自行借助 logrotate 等工具处理日志累积的问题
    2. keepalived 进程的日志仍会写到 /var/log/message 中。
        
```

## 详细步骤

### 步骤 1. 申请 VIP
在某个子网内申请 VIP（VPC 内用户主动申请的 IP 都可作为 VIP），**控制台或 云 API**均可申请，由于 VIP 绑定于弹性网卡上，弹性网卡分为主网卡和辅助网卡，而 VPC 内每台 CVM 在创建时会默认分配一个主网卡，因此您可以选择在主服务器所绑定的主弹性网卡上申请 VIP :

- **控制台**操作：点击查看 [在弹性网卡上分配内网 IP（Qcloud 控制台）](https://cloud.tencent.com/document/product/215/6513#.E5.88.86.E9.85.8D.E5.86.85.E7.BD.91ip.EF.BC.88qcloud.E6.8E.A7.E5.88.B6.E5.8F.B0.EF.BC.8910) （推荐） 

>**注意：**
 1. 这个操作的重点是给网卡分配内网IP，而不是分配另一个网卡。
 2. 注意：不要把vip配置到/etc/sysconfig/network-scripts/的脚本中
 1. 后续配置完成后，在主备设备上启用 keepalived 服务，可以看到 VIP 出现在主设备上，并可以从 VPC 其它子机内 ping 通该 VIP 或外网 VIP。（请同时注意安全组对您主备云主机的网络隔离的功能，建议在实验阶段为主备云主机设置全通安全组）
 2. 申请到 VIP 后，云主机内不会自动在网卡配置上 VIP，但 VPC 管理平台已为您建立好了 VIP 相关功能。但云主机内不会自动感知自己有这个VIP，以下两种方式可以让你在云主机内看见网卡内看见vip。
1） 未使用本文配置的 keepalived 管理Vip时，需要您在分配内网 IP 后，在云服务器内配置该内网 IP 才能使 VIP 在云主机内可见，点击查看[分配内网IP（云服务器系统内）的方法](https://cloud.tencent.com/document/product/215/6513#.E5.88.86.E9.85.8D.E5.86.85.E7.BD.91ip.EF.BC.88.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E7.B3.BB.E7.BB.9F.E5.86.85.EF.BC.8911) 。 云主机内配置命令： `ip addr add $vip dev $ethX` ；查看命令：`ip addr show $ethx`
2）本文配置的 keepalived 可在使用时帮您在云主机网卡配置 VIP 实现云主机内可见。  注意：用keepalived管理时，不要把vip配置到/etc/sysconfig/network-scripts/的脚本中。


### 步骤 2. 主备子机安装 keepalived（1.3.5 版本以上）
- 安装
以 CentOS 为例：
`yum –y install keepalived`

### 步骤 3. 确定主备需求
本文并行介绍两种使用模式：
- 无常主模式，即双机选举主设备的优先级相同；
- 常主常备模式，即需要让其中一台设备在无故障时尽量当主的场景。  

常主常备模式较无常主模式增加了主备倒换次数，推荐使用无常主模式（非常主常备模式）

### 步骤 4. 修改配置 keepalived.conf
- 配置文件修改

```
    常主常备模式步骤，以主设备为例，修改 keepalived.conf: 
        0) state            初始角色，主机填 MASTER, 备机填 BACKUP
        1) interface        改成本机网卡名 例如 eth0
        2) priority         主机值高于备，如：主 50 备 30 
        3) unicast_src_ip   改成本机内网 IP
        4) unicast_peer     改成对端机器内网 IP
        5) virtual_ipaddress    改成内网 VIP 
        6) track_interface  改成本机网卡名 例如 eth0
   非常主常备步骤，双机改法相同，修改 keepalived.conf: 
        0) state            初始角色，均填写 BACKUP
        1) interface        改成本机网卡名 例如 eth0
        2) priority         两台设备配置大小相同的整数，如 50
        3) unicast_src_ip   改成本机内网 IP
        4) unicast_peer     改成对端机器内网 IP
        5) virtual_ipaddress    改成内网 VIP  
        6) track_interface  改成本机网卡名 例如 eth0
 
 ```

> **注意：**需要配置单播模式是很重要的，即指定对端设备的 IP 地址。


```
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

vrrp_script checkhaproxy
{
    script "/etc/keepalived/check_self.sh"
    interval 5
}

vrrp_instance VI_1 {
    #注意主备参数选择
    state MASTER            #主   #修改点, 主机为 MASTER，备机为 BACKUP
#state BACKUP           #备
    interface eth0          #改成本机网卡名 例如 eth0  
    virtual_router_id 51
    nopreempt                   #非抢占模式
#    preempt_delay 10
    priority 50             #主高于备, 例如 主 50，备 30
    advert_int 1        
    authentication {
        auth_type PASS
        auth_pass 1111
    }
        unicast_src_ip 10.0.1.17   #本机内网 IP
    unicast_peer {
        10.0.1.16           #对端设备的 IP 地址，例如：10.0.0.1
    }
    virtual_ipaddress {
        10.0.1.100          #内网 VIP 
    }

    notify_master "/etc/keepalived/notify_action.sh MASTER"
    notify_backup "/etc/keepalived/notify_action.sh BACKUP"
    notify_fault "/etc/keepalived/notify_action.sh FAULT"
    notify_stop "/etc/keepalived/notify_action.sh STOP"
    garp_master_delay 1
    garp_master_refresh 5

        track_interface {
                eth0                #改成本机网卡名 例如 eth0
        }

    track_script {
        checkhaproxy 
    }
}
```
### 步骤 5. 修改 notify_action.sh 帮助云主机在故障时角色切换

```
    常主常备模式步骤. 修改 notify_action.sh:
        1) 无
    非常主常备模式步骤. 修改 notify_action.sh:
        1) 无
```

```
#!/bin/bash
#/etc/keepalived/notify_action.sh
log_file=/var/log/keepalived.log
log_write()
{
    echo "[`date '+%Y-%m-%d %T'`] $1" >> $log_file
}

[ ! -d /var/keepalived/ ] && mkdir -p /var/keepalived/

case "$1" in
    "MASTER" )
        echo -n "$1" > /var/keepalived/state
        log_write " notify_master" 
        echo -n "0" > /var/keepalived/vip_check_failed_count       
        python /etc/keepalived/vip.py migrate &
        ;;

    "BACKUP" )
        echo -n "$1" > /var/keepalived/state
        log_write " notify_backup" 
        ;;

    "FAULT" )
        echo -n "$1" > /var/keepalived/state
        log_write " notify_fault" 
        ;;

    "STOP" )
        echo -n "$1" > /var/keepalived/state
        log_write " notify_stop" 
        ;;
    *)
        log_write "notify_action.sh: STATE ERROR!!!"
        ;;
esac
```
### 步骤 6. 修改 vip.py 帮助您在云主机之间迁移 VIP 和查询本机当前 IP

vip.py：通过云 API 开发主备切换程序，通过调用内网 IP 迁移的云 API 来进行 IP 地址的切换，以 Python 为例：

1) 下载 Python SDK
- pip 安装使用方式
	- yum install python-pip
	- pip install qcloudapi-sdk-python
- github 源码下载方式
	- [转到 github 查看 Python SDK >>](https://github.com/QcloudApi/qcloudapi-sdk-python)
	- [点击下载 Python SDK >>](https://mc.qcloudimg.com/static/archive/b61ee1ce734e7437530304152c20ee14/qcloudapi-sdk-python-master.zip)

请仔细阅读其中`README.md`，并将 SDK 下载到`/etc/keepalived`目录中.
2) 全内网环境的host修改
- 若您的主备云主机的网卡主 IP 没有外网 IP，您可以参考步骤 9，修改 SDK 使用的 host，达到对云 API 的内网调用。

3) 云 API 密钥获取：

<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/ffd379c9e886d0ae3de4fba34539aac7/2.png)

</div>
<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/900df050c3d619566a482ff4e1bd5433/4.png)

</div>
4) 基于 SDK 开发切换调用云 API 的程序 vip.py，并将 vip.py 保存到```/etc/keepalived```目录，用于调用内网 IP 迁移云 API：
- 从控制台云主机详情页弹性网卡标签下找到主网卡 ID：
![](//mc.qcloudimg.com/static/img/fa9fc6b8995bef9734c8de9cb004543c/image.png)
- 修改代码参数（注意python对缩进的严格要求）后使用

```
    常主常备模式步骤: 修改 vip.py
        1) 第12行   interface   改成本机内网 IP，该 IP 要有外网 IP，否则步骤 9 修改 SDK host
        2) 第13行   vip         改成您的 VIP       
        3) 第14行   thisNetworkInterfaceId         改成本机的主机网卡 ID      
        4) 第15行   thatNetworkInterfaceId         改成对端机器的主机网卡 ID      
        5) 第16行   vpcId         改成您的 vpc ID      
        6) 第19-22行            填写您的 secretId 和您的 secretKey
    非常主常备模式步骤: 修改 vip.py
        1) 第12行   interface   改成本机内网 IP，该 IP 要有外网 IP，否则步骤9修改SDK host
        2) 第13行   vip         改成您的 VIP       
        3) 第14行   thisNetworkInterfaceId         改成本机的主机网卡 ID      
        4) 第15行   thatNetworkInterfaceId         改成对端机器的主机网卡 ID      
        5) 第16行   vpcId         改成您的 vpc ID      
        6) 第19-22行            填写您的 secretId 和您的 secretKey
```

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
#/etc/keepalived/vip.py

"""
#注意python代码的缩进须与本文一致
pip 安装使用方式：
	安装好 Python 后执行如下步骤：
step1:  yum install python-pip
step2:  pip install qcloudapi-sdk-python
step3: 将代码中“from src.QcloudApi.qcloudapi import QcloudApi”改为“from QcloudApi.qcloudapi import QcloudApi”
step4: 编辑好代码并保存在/etc/keepalived试用

下载 SDK 源码直接使用方式：
	安装好 Python 后执行如下步骤：
step1: 下载 python-sdk: 网页操作https://github.com/QcloudApi/qcloudapi-sdk-python 
	或 linux执行"wget https://github.com/QcloudApi/qcloudapi-sdk-python/archive/master.zip"；
step2: 将下载的 SDK 包放在 /etc/keepalived 并解压。修改解压后的文件夹名称为 src，并在 src 文件夹下创建名为__init__.py的空白文件；
step3: 将以下 python 代码保存成 vip.py 放到 SDK 的 src 同级目录, 编辑好内容试用 。

具体参数参考: https://cloud.tencent.com/doc/api/245/1361
"""


import os
import time
import json
import sys
from QcloudApi.qcloudapi import QcloudApi 	#pip 安装使用方式使用 -- 推荐
#from src.QcloudApi.qcloudapi import QcloudApi 	#源码 安装使用方式使用

#当前机器主网卡和主 IP
interface = {"eth0":"10.0.1.17"}            #该 IP 要有外网 IP
vip = "10.0.1.100"                          #改成您的本机内网 VIP
thisNetworkInterfaceId = 'eni-pvsvph0u'     #IP 迁移后所在的弹性网卡 ID(本机网卡 ID)
thatNetworkInterfaceId = 'eni-qnxioxyi'     #IP 迁移前所在的弹性网卡 ID(对端主机网卡 ID)


vpcId = 'vpc-1yxuk010'                      #vpcId

config = {
    'Region': 'bj',                      #您的地域
    'secretId': '您的secretId',              #您的 secretId
    'secretKey': '您的secretKey',        #您的 secretKey
    'method': 'post'
}


log = open('/var/log/keepalived.log', 'a+')
state_file = open('/var/keepalived/state', 'r')

def get_now_time():
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time())) + '[pid' + str(os.getpid()) + ']' 

def log_write(message=''):
    log.write(get_now_time() + " " + str(message) + "\n")

def get_ip():
    f = os.popen('ip addr show dev %s | grep %s | awk \'{print $2}\' | awk -F/ \'{print $1}\'' % (interface.keys()[0] , interface.values()[0]))
    return f.read().strip()


def migrateVip():
    module = 'vpc'
    action = 'MigratePrivateIpAddress'
    params = {
        'vpcId': vpcId,             #vpcId 本行毋须修改
        'privateIpAddress': vip,      #VIP  本行毋须修改
        'oldNetworkInterfaceId': thatNetworkInterfaceId, #IP 迁移前所在的弹性网卡 ID(对端主机网卡 ID)   本行毋须修改
        'newNetworkInterfaceId': thisNetworkInterfaceId  #IP 迁移后所在的弹性网卡 ID(本机网卡 ID)   本行毋须修改
    }
    
    log_write(sys.argv[1])
    log_write(" try set vip.")
    retry_times_when_mgr_ip_got = 4
    exceptimes = 0
    get_ip_times = 0
    time.sleep(0.5)
    while get_ip_times < 5:
        log_write(" get_ip=" + get_ip())
        if get_ip()==interface.values()[0]:
            log_write(" now set vip.")
            try:
                service = QcloudApi(module, config)
                ret = service.generateUrl(action, params)
                log_write(" generateUrl ret " + ret)
                i = 0
                while i < retry_times_when_mgr_ip_got:
                    check_vip_str = queryVip()
                    if check_vip_str == "true":
                        break 
                    state_file.seek(0)
                    state = state_file.readline()
                    if state != 'MASTER':
                        break 
                    ret = service.call(action, params)
                    ret_json = json.loads(ret)
                    log_write(" call ret " + ret)
                    #log_write(" last_code_mark: " + str(ret_json.get("code"))) 
                    if ret_json.get("code") == 0:
                        log_write(" set done")
                        break
                    if ret_json.get("code") == 6300:
                        break
                    i = i + 1
                    time.sleep(2)
                if i >= retry_times_when_mgr_ip_got:
                    log_write(" set vip failed")
                break
            except Exception, e:
                log_write(' exception:' + str(e))
                exceptimes = exceptimes + 1
                if exceptimes > 3:
                    break
        time.sleep(0.5)
        get_ip_times = get_ip_times + 1
    log_write("vip.py checks vip: is this cvm holding the vip? " + queryVip())


def queryVip():
    module = 'vpc'
    action = 'DescribeNetworkInterfaces'
    params = {
        "networkInterfaceId": thisNetworkInterfaceId  #您的本机网卡 ID     本行毋须修改
    }

    result = 'true'
    return_json_str = None
    try:
        service = QcloudApi(module, config)
        ret = service.generateUrl(action, params)
        ret = service.call(action, params)
        return_json_str = ret
        ret_json = json.loads(ret)
        if ret_json.get("code") == 0:
            eni_data = ret_json['data']['data'][0]['privateIpAddressesSet']
            privateIpAddressSet = set([k['privateIpAddress'] for k in eni_data])
            if len(privateIpAddressSet) > 0 and vip not in privateIpAddressSet:
                log_write(" vip not in master in qcloud")
                result = 'false'
        else:
            log_write("call ret: " + return_json_str)
            log_write("attempt query vip failed")
    except Exception, e:
        log_write("call ret: " + return_json_str)
        log_write(' exception:' + str(e))
        exceptimes = exceptimes + 1
    return result



def print_help():
    log_write(
            '''
            ./vip.py migrate
                migrate your vip
                    
            ./vip.py query
                query that if this cvm hold your vip in tencent cloud
                return: true or false
            ''')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        log_write("vip.py: parameter num is 0")
        print_help()
    elif sys.argv[1] == 'migrate':
        migrateVip()   
        log_write()
    elif sys.argv[1] == 'query':
        print queryVip()
    else:
        log_write("vip.py: misMatched parameter")
        print_help()
```
### 步骤 7. 修改 check_self.sh 增强 keepalived 处理故障的能力

```
    常主常备模式步骤:  修改 check_self.sh:
        1) 第3行    vip           改成内网 VIP
        2) 第4行    interface     改成本机网卡名
    非常主常备模式步骤:  修改check_self.sh:
        1) 第3行    vip           改成内网 VIP
        2) 第4行    interface     改成本机网卡名
```
```
#!/bin/bash 
#/etc/keepalived/check_self.sh
vip=10.0.1.100 #请您改成内网 VIP
interface=eth0 #您的网络接口名

state_file=/var/keepalived/state
vip_last_check_result_file=/var/keepalived/vip_last_check_result
vip_operater=/etc/keepalived/vip.py
state=`cat $state_file`


log_file=/var/log/keepalived.log
log_write()
{
    echo "[`date '+%Y-%m-%d %T'`] $1" >> $log_file
}

[ ! -d /var/keepalived/ ] && mkdir -p /var/keepalived/
[ ! -f $vip_last_check_result_file ] && touch $vip_last_check_result_file 
[ ! -f $state_file ] && echo -n "FAULT" > $state_file 

CMD=`ip addr show dev $interface | grep $vip | awk '{print $2}' | awk -F/ '{print $1}'| wc -l`

case $state in
    "MASTER") 
        if [ ${CMD} -ne 1 ]; then
            log_write "it is detected no vip on nic in cvm in MASTER state, add vip on this nic" 
            ip addr add $vip dev $interface
            echo -n "false" > $vip_last_check_result_file
        else
            is_vip_in_master=`timeout 3 python $vip_operater query`
            if [ "x$is_vip_in_master" == "xfalse" ]; then
                echo -n "false" > $vip_last_check_result_file
                python $vip_operater migrate &
            elif [ "x$is_vip_in_master" == "xtrue" ]; then
                vip_last_check_result=`cat $vip_last_check_result_file`
                [ "x$vip_last_check_result" == "xfalse" ] && log_write " vip_check pass"
                echo -n "true" > $vip_last_check_result_file
            else
                log_write "$vip_operater check vip time out" 
            fi
        fi
        exit 0
        ;;

    *) 
        if [ ${CMD} -ne 0 ]; then
            sleep 2  
            CMD=`ip addr show dev eth0 | grep $vip | awk '{print $2}' | awk -F/ '{print $1}'| wc -l`
            if [ ${CMD} -ne 0 ]; then
                log_write "detect vip in non-MASTER status, so ystemctl restart keepalived" 
                ip addr del $vip dev $interface
                systemctl restart keepalived &
                exit 1
            fi
        fi
        exit 0
        ;;
esac
```

### 步骤 8.（可选）给 VIP 分配外网 IP
- 控制台：先在控制台申请 EIP，绑定到**步骤 1** 中申请的内网 VIP，操作与步骤 1 类似。


### 步骤 9.主备云主机本机主 IP 没有外网IP的使用方式（全内网环境调用帮助）
由于云 API Python SDK 的默认 host 是外网 host，无法走内网访问。如果您的主备云主机的本机 IP 只有内网 IP，没有外网 IP，则需求将 Python SDK 进行修改，将 host 改成内网云 API 访问域名。修改步骤如下：
 - 确认自己的 SDK 安装方式：是 pip 方式安装，还是直接下载源码安装到/etc/keepalived/的？
 - 装方式确认修改 host 的文件的路径。
	  - 源码方式安装则修改 /etc/keepalived/src/QcloudApi/modules/vpc.py
	  - pip 方式安装则修改 /usr/lib/pythonX.Y/site-packages/QcloudApi/modules/vpc.py  (pythonX.Y依实际，如python2.6)
 - `requestHost = 'vpc.api.qcloud.com'` 修改为 `requestHost = 'vpc.api.tencentyun.com'`

### 步骤 10. 验证主备倒换时 VIP 及外网 IP 是否正常切换
1. 启动 keepalived：`/etc/init.d/keepalived start` 或 `systemctl start keepalived` 或 `service keepalived start`

2. 验证主备切换容灾效果：通过重启 keepalived 进程、重启子机等方式模拟主机故障，检测 VIP 是否能迁移。/var/log/keepalived.log中同时会留下相应的日志。通过 ping VIP 或其 EIP 的方式，可以查看网络中断到恢复的时间间隔。
>说明：
1) 由于迁移 IP 以云 API 方式异步实现，需要数秒才能落地到新子机上。所以，常主常备模式式，主的故障时间**极短**时，可能发生两次短时间的主备状态倒换，但 VIP 重新落地到恢复的主机上需要较长时间（10s）。
2) 脚本日志将会写到`/var/log/keealived.log`中。日志会占用您的磁盘空间。您可以自行借助 logrotate 等工具处理日志累积的问题。keepalived 进程的日志仍会写到`/var/log/message`中。

