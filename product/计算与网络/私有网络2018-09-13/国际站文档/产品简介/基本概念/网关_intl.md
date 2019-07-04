## 1. Public Network Gateway

Public network gateway is a CVM on which the forwarding feature is enabled. If a CVM without public IP needs to access the Internet, it can do so through the forwarding via public network gateway in a different subnet.

## 2. NAT Gateway
Similar to public network gateway, NAT gateway is another way by which a CVM in the VPC accesses the public network. NAT gateway's underlying implementation uses master/slave hot backup. In case of the failure of the master machine, switching to a slave machine is supported without affecting the network connection. This ensures the high availability of network egress.

NAT gateway is available in three configuration types, and supports a maximum of 5Gbps traffic surge and 10,000,000 concurrent connections.

Charges for a NAT gateway device include two parts: Gateway rental fee (by hour) and the fee for traffic generated during the access to the Internet. For more information on billing rules, refer to [Price Overview](https://cloud.tencent.com/doc/product/215/%E4%BB%B7%E6%A0%BC%E6%80%BB%E8%A7%88).

Both NAT gateway and public network gateway are used by the CVM in the VPC to access the Internet. Differences between these two gateways are shown below:

| Attribute | NAT Gateway | Public Network Gateway |
|---------|---------|---------|
| Availability	| Master/slave hot backup, automatic hot switching |	Switch the failed gateway manually
| Public network bandwidth	| Maximum is 5Gbps	| Depend on the network bandwidth of CVM
| Public IP	| Bind to a maximum of 10 EIPs |	An EIP or ordinary public IP
| Rate limit of public network	| N/A |	Depend on the rate limit of CVM
| Maximum number of connections	| 10,000,000 |	500,000
| Private IP	| Private IP of VPC user is not occupied |	IP in subnet is occupied
| Security group |	Binding of security group is not supported. You can bind the security group to the NAT gateway backend CVM	| Support
| Network ACL |	Binding of network ACL is not supported. You can bind the network ACL to the subnet where the NAT gateway backend CVM resides in	| Binding of network ACL is not supported. You can bind the network ACL to the subnet to which the public network gateway belongs


## 3. VPN Gateway

VPN gateway is an end of the encrypted network tunnel established between VPC and user IDC (the other end is peer gateway). It is mainly used to establish secure and reliable hybrid cloud connection.

## 4. Peer Gateway

Peer gateway refers to user's private cloud data center. The user only needs to provide the custom name of the data center and the public IP to establish a peer gateway. A VPN gateway in the VPC can establish encrypted VPN network tunnels with multiple peer gateways.
