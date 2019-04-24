## Introduction
Classiclink means to associate CVMs in the basic network with specified VPCs, thus allowing CVMs in the basic network to communicate with cloud services in VPCs (such as CVMs and databases). By default, VPC network is completely isolated. Neither other VPCs nor the basic network is able to communicate with it. [Peering Connection](https://cloud.tencent.com/doc/product/215/5000) made it possible for different VPCs to communicate with each other. While communication between the basic network and a certain VPC is made possible by Classiclink. As shown in the figure below, the basic network CVM can access cloud resources within the VPC such as CVM, cloud database, private network cloud load balancer, cloud cache and so on. However, the CVM in the VPC can only access the basic network CVM which is interconnected with it, but not the other computing resources within the basic network. This feature only supports interconnection within the same region, as shown below.
![](https://mc.qcloudimg.com/static/img/dfdbaa364ad46920f10053536fb6363f/VPC-Classiclink.png)

## Influence on Basic Network Interconnected CVMs Caused by Router, Security Group and Network ACL
- The private IP of the associated basic network CVM will be automatically added to the Local policy of the VPC's routing table, in which case the CVM in the VPC and services in this basic network will be able to communicate with each other. You do not need to manually modify the routing table rules in the current VPC. 
- After the basic network CVM is associated with VPC, their security firewall and network ACL will remain effective. That is to say, you can restrict the access from associated basic network CVM by configuring network ACL for the VPC subnet. You can also configure security group rules for CVMs in the basic network and VPC to restrict network access for both directions.

## Service Limits
- This feature only supports the interconnection between basic network and VPC. You cannot change the network environment for the CVM. Once the network environment (VPC or basic network) has been determined for the CVM, you will no longer be able to change it.
- A basic network CVM can be associated with only one VPC at a time.
- Currently, interconnection feature is only supported for VPC and basic network under the same region.
- Classiclink feature is only supported for VPCs within the network segment `10.[0~47].0.0/16`. The IP range for VPCs of other network segments may conflict with the basic network IP segment.
- CVM traffic during the Classiclink can only be routed to private IP address within the VPC, but not the other destinations other than the VPC. That is, the basic network CVM cannot access public network or VPC resources outside the current VPC through network equipment such as its VPN gateway, direct connect gateway, public network gateway, peering connection, NAT gateway and so on. Likewise, the peer of VPN, direct connection and peering connection cannot access the current basic network CVM either.
- The cloud load balancer instance within the VPC cannot be bound with the basic network CVM which is interconnected with the current VPC.
- Changing the private IP of the basic network CVM will cancel the association with the VPC, which means the original record will lose its functional effect. Please add the record again in the VPC Console if you wish to associate them.
- The interconnection relationship with VPC will not be unbound by actions against the CVM such as isolation due to arrears, security isolation, cold migration, failover, configuration modification, operating system switching and so on.
- The interconnection relationship with VPC will be automatically unbound if the CVM is returned.

| Resource | Restriction | Description |
|---------|---------| ---|
| Number of basic network CVMs that can be associated with each VPC | 100 | 　　|
| Supported network segment | Only VPCs of the network segment `10.[0~47].0.0/16 (including subsets)` are supported | To prevent conflict between the IPs of basic network CVM and VPC |
| Supported cloud resources | Cloud virtual machine (CVM) | Cannot access basic network resources such as CDB, CMEM, LB, etc. |

## Billing Method
The Classiclink feature is free to use. Refer to [Tencent Cloud VPC Pricing Overview](https://cloud.tencent.com/doc/product/215/3079) for prices of other VPC services.

## Instructions
### Associating Basic Network CVM with VPC
Example:
If you wish to allow CVM "TomCVM" to communicate with VPC "TomVPC" via Classiclink, you will need to follow the following steps:
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Select **Region: Beijing**, click the VPC to be interconnected with basic network (`TomVPC`) and enter its detail page.
3) Click "Classlink" tab, and click "Bind CVM" button. 
4) In the pop-up window, select the CVM in the basic network to be associated with the VPC: `TomCVM`.
5) Click "OK" to complete the operation. The association relationship will take effect immediately.

### Viewing CVMs Interconnected with the Basic Network
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Select region, click the ID of the VPC to be interconnected with basic network and enter its detail page.
3) Click "Classlink" tab to view the list of basic network CVMs associated with the VPC.


### Disassociating VPC and Basic Network CVM
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to enter the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2) Click the ID of the VPC to be interconnected with basic network and enter its detail page.
3) Click "Classlink". In the list of basic network CVMs, select the CVM to be disassociated and click "Disassociate" button.
4) Click "OK" to complete the disassociation process.

## Related APIs
You can use APIs to configure and manage the interconnection between your VPC and basic network. Refer to [Overview of All VPC APIs](https://intl.cloud.tencent.com/document/product/215/909) for more information about VPC API services.





