本文将介绍如何在腾讯云 VPC 内通过 keepalived 搭建高可用主备集群。

## 本文小引
为了更清晰地阐述 keepalived 如何在腾讯云主机上实践，本文：
- 首先对 keepalived 简述，并说明其在云主机的应用与物理网络的区别。
- 然后开始阐述如何通过何种步骤，达到两种使用模式：1) 无常主模式，即双机选举主设备的优先级相同；2) 常主常备模式，即需要让其中一台设备在无故障时尽量当主的场景。  常主常备模式较无常主模式增加了主备倒换次数，推荐使用无常主模式（非常主常备模式）
- 本文通过给出若干 keepalived 配置和脚本文件 + 不同场景配置方法的形式，帮助用户在云主机上作本次实践。


## 基本原理
通常高可用主备集群包含 2 台服务器，一台主服务器处于某种业务的激活状态（即 Active 状态），另一台备服务器处于该业务的备用状态（即 Standby 状态)，它们共享同一个 VIP（Virtual IP），同一时刻 VIP 只在一台主设备上生效，当主服务器出现问题，备用服务器接管 VIP 继续提供服务。高可用主备模式有着广泛的应用，例如：MySQL 主备切换、Ngnix Web 接入。
<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/a5aa34fb87508284d9e7a07898085728/1.png)

</div>
## 与物理网络的区别
在传统的物理网络中可以通过 keepalived 的 VRRP 协议协商主备状态，其原理是：主设备周期性发送免费 ARP 报文刷新上联交换机的 MAC 表或终端 ARP 表，触发 VIP 的迁移到主设备上。腾讯云 VPC 内支持部署 keepalived 来搭建主备高可用集群，与物理网络相比，主要有两个区别：
1)  暂不支持 VRRP 组播报文，需要将 keepalived 的 VRRP Instance 配置为单播 VRRP 报文。
2)  暂不支持通过免费 ARP 报文做 VIP 的迁移，而是通过调用云 API来绑定 VIP 到主设备上。




## 本文步骤预览
1.  申请 VIP，该 VIP 仅支持在子网内迁移（因此需要保证主备服务器位于同一个子网）。
2.  主备服务器安装及配置 keepalived (**1.3.5版本以上**)，并修改配置文件。
3.  编辑使用 keepalived  的 notify 机制，借助notify_action.sh和vip.py，调用云 API 进行主备切换。
4.  编辑使用 keepalived 的 track_script 机制，借助check_self.sh和query_vip.py，周期性执行检查脚本增强可用性。
5.  给 VIP 分配外网 IP。**（可选）**
6.  验证主备倒换时 VIP 及外网 IP 是否正常切换。

说明：由于本文给出了数个配置和脚本文件，为了更清晰地说明，**本节先给出各脚本的详细修改步骤**。然后您可以根据后文解决各步骤可能遇到的困难，如云api的使用，vip的申请等。**修改步骤预览如下：**
```
常主常备用法使用步骤：
主机操作： (常主)
    1. 安装keepalived
    2. 在keepalived使用的配置目录/etc/keepalived/中，将本目录文件移入
    3. 修改keepalived.conf: 
        0) state            初始角色，主机填MASTER, 备机填BACKUP
        1) interface        改成本机网卡名 例如eth0
        2) priority         主机值高于备于，如：主50备30 
        3) unicast_src_ip   改成本机内网IP
        4) unicast_peer     改成对端机器内网IP
        5) virtual_ipaddress    改成内网vip 
        6) track_interface  改成本机网卡名 例如eth0
    4. 修改query_vip.py:
        1) 第11行   interface 改成本机内网IP
        2) 第12行   vip       改成内网vip
        3) 第16行至第20行     修改使用用户自己的对应参数，并填好地域。可参考官网文档
        4) 第23行             改成本机网卡id 
    5. 修改vip.py
        1) 第11行   interface 改成本机内网IP
        2) 第16第至25行     修改与 query_vip.py修改类似， 注意第24行填对端网卡ID，第25行填写本机网卡ID
    6. 修改check_self.sh:
        1) 第3行    vip           改成内网vip
        2) 第4行    interface     改成本机网卡名
        
备机操作：(常备)
    与主机操作类似

===================================================================================================================================

stable用法使用步骤：(两台设备选举主机优先权相同)
双机操作相同：
    1. 安装keepalived
    2. 在keepalived使用的配置目录/etc/keepalived/中，将本目录文件移入
    3. 修改keepalived.conf: 
        0) state            初始角色，均填写BACKUP
        1) interface        改成本机网卡名 例如eth0
        2) priority         两台设备配置大小相同的整数，如50
        3) unicast_src_ip   改成本机内网IP
        4) unicast_peer     改成对端机器内网IP
        5) virtual_ipaddress    改成内网vip 
        6) track_interface  改成本机网卡名 例如eth0
    4. 修改query_vip.py:
        1) 第11行   interface 改成本机内网IP
        2) 第12行   vip       改成内网vip
        3) 第16行至第20行     修改使用用户自己的对应参数，并填好地域。可参考官网文档
        4) 第23行             改成本机网卡id 
    5. 修改vip.py
        1) 第11行   interface 改成本机内网IP
        2) 第16第至25行     修改与 query_vip.py修改类似， 注意第24行填对端网卡ID，第25行填写本机网卡ID
    6. 修改check_self.sh:
        1) 第3行    vip           改成内网vip
        2) 第4行    interface     改成本机网卡名
        
```

