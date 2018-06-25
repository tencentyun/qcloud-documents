## 1. Querying by domain name and user IP
Data request and response are made using HTTP protocol.
Request format is `http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1`
"dn" refers to the domain name to be queried
"ip" refers to user IP. If it is not specified, the source IP in HTTP message is used as user IP by default.

### 1.1 Success Case
If HttpDNS can acquire the IP to which the domain name is pointed, IP is returned directly.
If the request is `http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1`. `183.60.57.155` is returned:
![Returned value 1](//mccdn.qcloud.com/static/img/ad7dbfd17112fba557f96deec30677df/image.png)

### 1.2 Failure Case
If no domain name exists, HttpDNS cannot acquire the ip to which the domain name is pointed, therefore null is returned.
If the request is `http://119.29.29.29/d?dn=www.dnspod2.cn.&ip=1.1.1.1`, null string is returned:
![Returned value 2](//mccdn.qcloud.com/static/img/15b5daaeeedd2f2c68c00465554dbae2/image.png)


## 2. Query the result with TTL based on domain name and user IP
Data request and response are made using HTTP protocol.
Request format is `http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1&ttl=1`
ttl=1 means that the returned result should contain the ttl value of resolution result.
Returned ttl and the resolution result of domain name are separated with comma.

If the request is `http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1&ttl=1`, the returned result must come with TTL. The returned value `183.60.57.155,60` means the time span during which TTL is cached in recursive server is 60 seconds:
![Returned value 3](//mccdn.qcloud.com/static/img/0e845c5b777dbcd81ebb800437c786ee/image.png)

