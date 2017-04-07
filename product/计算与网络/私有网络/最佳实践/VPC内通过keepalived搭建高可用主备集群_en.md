Here we will show you how to build a highly available master/slave cluster through keepalived in Tencent Cloud VPC.
## Basic Principle
Typically, the highly available master/slave cluster consists of two servers, the master server in the active state of a service (Active state) and the slave server in the standby state of the service (Standby state). Both servers share the same VIP (Virtual IP). The VIP can only be valid in one master device at a time. When the master server fails, the slave server will take over the VIP to continue providing services. Highly available master/slave mode has a wide range of applications, such as mysql master/slave switchover and Ngnix web access.
![](//mc.qcloudimg.com/static/img/a5aa34fb87508284d9e7a07898085728/1.png)

## The Difference from the Physical Network
In the traditional physical network, you can negotiate the master/slave state through the keepalived VRRP protocol. Principle: The master device periodically sends gratuitous ARP message to purge the MAC table or terminal ARP table of the uplink switch, triggering the VIP migration to the master device. Tencent Cloud VPC supports the deployment of keepalived to build a highly available master/slave cluster. Compared with the physical network, there are two main differences:
1) VRRP multicast message is currently not supported. You need to configure keepalived vrrp instance to unicast VRRP message.
2) Gratuitous ARP message is currently not supported for VIP migration. VIP is bound to the master device by calling Cloud APIs.

## How To
1. Apply for VIP, which only supports migration within subnet (the master and slave servers must be in the same subnet).
2. Install and configure keepalived (**Version 1.2.8 or above**) on master and slave servers.
3. Use the "notify" mechanism of keepalived to call the Cloud APIs for master/slave switchover.
4. (Optional) Assign public IPs to the VIP.
5. Verify whether the VIP and public IP are switched normally when the master/slave switchover occurs.

## Detailed Steps
### Step 1. Apply for VIP
Apply for a VIP in a subnet (any IP applied by users within the VPC can be used as VIP). Currently only Cloud API is supported. Please refer to Step 6 for the development instruction of Cloud API codes. VIP is bound on ENI (including the primary ENI and secondary ENI). A primary ENI will be assigned to each CVM in VPC by default when it's created, so you can apply for VIP on the primary ENI bound to the master server.
**The specific procedure is as follows:** 
1) Get the `networkInterfaceId` of CVM primary ENI (enter the input parameters: **VPC ID** and **CVM ID**) through the Cloud `API: DescribeNetworkInterfaces` [click to view the API details](https://www.qcloud.com/doc/api/245/4814).
2) When applying for Private IP in the ENI through the Cloud `API: AssignPrivateIpAddresses` [Click to view API details](https://www.qcloud.com/doc/api/245/4817), please refer to the following Python code for VIP application:

```
        
#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'vpc'
action = 'AssignPrivateIpAddresses'
config = {
    'Region': 'bj',
    'secretId': 'Your secretId',
    'secretKey': 'Your secretKey',
    'method': 'post'
}
params = {
    'vpcId': 'Your vpcID',
    'networkInterfaceId': 'Elastic NIC ID to which you need to bind the IP for the first time',
    'secondaryPrivateIpAddressCount': 'The number of IP addresses you need to apply for'
}

try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
       
```
        
### Step 2. Install keepalived (**Version 1.2.8 or above**) on master and slave submachines.
Take centos as an example: `yum -y install keepalived`

### Step 3. Use keepalived.conf to configure unicast mode
Edit the file /etc/keepalived/keepalived.conf. Configure the VRRP configuration of basic keepalived and, more importantly, the unicast mode, that is, to specify the IP address of the peer device and unicast mode in vrrp_instance of keepalived.conf:

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
        10.0.0.1    # IP address of the peer device, for example: 10.0.0.1
    }
    virtual_ipaddress {
        10.100.0.27   # VIP applied in Step 1
    }
    nopreempt
    garp_master_delay 1
    garp_master_refresh 5
}
```

### Step 4. (Optional) Assign a public IP to the VIP
Apply for EIP on the console, and then bind it to the private IP applied in Step 1 through Cloud API, [click to view the specific call method](https://www.qcloud.com/doc/api/229/1377). The python code is similar to that of Step 1.

### Step 5. Use keepalived.conf to configure the switch script
When the master/slave switchover occurs, the new master device is switched by calling vip.py with "notify".

```
vrrp_sync_group G1 {
    group {
        E1
    }
    notify_master "/etc/keepalived/vip.py"
}

```
Step 6. Verify whether the VIP and public IP are switched normally when the master/slave switchover occurs.
Vip.py: Develop the master/slave switchover program through Cloud API, and switch the IP address by calling the Cloud API of private IP migration. Take python as an example:
1) [Download python-sdk](https://github.com/QcloudApi/qcloudapi-sdk-python)
Please read README.md carefully and download sdk to the directory /etc/keepalived:

2) Get Cloud API key:
![](//mc.qcloudimg.com/static/img/ffd379c9e886d0ae3de4fba34539aac7/2.png)
![](//mc.qcloudimg.com/static/img/900df050c3d619566a482ff4e1bd5433/4.png)
3) Develop vip.py switchover program for calling the Cloud API based on the SDK, save vip.py to the directory /etc/keepalived. The Cloud API of private IP migration:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
step1: Download python-sdk:  https://github.com/QcloudApi/qcloudapi-sdk-python
step2: Save the following python code as vip.py to the same level directory of sdk src. Please refer to the following for specific parameters: https://www.qcloud.com/doc/api/245/1361
"""

from src.QcloudApi.qcloudapi import QcloudApi

module = 'vpc'
action = 'MigratePrivateIpAddress'
config = {
    'Region': 'bj',
    'secretId': 'Your secretId',
    'secretKey': 'Your secretKey',
    'method': 'post'
}
params = {
    'vpcId': 'vpc-2l52o5c2',
    'privateIpAddress': '10.100.0.27',
    'oldNetworkInterfaceId': 'ID of Elastic NIC of IP before migration',
    'newNetworkInterfaceId': 'ID of Elastic NIC of IP after migration'
}

try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
```

Note: The Elastic NICs of vip.py on master/slave devices shall be exchanged before and after the migration, and it is necessary to add executable attributes to vip.py:
`Chmod +x vip.py`
Manually execute the vip.py check, and execute the following command to trigger the IP address migration:
`/etc/keepalived/vip.py`
4) Start keepalived：`/etc/init.d/keepalived start`
5) Verify the disaster recovery effect of master/slave switchover: simulate the CVM failure by restarting the keepalived process and restarting the submachine to detect whether the VIP can be migrated.

#### Attachment: Keepalived.conf reference

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
        10.0.0.1    # IP address of the peer device, for example: 10.0.0.1
    }
    virtual_ipaddress {
        10.100.0.27
    }
    nopreempt
    garp_master_delay 1
    garp_master_refresh 5
}
```

