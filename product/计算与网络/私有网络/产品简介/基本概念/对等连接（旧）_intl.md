By default, if not configured, different VPCs cannot communicate with each other via private network. If a CVM with a public IP/EIP is used, such communication can be accomplished over the Internet. If a private network is requested for traffic access, peering connection and routing should be used.

## 1. Basics
VPCs Interconnection provides cloud resource access across VPCs, and allows CVMs to access cloud servers, cloud databases, CMEMs, and load balancing resources across VPCs. Peering connections do not depend on a single piece of hardware, so there is no single point of failure or bandwidth bottleneck.

VPCs interconnection can be deployed among VPCs from one or more users <font color="red">in one region</font> or <font color="red">across regions</font>. Interconnection does not occur unless the two VPCs are directly connected to each other.

![](//mccdn.qcloud.com/img5695f223723bd.png)

> Note: VPCs cannot communicate with each other before routing. Both VPCs shall be configured with routes for sending and returning packets to achieve traffic access.

## 2. Usage Restrictions
- Your VPC and the peer VPC should not have overlapping CIDR
- For a cross-region peering connection, all peer VPCs of your VPC should not have overlapping CIDR (not applicable to a regional peering connection)
- A VPC can simultaneously communicate with up to 10 VPCs (including connected and pending ones)
- Only one peering connection can be created between two VPCs
- The application for VPCs interconnection is valid for 1 week
- The cloud load balancer does not support cross-region peering connection or cross-VPC CVM binding.

## 3. Regional Peering Connection vs. Cross-region Peering Connection
VPC supports both regional and cross-region peering connections. Despite the same usage of connecting VPCs, regional and cross-region peering connections differ in their functions and billing rules due to different physical distances between VPCs:

| Item | Regional Peering Connection | Cross-region Peering Connection |
|---------|---------|---------|
| Infrastructure | Based on regional local private network of Tencent Cloud | Based on cross-region internal MPLS network of Tencent cloud |
| Bandwidth | No upper limit | Up to 10 Gbps, you can set the upper limit of bandwidth |
| Billing Rule | 	Free | 	Bill by Day based on the regions your VPC and the peer VPC are located and the actually used network bandwidth. For details, refer to [Price Overview](https://cloud.tencent.com/doc/product/215/%E4%BB%B7%E6%A0%BC%E6%80%BB%E8%A7%88) |	
| Availability | 99.95% or more, no single point of failure | 99.95% or more, no single point of failure |	
| Cross-account connection | Support | Support |	
| Access Permission | CVM of each VPC can access CVM, database, cloud load balancer and other resources in the peer VPC | CVM of each VPC can access CVM, database, cloud load balancer and other resources in the peer VPC |	
| Function Restrictions | VPC segments in peering connection cannot overlap; multiple peering connections cannot affect one another | VPC segments in peering connection cannot overlap; <br><font color="red">Peer VPC segments cannot overlap when multiple VPCs are connected to one VPC</font> |	

## 4. Peering Connection Lifecycle
The following two figures describe the process and lifecycle of VPC peering connection.
How to apply:
![](//mccdn.qcloud.com/img5695f31b9c668.png)

How to delete:
![](//mccdn.qcloud.com/img5695f33e85c6c.png)

