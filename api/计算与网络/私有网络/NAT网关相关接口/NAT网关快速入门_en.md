The CVM only with private IP within the VPC can quickly access the Internet by creating a NAT gateway. Generally, it needs the following steps:

1) Create NAT gateway
You can use [Create NAT Gateway](/doc/api/245/4094) API to purchase a NAT gateway. This API will return an order number, and you can use [Query the Operation Status of NAT Gateway](https://www.qcloud.com/doc/api/245/4089) API to query the information of purchased NAT gateway.

2) Modify routing table
After the NAT gateway is created, you can modify the routing table policy using the [Modify Routing Table](https://www.qcloud.com/doc/api/245/1417) API. Add a routing policy that will direct the next hop that needs to access the Internet through NAT gateway to the NAT gateway.

3) Modify routing table associated with subnet
After the routing policy is configured, you can use the [Modify Routing Table Associated with Subnet](https://www.qcloud.com/doc/api/245/1416) API to direct the subnet that needs to access the Internet through NAT gateway to the routing table.

For more information about specific usage scenarios of NAT gateway, refer to <a href="https://www.qcloud.com/doc/product/215/1682#2.-nat.E7.BD.91.E5.85.B3" title="NAT Gateway">NAT Gateway Description</a>
