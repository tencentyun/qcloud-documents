## 功能描述
GET Bucket cors 接口实现 Bucket 持有者在 Bucket 上获取跨域资源共享的信息配置。（cors 是一个 W3C 标准，全称是"跨域资源共享"（Cross-origin resource sharing））。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

## 请求
#### 请求示例

```shell
GET /?cors HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头
此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


#### 请求体
该请求的请求体为空。

## 响应

#### 响应头
此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体
获取跨域资源共享的信息配置成功。

```shell
<?xml version="1.0" encoding="UTF-8" ?>
<CORSConfiguration>
    <CORSRule>
        <ID>1234</ID>
        <AllowedOrigin>http://www.qq.com</AllowedOrigin>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>x-cos-meta-test</AllowedHeader>
        <MaxAgeSeconds>500</MaxAgeSeconds>
        <ExposeHeader>x-cos-meta-test1</ExposeHeader>
    </CORSRule>
</CORSConfiguration>
```

具体的节点描述如下：

节点名称（关键字）|父节点|描述|类型
---|---|---|--
CORSConfiguration|无|说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule|Container

Container 节点 CORSConfiguration 的内容：

节点名称（关键字）|父节点|描述|类型|
---|---|---|--
CORSRule|CORSConfiguration|说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule|Container

Container 节点 CORSRule 的内容：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
ID|CORSConfiguration.CORSRule|配置规则的 ID，是否包含该字段取决于 PUT Bucket cors 时是否指定 ID 字段|string
AllowedOrigin|CORSConfiguration.CORSRule|允许的访问来源，支持通配符`*`<br>格式为：`协议://域名[:端口]`，例如：`http://www.qq.com`|strings
AllowedMethod|CORSConfiguration.CORSRule|允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE|strings
AllowedHeader|CORSConfiguration.CORSRule|在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符`*`|strings
MaxAgeSeconds|CORSConfiguration.CORSRule|设置 OPTIONS 请求得到结果的有效期|integer
ExposeHeader|CORSConfiguration.CORSRule|设置浏览器可以接收到的来自服务器端的自定义头部信息|strings


#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
GET /?cors HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUj****&q-sign-time=1484815944;32557711944&q-key-time=1484815944;32557711944&q-header-list=host&q-url-param-list=cors&q-signature=a2d28e1b9023d09f9277982775a4b3b705d0****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 345
Connection: keep-alive
Date: Wed, 28 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdlNGZfNDYyMDRlXzM0YWFf****

<CORSConfiguration>
    <CORSRule>
        <ID>1234</ID>
        <AllowedOrigin>http://www.qq.com</AllowedOrigin>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>x-cos-meta-test</AllowedHeader>
        <MaxAgeSeconds>500</MaxAgeSeconds>
        <ExposeHeader>x-cos-meta-test1</ExposeHeader>
    </CORSRule>
</CORSConfiguration>
```


