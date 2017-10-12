You usually need to go through the following steps to quickly establish a VPC:

1) Create a VPC and its subnets
You can use [Create a Virtual Private Cloud](https://cloud.tencent.com/doc/api/245/1309) API to create a VPC and its subnets. After creation, the system will create a default routing table and direct the subnet to the default routing table.

2) Purchase VPC sub-machines 
After the subnets are created, you can use API [Create Instance](https://cloud.tencent.com/doc/api/229/1350) to purchase VPC CVMs. These CVMs may come with no public IPs, and we can use the public network gateway as a uniform egress.

3) Purchase an NAT gateway (optional)
If the CVM purchased does not have a public IP, you can use API [Create NAT Gateway](/doc/api/245/4094) to purchase an NAT gateway, which can be used as an egress for external access by the CVM in the VPC.

4) Modify the routing table (optional)
In the subnet that needs to access the Internet, you can modify the routing table policy by using API [Modify Routing Table](https://cloud.tencent.com/doc/api/245/1417), and create a new routing policy which directs the next hop of the destination network segment that needs external access towards the public network gateway.

