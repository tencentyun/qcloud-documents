To create a VPC peering connection between different developers within the same region, you need to perform the following steps:

1) Initiator makes a request for creating a regional peering connection
You can use API [Create Regional Peering Connection](https://cloud.tencent.com/document/product/215/2107) to initiate a request for creating regional peering connection. After this, you need to notify the receiver's developer to accept request.

2) Receiver accepts the request for peering connection
If you are the receiver, you can use API [Accept Regional Peering Connection](https://cloud.tencent.com/document/product/215/2106) to accept the regional peering connection created by the initiator's developer.

3) Initiator modifies the routing table
After the receiver accepts the request for peering connection, you need to modify routing table policy by calling API [Modify Routing Table](https://cloud.tencent.com/document/product/215/1416), and create a new routing policy, which directs the next hop that accesses receiver's VPC through peering connection towards the this peering connection.

4) Initiator modifies the routing table associated with subnet
After the routing policy is configured, you can use API [Modify Routing Table Associated with Subnet](https://cloud.tencent.com/document/product/215/1416) to direct the subnet that needs to access receiver's VPC through peering connection to the routing table mentioned above.

5) Receiver modifies the routing table
After the request for peering connection is accepted, you need to modify routing table policy by calling the API [Modify Routing Table](https://cloud.tencent.com/document/product/215/1416), and create a new routing policy, which will direct the next hop that accesses initiator's VPC through peering connection to this peering connection.

6) Receiver modifies the routing table associated with subnet
After the routing policy is configured, you can use API [Modify Routing Table Associated with Subnet](https://cloud.tencent.com/doc/api/245/1416) to direct the subnet that needs to access initiator's VPC through peering connection to the routing table mentioned above.

The cross-regional interconnection is configured in the same way as regional interconnection. For application scenarios of peering connection, refer to <a href="https://cloud.tencent.com/doc/product/215/5000" title="Peering Connection Overview">Peering Connection Overview</a>

