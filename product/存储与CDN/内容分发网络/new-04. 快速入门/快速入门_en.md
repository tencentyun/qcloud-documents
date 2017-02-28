You can get started with CDN service quickly by following these steps.



## Step 1: Activate CDN Service

You need to complete qualification verification and activate CDN service before you can use it. You can skip this step if CDN has already been activated for your Tencent Cloud account.



![](https://mccdn.qcloud.com/static/img/d5c70cd18181ccfc2877b33a4f558015/image.png)

## Step 2: Connect a Domain

1. Go to [CDN Console](https://console.qcloud.com/cdn) and click "Create a distribution" in "Domain Management" menu:	

   ![](https://mccdn.qcloud.com/static/img/aab5853c8e017d5abe14b043a5b3afab/image.png)

2. Enter basic information and the acceleration domain; select a content type and a proper origin type:

   ![](https://mc.qcloudimg.com/static/img/0f0615a58b0efb43bda5a44f88416e86/1.png)

3. Perform custom configuration based on actual business demand, such as cache configuration and hotlink protection configuration:

   ![](https://mccdn.qcloud.com/static/img/7c6a1d69406e92c51c9b0296e9c5e306/image.png)

4. Verify basic information and configuration. Click "Back" to modify, or "Submit" if all information is correct:

   ![](https://mc.qcloudimg.com/static/img/3b95a9deec69bb8c6a098c5a5810ee74/image.png)

5. The domain will be added once submitted. Please wait for the domain configuration (about 10 minutes).

   ![](https://mccdn.qcloud.com/static/img/8bd9ee32953db24d825be3ddcb9c47d6/image.png)



## Step 3: Configure CNAME

1. Once domain configuration is completed, the system will assign the corresponding CDN domain to you, which should be suffixed with .cdn.dnsv1.com:

   ​

   ![](https://mccdn.qcloud.com/static/img/93257fff3cdf7311a2108bfec8d9fab0/image.png)

2. You need to complete CNAME configuration at the DNS service provider of the connection domain to map your domain to the CDN domain using CNAME. To learn about how to configure it, please click [CNAME Configuration Instruction](https://www.qcloud.com/doc/product/228/3121);

3. Verify if domain CNAME resolution is successful: The time needed for the CNAME to take effect varies for different DNS service providers (usually within 30 minutes). You can also check whether a CNAME is in effect by using PING. If you are directed to the domain suffixed with "cdntip.com" or "tcdn.qq.com" by using PING, the domain CNAME is already in effect.

   ![](https://mccdn.qcloud.com/static/img/dbf7687249e59b5d0aeef4f9cdadfec5/image.png)
