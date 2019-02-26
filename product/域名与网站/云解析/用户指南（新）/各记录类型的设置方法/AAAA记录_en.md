### When Do I Need to Use AAAA Record?
You can use AAAA record if you want visitors to access your domain name via IPv6 address.
### How to Add AAAA Records?
1. Enter sub domain name as host name. For example, if you want to add resolution for `www.123.com`, enter "www" as host name. If you only want to add resolution for `123.com`, you can leave the host name empty, and the system will automatically enter an "@" into the input box.
2. Record type is AAAA.
3. Line type (this is required by default, otherwise certain users will not be able to resolve the domain. The default line type in the figure below directs all users except China Unicom users towards ff06:0:0:0:0:0:0:c3).
4. Record value is the IP address (IPv6 address only).
5. TTL is the duration for cache. The smaller the value is, the faster the modified record will take effect globally. Default is 600 seconds.
![](//mc.qcloudimg.com/static/img/2b1e91003b5241e47f7313a820189511/image.png)
![](//mc.qcloudimg.com/static/img/e0ee082c511e65e38c720b1339e6859c/image.png)

