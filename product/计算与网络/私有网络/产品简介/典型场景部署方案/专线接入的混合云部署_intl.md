According to your different connection needs, Tencent Cloud provides two services respectively to connect your enterprise data center and VPC: VPN connection and Direct Connect. The main differences are as follows:
- [VPN Connections](https://cloud.tencent.com/product/vpn.html) uses the public network and IPsec protocol to establish an encrypted network connection between your data center and VPC. You can purchase, enable and configure the VPN gateway in a few minutes. But the VPN connection may be interrupted due to Internet jitter, block or other public network quality problems. If users' services have low requirement for the network connection quality, it is a highly cost-effective choice for fast deployment.
- Direct Connect provides a dedicated direct network connection method. It has relatively long construction duration, but can provide high-quality, highly reliable network connection service. If your business has high requirements on network quality and network security, you can choose to deploy this program.

The following describes how to deploy a hybrid cloud using **Direct Connect**.

## Application Scenarios
Direct Connect provides a fast and secure approach to connect Tencent Cloud with local data centers. Users can have access to Tencent Cloud computing resources in multiple regions in one go using a physical direct connection line, to achieve a flexible and reliable hybrid cloud deployment.

There are two ways to set up a slave for Direct Connect
- **Dual Direct Connect** slave, Tencent Cloud supports main/slave failover configuration.
![](https://mc.qcloudimg.com/static/img/a73e60175bb118a137f1b9817e0a695b/VPC-Direct+Connect-accessed.png)

- **VPN connection** serves as Direct Connect slave (master/slave).

>Note:
> Your **network segment** between VPC and data center does not affect their communication, for Tencent Cloud Direct Connect gateway supports NAT. [Click here to view details](https://cloud.tencent.com/doc/product/215 /4976#.E4.B8.93.E7.BA.BFnat).

## Solutions:
**Cloud data center**: Use CVM and Cloud Database to deploy cloud data center in a VPC created on Tencent Cloud.
**Connection method**: Integrate VPC data center with your IDC private network via physical Direct Connect.
**Slave connection method**: Dual Direct Connect/VPN connection


## Steps
If Direct Connect is to used to connect your data center and the VPC Data Center on Tencent Cloud, you need to complete the following steps:
Step 1: Creating a physical Direct Connect
Step 2: Creating a Direct Connect tunnel
Step 3: Creating a Direct Connect tunnel for Direct Connect gateway, thus connecting your data center to your VPC.
(Optional) Step 4: Configuring the Direct Connect NAT
Step 5: Configuring the routing table associated with the subnets to be communicated with.
Step 6: You can set up slaves for a Direct Connect by creating multiple physical Direct Connect or VPN connections.
[Click here to view details](https://cloud.tencent.com/doc/product/215/4976#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97)

