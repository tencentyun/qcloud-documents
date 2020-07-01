## 1. How will I be charged for my use of VPC/subnet/routing table/NAT gateway/peering connection/public network gateway/VPN connection/network ACL?
Paid services include: cross-region peering connection, public network gateway, NAT gateway, and VPN gateway. These services are chargeable because they have CVMs or license involved in their costs. [Click to view the billing details](https://cloud.tencent.com/doc/product/215/3079).
**Except the paid services mentioned above, the other services are free**.

## 2. Are there additional network charges for services (CVMs, databases, etc.) within a VPC?
No. Network fee is only charged once.
- For accesses to the Internet through **public network gateways and NAT gateways**, a network fee for **public network gateways and NAT gateways** is charged.
- For accesses to services in other VPCs through **cross-region peering connections**, a network fee for **peering connections** is charged.
- For accesses to other services through **VPN connections**, a fee for **VPN gateways** is charged.
