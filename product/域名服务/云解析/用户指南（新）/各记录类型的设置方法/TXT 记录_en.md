### When Do I Need to Use TXT Record?
You can use TXT record if you need to identify and describe a domain name. Most TXT records are used as SPF records (anti-spam).
### How to Add TXT Record?
1. Enter sub domain name as the host name. For example, enter "www" if you want to add a TXT record for `www.123.com`. If you only want to add a TXT record for `123.com`, you can leave the host name empty, and the system will automatically enter an "@" into the input box.
2. Record type is TXT.
3. Line type (this is required by default, otherwise certain users will not be able to resolve the domain. You can choose default since TXT records don't need smart resolution).
4. There is no fixed format for record value. However, TXT records are used as SPF anti-spam in most cases. Here's an example for a TXT record in the most typical SPF format: "v=spf1 a mx ~all", which means only IP addresses in the A record and the MX record of this domain name are allowed to use this domain name to send emails.
5. MX priority is not required.
6. TTL is not required as the system will automatically generate one. Default is 600 seconds. TTL is the duration for cache. The smaller the value is, the faster the modified record will take effect globally.
![](//mc.qcloudimg.com/static/img/77b55e2f5fb0263fc5ff1cb13fb442cb/image.png)
