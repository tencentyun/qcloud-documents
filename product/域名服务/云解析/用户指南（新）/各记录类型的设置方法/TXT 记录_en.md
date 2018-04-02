### When do I need to use TXT record?
You can use TXT record if you need to identify and describe a domain name. Most TXT records are used as SPF records (anti-spam).
### How to add a TXT record?
1. Enter the sub-domain name as the host name. For example, if you want to add a TXT record for `www.123.com`, only enter "www"; if you want to add a TXT record only for "123.com", leave the host name empty, and the system will automatically enter an "@" in the input box.
2. Record type is TXT.
3. Line type. This is required by default. If it is left empty, some users will not be able to resolve the domain name. You can choose default since TXT records don't need intelligent resolution.
4. The record value dose not have a fixed format. TXT records are used for SPF anti-spam in most cases. A typical example of a TXT record in SPF format is "v=spf1 a mx ~all", which means only the IP addresses in the A record and the MX record of this domain name are allowed to use this domain name to send emails.
5. MX priority is not required.
6. TTL is not required as the system will automatically generate one. Default is 600 seconds. TTL (Time to Live) is the duration for cache. The smaller the value is, the faster the modified record takes effect globally.
![](//mc.qcloudimg.com/static/img/77b55e2f5fb0263fc5ff1cb13fb442cb/image.png)
