## Overview
The custom rule support controlling the accesses of public network users by combining multiple features such as request paths, GET parameters, POST parameters, Referer, and User-Agent of HTTP messages, and performing feature matching. For various attacks on the Internet, Tencent Cloud users can respond flexibly with custom rules, using a combination of rules to block them easily.

## Notes
- Each custom rule can set a maximum of five conditions for feature control.
- The relationship between multiple conditions in each custom rule is "AND", that is, the rule does not take effect unless all the conditions are satisfied.
- For each custom rule to be matched, you can configure two actions: block and allow.

## Configuration Case
### Case 1: Prohibiting specific IP addresses from accessing a designated site
To prohibit a specific IP address from accessing the designated site, the webmaster can:
1. Log in to the [WAF Console](https://console.cloud.tencent.com/guanjia), click **Web Application Firewall** -> **Defense Settings**, select the domain name of the site to be protected, and click **Custom Rule**.
![Custom Rules](https://main.qcloudimg.com/raw/e98a0f0b2d0c613d5fafbdad9f9fc8bf.png)
2. Click **Add a Rule**, enter the name of the rule (e.g. 001), select a field (such as source IP) in Field, select "matched" in Condition and enter the source IP (e.g. `192.168.1.1`) prohibited from accessing in Content. Then select an action (e.g. block).
![Custom Rules](https://main.qcloudimg.com/raw/205b99240e67df8dc9643c0d74be951d.png)
Custom rules of the WAF allow you to use masks to control access requests from source IPs within a range. You can enter a specific IP address range (e.g. `10.10.10.10/24`) in Content.
![Custom Rules](https://main.qcloudimg.com/raw/65a2333e7bed7414fa4de8ab83faa39b.png)
3. Click **Confirm** to save the rule, and then the rule will take effect immediately. All HTTP access requests from specific source IPs will be blocked.
![Custom Rules](https://main.qcloudimg.com/raw/b83bcf1035ba4064f46d2a94cf6ba3be.png)

### Case 2: Prohibiting public network users from accessing specific Web resources 
When the webmaster does not want public network users to access specific Web resources (e.g. management backend `/admin.html`), he can select Request Path in Field, select Equals to in Condition, enter `/admin.html` in Content, and select Block in Action to configure.
![Custom Rules](https://main.qcloudimg.com/raw/8de4ec8039a464d923c52cdf20496488.png)

### Case 3: Prohibiting an external site from hotlinking certain resources
To block hotlinking from an external site (e.g. `www.test.com`), the webmaster can use custom rules to capture and block the Referer feature of hotlink requests.
Select Referer in Field, select Includes in Condition, enter `www.test.com` in Content, and select Block in Action.
![Custom Rules](https://main.qcloudimg.com/raw/cfb596eccc16787fb4f755406a4e7e75.png)

<a href="https://cloud.tencent.com/document/product/627/11710" target="_blank">Previous: Anti-tampering of Webpage</a>


