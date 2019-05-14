## Overview
The CC protection feature supports frequency control and man-machine identification on the access to specific URLs by public network users to block malicious high-frequency accesses.

## Configuration Example 
In the configuration example, when the number of accesses to `/test.html` from a single source IP within 10 seconds is greater than 10, the malicious access punishment feature blocks the source IP for 30 minutes. 
1. Enter the WAF Console, click **Protection Settings**, and click the domain name of the site to be protected, and then click **CC Protection Settings** to go to the malicious access punishment configuration interface. ![CC Protection Settings](https://mc.qcloudimg.com/static/img/09a2826e5557025a126a9935c6f328dc/cc_01.png)
2. Click **Add Rule**, enter the rule name in the rule name input box, select the matching condition (equal to), enter specific URI (`/test.html`), select access frequency (10 times within 10 seconds), and select **Block access** (or **Human-machine identification**, which uses a certain algorithm to perform verification. If the verification fails, it will automatically block access) in **Action**, and then enter 30 minutes in **Punishment Time**. ![CC Protection Settings](https://mc.qcloudimg.com/static/img/22c9036197dab6cbba9579227122abd0/cc_02.png)
3. Click **Add** to save the rule, and then the rule takes effect to punish malicious access activities.
![CC protection settings](https://mc.qcloudimg.com/static/img/1ebb4c29b0a9a4723ce78b72e57f302b/cc_03.png)

[Previous: DNS Hijacking Detection](/document/product/627/11708)
[Next: Anti-tampering of Webpage](/document/product/627/11710)

