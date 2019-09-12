## 功能描述
GET Bucket cors 接口实现 Bucket 持有者在 Bucket 上进行跨域资源共享的信息配置。（cors 是一个 W3C 标准，全称是"跨域资源共享"（Cross-origin resource sharing））。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

## 请求
### 请求示例

```
GET /?cors HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String（详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节）。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
获取跨域资源共享的信息配置成功。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<CORSConfiguration>
    <CORSRule>
        <ID>bucketid</ID>
        <AllowedOrigin>http://www.qq.com</AllowedOrigin>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>x-cos-meta-test</AllowedHeader>
        <ExposeHeader>x-cos-meta-test1</ExposeHeader>
        <MaxAgeSeconds>500</MaxAgeSeconds>
    </CORSRule>
</CORSConfiguration>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
CORSConfiguration|无|说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule|Container|是

Container 节点 CORSConfiguration 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
CORSRule|CORSConfiguration|说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule|Container|是

Container 节点 CORSRule 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
ID|CORSConfiguration.CORSRule|配置规则的 ID，可选填|string|是
AllowedOrigin|CORSConfiguration.CORSRule|允许的访问来源，支持通配符`*`，格式为：协议://域名[:端口]如：`http://www.qq.com`|strings|是
AllowedMethod|CORSConfiguration.CORSRule|允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE|strings|是
AllowedHeader|CORSConfiguration.CORSRule|在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 *|strings|是
MaxAgeSeconds|CORSConfiguration.CORSRule|设置 OPTIONS 请求得到结果的有效期|integer|是
ExposeHeader|CORSConfiguration.CORSRule|设置浏览器可以接收到的来自服务器端的自定义头部信息|strings|是


### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 章节。

## 实际案例

### 请求

```
GET /?cors HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484815944;32557711944&q-key-time=1484815944;32557711944&q-header-list=host&q-url-param-list=cors&q-signature=a2d28e1b9023d09f9277982775a4b3b705d0e23e
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 345
Connection: keep-alive
Date: Wed, 28 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdlNGZfNDYyMDRlXzM0YWFfZTBh

<CORSConfiguration>
    <CORSRule>
        <ID>bucketid</ID>
        <AllowedOrigin>http://www.qq.com</AllowedOrigin>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>x-cos-meta-test</AllowedHeader>
        <ExposeHeader>x-cos-meta-test1</ExposeHeader>
        <MaxAgeSeconds>500</MaxAgeSeconds>
    </CORSRule>
</CORSConfiguration>
```


