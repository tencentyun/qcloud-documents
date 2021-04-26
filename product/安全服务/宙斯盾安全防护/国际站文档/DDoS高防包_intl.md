# **Getting Started with DDoS High-defense Packet** #
Below is the flow chart of Tencent Cloud Aegis Anti-DDoS high-defense packet:
![](https://main.qcloudimg.com/raw/7029e392a6f9242894bea188961a296b.png)
## **I. Preparation and Selection** 
1. Sign up for a Tencent Cloud account
New user needs to **sign up** at [Tencent Cloud's official website](https://cloud.tencent.com/) and purchase Aegis Anti-DDoS. For more information, see [Signing up with Tencent Cloud](https://cloud.tencent.com/document/product/378/9603) and [Purchase Guide]() for Aegis Anti-DDoS.
2. Confirm the region for high-defense packet
 - Region selection principle
DDoS high-defense packet can only provide high-defense protection for Tencent Cloud public IPs in the same region where it is available. Therefore, please be sure to select the packet available in the region where your Tencent Cloud origin server is located.
3. Confirm the configuration plan for high-defense IP
 - Protection scope
 You can choose single-IP or multi-IP mode. In single-IP mode, high-defense packet can be bound to one Tencent Cloud public IP which utilizes the peak bandwidth for protection exclusively. In multi-IP mode, high-defense packet can be bound to multiple Tencent Cloud public IPs which share the resources. When multiple IPs are under DDoS attacks, if the peak bandwidth of the combined attack traffic is higher than the peak bandwidth for protection, blocking will start from the IP address suffering the largest attack traffic.
 - Peak bandwidth for base protection
 Peak bandwidth for base protection is prepaid. It is suggested that the peak bandwidth for base protection be set to higher than the average historical attack traffic. This makes sure base protection is robust enough to prevent most attacks.
 - Peak bandwidth for elastic protection
 Peak bandwidth for elastic protection is postpaid on a daily basis. It is suggested that the peak bandwidth for elastic protection be set to higher than the highest historical attack traffic. This makes sure potential IP blocking is avoided in case of large-traffic attacks. Meanwhile, elastic protection is pay-per-use and you only pay for what you use, significantly reducing the protection costs.

## **II. Adding Protected IP**
After purchasing high-defense packet, you can view the assigned resources on the DDoS high-defense packet management page. DDoS high-defense packet provides direct DDoS protection capabilities to Tencent Cloud public IP addresses.
This section describes how to add IPs.
1. In Aegis Anti-DDoS Console, select **DDoS high-defense packet** on the left to enter the DDoS high-defense packet management page;
 ![](https://i.imgur.com/EyS5666.jpg)
2. In the high-defense packet list, click the number of IPs in the **Number of bound IPs** column to enter the protected IP list;
 ![](https://i.imgur.com/SWyyKSx.jpg)
3. In the protected IP list, click **Add an IP** and choose the IP address to be added to the high-defense packet for protection;
 ![](https://i.imgur.com/nPTbOqg.jpg)
 ![](https://i.imgur.com/itOyZcR.jpg)
4. After added, the IP address will be protected by Aegis Anti-DDoS.
![](https://i.imgur.com/7wzmM0D.jpg)
