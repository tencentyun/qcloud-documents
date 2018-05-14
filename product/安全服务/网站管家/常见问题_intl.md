### Can servers outside Tencent Cloud use Web Application Firewall (WAF)?
Web application firewall can be applied in data centers not deployed on Tencent Cloud and protect any servers on public network, including but not limited to Tencent Cloud, cloud from other vendors, and IDC. 
> Note: Domain names accessed in Mainland China must acquire an ICP license in accordance with MIIT requirements.

### Does WAF support HTTPS protection?
WAF completely supports HTTPS service. After you upload the SSL certificate and private key according to the prompts or select the Tencent Cloud hosting certificate, the web application firewall can protect HTTPS traffic.

### Is the QPS of WAF set based on the whole instance or on a single domain?
The QPS of WAF is set based on the whole instance. For example, if three domains are under protection of the WAF, the cumulative QPS of the three domains may not exceed the specified limit, otherwise the rate limit will be triggered and result in packet loss.

### Can a Tencent Cloud CVM private IP be entered as the IP of WAF origin server?
WAF does not support CVM private IPs for now.

### Can WAF directly use BGP high defense packages?
Yes. High defense capacity can be enabled for WAF by directly selecting the IP of the WAF instance on the configuration page in the BGP high defense package console.

### How is WAF accessed with CDN or BGP high defense package?
WAF can directly integrates with BGP high defense packages. And you can point the origin server of CDN to the IP of WAF instance.

Best deployment architecture:
Client > CDN > WAF + High defense package > Load balancer > Origin server

If you need CDN and high defense capability, set the CNAME provided after WAF is accessed as the CDN origin server, and add the BGP high defense package to the WAF instance. Then after passing through the CDN, the user traffic is forwarded to the WAF with high-traffic DDOS cleaning capability enabled, and ultimately forwarded to the origin server, so as to provide all-round protection for the origin server.

### Is WAF able to protect multiple origin server IPs under one domain name?
Yes. Up to 20 domain names can be protected by one WAF.

### How to perform load balancing when WAF has multiple origin servers configured?
If multiple origin server IPs are configured, WAF achieves load balancing of access requests in the polling mode.

### Does WAF support health check?
The health check feature of WAF is enabled by default. WAF checks the access status of all origin server IPs. If an origin server IP does not respond, WAF will not forward requests to this IP until its access status becomes normal.

### Does WAF support session persistence?
WAF supports session persistence, which is enabled by default.

### How long does it take for changes to configurations in the WAF console to take effect?
In general, changes to configurations take effect within 10s.

### Does WAF automatically add origin server IP range into security groups?
High defense origin server IP range cannot be automatically added into security groups. For more information on adding origin server IP range into security groups, see [Quick Start](/doc/product/627/11706).

### If the uploaded file is blocked, will it still be blocked using HTTPS or SFTP?
Files are not blocked without WAF. HTTPS and HTTP use WAF, but SFTP does not. WAF blocks a file only if it is an invalid uploaded file.

