## 1. 根据域名和用户IP查询
数据请求和应答均使用http协议。
请求格式为`http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1`
dn表示要查询的域名
ip表示用户ip，ip没有定义时，默认为http报文的源ip为用户ip

### 1.1 域名存在
如果HttpDNS能查询到最终的IP指向，则直接返回IP。
以请求`http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1`为例，返回`183.60.57.155`：
![返回值一](//mccdn.qcloud.com/static/img/ad7dbfd17112fba557f96deec30677df/image.png)

### 1.2 域名不存在
如果域名不存在，HttpDNS无法查询到最终的IP指向，则返回空。
以请求`http://119.29.29.29/d?dn=www.dnspod2.cn.&ip=1.1.1.1`为例，返回空字符串：
![返回值二](//mccdn.qcloud.com/static/img/15b5daaeeedd2f2c68c00465554dbae2/image.png)


## 2. 根据域名和用户IP查询带TTL的结果
数据请求和应答均使用http协议。
请求格式为`http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1&ttl=1`
ttl=1表示要求返回结果携带解析结果的ttl值。
返回的ttl和域名解析结果用英文逗号分隔。

以请求`http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1&ttl=1`为例，表示要求返回结果带上TTL，返回值`183.60.57.155,60`则表示递归服务器缓存的TTL是60秒：
![返回值三](//mccdn.qcloud.com/static/img/0e845c5b777dbcd81ebb800437c786ee/image.png)
