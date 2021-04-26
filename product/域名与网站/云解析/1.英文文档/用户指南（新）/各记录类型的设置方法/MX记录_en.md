### When Do I Need to Use MX Record?
You need to add MX record if you need to set an e-mail to receive mails.
### How to Add MX Record?
1. Enter sub domain name as the host name. In normal situations, if you need to set an email address `xxx@123.com`, host name should be left empty. If you enter "mail", the email address will become `xxx@mail.123.com`.
2. Record type is MX record.
3. Line type (this is required by default, otherwise certain users will not be able to resolve the domain or receive emails. You can choose default since MX usually doesn't need smart resolution).
4. Record value can be a domain name, or an IP address. If you use domain name, the domain name being directed to must have A record (such as `mail.123.com` shown in the figure below). A "." will be automatically added after the domain name when record is generated (this is completely normal). If you use an IP, you can simply enter the email server IP. Likewise, a "." will be automatically added.
5. TTL is not required as the system will automatically generate one. Default is 600 seconds. TTL is the duration for cache. The smaller the value is, the faster the modified record will take effect globally.
6. A smaller MX priority value indicates a higher priority level. As shown in the figure below, emails will be sent to 1.1.1.1 (MX priority: 5) preferentially. And if it is failed, emails will be sent to `mail.123.com` (MX priority: 10).
![](//mc.qcloudimg.com/static/img/db9bb92dc335c2a23c51c31f132d522f/image.png)
![](//mc.qcloudimg.com/static/img/fc0f0d8798999188d2aeabfea71d7fbd/image.png)
![](//mc.qcloudimg.com/static/img/69782527860e469c637c62fdedf378a7/image.png)

