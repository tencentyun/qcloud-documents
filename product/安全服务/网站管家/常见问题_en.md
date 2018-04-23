### My server is not deployed on Tencent Cloud, can I use Web Application Firewall (WAF)?
Yes. WAF can be applied in data centers not deployed on Tencent Cloud and protect any servers on public network, including but not limited to Tencent Cloud, cloud from other vendors, and IDC. 
> Note: Domain names accessed in Mainland China must obtain an ICP license in accordance with MIIT requirements.

### Does WAF support HTTPS protection?
Yes. WAF completely supports HTTPS service. After you upload the SSL certificate and private key according to the prompts or select the Tencent Cloud hosting certificate, the WAF can protect HTTPS traffic.

### Is the QPS of WAF set for the whole instance or for a single domain?
The QPS of WAF is set for the whole instance. For example, if three domains are under the protection of WAF, the cumulative QPS of the three domains may not exceed the specified limit, otherwise the rate limit will be triggered and result in packet loss.

### Can a Tencent Cloud CVM private IP be entered as the IP of WAF origin server?
Not for now. WAF does not support CVM private IPs for now.

### Can WAF directly use BGP high defense packages?
Yes. You can enable the high defense capacity for WAF by directly selecting the IP of the WAF instance on the configuration page in the BGP high defense package console.

### How is WAF accessed with CDN or BGP high defense package?
WAF can directly integrates with BGP high defense packages. And you can point the origin server of CDN to the IP of WAF instance.

Best deployment architecture:
Client > CDN > WAF + High defense package > Load balancer > Origin server

If you need CDN and high defense capability, set the CNAME provided after WAF is accessed as the CDN origin server, and add the BGP high defense package to WAF instance. Then after being handled via CDN, the user traffic is forwarded to WAF with high-traffic DDoS cleaning capability enabled, and ultimately forwarded to the origin server with all-round protection for the origin server.

### Is WAF able to protect multiple origin server IPs under one domain name?
Yes. Up to 20 domain names can be protected by one WAF.

### How to perform load balancing when WAF has multiple origin servers configured?
If multiple origin server IPs are configured, WAF achieves load balancing of access requests in polling mode.

### Does WAF support health check?
Yes. Health check is enabled for WAF by default. WAF checks the access status of all origin server IPs. If an origin server IP does not respond, WAF will no longer forward requests to this IP until its access status becomes normal.

### Does WAF support session persistence?
Yes. WAF supports session persistence, which is enabled by default.

### How long does it take for configuration changes in the WAF console to take effect?
In general, configuration changes take effect within 10s.

### What is the origin server IP range of WAF?
```
123.207.88.0/24
123.207.124.0/24
119.29.245.0/24
139.199.169.0/24
123.207.83.0/24
119.29.218.0/24
119.29.106.0/24
118.89.61.0/24
```

### Does WAF automatically add origin server IP range into security groups?
No. WAF does not automatically add high defense origin server IP range into security groups. For more information on adding origin server IP range into security groups, see [Getting Started](/doc/product/627/11706).

### If the uploaded file is blocked, will it still be blocked using HTTPS or SFTP?
Files are not blocked without WAF. HTTPS and HTTP use WAF, but SFTP does not. WAF blocks a file only if it is an invalid uploaded file.

### Why only one domain name can be added to an IP?
Essentially, WAF provides protection based on IPs. So all domain names associated with a CVM are under the protection, but only the first associated domain name is shown. In other words, a new domain name can be essentially added but not shown.

