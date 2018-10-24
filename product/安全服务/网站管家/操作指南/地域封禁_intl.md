## Overview
The region blocking feature can add overseas regions and major Chinese provinces into blacklist.

## Configuration Instructions
1. Log in to the [WAF Console](https://console.cloud.tencent.com/guanjia), click **Web Application Firewall** -> **Defense Settings**, and select the domain name to be protected.

 ![p1](https://main.qcloudimg.com/raw/36aeb3ce69e92275a5806bbc994df5c1.png)

2. Click **Basic Settings** -> **Edit Blocked Region**.

 ![p2](https://main.qcloudimg.com/raw/fc8c58a8970b205d513e12c3b0189eb3.png)

3. Select the region you want to block and click **Confirm**.

 ![p3](https://main.qcloudimg.com/raw/3c129ead884d668bf2a28c1641ce1b76.png)

4. Enable **Region Blocking Status**.

 ![p4](https://main.qcloudimg.com/raw/174ff48be5c2146a53cb459f65867ad0.png)

5. After that, the regions you chose to block will not be able to access your website.
 This document takes Guangdong Province as an example. After Guangdong Province is listed in the blocked regions, when you visit the website with a local IP (China Telecom, Shenzhen, Guangdong Province), WAF will prompt that you have been blocked by Tencent Cloud WAF.
 ![p6](https://main.qcloudimg.com/raw/89d4a5579c351a54f3d9984416a57c14.png)

