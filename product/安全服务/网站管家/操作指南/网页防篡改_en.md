## Overview
The anti-tampering feature is used to prevent exceptional display on a specific page caused by tampering.
## Notes 
The specific page is limited to static resources, such as `.html`, `.js`, and `.txt`.
## Configuration Example 
### Preventing Home Page from Being Tempered
1. Log in to the [WAF Console](https://console.cloud.tencent.com/guanjia), click **Web Application Firewall** -> **Protection Settings**, and select the domain name to be protected (e.g. `www.qcloudwaf.com`), and then click **Anti-tampering** to enter the anti-tampering configuration page.
![Anti-tampering](https://mc.qcloudimg.com/static/img/c9106a237b587095888e7fcbe122925f/fangcuangai_01.png)
2. Click **Add Rules**, and enter the rule name (such as homepage) and the complete URL path of the homepage (e.g. `http://www.qcloudwaf.com/index.html`).
![Anti-tampering](https://mc.qcloudimg.com/static/img/68308add45699fe70de824009d582495/fangcuangai_02.png)
3. Click **Add** to save the rule, and then the rule will take effect. If there is an update of home page, click **Refresh Cache** to update the cache.
![Anti-tampering](https://mc.qcloudimg.com/static/img/2d06fd9d70dc242cb9e047bf31b86fd2/fangcuangai_03.png)

[Previous: CC Protection Settings](/document/product/627/11709)
[Next: Custom Policy](/document/product/627/11711)

