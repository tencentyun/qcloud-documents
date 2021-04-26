**Overview of Steps**

![Flow Chart](https://mc.qcloudimg.com/static/img/5a3583a665decdd4ffe2985dec6871ae/cdn-start.png)
## Step 1: Activate CDN Service
First of all, you need to complete identity verification and activate CDN service. You can proceed with Step 2 if CDN has been activated for your Tencent Cloud account.
### 1. Complete Identify Verification
By logging in to the [CDN Console](https://console.cloud.tencent.com/cdn), you can see the identity verification guide. Click "Go to Verify" to complete identity verification.
![](https://mc.qcloudimg.com/static/img/1784f11f0b2ffcdda8872c50550804b5/identity.png)
You can also go to the [Account Center](https://console.cloud.tencent.com/developer) and click ["Identity Verification"](https://console.cloud.tencent.com/developer?to=auth) to complete verification.
![](https://mc.qcloudimg.com/static/img/89cf6aefa8292bdc64662fcc8817a397/auth.png)
> For more information about the verification process, please see [Identity Verification Guide](https://cloud.tencent.com/doc/product/378/3629). Individual verification is completed immediately after the application is submitted. It takes about one working day to review the enterprise verification, and a notification is sent to you via SMS when the verification is completed. You can [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=1&level2_id=41&level1_name=%E5%85%AC%E5%85%B1%E5%9F%BA%E7%A1%80%E7%B1%BB%E9%97%AE%E9%A2%98&level2_name=%E8%B4%A6%E5%8F%B7%E7%B1%BB) to query the identity verification progress.

### 2. Add Service Information
After the identity verification is completed, log in to the [CDN Console](https://console.cloud.tencent.com/cdn), confirm your identity verification information, then select the service content, and click "Next".
![](https://mc.qcloudimg.com/static/img/7ddd56c73162b7ff908c70f52b3eb4e1/addinfo.png)
### 3. Select a Billing Method
Add service information before you can select the billing method on the [CDN Console](https://console.cloud.tencent.com/cdn). For more information on how to calculate prices, please see [Billing](https://cloud.tencent.com/doc/product/228/2949).
![](https://mc.qcloudimg.com/static/img/b13dd5b1c61fc44a44824d7d45cd1a9c/paychoose.png)
Confirm the billing method, click "Activate CDN" and jump to the CDN overview page, to get an overall picture of your CDN.
![](https://mc.qcloudimg.com/static/img/eff4d520fb07998d741a95719d966937/cnddesc.png)

## Step 2: Access a Domain Name
1. Go to the [CDN Console](https://console.cloud.tencent.com/cdn), click "Domain Management" in the left navigation bar, and click "Add Domain Name".
![](https://mc.qcloudimg.com/static/img/b1c4623293ce5e4600bd905d5a795622/addhost.png)

2. Enter the related configuration of both domain name and acceleration service.
Enter the domain name to be accelerated in **Domain Name** field. The following conditions must be met:
+ An ICP license have been obtained from MIIT for your domain name.
+ The domain name has not been accessed to Tencent Cloud CDN.

The selected **service type** determines which resource platform is used by the domain name. Acceleration configurations vary with resource platforms. Choose the service type that matches your business:
-  Static content: Suitable for acceleration scenarios for static resources such as e-commerce, websites and game images.
-  Downloading: Suitable for scenarios such as download of game installation packages and audio/video source files, mobile phone firmware delivery.
-  Streaming Media VOD acceleration: Suitable for scenarios such as audio/video VOD acceleration.
-  Streaming Media LVB acceleration: Suitable for scenarios such as LVB, ILVB downstream acceleration.
![](https://mc.qcloudimg.com/static/img/b2fdd0bef148d38e256aaf8b9648433f/addhost.png)

3. The domain name is added once submitted. Wait for the domain name configuration to be distributed to all nodes of the network, which takes about 15 minutes.
![](https://mc.qcloudimg.com/static/img/c3ff6aae83f3b19b242f859df32ab7bd/addok.png)

## Step 3: Configure CNAME
1. When the configuration of domain name is completed, a corresponding **CNAME** suffixed with "```.cdn.dnsv1.com```" is assigned to you by the system.
![](https://mccdn.qcloud.com/static/img/93257fff3cdf7311a2108bfec8d9fab0/image.png)

2. You need to complete CNAME configuration at the DNS service ISP of the accessed domain name. For more information about the configuration method, please see [CNAME Configuration](https://cloud.tencent.com/doc/product/228/3121).

3. Verify whether the CNAME is in effect: The time needed for the CNAME to take effect varies with different DNS service ISPs (usually within 30 minutes). You can also check the effectiveness of CNAME by use of PING. If a domain name suffixed with "```.sp.spcdntip.com```" is pinged, then the CNAME has taken effect.
![](https://mc.qcloudimg.com/static/img/13b5d4cc294c6f11543553a4d0f61b09/ping.png)
