## 功能描述
Get Bucket CORS实现跨域访问配置读取。

## 请求

### 请求语法

```HTTP
GET /?cors HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称                | 描述                                       | 类型        | 必选   |
| ----------------- | ---------------------------------------- | --------- | ---- |
| CORSConfiguration | 说明跨域配置的所有信息，最多可以包含100条CORSRule            | Contianer | 是    |
| CORSRule          | 单条配置的信息<br/>父节点：CORSRule                 | Contianer | 是    |
| ID                | 规则名称，可选填<br/>父节点：CORSRule                | String    | 否    |
| AllowedMethod     | 允许的HTTP操作，枚举值：Get，Put，Head，Post，Delete<br/>父节点：CORSRule | Enum      | 是    |
| AllowedOrigin     | 允许的访问来源，支持『*』通配符<br/>父节点：CORSRule        | String    | 是    |
| AllowedHeader     | 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部<br/>父节点：CORSRule | String    | 否    |
| MaxAgeSeconds     | 设置 OPTIONS 请求得到结果的有效期<br/>父节点：CORSRule   | Integer   | 否    |
| ExposeHeadr       | 设置浏览器可以接收到的来自服务器端的自定义头部信息<br/>父节点：CORSRule | String    | 否    |

```xml
<CORSConfiguration>
  <CORSRule>
    <ID></ID>
    <AllowedOrigin></AllowedOrigin>
    <AllowedMethod></AllowedMethod>
    <AllowedHeader></AllowedHeader>
    <MaxAgeSeconds></MaxAgeSeconds>
    <ExposeHeader></ExposeHeader>
  </CORSRule>
  <CORSRule>
    ...
  </CORSRule>
  ...
</CORSConfiguration>
```

## 示例
### 请求
```xml
GET /?cors HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484815944;32557711944&q-key-time=1484815944;32557711944&q-header-list=host&q-url-param-list=cors&q-signature=a2d28e1b9023d09f9277982775a4b3b705d0e23e

```
### 返回
```xml
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 345
Connection: keep-alive
Date: Thu Jan 19 16:52:31 2017
Server: tencent-cos
x-cos-request-id: NTg4MDdlNGZfNDYyMDRlXzM0YWFfZTBh

<CORSConfiguration> 
  <CORSRule> 
    <ID>1234</ID>  
    <AllowedOrigin>http://www.qq.com</AllowedOrigin>  
    <AllowedMethod>PUT</AllowedMethod>  
    <AllowedHeader>x-cos-meta-test</AllowedHeader>  
    <ExposeHeader>x-cos-meta-test1</ExposeHeader>  
    <MaxAgeSeconds>500</MaxAgeSeconds> 
  </CORSRule> 
</CORSConfiguration>

```

