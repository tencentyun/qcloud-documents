## 1. How much bandwidth does a Direct Connect support?
Tencent Cloud Direct Connect service supports Direct Connect bandwidths of 2, 4, 6, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 155, 622, 1000, 2500, and 10000 Mbps.
## 2. Are there any restrictions on the amount of data traffic when using Direct Connect?
There is no restriction and you can transfer any volume of data. The maximum speed is the Direct Connect bandwidth you selected.
## 3. When using Direct Connect, which Tencent Cloud regions and availability zones are supported?
For one-time access to Tencent Cloud via Direct Connect in mainland China, Tencent Cloud's resources for all availability zones in the East China, South China, and North China are available for connecting. For Direct Connect in Hong Kong, currently you can only connect to Tencent Cloud Hong Kong Region. For North America Region, there's no Direct Connect support at the time.
## 4. Is the connection to Direct Connect redundant?
With Tencent Cloud physical Direct Connect, dual-line redundancy of entire network is supported. If you need a redundant configuration, please apply for two dedicated lines for Direct Connect, and indicate the redundant physical Direct Connect when applying for a second line.
## 5. Is there any service level agreement (SLA) for Direct Connect?
Not available yet.
## 6. Which routing protocols are supported by Direct Connect?
Tencent Cloud Direct Connect service support BGP route and static route.
## 7. What is the difference between Direct Connect and IPSec VPN connection?
The public network and IPsec protocol are used by IPSec VPN connection to establish an encrypted connection between your data center and VPC. You can purchase, enable and configure the VPN gateway in a few minutes. But the VPN connection may be interrupted due to Internet jitter, block or other public network quality problems. If users' services have low requirement for the network connection quality, it is a highly cost-effective choice for fast deployment.
Direct Connect provides you with a dedicated Direct Connect network connection solution, which needs relatively longer construction time, but can provide the network connection services with high quality and reliability. If your services have low requirement for the network quality and security, you may choose this solution for deployment.
## 8. Can I use both Direct Connect and IPsec VPN to connect to the same VPC?
Yes, you can. The network traffic is redirected according to the routing table of the VPC's subnet.
