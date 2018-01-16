## Fast Access to BGP High Defense IP (for business not deployed on Tencent Cloud)

**Step 1: Log in to the console and go to the High Defense IP Configuration page**

Log in to the **[Dayu Network Security]()** console. Select **BGP High Defense IP** from the left panel and find the high defense IP that deployed on the non-Tencent Cloud platform, and then click the instance ID to go to the configuration page.

 ![](//mc.qcloudimg.com/static/img/db5df43e3e35f514ce3e04261c36c583/image.png)
 
 ![](//mc.qcloudimg.com/static/img/d1af7bb865544d4bb0b0bb9b86c83989/image.png)
 
**Step 2: Create a forwarding rule**

Select **Non-web based** or **Website Business** in the **Forwarding Rules** configuration bar, and then click **New** to create a forwarding rule.

 ![](//mc.qcloudimg.com/static/img/7eaa40490cbfbf604afdd01973ececbd/image.png)
 
**1. Create a forwarding rule for non-web based business**

Select TCP in Forwarding Protocol, and then enter the forwarding port (through which the high defense IP can access, usually the same as the origin server port), origin server port (through which the origin server provides services) and origin server IP, as shown below:

 ![](//mc.qcloudimg.com/static/img/e7fd75b7e97ab83d9a157d230eb1d6c8/image.png)
 
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

 ![](//mc.qcloudimg.com/static/img/cab68b62607fe8fccfc1514eed4d760d/image.png)
 
**2.2** If you select the HTTPS protocol, the origin server port is 443. You can select your own certificate or Tencent Cloud hosting certificate, and then enter the origin server IP.

Note: Separate IPs by pressing Enter. A maximum of 20 public IPs from the target IP forwarding area can be added.

 ![](//mc.qcloudimg.com/static/img/f56642c8a1dabf436485ab44a8eb2317/image.png)
 
 ![](//mc.qcloudimg.com/static/img/e69fe2de74fab21bc9189a10b33c2b54/image.png)
 
**Step 3: Switch the business to high defense IP**

## Fast Access to BGP High Defense IP (for users whose business is deployed on Tencent Cloud)

**Step 1: Log in to the console and go to the High Defense IP Configuration page**

Log in to the "Dayu Network Security" console. On the "BGP High Defense IP" control page, find the high defense IP instance of the business you enabled and deployed on Tencent Cloud, and then click the instance ID to go to the configuration page.

 ![](//mc.qcloudimg.com/static/img/86171ae6f5c7d06ddf5a3549049528e9/image.png)
 
**Step 2: Create a listener**

In Basic Configuration, choose the protocol port based on business conditions. Select Layer-4 forwarding for high defense IP, and TCP for Layer-7 application protocol such as HTTP, as shown below:

![](//mc.qcloudimg.com/static/img/2f0c6d6607a6626859f9e6b768d96f10/image.png)
 
In Advanced Configuration, configure according to actual business conditions. If you are not sure, keep the default configuration.
![](//mc.qcloudimg.com/static/img/461e7fbf6aa40f4eaa2e4f2be5e6ce0f/image.png)
 
Health Check is enabled by default. You are recommended not to change the configuration. This module can automatically remove failed service ports and keep the business available.

**Step 3: Bind a CVM and set weight**

 ![](//mc.qcloudimg.com/static/img/b965ac4bc71ac1a2817c7eb6e73090c7/image.png)
 
**Step 4: Enable Elastic Defense & CC Defense and set the peak of elastic defense & threshold of HTTP requests**
 
![](//mc.qcloudimg.com/static/img/097c4a80f3bf53081f874c9fe677d8dc/image.png)

