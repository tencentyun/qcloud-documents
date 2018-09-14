ENI is a virtual network API. You can bind your CVM with an ENI to connect it to the network. ENI is very useful when you configure management networks and establish highly reliable network solutions.

ENI comes with VPC, availability zone and subnet attributes. You can only bind it to CVMs under the same availability zone. Each CVM can be bound with multiple ENIs. The allowed number of ENIs depends on the specifications of the CVM.

## Basic Information

An ENI has the following major relevant information:

1. Primary ENI or secondary ENI: The ENI that is created when you create the CVM within VPC is the primary ENI, and those created by users are secondary ENIs. You can bind/unbind secondary ENIs but not the primary one.

2. Primary private IP: The primary private IP of the ENI is assigned by the system or specified by users when the ENI is created. You can modify the primary private IP of the primary ENI, but not the ones for secondary ENIs.

3. Secondary private IP: Secondary private IPs that are bound to the ENI, other than the primary IP, are configured by users when they create or modify the ENI. You can bind/unbind these IPs.

4. EIP: Bound with private IPs of the ENI in a one-to-one correspondence manner.

5. Security group: An ENI can be bound with one or more security groups.

6. MAC address: Each ENI has a unique global MAC address.


## Service Limits

The number of ENIs that can be bound to a CVM and that of private IPs that can be bound to each ENI vary greatly with CPU and RAM configuration. The allowed numbers are shown in the following table. For more information, please see [Service Limits of Other VPC Products](https://cloud.tencent.com/doc/product/215/537).

| CVM Configuration | Number of ENIs | Number of IPs bound to each ENI |
| ------------------- | :---- | :------ |
| CPU: 1 core; Memory: 1 GB | 2 | 2 |
| CPU: 1 core; Memory: >1 GB | 2 | 6 |
| CPU: 2 cores | 2 | 10 |
| CPU: 4 cores; Memory: <16 GB | 4 | 10 |
| CPU: 4 cores; Memory: >16 GB | 4 | 20 |
| CPU: 8-12 cores | 6 | 20 |
| CPU: >12 cores | 8 | 30 |

## Billing Method
Free of charge. For more information about the prices of VPC services, please see [VPC Price Overview](https://cloud.tencent.com/doc/product/215/3079).

## Operation Instructions

### Routing and Security Configuration of VPC and CVM

The new ENI does not take effect immediately after it is bound to a CVM. You need to configure the routing table for both CVM and VPC properly to implement the expected network traffic distribution. As shown in the figure below:

CVM is bound with two ENIs: eth0 (the primary ENI) and eth1 (the secondary ENI). They are located in the subnet A of ``10.0.1.0/24`` and the subnet B of ``10.0.2.0/24``, respectively. Subnet A is used to locate the subnet connected to the Internet, while subnet B and subnet C can only access each other using private network traffic.
<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/17d751e1f63fcffb4c09a44fe832e176/image.png)

</div>
**Scenario 1: ``10.0.1.1`` actively accesses the Internet**

a) Query the routing table in the CVM, and eni0 is used if it matches the default route.

b) Query the routing table of subnet A where eni0 is located. If the route matches natgw-001 you can access the Internet through NAT gateway.

c) Internet packet is returned to eni0 via natgw-001 and then is returned to the CVM.

**Scenario 2: ``10.0.2.1`` actively accesses the Internet**

a) Query the routing table in the CVM, and eni0 is used if it matches the default route.

b) Query the routing table of subnet A where eni0 is located. If the route matches natgw-001 you can access the Internet through NAT gateway.

c) Check whether the destination IP is contained in eni1 in the returned packet. If so, the network packet is returned to CVM via eni1. (inbound and outbound packets are not returned via the same ENI)

In this case, since neither inbound nor outbound route is directed via the same ENI, when rp_filter verification (a mechanism used to check whether inbound and outbound network packets are returned via the same ENI) is enabled for the CVM, this network packet may be lost and cannot be pinged. It is not recommended to configure the network according to scenario 2. If you must to do so, you can disable rp_filter verification in the CVM.

**The role of security group**

Since the security group is bound with an ENI, the outbound filtering is implemented on the traffic of the eni0 accessing the Internet by the security group bound to eni0, and the status of security group is detected first for the returned packet. The inbound verification of security group is ignored if it has a status.

**The role of network ACL**

The network ACL is bound to the subnet and is detected as stateless. Inbound and outbound traffic is detected based on the network ACL bound to the subnet in which the source and destination IPs reside. Although inbound and outbound packets in scenario 2 are not on the same subnet, but since both outbound source IP and inbound destination IP are ``10.0.2.1``, only the network ACL configuration for the subnet in which this IP resides is verified.

