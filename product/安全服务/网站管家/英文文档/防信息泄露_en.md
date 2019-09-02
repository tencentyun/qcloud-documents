## Overview
The anti-information-leakage feature replaces the sensitive information returned from your web pages, such as mobile numbers, ID numbers.

## Configuration Example
1. Log in to the [WAF Console](https://console.cloud.tencent.com/guanjia), click **Web Application Firewall** -> **Protection Settings**, and select the domain name to be protected, and then click the **Anti-information-leakage** tab to enter the anti-information-leakage configuration page.
![](https://mc.qcloudimg.com/static/img/420ed7c79be86c2f1913f88bb6ecf94d/image.png)
2. Click **Add Rules**, and enter the rule name, select the matching conditions (the matching field is "sensitive information", and the matching condition is "contain", and the matching content is "ID card" or "mobile number") and the action (replacement or observation), and then click **OK**.
![](https://mc.qcloudimg.com/static/img/3493f316555de86c9ca6acb94c320739/image.png)
3. The rule takes effect, and the sensitive information returned from your web pages will be protected.
Protection effect (the sensitive content is fictitious).
 - **Before:**
![开启防护前](https://mc.qcloudimg.com/static/img/a1f9740fafcf3f8913cc5d5c3370e7f7/image.png)
 - **After:**
![开启防护后](https://mc.qcloudimg.com/static/img/6a738492711125c684fa0f132ba74250/image.png)

