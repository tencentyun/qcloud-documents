You usually need to go through the following steps to create a Direct Connect gateway to quickly connect Tencent Cloud with local data center:
1) Building your Physical Direct Connect
You need to build your Physical Direct Connect on <a href="https://console.cloud.tencent.com/vpc/dc"  title="Physical Direct Connect Management">Physical Direct Connect Management</a> on the Tencent Cloud console.

2) Creating Direct Connect gateway
You can create a Direct Connect gateway using the API of [Create Direct Connect Gateway](https://cloud.tencent.com/document/product/215/4824). You can choose whether to enable NAT based on the actual situation. The NAT Direct Connect gateway supports the configuration of network address translation.

3) Configuring Direct Connect channel. You need to create the Direct Connect channel connected to different Direct Connect gateways on<a href="https://console.cloud.tencent.com/vpc/dcConn"  title="Direct Connect Channel Management">Direct Connect Channel Management</a> on the Tencent Cloud console, in order to enable interconnection between local data center and multiple VPCs .

4) Modifying Routing Table
After the channel is created, you can modify routing table policy using the API of [Modify Routing Table](https://cloud.tencent.com/document/product/215/1416), and create a new routing policy, which, via the Direct Connect gateway, directs the next hop that accesses other VPCs towards the Direct Connect gateway.

5) Modifying Routing Table Associated with Subnet
After the routing policy is configured, you can use the API of [Modify Routing Table Associated with Subnet](https://cloud.tencent.com/document/product/215/1416) to direct the subnet that needs to access other VPCs through Direct Connect gateway to the routing table.

For more information about specific usage scenarios of Direct Connect gateway, refer to <a href="https://cloud.tencent.com/doc/product/215/4976" title="Direct Connect Gateway">Direct Connect Gateway Overview</a>
