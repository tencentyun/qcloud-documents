### When do I need to use SRV record?
An SRV record is used to specify that a server uses a certain service and is commonly used for directory management in Microsoft system.
### How to add an SRV record?
1. Host record format: <service name>.<protocol type>
For example: _sip._tcp
2. Record type is SRV.
3. Line type (this is required by default. If it is left empty, some users will not be able to resolve the domain name).
4. Record value format: <priority> <weight> <port> <server name>.
For example: 0 5 5060 sipserver.example.com.
Generally, a "." will be automatically added after the domain name when the record is generated.
5. MX priority is not required.
6. TTL is not required as the system will automatically generate one. Default is 600 seconds. TTL (Time to Live) is the duration for cache. The smaller the TTL value is, the faster the modified record takes effect globally.
![](//mc.qcloudimg.com/static/img/afcb502b0484cd24b71229c01b27af02/image.png)