### Viewing ENI

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Click the "Instance ID" of an ENI to go to its details page and view its information.

### Creating ENI

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Click "Create" in the upper left corner, select the CVM and subnet of the ENI in the pop-up window.

4) Select the number of private IPs assigned to the ENI (specified private IPs are supported).

4) Click "OK" to complete the creation process.

### Binding CVM

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Find the line of the ENI, and click "Bind CVM" in the "Operation" column (only CVMs in the same availability zone as the ENI are supported).

4) Select the CVM to be bound and click "OK" to finish the binding process.

Note: After being bound on the console, the ENI needs to be configured in the CVM before it can be used normally.

### Configuration of ENI in CVM (Taking Centos 7.2 as Example)

The ENI in the CVM is configured by following the steps below:

**1) Query the ENI mounted to the CVM**

```
ip addr
```

**2) Start the newly bound ENI**

```
ip link set eth1 up
```

>Note: "eth1" refers to the No. of ENI newly mounted in the CVM. You can identify the ENI using MAC address.

**3) Configure the private IP of the new ENI**

```
ip addr add 10.0.3.133/24 dev eth1
```

> Note 1: IP in the ``10.0.3.133/24`` is the private IP to be bound to the ENI, and the mask is the CIDR mask of the subnet in which the ENI resides.

>Note 2: "eth1" refers to the No. of ENI newly mounted in the CVM.

**4) Configure the routing table in the CVM (important)**

```
route add -net 192.168.0.0/16 dev eth1
```

>Note 1: ``192.168.0.0/16`` is the destination of the route configured for the newly bound ENI, and eth1 refers to the next-hop ENI to which this route is directed.

>Note 2: The above network configuration becomes invalid after the CVM restarts. You can change the configuration by modifying the network configuration file in the CVM. The modification of the network configuration file takes effect after the ENI is restarted.

>Note 3: The incorrect configuration of the routing table in the CVM may lead to the failure of CVM network. For more information, please see [Routing and Security Configuration of VPC and CVM](https://cloud.tencent.com/document/product/215/6513#.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B8.8E.E4.BA.91.E4.B8.BB.E6.9C.BA.E7.9A.84.E8.B7.AF.E7.94.B1.E5.8F.8A.E5.AE.89.E5.85.A8.E9.85.8D.E7.BD.AE) above.

### Assigning Private IP (Tencent Cloud Console)

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Click the "Instance ID" of an ENI to go to its details page and view its information.

4) Click "IP Management" tab to view the private IPs and EIPs that are already bound to the ENI.

5) Click "Assign Private IP" button to open the "Assign Private IP" window.

6) You can choose to "Auto Assign" or "Manually Enter" private IP.

7) You can click the "Add" button to assign multiple IPs for the ENI in the "Assign Private IP" window.

8) Click "OK" button to complete the assigning process.

Note: You also need to configure the private IPs in the CVM before they can take effect.



### Assigning Private IP (In the CVM System)

Private IPs can be configured in the CVM by the following ways. The example below is based on Centos 7.2.

**Method 1**

1) Log in to the CVM as admin.

2) Execute the command

`ip addr add [ip/mask] dev [ifname]` 

Example: To add IP ``192.168.0.5`` in the subnet ``192.168.0.0/24`` on the ENI eth0 of the CVM, you only need to execute the command

 `ip addr add 192.168.0.5/24 dev eth0`

3) The private IP is configured.

Note: Private IPs configured in this way are only written into the system memory of the CVM. They become invalid if the CVM restarts, in which case you need to configure again.

**Method 2**

1) Log in to the CVM as admin.

2) Execute the following command

`cd /etc/sysconfig/network-scripts/`

`ls`

3) Find the ENI name from the list. Take Tencent Cloud Centos 7.2 CVM as an example: If you need to bind private IP for an ENI named "ifcfg-eth0", execute the following command to open the configuration file of this ENI using vim

`vim ifcfg-eth0`

The original system configuration file is:

`DEVICE='eth0'`

`NM_CONTROLLED='yes'`

`ONBOOT='yes'`

`IPADDR='192.168.0.3'`

`NETMASK='255.255.255.0'`

`GATEWAY='192.168.0.1'`

Change the configuration to:

`DEVICE='eth0'`

`NM_CONTROLLED='yes'`

`ONBOOT='yes'`

` `

`IPADDR0='192.168.0.3'`


`NETMASK0='255.255.255.0'`


`GATEWAY0='192.168.0.1'`

` `

`IPADDR1='192.168.0.5'`


`NETMASK1='255.255.255.0'`


`GATEWAY1='192.168.0.1'`

` `

Save the modified configuration file and exit vim.

4) Restart the ENI

`systemctl restart network`

Check whether the IP has been added into ENI "eth0"