## 详细步骤

### 步骤 1.    申请VIP
在某个子网内申请VIP（VPC内用户主动申请的IP都可作为VIP），**控制台 或 云API**均可申请，由于VIP绑定于弹性网卡上，弹性网卡分为主网卡和辅助网卡，而VPC内每台CVM在创建时会默认分配一个主网卡，因此您可以选择在主服务器所绑定的主弹性网卡上申请VIP :


- 方式1 **控制台**方式：点击查看[在弹性网卡上  分配内网IP（Qcloud控制台）](https://cloud.tencent.com/document/product/215/6513#.E5.88.86.E9.85.8D.E5.86.85.E7.BD.91ip.EF.BC.88qcloud.E6.8E.A7.E5.88.B6.E5.8F.B0.EF.BC.8910) （推荐）

- 方式2 **云API** 方式：**通过云 API 分配 申请VIP 具体操作(云API代码开发指引请参考第6步)：** 

 > 注意 1：后续配置完成后，在主备设备上启用keepalived服务，可以看到VIP出现在主设备上，并可以从VPC其它子机内ping通该VIP或外网VIP。（请同时注意安全组对您主备云主机的网络隔离的功能，建议在实验阶段为主备云主机设置全通安全组）
 > 注意 2：申请到VIP后，云主机内不会自动在网卡配置上VIP，但VPC管理平台已为您建立好了VIP相关功能。1） VIP不用于keepalived时，需要您在分配内网IP后，在云服务器内配置该内网IP才能使VIP在云主机内可见，**点击查看[分配内网IP（云服务器系统内）的方法](https://cloud.tencent.com/document/product/215/6513#.E5.88.86.E9.85.8D.E5.86.85.E7.BD.91ip.EF.BC.88.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E7.B3.BB.E7.BB.9F.E5.86.85.EF.BC.8911) 。 2）本文配置的keepalived可在使用时帮您在云主机网卡配置VIP实现云主机内可见。

1) 通过云`API:DescribeNetworkInterfaces`得到云服务器的主网卡的`networkInterfaceId`（入参填写：**私有网络 ID**和**云服务器的 ID**即可）。[点击查看 API 详情](https://cloud.tencent.com/doc/api/245/4814)
2) 通过云`API:AssignPrivateIpAddresses`在弹性网卡上申请内网 VIP 的，申请 VIP 操作可参考以下  Python 代码：[点击查看 API 详情](https://cloud.tencent.com/doc/api/245/4817)   **若您通过方式1控制台申请VPC，可以跳过下段代码。**
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
        
### 步骤 2. 主备子机安装 keepalived（1.3.5 版本以上）
- 安装
以 CentOS 为例：
`yum –y install keepalived`

### 步骤 3. 确定主备需求
- 本文并行介绍两种使用模式：1) 无常主模式，即双机选举主设备的优先级相同；2) 常主常备模式，即需要让其中一台设备在无故障时尽量当主的场景。  
- 常主常备模式较无常主模式增加了主备倒换次数，推荐使用无常主模式（非常主常备模式）

### 步骤 4. 修改配置keepalived.conf
- 配置文件修改

