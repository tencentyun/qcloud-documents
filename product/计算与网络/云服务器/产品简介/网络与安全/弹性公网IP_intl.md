## Overview
Elastic IP, is referred to as ElP for short. It is a static IP designed for dynamic cloud computing, and a fixed public IP in a certain region. In case of an instance failure, the EIP can be remapped to another instance in your account (or [NAT gateway instance](/doc/product/215/%E7%BD%91%E5%85%B3#2.-nat.E7.BD.91.E5.85.B3) ) quickly to block the failure.

For example, if you need to remap a custom domain name to the public IP of a new instance, it takes a dozen or even dozens of hours to transmit and update the mapping over the Internet. In this case, the request will be completely parsed to the original instance, resulting in the inability of the new instance to receive the request. EIP can solve this problem by redirecting the request to the new instance.

## EIP Category
Tencent Cloud accounts are classified into the following classes based on whether an EIP has a capability of public network management:
- The EIPs purchased by Class I accounts are bare instances, with backend resources featured with public network capacity.
- Class II accounts manage public network capabilities on EIP and CLB, with backend resources being bare instances.

According to the above two account classes, EIPs are also divided into the following two types:
### Bare IP
The EIPs purchased by Class I accounts are bare instances, with backend resources featured with public network capacity. When you create a CVM instance, NAT gateway instance or VPN gateway instance, specify the public network capacity (bandwidth cap) and billing method (bill-by-traffic/bill-by-bandwidth) of the instance. Public IP or CLB only serves as a public network egress. This type of IP is referred to as **bare IP**.

### Non-bare IP
- Class II accounts manage public network capabilities on EIP and CLB, with backend resources being bare instances. When you create an EIP, specify the public network capacity (bandwidth cap) and billing method (bill-by-traffic/bill-by-bandwidth) of this IP. The backend instances (CVM/NAT gateway/VPN gateway) use the public network capability of the EIP. This type of IP is referred to as **non-bare IP**.
- There are three types of non-bare IPs: **EIP billed by bandwidth on an hourly basis, EIP billed by bandwidth on a monthly basis, and EIP billed by traffic**. (Non-bare IP is under internal trial. EIP billed by bandwidth on an hourly basis applies to most of the users.)

### How to determine the type of an EIP
- Log in to the [EIP Console](https://console.cloud.tencent.com/cvm/eip).
As shown below, if **no** bandwidth-related information appears in the EIP list, the EIPs are purchased by the Class I accounts. The EIPs are non-bare IPs with no public network attributes, and you need to purchase public network for the backend resources before accessing the public network via a public IP or CLB.
![](https://main.qcloudimg.com/raw/aa9bc5d1844dc8aa333bbd2cf5d10c84.png)
- As shown below, if bandwidth-related information **can be found** in the EIP list, the EIPs are purchased by the Class II accounts. The type of a non-bare IP can be queried based on the billing method.
![](https://main.qcloudimg.com/raw/8d99377cf8e7c34460206371c9913345.png)

## Rules and Limits
### Use rules
 - An EIP applies to the CVM instances of both basic networks and VPCs, and the [NAT gateway](/doc/product/215/4975) instances in VPCs.
 - An EIP is associated with a Tencent Cloud account, instead of an instance.
 - An EIP remains associated with a Tencent Cloud account until it is released or the account balance is in arrears for more than 26 hours.
 - When an EIP is bound to an instance, the current public IP of the instance will be released to the public IP pool of a basic network. If you choose to reassign a public IP when unbinding an EIP from an instance, the instance will be automatically assigned a new public IP (which may be different from the one before binding). Besides, terminating an instance will disassociate it from its EIP.
 
### Use limits
 - The maximum number of requests that can be made by each Tencent Cloud account in each region equals to **two times the quota**.
 - At most **20** EIPs can be created by each Tencent Cloud account in each region.
 - Each account can be reassigned **10** public IPs free of charge in a day when an EIP is unbound.
 - **One** EIP can only be bound to **one** CVM/NAT gateway instance in the same region at a time. Dynamic binding and unbinding are supported. 