`ip addr`

5) The private IP is bound.

Note: Private IPs configured in this way take effect after the CVM restarts. However, if you create a custom image of this CVM and use the image to create other CVMs, you need to manually update private IP configurations for those CVMs.

### Releasing Private IP

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Click the "Instance ID" of an ENI to go to its details page and view its information.

4) Click "IP Management" tab to view the private IPs and EIPs that are already bound to the ENI.

5) Click "Release" button in the "Operation" column of the line in which private IP resides.

6) Click "OK" to complete the operation.

Note 1: You can only release secondary IPs of ENIs, but not the primary one.

Note 2: Once the private IP is unbound, the EIP is automatically disassociated.

### Unbinding CVM

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Find the line of the ENI and click "Unbind CVM" in the "Operation" column.

4) Click "OK" to complete the unbinding process.

>**Tips: **After you unbind an ENI, information such as its associated private IPs, EIPs, security groups is retained.

### Deleting ENI

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Find the line of the ENI and click "Delete" in the "Operation" column.

4) Click "OK" to complete the deletion process.

>Note 1: Once the ENI is deleted, its private IPs, EIPs and security groups are automatically disassociated.

>Note 2: You can only delete ENIs that are not currently associated with CVMs.

>Note 3: The primary ENI is deleted as the CVM is deleted.

## Binding EIP

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Click the "Instance ID" of an ENI to go to its details page and view its information.

4) Click "IP Management" tab to view the private IPs that are already bound to the ENI.

5) Click "Bind" button in the "Bound EIP" column of the line in which private IP resides.

6) Select to bind an IP from the "Existing EIP" list or "Create EIP" in the pop-up window.

7) Click "OK" to complete the binding process.

### Unbinding EIP

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Click the "Instance ID" of an ENI to go to its details page and view its information.

4) Click "IP Management" tab to view the private IPs and EIPs that are already bound to the ENI.

5) Click "Unbind" button in the "Bound EIP" column of the line in which private IP resides.

6) Click "OK" to complete the unbinding process.

### Modifying Primary Private IP

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Click the "Instance ID" of an ENI to go to its details page and view its information.

4) Click "IP Management" tab to view the primary private IP that is already bound to the ENI.

5) Click "Modify Primary IP" button in the "Operation" column of the line in which the primary private IP resides.

6) Enter the new primary private IP in the pop-up window and click "OK" to modify.

### Modifying the Subnet of ENI

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the ENI list page.

3) Click the "Instance ID" of the ENI to go to its details page.

4) In the basic information page of the detail page, click "Change Subnet" button.

5) Select the subnet to be changed for the ENI and specify a new primary IP.

6) Click "Save" to finish the subnet changing process.

>Note 1: You can only change the subnet of the primary ENI.

>Note 2: You must unbind all secondary IPs before you can change the subnet of the ENI.

>Note 3: When changing the subnet of the ENI, you can only choose another subnet under the same availability zone.

## FAQs
### In Windows system, what to do if IP information is lost when the hot-plugging ENI is restarted?
You need to manually configure the IP information for hot-plugging ENI, and it may be lost when the sub-server is restarted. You can download a tool (link: http://enipackage-1251740579.cosgz.myqcloud.com/NetCardIPSet%20%281%29.exe) for configuration.

Steps:</BR>
1. Download the tool for Windows CVM.
</BR>
2. Insert the ENI and bind the IP.</BR>
3. Run the downloaded tool.



## API Overview
Functional APIs for ENI are listed below. For more information about other VPC resources, please see [Overview of All VPC APIs](https://cloud.tencent.com/doc/api/245/909).


| Feature | Action ID | Description |
|---------|---------|---------|
| Create ENI | [CreateNetworkInterface](https://cloud.tencent.com/doc/api/245/4811) | Create an ENI |
| Delete ENI | [DeleteNetworkInterface](https://cloud.tencent.com/doc/api/245/4813) | Delete an ENI |
| Query ENI Information | [DescribeNetworkInterfaces](https://cloud.tencent.com/doc/api/245/4814) | Query the information of an ENI |
| Assign Private IP for ENI | [AssignPrivateIpAddresses](https://cloud.tencent.com/doc/api/245/4817) | Assign a private IP for an ENI |
| Unassign Private IP for ENI | [UnassignPrivateIpAddresses](https://cloud.tencent.com/doc/api/245/4819) | Unassign a private IP for an ENI |
| Bind ENI to CVM | [AttachNetworkInterface](https://cloud.tencent.com/doc/api/245/4820) | Bind an ENI to a CVM |
| Unbind ENI from CVM | [DetachNetworkInterface](https://cloud.tencent.com/document/product/215/4822) | Unbind an ENI from a CVM |