```
    常主常备模式步骤，以主设备为例，修改keepalived.conf: 
        0) state            初始角色，主机填MASTER, 备机填BACKUP
        1) interface        改成本机网卡名 例如eth0
        2) priority         主机值高于备于，如：主50备30 
        3) unicast_src_ip   改成本机内网IP
        4) unicast_peer     改成对端机器内网IP
        5) virtual_ipaddress    改成内网vip 
        6) track_interface  改成本机网卡名 例如eth0
   非常主常备步骤，双机改法相同，修改keepalived.conf: 
        0) state            初始角色，均填写BACKUP
        1) interface        改成本机网卡名 例如eth0
        2) priority         两台设备配置大小相同的整数，如50
        3) unicast_src_ip   改成本机内网IP
        4) unicast_peer     改成对端机器内网IP
        5) virtual_ipaddress    改成内网vip 
        6) track_interface  改成本机网卡名 例如eth0
 
 ```

> 注意：需要配置单播模式是很重要的，即指定对端设备的 IP 地址


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
    #state MASTER            #主   #仅为初始状态, 主机为MASTER，备机为BACKUP
    state BACKUP           #备   #仅为初始状态
    interface eth0          #改成本机网卡名 例如eth0  
    virtual_router_id 51
    nopreempt                   #非抢占模式
    #preempt_delay 10
    priority 50             #常主高于常备, 例如 主50，备30；无常主时双机配相同大小值; 无常主的使用方式更加稳定和高可用
    advert_int 1        
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    unicast_src_ip 10.0.1.17   #本机内网IP
    unicast_peer {
        10.0.1.16           #对端设备的 IP 地址，例如：10.0.0.1
    }
    virtual_ipaddress {
        10.0.1.100          #内网VIP 
    }

    notify_master "/etc/keepalived/notify_action.sh MASTER"
    notify_backup "/etc/keepalived/notify_action.sh BACKUP"
    notify_fault "/etc/keepalived/notify_action.sh FAULT"
    garp_master_delay 1
    garp_master_refresh 5

    track_interface {
        eth0                #改成本机网卡名 例如eth0
    }

    track_script {
        checkhaproxy 
    }
}
```
### 步骤 5. 修改notify_action.sh帮助云主机在故障时角色切换

```
    常主常备模式步骤. 修改notify_action.sh:
        1) 无
    非常主常备模式步骤. 修改notify_action.sh:
        1) 无
```

```
#!/bin/bash
#/etc/keepalived/notify_action.sh
log_file=/etc/keepalived/log
log_write()
{
        echo "[`date '+%Y-%m-%d %T'`] $1" >> $log_file
}

mkdir -p /var/keepalived/
if [ $1 == 'MASTER' ]; then
        echo -n "$1" > /var/keepalived/state
        log_write " notify_master" 
        echo -n "0" > /var/keepalived/vip_check_failed_count       
        /etc/keepalived/vip.py &
fi

if [ $1 == 'BACKUP' ]; then
        echo -n "$1" > /var/keepalived/state
        log_write " notify_backup" 
fi

if [ $1 == 'FAULT' ]; then
        echo -n "$1" > /var/keepalived/state
        log_write " notify_fault" 
fi
```

### 步骤 6. 修改vip.py帮助您在云主机之间迁移VIP

vip.py：通过云 API 开发主备切换程序，通过调用内网 IP 迁移的云 API 来进行 IP 地址的切换，以 Python 为例：

1) 下载 Python SDK
- pip安装使用方式
	- yum install python-pip
	- pip install qcloudapi-sdk-python
- github源码下载方式
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
3) 基于 SDK 开发切换调用云 API 的程序 vip.py，并将 vip.py 保存到```/etc/keepalived```目录，用于调用内网 IP 迁移云 API：

```
    常主常备模式步骤: 修改vip.py
        1) 第11行   interface 改成本机内网IP
        2) 第16第至25行     修改与 query_vip.py修改类似， 注意第24行填对端网卡ID，第25行填写本机网卡ID
    非常主常备模式步骤: 修改vip.py
        1) 第11行   interface 改成本机内网IP
        2) 第16第至25行     修改与 query_vip.py修改类似， 注意第24行填对端网卡ID，第25行填写本机网卡ID
