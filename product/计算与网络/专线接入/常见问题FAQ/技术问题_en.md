### What bandwidth configurations does Direct Connect support?
Tencent Cloud Direct Connect supports the following bandwidth (in Mbps): 2, 4, 6, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 155, 622, 1,000, 2,500 and 10,000.

### Is there a limit set on the volume of data transferred when Direct Connect is used?
No. You can transfer any amount of data with the bandwidth you selected for Direct Connect as the maximum transfer speed.

### Which Tencent Cloud regions and availability zones can be connected when Direct Connect is used?
One-off access to Tencent Cloud using Direct Connect in Mainland China allows you to connect to Tencent Cloud resources of all availability zones in three major regions: East China, South China and North China. Hong Kong Direct Connect is only used to connect to Tencent Cloud Hong Kong region. North America cannot be accessed via Direct Connect.

### Is the connection to Direct Connect redundant?
Tencent Cloud Physical Direct Connect to support full network dual-line redundancy. If you need redundancy configuration, apply for two Direct Connect lines, and indicate the Physical Direct Connect corresponding to the redundancy when you apply for the second one.

### Is Service-Level Agreement (SLA) provided for Direct Connect?
No.

### Which routing protocols are supported for Direct Connect?
Tencent Cloud Direct Connect supports two service protocols: BGP routing and static routing.

### What is the difference between Direct Connect and IPSec VPN Connection?
IPsec VPN Connection uses public network and IPsec protocol to establish an encrypted network connection between your IDC and VPC. The purchase, enforcement and configuration of VPN gateway can be completed within minutes. However, the VPN connection may be interrupted by public network quality such as Internet jitter and congestion. When your business does not require high quality network connections, it is a fast and cost-effective option for deployment.

Direct Connect provides a dedicated network connection solution, which needs a relatively longer construction time, but can provide network connection services with high quality and reliability. If your businesses have low requirement for the network quality and security, you can choose this solution for deployment.

### Can both Direct Connect and IPsec VPN Connection be used to access the same VPC?
Yes. Network traffic flows according to the routing table of the subnet in the VPC.

### What if the stress testing for the bandwidth of Direct Connect is failed?
* Reconfirm the bandwidth you purchased for Direct Connect.
* Test whether packet loss occurred in the interconnection `ip fping`. If the loss rate is high, contact Tencent Cloud after-sales team for troubleshooting. If Direct Connect is built by users, report the failure to the ISP as well.
* Check whether the duplex mode of local Direct Connect router is full duplex.
* Try to initiate multiple processes from multiple clients and cloud servers using tools like `iperf`, and test whether the traffic is acceptable by performing stress testing, if no problem with application.
* If no problem is found, contact Tencent Cloud after-sales team for assistance.

### What if the Direct Connect used to access Tencent Cloud is interrupted?
* Interconnection IPs on both ends cannot be `pinged`, and MAC addresses cannot be received from both ends. Tencent Cloud after-sales team can be notified of alarm message automatically if Direct connect is exceptional.
* When the interruption is confirmed:
 - If Tencent Cloud owns the Direct Connect, report it to Tencent Cloud after-sales team as soon as possible. Generally, the after-sales team reports the automatic alarm of Direct Connect failure to the ISP immediately when they receive it.
 - If you are the owner of Direct Connect, you need to report the failure to the ISP. Contact the after-sales team if you need cooperation from Tencent Cloud.

### What if a specific IP address range of Direct Connect cannot be pinged?
* Confirm whether the network is a new IP address range. If so, a router needs to be configured on the cloud.
* Check whether the routing table on the cloud to be directed to the Direct Connect gateway is configured with an IP address range that cannot be pinged. Confirm whether the client server has a route to be directed to the Direct Connect.
* Confirm whether associated security group, network ACL and other security features are provided on the cloud, and whether security features like iptables are configured for the client server.
* If no exception is found, provide the troubleshooting information to the after-sales team for follow-up.

### For other problems, provide the following information as much as possible, to help improve the efficiency of troubleshoot.
* Description of the problem, and check whether it may reoccur
* The source/destination IP address pair in question
* Region information of Direct Connect
* Direct Connect gateway ID
* "ping/traceroute" screenshot when a failure occurred
* "iptables", "nat" and other information
* Access topology

