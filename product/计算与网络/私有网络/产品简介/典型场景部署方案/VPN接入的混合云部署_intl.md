According to your different connection needs, Tencent Cloud provides two services respectively to connect your enterprise data center and VPC: VPN connection and Direct Connect. The main differences are as follows:
- [VPN Connections](https://cloud.tencent.com/product/vpn.html) uses the public network and IPsec protocol to establish an encrypted network connection between your data center and VPC. VPN gateway can be purchased, take effect and be configured completely in a few minutes. But the VPN connection may be interrupted due to Internet jitter, block or other public network quality problems, and if users' businesses do not have high requirements for the network connection quality, it is a high cost-effective choice with fast deployment.
- [Direct Connect](https://cloud.tencent.com/product/dc.html) provides a dedicated direct network connection method. It has relatively long construction duration, but can provide high-quality, highly reliable network connection service. If your business has high requirements on network quality and network security, you can choose to deploy this program.

The following describes how to deploy a hybrid cloud using VPN Connections.

## Application Scenarios
VPN Connections is a service which connects your enterprise data center with Tencent Cloud Virtual Private Cloud (VPC) and provides secure and reliable encrypted communication through IPsec encrypted tunnels.
Currently, VPN tunnels support IKE/IPesec encryption protocol, and a maximum bandwidth of 100M. If you have special demands, we can also provide customized VPN connection services that will better suit your needs. Please fill in [Ticket for Application](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=168&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC).

> Note: Users need to pay for the public network bandwidth occupied by VPN tunnels. If you need a hybrid cloud interconnection bandwidth that is greater than 200M, it is recommended that you choose the [Direct Connect-Based Hybrid Cloud](https://cloud.tencent.com/document/product/215/7543) deployment scheme in Scenario 2.

The network quality of VPN tunnels depends on the network quality of public network connections. It is recommended that you test the network latency between your own IT resources and Tencent Cloud in different regions when choosing a region to deploy a VPC, so as to get the optimal hybrid cloud deployment architecture.

## Solutions:
**Cloud data center**: Deploy cloud data center in a VPC created on Tencent Cloud.
**Connection method**: VPN connection
**Network Segment Layout**: The network segment between the physical data center and the VPC that needs to be connected **cannot overlap**.


## Steps
Deploy cloud data center in a VPC created on Tencent Cloud, [Click here to view instructions](https://cloud.tencent.com/document/product/215/4927#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97).

**VPN connection** can be fully customized in the console. You need to complete the following steps to make the VPN connection to take effect:
1) Create VPN gateway
2) Create peer gateway
3) Create VPN tunnel
4) Load the configuration file in its own IPsec VPN gateway
5) Configure the routing table
6) Enable VPN tunnel
[Click here to view details](https://cloud.tencent.com/doc/product/215/4956#.E5.BF.AB.E9.80.9F.E5.85.A5.E9.97.A8)
