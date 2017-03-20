You usually need to go through the following steps to quickly establish a VPN:
1) Creating VPN Gateway
You can use [Purchase VPN Gateway](https://www.qcloud.com/doc/api/245/5106) API to purchase a VPN gateway instance. This API will return an order number, and you can use [Query VPN Gateway List](https://www.qcloud.com/doc/api/245/5108) API to query the information of purchased VPN gateway.

2) Creating Peer Gateway 
Once the VPN gateway is created, you can use [Create Peer Gateway](https://www.qcloud.com/doc/api/245/5116) API to create a peer gateway, you need to specify the IP address of the peer gateway.

3) Creating Channel
Once the peer gateway is created, you can use [Create VPN Channel](https://www.qcloud.com/doc/api/245/5110) API to create a VPN channel. You need to specify the local VPN gateway and peer gateway of the channel. The channel will be successfully created after you configure a pre-shared private key and a name.

4) Modifying Routing Table
After the channel is created, you can modify routing table policy using the [Modify Routing Table](https://www.qcloud.com/doc/api/245/1417) API, and create a new routing policy, which directs the next hop that accesses the peer gateway segment towards the VPN gateway.

5) Modifying Routing Table Associated with Subnet
After the routing policy is configured, you can use the [Modify Routing Table Associated with Subnet](https://www.qcloud.com/doc/api/245/1416) API to direct the subnet that needs to access IDC through VPN gateway to the routing table mentioned above.

