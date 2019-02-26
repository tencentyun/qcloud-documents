## Overview
Custom policy allows for controlling accesses of public network users by combining multiple features such as request paths, GET parameters, POST parameters, Referer, and User-Agent of HTTP messages, and performing feature matching. For various attacks on the Internet, Tencent Cloud users can respond flexibly with custom policies, using a combination of rules to block them easily.

## Notes
- Each custom policy can set up to five conditions for feature control.
- The relationship between multiple conditions in each custom policy is "AND", that is, the policy does not take effect unless all the conditions are matched.
- For each custom policy to be matched, you can configure two consequential actions: block and allow.

## Configuration Case
### Case 1: Prohibiting specific IP addresses from accessing a designated site
To prohibit a specific IP address from accessing the designated site, the webmaster can:
1. Log in to the [WAF Console](https://console.cloud.tencent.com/guanjia), click **Web Application Firewall** -> **Protection Settings**, select the domain name of the site to be protected, and click **Custom Policy** to enter the custom policy configuration interface.
![Custom Rules](https://mc.qcloudimg.com/static/img/f2b0f14378b7ecc2e9aa1a2ae2f73246/zdy_01.png)
2. Click **Add Rules**, enter the name of the rule (e.g. 001), select a field (such as source IP) in **Matched Field**, select "match" in **Logic Operator** and enter the source IP (e.g. `192.168.1.1`) prohibited from accessing in **Matched Content**. Then select action (e.g. block).
![Custom rules](https://mc.qcloudimg.com/static/img/d94ffab9b57bbcefb64a2b874381ba24/zdy_02.png)
Custom policies of the WAF allow you to use masks to control access requests from source IPs within a range. We can enter a specific IP address range (e.g. `10.10.10.10/24`) in **Matched Content**.
![Custom rules](https://mc.qcloudimg.com/static/img/35d18c185c7fb64e4347907a7c4e7021/zdy_02_01.png)
3. Click **OK** to save the rule, and then the rule will take effect immediately. All HTTP access requests from specific source IPs will be blocked.
![Custom rules](https://mc.qcloudimg.com/static/img/928321526ed2fad440f24f5f87087353/zdy_03.png)

### Case 2: Prohibiting public network users from accessing specific Web resources 
When the webmaster does not want public network users to access specific web resources (e.g. management backend `/admin.html`), he can select **Request path** in **Matched Field**, select **Equal to** in **Logic Operator**, enter `/admin.html` in Matched Content, and select **Block** in Action to configure.
![Custom rules](https://mc.qcloudimg.com/static/img/8f0df39b43dbfcf5bc1d9070a2857a2e/zdy_04.png)

### Case 3: Prohibiting an external site from hot-linking certain resources 
To block hotlinking from an external site (e.g. `www.test.com`), the webmaster can use custom policies to capture and block the Referer feature of hotlink requests.
Select **Referer** in **Matched Field**, select **Contain** in **Logic Operator**, enter `www.test.com` in **Matched Content**, and select **Block** in **Action** to configure.
![Custom rules](https://mc.qcloudimg.com/static/img/59acfeacb52cb3180e6fa926313966d6/zdy_05.png)

<a href="https://cloud.tencent.com/document/product/627/11710" target="_blank">Previous: Anti-tampering of Webpage</a>

