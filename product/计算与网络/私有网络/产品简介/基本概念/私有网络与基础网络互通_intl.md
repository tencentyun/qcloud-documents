Tencent Cloud Virtual Private Cloud (VPC) provides the ability to interconnect with basic network. The basic network CVM interconnected with VPC can actively access such computing resources as CVM and cloud database within VPC via private network. The CVM in the VPC can also actively access the basic network CVM via private network.

## 1. Basic Concepts
Tencent Cloud enables the Classiclink feature for eligible VPCs. The network communication between CVM within basic network and a specified VPC can be achieved by linking the CVM with the VPC. This free feature is only applicable to the interconnection between basic network CVM and VPC in the same region.

After being linked with the VPC, the basic network CVM can access such computing resources as CVM, cloud database, private network cloud load balancer and cloud cache within the VPC. However, the CVM in the VPC cannot access the computing resources other than CVM within basic network.

To avoid the conflict between IPs of basic network and VPC, we only enable Classiclink for the VPC within specific network segments.

The private IP of basic network CVM remains unchanged after the CVM is linked with VPC. You can use this IP access both computing resources in the VPC and other CVMs in the basic network.

The private IP of the linked basic network CVM can be automatically added to the local policy of VPC's routing table. You do not need to modify the routing table rules in the VPC. No additional configurations are needed after the interconnection is established.

When the link between basic network CVM and VPC is built, their security firewall and network ACL remain effective. That is to say, VPC subnet can restrict the access of the linked CVM within basic network by setting network ACL. The CVMs of both basic network and VPC can also be configured with security group rules to restrict mutual network access.

## 2. Usage Restrictions

- Only the VPC with the network segment of 10.[0~47].0.0/16 and its subset is supported
- A basic network CVM can be linked with one VPC at a time. To link with another VPC, you need to unbind the linked VPC first.
- After the basic network CVM is linked with VPC, the linkage is not allowed to be transferred. That is, the basic network CVM cannot access the public network or VPC resources outside the current VPC via the VPN gateway, Direct Connect gateway, public network gateway of the VPC or through peering connection. Likewise, the peer of VPN, Direct Connect and peering connection cannot access the basic network CVM.
- The cloud load balancer instance within VPC cannot be bound to the basic network CVM interconnected with the current VPC
- The access to such resources as basic network CDB, CMEM and LB is not supported for the CVM in the VPC
- Only the interconnection between basic network CVM and VPC in the same region is supported
- The interconnection relationship with VPC will not be unbound by actions against the CVM such as isolation due to arrears, security isolation, cold migration, failover, configuration modification, operating system switching and so on.
- The interconnection relationship with VPC will be unbound automatically after the CVM is returned.
