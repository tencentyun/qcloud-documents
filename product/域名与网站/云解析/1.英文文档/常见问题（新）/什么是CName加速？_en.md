### Feature Overview
CNAME acceleration feature is a service independently developed by Tencent Cloud DNSPod which is designed to solve the resolution time-consuming problem caused by the repeated request to authoritative servers by recursive servers when users set CNAME resolution records with multiple redirections.
Suppose a.com, b.com,and c.com are all domain names resolved using DNSPod:
`www.a.com` is configured with a CNAME record with the value `www.b.com`
`www.b.com` is configured with a CNAME record with the value `www.c.com`
`www.c.com` is configured with an A record with the value 1.2.3.4
Under normal circumstances, the recursive server needs to send request to the authoritative server for three time before acquiring the IP address of `www.a.com`, as shown in the figure below:
![Acceleration-1](https://mc.qcloudimg.com/static/img/57938b0d24aa1a136c852c0cf0d1abc3/123.png)
When CNAME acceleration feature is enabled, the authoritative server returns CNAME record and the final A record back to the recursive server in one go, so the recursive server only needs to send request for one time instead of three times, as shown in the figure below:
![Acceleration-2](https://mc.qcloudimg.com/static/img/a8b35c14692209372897e985990be3a6/123.png)
This greatly reduces the time needed for network communication during requests and responses and quicken the resolution. The outcome is more obvious when users set CNAME resolution records with multiple redirections.
### Acceleration Outcome
Before enabling CNAME acceleration (query time: 1,021 msec):
![1](https://mc.qcloudimg.com/static/img/a3b44b2e056e921ca1adac9e5dfb77d3/speedup_off.png)
After enabling CNAME acceleration (query time: 410 msec):
![2](https://mc.qcloudimg.com/static/img/f71dfc679621faff5a93889f56c9ac48/speedup_on.jpg)
Resolution time is substantially reduced by 59.84%.
>**Note:**
>The test is performed after the cache is cleared. You need to wait for TTL to expire before modifying the configuration.

### Note
1. All related domain names for which CNAME acceleration is enabled must use Tencent Cloud DNS or resolution services provided by DNSPod platform, otherwise the feature cannot be enabled, the acceleration may fail, or resolution error may occur in certain situations;
2. For domain names that have enabled CNAME acceleration, when the system detects that a domain name isn't using Tencent Cloud NDS service (for example, domain name registration has expired or domain name is switched to another DNS service provider), the system will automatically disable CNAME acceleration. It will automatically enable CNAME acceleration again once it detects that the domain name is using DNSPod resolution service again);
3. You do not need to enable CNAME acceleration respectively for different sub-domain names under the same domain name, because the system will automatically accelerate them;
4. CNAME acceleration should be disabled before a domain name is transferred from Tencent Cloud. If a domain name is already transferred out and the system has not obtained the current status of the domain name, the user can disable CNAME acceleration by himself or contact technical support to do so.

