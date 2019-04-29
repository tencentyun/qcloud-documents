By creaing an NAT gateway, you can connect a private-network CVM to the Internet.

1) Create NAT gateway
You can use [CreateNatGateway](/doc/api/245/4094) API to purchase a NAT gateway. This API will return an order number, and you can use [QueryNatGatewayProductionStatus](https://cloud.tencent.com/doc/api/245/4089) API to query the information of purchased NAT gateway.

2) Modify routing table
Modify the routing table policy using the [ModifyRouteTableAttribute](https://cloud.tencent.com/doc/api/245/1417) API. Add a routing policy that will direct the next hop that needs to access the Internet through NAT gateway to the NAT gateway.

3) Modify routing table associated with subnet
After the routing policy is configured, you can use the [AssociateRouteTable](https://cloud.tencent.com/doc/api/245/1416) API to direct the subnet that needs to access the Internet through NAT gateway to the routing table.

For more information about specific usage scenarios of NAT gateway, refer to <a href="https://intl.cloud.tencent.com/document/product/215/1682#2.-nat.E7.BD.91.E5.85.B3" title="NAT Gateway">NAT Gateway Description</a>
