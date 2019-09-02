## Product Overview
Direct Connect provides a fast and secure approach to connect Tencent Cloud with local data centers, by which the users can have access to Tencent Cloud computing resources in the multiple regions in one time using a physical Direct Connect, to achieve a flexible and reliable hybrid cloud deployment.

## Components
Direct Connect consists of three parts: physical Direct Connect, Direct Connect tunnel and Direct Connect gateway.
1) **Physical Direct Connect**: the physical line connection used to connect Tencent Cloud with local data centers. There are two methods to establish: by users themselves by communicating with the operators, or by Tencent Cloud. Physical Direct Connect supports dual-line hot backup connect, dual-line access point power supply, complete network pipeline isolation.
2) **Direct Connect tunnel**: Direct Connect tunnel is the network link segmentation of the physical Direct Connect. Users can create the Direct Connect tunnels connected to different Direct Connect gateways to achieve the interconnection between the local data center and multiple VPCs.
3) **Direct Connect gateway**: Direct Connect traffic entry for VPC, which can have the interconnection with different IDCs by connecting to multiple Direct Connect tunnels. Direct Connect gateway is enabled in the cluster manner, without SPOF (single point of failure) risk in the full path, which can meet the finance-level network interconnection requirements.

Direct Connect gateway serves as the bridge connecting VPC to the physical Direct Connect, and you can create a Direct Connect tunnel associated with a Direct Connect gateway inside a physical Direct Connect. The Direct Connect gateway can connect with Direct Connect tunnels from more than one physical Direct Connects to link with multiple local data centers. You can create only one Direct Connect gateway for each VPC in the Direct Connect gateway console. The created gateway can link with the requests for Direct Connect tunnels from different physical Direct Connects.

## Differences from IPsec VPN
| Advantages | Direct Connect | IPsec VPN |
|---------|---------|---------|
| Stable network latency | Tencent Cloud Direct Connect delivers a reliable and guaranteed performance on network latency, which is guaranteed of over 99.5%. You can avoid unstable network latency resulted from congestion or fault bypass through a fixed routing configuration | Tencent Cloud network connection setup by IPsecVPN is based on the Internet, and may lead to unstable latency due to routing bypass resulted from link congestion during network peak |
| Highly reliable disaster recovery | Both network access and network forwarding devices for Tencent Cloud Direct Connect are deployed in a distributed and clustered manner. With highly reliable configuration adopted along the whole network link and two ISP uplinks supported, your demand of over 99.95% high availability is guaranteed. | Tencent Cloud IPsec VPN gateway uses dual-system hot backup configuration, leading to a highly reliable gateway layer, but can't provide the same level of reliability as Direct Connect because Internet network link is not always reliable |
| Support large bandwidth | With Tencent Cloud Direct Connect, a single-line support maximum 10 Gbps bandwidth connection, and you can also implement  load balancing by using multiple 10 Gbps links , theoretically with no ceiling | A single gateway of Tencent Cloud IPsec VPN support maximum 100 Mbps bandwidth. Multi-VPN gateway is supported by VPC. For VPN access of over 100 Mbps, you can use multi-VPN gateway configuration |
| High security | With Tencent Cloud Direct Connect, the network link is used exclusively, with high security and no risk of data leakage, which can be used to meet the rigid network connection requirements of the financial industry, government and other enterprises | Tencent Cloud IPsec VPN network implements encryption by transmitting IKE protocol-based pre-shared secret key and can meet the vast majority of network transmission security requirements |
| Support network address translation | With Tencent Cloud Direct Connect, you can configure network address translation service on gateway, and support IP mapping on both endpoints of Direct connect and IP port mapping on VPC endpoint. Address conflicts resulted from multi-third party network interconnection can be solved perfectly |