```

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
#/etc/keepalived/vip.py

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
import os
import time
import json
from QcloudApi.qcloudapi import QcloudApi 

#当前机器主网卡和主IP
interface = {"eth0":"10.0.1.17"}

module = 'vpc'
action = 'MigratePrivateIpAddress'
config = {
    'Region': 'bj',  #改成您操作的地域
    'secretId': '您的secretId',  #您的secretId
    'secretKey': '您的secretKey', #您的secretKey
    'method': 'post'
}
params = {
    'vpcId': 'vpc-1yxuk010',    #VPCID
    'privateIpAddress': '10.0.1.100',   #VIP
    'oldNetworkInterfaceId': 'eni-pvsvph0u',  #IP迁移前所在的弹性网卡ID
    'newNetworkInterfaceId': 'eni-qnxioxyi'   #IP迁移后所在的弹性网卡ID
}

#time.sleep(3)
log = open('/etc/keepalived/log', 'a+')
state_file = open('/var/keepalived/state', 'r')
def get_now_time():
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time())) + '[pid' + str(os.getpid()) + ']' 

def get_ip():
    f = os.popen('ip addr show dev %s | grep %s | awk \'{print $2}\' | awk -F/ \'{print $1}\'' % (interface.keys()[0] , interface.values()[0]))
    return f.read().strip()

log.write(get_now_time() + " try set vip.\n")
retry_times_when_mgr_ip_got = 4
exceptimes = 0
get_ip_times = 0
time.sleep(0.5)
while get_ip_times < 5:
    log.write(get_now_time() + " get_ip=" + get_ip() + "\n")
    if get_ip()==interface.values()[0]:
        log.write(get_now_time() + " now set vip.\n")
        try:
            service = QcloudApi(module, config)
            ret = service.generateUrl(action, params)
            log.write(get_now_time() + " generateUrl ret " + ret + "\n")
            i = 0
            while i < retry_times_when_mgr_ip_got:
                state_file.seek(0)
                state = state_file.readline()
                if state != 'MASTER':
                    break 
                ret = service.call(action, params)
                ret_json = json.loads(ret)
                log.write(get_now_time() + " call ret " + ret + "\n")
                log.write(get_now_time() + " last_code_mark: " + str(ret_json.get("code")) + "\n") 
                if ret_json.get("code") == 0:
                    log.write(get_now_time() + " set done\n")
                    break
                if ret_json.get("code") == 6300:
                    break
                i = i + 1
                time.sleep(2)
            if i >= retry_times_when_mgr_ip_got:
                log.write(get_now_time() + " set vip failed\n")
            break
        except Exception, e:
            log.write(get_now_time() + ' exception:' + str(e) + '\n')
            exceptimes = exceptimes + 1
            if exceptimes > 3:
                break
    time.sleep(0.5)
    get_ip_times = get_ip_times + 1
print 'done'

```
### 步骤 7. 修改check_self.sh增强keepalived处理故障的能力

```
    常主常备模式步骤:  修改check_self.sh:
        1) 第3行    vip           改成内网vip
        2) 第4行    interface     改成本机网卡名
    非常主常备模式步骤:  修改check_self.sh:
        1) 第3行    vip           改成内网vip
        2) 第4行    interface     改成本机网卡名
```
```
#!/bin/bash 
#/etc/keepalived/check_self.sh
vip=10.0.1.100 #请您改成内网vip
interface=eth0 #您的网络接口名

state_file=/var/keepalived/state
vip_check_failed_count_file=/var/keepalived/vip_check_failed_count
vip_retry_failed_count_file=/var/keepalived/vip_retry_failed_count
vip_last_check_result_file=/var/keepalived/vip_last_check_result
query_vip_asker=/etc/keepalived/query_vip.py
vip_migrater=/etc/keepalived/vip.py
state=`cat $state_file`


log_file=/etc/keepalived/log
log_write()
{
        echo "[`date '+%Y-%m-%d %T'`] $1" >> $log_file
}

CMD=`ip addr show dev $interface | grep $vip | awk '{print $2}' | awk -F/ '{print $1}'| wc -l`
if [ $state == "MASTER" ]; then
        if [ ${CMD} -ne 1 ]; then
            log_write "it is detected no vip on nic in cvm in MASTER state, add vip on this nic" 
        ip addr add $vip dev $interface
    else
        is_vip_in_master=`$query_vip_asker`
        if [ $is_vip_in_master == "false" ]; then
            echo "false" > $vip_last_check_result_file
            $vip_migrater &
        else
            vip_last_check_result=`cat $vip_last_check_result_file`
                [ $vip_last_check_result == "false" ] && log_write " vip_check pass"
            echo "true" > $vip_last_check_result_file
        fi
    fi

        exit 0
fi

if [ $state == "BACKUP" -o $state == "FAULT" ]; then
        if [ ${CMD} -ne 0 ]; then
                sleep 2  #用于keepalived启动时，vip还未配置完成的情况; 防止启动keepalived时误判所导致的keepalived循环重启
                CMD=`ip addr show dev eth0 | grep $vip | awk '{print $2}' | awk -F/ '{print $1}'| wc -l`
                if [ ${CMD} -ne 0 ]; then
                                log_write "detect vip in non-MASTER status, so ystemctl restart keepalived" 
                ip addr del $vip dev $interface
                    systemctl restart keepalived &
                    exit 1
                fi
        fi
        exit 0
fi
```
### 步骤 8. 修改query_vip.py增强keepalived处理故障的能力
```
    常主常备模式步骤:   修改query_vip.py:
        1) 第11行   interface 改成本机内网IP
        2) 第12行   vip       改成内网vip
        3) 第16行至第20行     修改使用用户自己的对应参数，并填好地域。可参考官网文档
        4) 第23行             改成本机网卡id 
    非常主常备模式步骤:   修改query_vip.py:
        1) 第11行   interface 改成本机内网IP
        2) 第12行   vip       改成内网vip
        3) 第16行至第20行     修改使用用户自己的对应参数，并填好地域。可参考官网文档
        4) 第23行             改成本机网卡id 
```
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

