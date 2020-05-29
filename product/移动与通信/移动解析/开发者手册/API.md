## 根据域名和用户 IP 查询
数据请求和应答均使用 HTTP 协议。
请求格式为：
```
http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1
```
其中，`dn` 表示要查询的域名；
`ip` 表示用户 IP，当 `ip` 为内网 IP 或非法 IP，默认取 HTTP 报文的源 IP 为用户 IP，此时 HTTPDNS 会按照用户设置的默认线路进行解析。

### 域名存在
如果 HTTPDNS 能查询到最终的 IP 指向，则直接返回 IP。
以下列请求为例：
```
http://119.29.29.29/d?dn=www.dnspod.cn.&ip=1.1.1.1
```
返回
```
183.60.57.155
```
![返回值一](https://main.qcloudimg.com/raw/8ee0fc1e70b755d078e153ac55cf1202.png)

### 域名不存在
如果域名不存在，HTTPDNS 无法查询到最终的IP指向，则返回空。
以下列请求为例：
```
http://119.29.29.29/d?dn=www.dnspod2.cn.&ip=1.1.1.1
```
返回空字符串，如下图所示：
![返回值二](https://main.qcloudimg.com/raw/7c677e5fa179ebfdc45415fe1de49de5.png)


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
```
![返回值三](https://main.qcloudimg.com/raw/869e631f3efb232feee6caeea3199af0.png)

## 根据域名查询解析地址及用户公网出口 IP
数据请求和应答均使用 HTTP 协议。
请求格式为：
```
http://119.29.29.29/d?dn=www.dnspod.cn&clientip=1
```
- `clientip=1` 表示返回用户的出口 IP。
- 返回结果包括 `www.dnspod.cn` 的解析地址以及用户公网出口 IP，二者用`|`分隔。

以下列请求为例，表示要求返回结果带上解析地址以及用户公网出口 IP。
```
http://119.29.29.29/d?dn=www.dnspod.cn&clientip=1
```
返回值如下，表示解析地址为113.96.208.81，用户出口 IP 为14.17.22.47。
```
113.96.208.81|14.17.22.47
```

