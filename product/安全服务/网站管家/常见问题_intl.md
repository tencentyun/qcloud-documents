### Can servers outside Tencent Cloud use Web Application Firewall (WAF)?
WAF can be connected with servers in data centers outside Tencent Cloud. WAF protects servers in any public networks, including but not limited to Tencent Cloud, cloud from other vendors, and IDC. 
> Note: To access WAF in Mainland China, domain names must obtain an ICP license as required by MIIT.

### Does WAF support HTTPS protection?
WAF completely supports HTTPS services. You just need to upload the SSL certificate and private key as instructed, or select the Tencent Cloud hosting certificate to make WAF protect HTTPS traffic.

### The QPS limit in WAF is for the entire instance, or for a single configured domain name?
The QPS limit in WAF is for the entire instance. For example, if three domain names are under the protection of WAF, the total QPS of the three domains names cannot exceed the upper limit. If the QPS limit of the purchased instance is exceeded, speed limit is triggered, which will result in packet loss.

### Can a Tencent Cloud CVM private IP be entered as the origin server IP of WAF?
WAF does not support using CVM private IP as the origin server IP.

### Can Dayu high defense packages be used directly for WAF?
Yes. You can enable high defense capability for WAF by simply selecting the IP of the WAF instance on the configuration page in the Dayu high defense package console.

### How to access WAF and CDN or Dayu high defense package at the same time?
Dayu high defense package can be directly associated with WAF. And you just need to point the origin server of CDN to the IP of WAF instance.

The optimal deployment architecture:
Client > CDN > WAF+High defense package > Load balancer > Origin server

If you need CDN and high defense capability, set the CNAME provided after the access to WAF to the CDN origin server, and associate the Dayu high defense package with the WAF instance. The user traffic, after going through CDN, is forwarded to WAF, which has the capability of cleaning high-traffic DDoS attacks, and then be forwarded to the origin server to achieve a full protection.

### Is WAF able to protect multiple origin server IPs under one domain name?
Yes. Up to 20 domain names can be protected by one WAF.

### How to perform load balance if multiple origin servers are configured for WAF?
If multiple origin server IPs are configured, WAF achieves load balance of access requests by polling.

### Does WAF support health check?
Health check is enabled for WAF by default. WAF checks the access status of all origin server IPs. For the origin server IP that does not respond, WAF will not forward requests to this IP until its connection status returns to normal.

### Does WAF support session persistence?
Yes. Session persistence is enabled by default.

### How long does it take for changes to configuration to take effect in the WAF console?
In general, changes to configuration take effect within 10s.

### Does WAF automatically add origin server IP range to security groups?
High defense origin server IP range cannot be automatically added to security groups. For more information on how to add origin server IP range to security groups, please see [here](/doc/product/627/11706).

### If the uploaded files are blocked, will they still be blocked when using HTTPS or SFTP?
If WAF is used, files uploaded with HTTPS and HTTP will be blocked, but the ones uploaded with SFTP will not. WAF blocks a file only if it is an invalid uploaded file.

