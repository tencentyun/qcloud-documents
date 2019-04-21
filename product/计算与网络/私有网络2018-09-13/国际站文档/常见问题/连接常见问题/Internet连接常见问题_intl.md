## 1. How do instances without public IP addresses (CVMs, databases) access the Internet?
They can access the Internet through NAT gateways/public network gateways.
- [NAT gateways](https://cloud.tencent.com/doc/product/215/4975). By creating NAT gateways and configuring the routing table associated with relevant subnet, the instances within the subnet can access the Internet. [Click to view the operation instructions](https://cloud.tencent.com/doc/product/215/4975#.E4.BD.BF.E7.94.A8-nat-.E7.BD.91.E5.85.B3.E8.AE.BF.E9.97.AE-internet).
- Public network gateways. CVMs without public IPs can access the Internet via public network gateways located in different subnets. 

## 2. What is the difference between public network gateways and CVMs with public IPs?
A public IP coming with a CVM is equivalent to an additional public network NIC, enabling the CVM to freely access the Internet.

## 3. Why cannot a routing policy be forwarded after the policy is configured for a subnet and directed to a public network gateway?
When the CVM that accesses the Internet through a public network gateway and the public network gateway are in the same subnet, the forwarding function will fail. Please arrange the CVM and the public network gateway in different subnets.

## 4. In the routing table, the access to the public network within a subnet is set to be made through NAT gateways, but the CVMs in the subnet are configured with elastic IPs. So whether these CVMs access the public network through NAT gateways or elastic IPs?
Through the **NAT gateways**. Click to view [routing rule priority](https://cloud.tencent.com/doc/product/215/4954#.E8.B7.AF.E7.94.B1.E8.A7.84.E5.88.99.E4.BC.98.E5.85.88.E7.BA.A7).
