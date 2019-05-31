## Overview
The anti-tampering feature is used to prevent exceptional display on a specific page caused by tampering.
## Notes 
The specific page is limited to static resources, such as `.html`, `.js`, and `.txt`.
## Configuration Example 
### Preventing homepage from being tempered
1. Log in to the [WAF Console](https://console.cloud.tencent.com/guanjia), click **Web Application Firewall** -> **Defense Settings**, and select the domain name to be protected (e.g. `www.qcloudwaf.com`), and then click **Tamper Resistance**.
![](https://main.qcloudimg.com/raw/21643cd78783fac306ae8aade064aab0.png)
2. Click **Add a Rule**, and enter the rule name (such as homepage) and the complete URL path of the homepage (e.g. `http://www.qcloudwaf.com/index.html`).
![](https://main.qcloudimg.com/raw/f64f52177854f67b2dfb57086105cb9c.png)
3. Click **Add** to save the rule, and the rule will take effect immediately. If there is an update of homepage, click **Refresh** to update the cache.
![](https://main.qcloudimg.com/raw/0292f8dd8b035478811e881e1e61a55b.png)

[Previous: CC Defense Settings](/document/product/627/11709)
[Next: Custom Rule](/document/product/627/11711)

