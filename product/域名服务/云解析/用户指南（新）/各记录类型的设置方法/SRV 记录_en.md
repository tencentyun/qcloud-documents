### When Do I Need to Use SRV Record?
An SRV record is used to identify that a server uses a certain service. This is commonly seen in directory management in Microsoft system.
### How to Add SRV Record?
1. Host name format: <service name>.<protocol type>
For example: _sip._tcp
2. Record type is SRV.
3. Line type (this is required by default, otherwise certain users will not be able to resolve the domain).
4. Record value format: <priority> <weight> <port> <host name>.
For example: 0 5 5060 sipserver.example.com.
A "." will be automatically added after the domain name when record is generated (this is completely normal).
5. MX priority is not required.
6. TTL is not required as the system will automatically generate one. Default is 600 seconds. TTL is the duration for cache. The smaller the value is, the faster the modified record will take effect globally.
![](//mc.qcloudimg.com/static/img/afcb502b0484cd24b71229c01b27af02/image.png)