#pip安装使用方式使用
import os
import time
import json
from QcloudApi.qcloudapi import QcloudApi 

#当前机器主网卡和主IP
interface = {"eth0":"10.0.1.17"} #改成您的本机内网IP
vip = "10.0.1.100"  #改成您的本机内网VIP

module = 'vpc'
action = 'DescribeNetworkInterfaces'
config = {
    'Region': 'bj',  #改成您操作的地域
    'secretId': '您的secretId',  #您的secretId
    'secretKey': '您的secretKey', #您的secretKey
    'method': 'post'
}
params = {
    "networkInterfaceId": "eni-qnxioxyi"  #您的本机网卡ID
}

#time.sleep(3)
log_level = 2 
log = open('/etc/keepalived/log', 'a+')

def log_write(str):
    if log_level > 3:
        log.write(str)

def get_now_time():
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time())) + '[pid' + str(os.getpid()) + ']' 

def get_ip():
    f = os.popen('ip addr show dev %s | grep %s | awk \'{print $2}\' | awk -F/ \'{print $1}\'' % (interface.keys()[0] , interface.values()[0]))
    return f.read().strip()

log_write(get_now_time() + " try query vip.\n")
result = 'true'
log_write(get_now_time() + " now query vip.\n")
try:
    service = QcloudApi(module, config)
    ret = service.generateUrl(action, params)
    log_write(get_now_time() + " generateUrl ret " + ret + "\n")
    ret = service.call(action, params)
    log_write(get_now_time() + " call ret " + ret + "\n")
    ret_json = json.loads(ret)
    log_write(get_now_time() + " query vip last_code: " + str(ret_json.get("code")) + "\n") 
    if ret_json.get("code") == 0:
        eni_data = ret_json['data']['data'][0]['privateIpAddressesSet']
        privateIpAddressSet = set([k['privateIpAddress'] for k in eni_data])
        log_write(get_now_time() + " " + str(privateIpAddressSet) + "\n")
        if len(privateIpAddressSet) > 0 and vip not in privateIpAddressSet:
            log.write(get_now_time() + " vip not in master in qcloud\n")
            result = 'false'
        log_write(get_now_time() + " query vip done\n")
    else:
        log.write(get_now_time() + " query vip failed\n")
except Exception, e:
    log.write(get_now_time() + ' exception:' + str(e) + '\n')
    exceptimes = exceptimes + 1
print result
```
### 步骤 9.（可选）给 VIP 分配外网 IP
有两种控制台操作和云API操作两种方式：
- 控制台：先在控制台申请 EIP，绑定到**步骤 1** 中申请的内网 VIP，操作步骤 1 类似。
- 云API：[点击查看具体调用方式](https://cloud.tencent.com/doc/api/229/1377)。

### 步骤 10. 验证主备倒换时 VIP 及外网 IP 是否正常切换
1) 启动 keepalived：`/etc/init.d/keepalived start` 或 `systemctl start keepalived` 或 `service keepalived start`

2) 验证主备切换容灾效果：通过重启 keepalived 进程、重启子机等方式模拟主机故障，检测 VIP 是否能迁移。通过ping VIP 或其EIP的方式，可以查看网络中断到恢复的时间间隔。
说明：由于迁移IP以云API方式异步实现，需要数秒才能落地到新子机上。所以，常主常备模式式，主的故障时间**极短**时，可能发生两次短时间的主备状态倒换，但VIP重新落地到恢复的主机上需要较长时间（10s）。



