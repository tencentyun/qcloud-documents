### When Do I Need to Use NS Record?
You need to add NS record if you need to deliver the sub domain name to other DNS service providers for resolution.
### How to Add NS Record?
1. Enter sub domain name as the host name. For example, enter "www" as the host name if you want to delegate the resolution of `www.123.com` to another DNS server. The host name "@" can't be used for NS record. Delegated sub domain names do not affect the resolution for other sub domain names.
2. Record type is NS.
3. Line type (this is required by default, otherwise certain users will not be able to resolve the domain).
4. The record value is the domain name of the DNS server to which you want to delegate your domain name. A "." will be automatically added after the domain name when record is generated (this is completely normal).
5. TTL is not required as the system will automatically generate one. Default is 600 seconds. TTL is the duration for cache. The smaller the value is, the faster the modified record will take effect globally.
6. MX priority is not required.
![](//mc.qcloudimg.com/static/img/ade89d17313705d405470208397d3a2a/image.png)

