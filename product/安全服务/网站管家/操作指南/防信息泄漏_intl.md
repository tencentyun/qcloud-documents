## Overview
The anti-data leak feature supports replacing the sensitive information returned from your web pages, such as mobile numbers, ID numbers.

## Configuration Example
1. Log in to the [WAF Console](https://console.cloud.tencent.com/guanjia), click **Web Application Firewall** -> **Defense Settings**, and select the domain name to be protected, and then click the **Leak Resistance** tab.
![](https://main.qcloudimg.com/raw/f52f8aa75c5e745ddbb7fb954ff182af.png)
2. Click **Add a Rule**, and enter the rule name, select the matching conditions (the matching field is "sensitive info", and the matching condition is "Includes", and the matching content is "ID card" or "mobile number") and the action is "replace" or "observe", and then click **Confirm**.
![](https://main.qcloudimg.com/raw/d9e0604cc0fa8f3b6482231c10d028cf.png)
3. Onece the rule takes effect, the sensitive information returned from your web pages will be protected.
Defense effect (the sensitive content is fictitious).
 - **Before defense is enabled:**
 ![](https://main.qcloudimg.com/raw/294553dd559c425d29e6a96ed64c126e.png)
 - **After defense is enabled:**
 ![](https://main.qcloudimg.com/raw/723fb0f2de676996a3400095b447a3cd.png)

