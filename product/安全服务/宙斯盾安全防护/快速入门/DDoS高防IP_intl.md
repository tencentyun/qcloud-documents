Below is the flow chart of Tencent Cloud Aegis Anti-DDoS high-defense IP protection:
![Get started](https://main.qcloudimg.com/raw/50f86c7058e62640a279c292fc5d8bb8.png)
## **I. Preparation and Selection**
1. Sign up for a Tencent Cloud account
New user needs to **sign up** at [Tencent Cloud's official website](https://cloud.tencent.com/) and purchase Aegis Anti-DDoS. For more information, see [Signing up with Tencent Cloud](https://cloud.tencent.com/document/product/378/9603) and [Purchase Guide](https://cloud.tencent.com/document/product/685/15264) for Aegis Anti-DDoS.
2. Confirm high-defense IP region and network
 - Region selection principle
DDoS high-defense IP work in proxy forwarding mode. Therefore, please try to select a region near the physical location of your origin server. The closer the high-defense IP region is to the origin server, the lower the access latency and the higher the access speed.
 - Network selection principle
When selecting the network, take into account the region and the needs for peak bandwidth for protection. BGP network provides a better network experience, but its highest peak bandwidth for protection is lower than that of MUT high-defense IP. The maximum peak bandwidth for protection of MUT high-defense IP decreases in sequence of China Telecom, China Unicom and China Mobile. Please select the corresponding ISP based on your end user distribution and try to avoid cross-network access.
3. Confirm the configuration plan for high-defense IP
 - Peak bandwidth for base protection
 Peak bandwidth for base protection is prepaid. It is suggested that the peak bandwidth for base protection be set to higher than the average historical attack traffic. This makes sure base protection is robust enough to prevent most attacks.
 - Peak bandwidth for elastic protection
 Peak bandwidth for elastic protection is postpaid on a daily basis. It is suggested that the peak bandwidth for elastic protection be set to higher than the highest historical attack traffic. This makes sure potential IP blocking is avoided in case of large-traffic attacks. Meanwhile, elastic protection is pay-per-use and you only pay for what you use, significantly reducing the protection costs.
 - Forwarded business traffic
 This is the non-attacking traffic of normal business requests forwarded to the origin server. It can be charged by bandwidth or by traffic. It is recommended to select based on the characteristics of normal business traffic.

## **II. Creating High-defense IP Forwarding Rule Group**

After purchasing high-defense IP, you can view the assigned resources on the DDoS high-defense IP management page. DDoS high-defense IP provides protection service in proxy forwarding mode.
This section describes how to configure forwarding rule group and forwarding rule:
1. In Aegis Anti-DDoS Console, select **DDoS high-defense IP** to enter the DDoS high-defense IP management page;
 ![](https://i.imgur.com/Jl7I2Rm.jpg)
2. Click **Forwarding rule group** on the top of the page to enter the forwarding rule group management page.
 ![](https://i.imgur.com/MsqFmaW.jpg)
3. Click **Add a forwarding rule group** on the page and enter the rule group name and linked project name. After creating the rule group, you can directly select **Create a forwarding rule** or click the forwarding rule group ID in the rule group list to enter the details page to create a forwarding rule.
 ![](https://i.imgur.com/39tqC3z.jpg)
 ![](https://i.imgur.com/PY5rOkh.jpg)
4. On the rule group details page, click **Add a forwarding rule**, choose the protocol type and session hold, enter the forwarding port, origin server port and origin server IP address, and then click **OK** to complete forwarding rule creation.
Forwarding ports and origin server ports can be entered in batch where these ports correspond one-to-one in sequence, so you can batch create multiple rules.
 ![](https://i.imgur.com/qSdOS2p.jpg)

## **III. Binding Forwarding Rule Group to High-defense IP**
After the forwarding rule group and forwarding rule are created, you need to bind them to high-defense IP in the Action column.
Click **Bind to high-defense IP** in the column to enter the protected IP interface, select the high-defense IP to bind and click **OK** to complete binding.
![](https://i.imgur.com/9MSxCEJ.jpg)
![](https://i.imgur.com/AEJdO9K.jpg)
After completing the configuration described above, your origin server is protected by high-defense IP. Verify end-to-end connectivity and then point the business requests to the high-defense IP to get protection from Aegis Anti-DDoS.

## **IV. Creating Business and Enabling Protective Domain Name (Optional)**
If your business supports access via domain name, you can also configure the CNAME set at your primary domain name's DNS provider to the free protective domain name, add high-defense IP to the business, and then enable domain name resolution to intelligently resolve end user's source IP to the high-defense IP.
Relevant configurations are described below:
1. In Aegis Anti-DDoS Console, select **Business list** on the left to enter the business management page and click **Create a business**;
 ![](https://i.imgur.com/PWJONt5.jpg)
2. Choose the linked project, enter the business name, contact and mobile number, and choose the development platform and business category. Click **Create** to complete;
 ![](https://i.imgur.com/PVt4Wjz.jpg)
3. After creating the business, click Protective domain name in the business list to enter the domain name management page and click **Add a high-defense IP**;
 ![](https://main.qcloudimg.com/raw/a9bae728b04fc82fce3e97d6544bb2b9.png)
4. Choose the high-defense IP to be used for the business and enable Name resolution.
 ![](https://i.imgur.com/UetB42r.jpg)

After the aforementioned configurations are completed, domain name resolution takes effect. Then, configure the CNAME resolution to the protective domain name at the primary domain name service provider to enable domain name access.
