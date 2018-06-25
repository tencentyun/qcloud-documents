## Accessing to Dayu High Defense IP Service (For non-Tencent Cloud Servers)

**Step 1: Log in to the console and go to the High Defense IP Configuration page**

Log in to the **[Dayu Anti-DDoS](https://console.cloud.tencent.com/dayu/bgpip)** console. Select **High Defense IP** from the left panel and find the high defense IP that deployed on non-Tencent Cloud servers, and then click the instance ID to go to the configuration page.

![](https://mc.qcloudimg.com/static/img/8ef58dac854d557cf557688e63a2bd2a/image.png)
 
**Step 2: Create a forwarding rule**

Select **Non-website business** or **Website Business** in the **Forwarding Rules** configuration bar, and then click **New** to create a forwarding rule.

![](https://mc.qcloudimg.com/static/img/9ca82943f397177cfe4dd7413d4b598d/image.png)
 
**1. Create a forwarding rule for non-web based business**

Select TCP in Forwarding Protocol, and then enter the forwarding port (through which the high defense IP can access, usually the same as the origin server port), origin server port (through which the origin server provides services) and origin server IP, as shown below:

![](https://mc.qcloudimg.com/static/img/b21663cb5be292fad6de43fc3a8ed664/image.png)
 
**Notes**

- 80/443 port cannot be configured for non-web based business.
- You can only "Edit" or "Delete" existing 80/443 forwarding rules under non-web based business. To add a forwarding rule for 80/443 port, configure it in "Web Based Business".
- 80/443 port cannot be configured for non-web based business and web-based business at the same time.
- Separate IPs by pressing Enter. A maximum of 20 public IPs from the target IP forwarding area can be added.
- Load balancing of multiple origin servers is performed in polling mode. A maximum of 60 forwarding rules can be configured for a high defense IP.
- Click "OK" to general a forwarding rule.

**2. Create a forwarding rule for web-based business**

Enter the domain name and select HTTP or HTTPS protocol for web-based business, as shown below:

**2.1** If you select the HTTP protocol, the origin server port is 80. Enter the origin serve IP. 

Note: Separate IPs by pressing Enter. A maximum of 20 public IPs from the target IP forwarding area can be added.

![](https://mc.qcloudimg.com/static/img/9d541e1800948ed51a7c589b4126cf97/image.png)
 
**2.2** If you select the HTTPS protocol, the origin server port is 443. You can select your own certificate or Tencent Cloud hosting certificate, and then enter the origin server IP.

Note: Separate IPs by pressing Enter. A maximum of 20 public IPs from the target IP forwarding area can be added.

![](https://mc.qcloudimg.com/static/img/2ea8bc512c99a72270dbbc96a32bf888/image.png)
 
**Step 3: Switch the business to high defense IP**

##Accessing to High Defense IP (for Tencent Cloud servers)

**Step 1: Log in to the console and go to the High Defense IP Configuration page**

Log in to the **[Dayu Anti-DDoS](https://console.cloud.tencent.com/dayu/bgpip)** console. On the "High Defense IP" control page, find the high defense IP instance of the business you enabled and deployed on Tencent Cloud, and then click the instance ID to go to the configuration page.

![](https://mc.qcloudimg.com/static/img/3fa91839afbc62d81a7960500a4a5920/image.png)
 
**Step 2: Create a listener**

In Basic Configuration, choose the protocol port as required. :

![](https://mc.qcloudimg.com/static/img/69e9afef020cac7c7898391ecff1e4a6/image.png)
 
In Advanced Configuration, configure according to actual business conditions.
![](https://mc.qcloudimg.com/static/img/da76509e7c6ee80778c92d8998e36892/image.png)
 
Health Check is enabled by default and can automatically remove failed service ports and keep the business available.

**Step 3: Bind a CVM and set weight**

![](https://mc.qcloudimg.com/static/img/dc349f14824c8562bd0b7e5ffe41e463/image.png)
 
**Step 4: Enable Elastic Defense & CC Defense and set the peak of elastic defense & threshold of HTTP requests**
 
![](https://mc.qcloudimg.com/static/img/f08d6a2ce578f602de1ce45a5067017f/image.png)


