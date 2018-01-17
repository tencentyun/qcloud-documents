
As with all CVMs, the access to the backend server instances of a cloud load balancer can be controlled via a security group, which acts as a firewall. You can associate one or more security groups with a backend CVM and add one or more rules to each security group to control traffic to different servers. You can modify the rules for a security group at any time, and the new rules are automatically applied to all instances associated with the security group. For more information, please see [Security Group](https://intl.cloud.tencent.com/document/product/213/5221) product documentation. In the [Virtual Private Cloud](https://console.cloud.tencent.com/) environment, you can also use [Network ACL](https://intl.cloud.tencent.com/document/product/215/5132) for access control.

 
You can use a security group to allow the backend instances to receive traffic only from the cloud load balancer or from other sources. Please note that, <font color="red">you must ensure that the instance's security group allows the cloud load balancer to communicate with the backend instance on the listener port and health check port</font>. In the VPC, your security groups and network ACLs must allow traffic to flow in both directions on these ports.

## Recommended Rules for LB Security Group
The configuration of LB security group is as follows:

![](https://mc.qcloudimg.com/static/img/3a6b17d397868d9f1de9e02eae38dccb/image.png)

| Type | SNAT Processing | Health Check Traffic | Recommended Security Group Configuration | Note |
| :-------- | :--------| :----- |:---- |:---- |
| Public Network CLB | No | Initiated via LB vip | If you want to specify a fixed IP for access, both client IP and LB vip need to be enabled. If not, it is recommended that all IPs of the listener port are enabled, i.e. 0.0.0.0/0. | Applicable to both basic network and VPC |
| Private Network CLB (purchased prior to December 5, 2016) | Yes | No need to configure, the health check IP is enabled by default. | Since the client IP is processed via SNAT, LB vip needs to be enabled. | Applicable to both basic network and VPC |
| Private Network CLB (purchased prior to December 5, 2016) | No | No need to configure, the health check IP is enabled by default. | The CLB can be accessed once the health check IP is enabled. | Applicable to both basic network and VPC |

**Application scenario 1:**
If the public network CLB listener is configured with TCP: port 80, and only client IPs (clientA IP and clientB IP) are allowed to access the CLB, configure the security group rules of the backend server as follows:
```
clientA ip+80 allow
clientB ip+80 allow
LB vip +80 allow
0.0.0.0/0 +80 drop
```

**Application scenario 2:**
If the public network CLB listener is configured with HTTP+port, and all IPs (clientA IP and clientB IP) under port 80 are enabled to access the CLB, configure the security group of the backend server as follows:
```
0.0.0.0/0 +80 allow
```

**Application scenario 3:**
The private network CLB (purchased after December 5, 2016) is configured with TCP:port 80 in the VPC, and only client IPs (clientA IP and clientB IP) are allowed to access the LB vip and only access the backend CVMs bound to the LB.

a. Configure the security group of the backend server as follows:
```
clientA ip+80 allow
clientB ip+80 allow
0.0.0.0/0 +80 drop
```
b. Configure the security group of the client server as follows:
```
LB vip+80 allow
0.0.0.0/0 +80 drop
```
**Application scenario 4: Blacklist**
If you need to set a blacklist for some client IPs to reject their accesses, you can configure the security group associated with the cloud services. The security group rules need to be configured as follows:
- Add the client IPs from which access needs to be rejected plus ports to the security group, and choose "reject the access from the IPs" in the Policy section.
- When the setting is made, add another security group rule that allows all accesses to the port from all IPs by default.
When the configuration is completed, the security group rules are as follows:
```
clientA ip+port drop
clientB ip+port drop
0.0.0.0/0+port accept
```
Note:
The above configuration steps should be performed ***in a correct order***, otherwise the blacklist configuration cannot take effect.
Security groups are stateful. Therefore, the above configurations are used for ***outbound rules***, and inbound rules do not need special configuration.

## Using the Console to Manage Backend Server Security Groups
1) Log in to [Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance) and click the CLB instance ID to go to the CLB details page.

2) In the "Backend Server" tab, click the corresponding backend server ID to go to the CVM details page.

3) Click the "Security Group" tab, and click the "Edit" button under "Security Groups Joined" to edit the associated security group. Click "Configure Security Group" to add a new security group for association.

## Using API to Manage Backend Server Security Groups
Please see the APIs [ModifySecurityGroupsOfInstance](https://cloud.tencent.com/doc/api/229/1367) and [ModifySecurityGroupPolicy](https://cloud.tencent.com/doc/api/229/1365).


