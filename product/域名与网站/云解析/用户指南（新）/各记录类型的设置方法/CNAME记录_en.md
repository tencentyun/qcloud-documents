### When Do I Need to Use CNAME Record?
You need to add CNAME record if you want to point your domain name to another domain name which provides the IP address. CNAME is often used for establishing CDN or enterprise email providers.
### How to Add CNAME Record?
1. Enter sub domain name as the host name. For example, simply enter "www" if you want to add resolution for `www.123.com`. If you only want to add resolution for `123.com`, you can leave the host name empty, and the system will automatically enter an "@" into the input box. Be careful when adding such record because CNAME record with "@" can affect the resolution of MX record.
2. Record type is CNAME record.
3. Line type (this is required by default, otherwise certain users will not be able to resolve the domain. The default line type in the figure below directs all users except China Unicom users towards 1.com).
4. The record value is the domain name to which CNAME directs (domain name only).
![3](//mc.qcloudimg.com/static/img/30a2b97454e0efa21a4ad03be1020043/image.png)
![4](//mc.qcloudimg.com/static/img/a6138bdfbe3ff7401f67140a7853a401/image.png)

