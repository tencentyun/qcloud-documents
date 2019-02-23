### When Do I Need to Use A Record?
You need to add an A record if you want to direct your domain name to an IP address.
### How to Add A Record?
1. Enter sub domain name as the host name. For example, if you want to add resolution for `www.123.com`, enter "www" as the host name. If you only want to add resolution for `123.com`, you can leave the host name empty, and the system will automatically enter an "@" into the input box.
2. Record type is A record.
3. Line type (this is required by default, otherwise certain users will not be able to resolve the domain. The default line type in the figure below directs all users except China Unicom users towards 10.10.10.10).
4. Record value is the IP address (IPv4 address only).
5. TTL is the duration for cache. The smaller the value is, the faster the modified record will take effect globally. Default is 10 minutes (600 seconds).
![1](//mc.qcloudimg.com/static/img/82400afe3c333b11ec5c35058fda4d61/image.png)
![2](//mc.qcloudimg.com/static/img/14c8e2c1fb2ae27ab803393b478053b6/image.png)
