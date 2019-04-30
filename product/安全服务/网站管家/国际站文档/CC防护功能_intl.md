## Overview
The CC defense feature supports frequency control and man-machine identification on the accesses to specific URLs by public network users to block malicious high-frequency accesses.

## Configuration Example 
In the configuration example, when the number of accesses to `/test.html` from a single source IP within 10 seconds is greater than 10, the malicious access punishment function blocks the source IP for 30 minutes. 
1. Enter the WAF Console, click **Defense Settings**, and click the domain name of the site to be protected, and then click **CC Defense Settings** tab to go to the malicious access penalty configuration interface. ![CC Defense Settings](https://main.qcloudimg.com/raw/4b1821f1de23699396201aaad463e13a.png)
2. Click **Add a Rule**, enter the rule name in the rule name input box, select the matching condition (equal to), enter specific URI (`/test.html`), select access frequency (10 times within 10 seconds), and select "Block access" in Action (or "Verify identity", which uses a certain algorithm to perform verification. If the verification fails, it will automatically block access), and then enter 30 minutes in Punishment Period.
![CC Defense Settings](https://main.qcloudimg.com/raw/0d6b304bf61c035f4df51185cb54e849.png)
3. Click **Add** to save the rule, and then the rule takes effect to punish malicious access activities.
![CC Defense Settings](https://main.qcloudimg.com/raw/8dc0a752e740ce957ce48810c0b6dd2e.png)

[Previous: DNS Hijacking Detection](/document/product/627/11708)
[Next: Anti-tampering of Webpage](/document/product/627/11710)

