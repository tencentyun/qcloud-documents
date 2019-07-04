You can get started with CDN service quickly by following these steps.



## Step 1: Activate CDN Service

You need to complete qualification verification and activate CDN service before you can use it. You can skip this step if CDN has already been activated for your Tencent Cloud account.



![](https://mc.qcloudimg.com/static/img/e18070b417464286ac4badf201f9c766/1.png)

## Step 2: Connect a Domain

1. Go to [CDN Console](https://console.cloud.tencent.com/cdn) and click "Create a distribution" in "Domain Management" menu:	

   ![](https://mc.qcloudimg.com/static/img/81a12799500ecd1cc2c5668755db6cd0/2.png)

2. Enter basic information and the acceleration domain; select a content type and a proper origin type.

   Perform custom configuration based on actual business demand, such as cache configuration:

   ![](https://mc.qcloudimg.com/static/img/18d66f24137e00ac86bd5e5795300adb/3%283%29.png)

   ​

3. The domain will be added once submitted. Please wait for the domain configuration (about 10 minutes).

   ![](https://mc.qcloudimg.com/static/img/0a03db953d30949addab41f3c7078a45/4.png)



## Step 3: Configure CNAME

1. Once domain configuration is completed, the system will assign the corresponding CDN domain to you, which should be suffixed with .cdn.dnsv1.com:

   ![](https://mc.qcloudimg.com/static/img/91d44977a92cde67d2ee52568d0bb694/5.png)

2. You need to complete CNAME configuration at the DNS service provider of the connection domain to map your domain to the CDN domain using CNAME. To learn about how to configure it, please click [CNAME Configuration Instruction](https://cloud.tencent.com/doc/product/228/3121);

3. Verify if domain CNAME resolution is successful: The time needed for the CNAME to take effect varies for different DNS service providers (usually within 30 minutes). You can also check whether a CNAME is in effect by using PING. If you are directed to the domain suffixed with "cdntip.com" or "tcdn.qq.com" by using PING, the domain CNAME is already in effect.

   ![](https://mc.qcloudimg.com/static/img/d89485f878a6a08c594bd8f65c961ed8/6.png)
