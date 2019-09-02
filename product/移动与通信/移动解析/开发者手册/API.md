## 根据域名和用户 IP 查询
数据请求和应答均使用 HTTP 协议。
请求格式为：
```
http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1
```
其中，`dn` 表示要查询的域名；
`ip` 表示用户 IP，当 `ip` 为内网 IP或非法 IP，默认取 HTTP 报文的源 IP 为用户 IP，此时 HttpDNS 会按照用户设置的默认线路进行解析。

### 域名存在
如果 HttpDNS 能查询到最终的 IP 指向，则直接返回 IP。
以下列请求为例
```
http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1
```
返回
```
183.60.57.155
```
![返回值一](//mccdn.qcloud.com/static/img/ad7dbfd17112fba557f96deec30677df/image.png)

### 域名不存在
如果域名不存在，HttpDNS 无法查询到最终的IP指向，则返回空。
以下列请求为例：
```
http://119.29.29.29/d?dn=www.dnspod2.cn.&ip=1.1.1.1
```
返回空字符串，如下图所示：
![返回值二](//mccdn.qcloud.com/static/img/15b5daaeeedd2f2c68c00465554dbae2/image.png)


## 根据域名和用户 IP 查询带 TTL 的结果
数据请求和应答均使用 HTTP 协议。
请求格式为:
```
http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1&ttl=1
```
`ttl = 1` 表示要求返回结果携带解析结果的 TTL 值。
返回的 TTL 和域名解析结果用英文逗号分隔。

以下列请求为例，表示要求返回结果带上 TTL：
```
http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1&ttl=1
```
返回值如下，表示递归服务器缓存的 TTL 是 60 秒：
```
183.60.57.155,60
```：
![返回值三](//mccdn.qcloud.com/static/img/0e845c5b777dbcd81ebb800437c786ee/image.png)
