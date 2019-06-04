## 功能描述
PUT Bucket cors 接口用来请求设置 Bucket 的跨域资源共享权限，您可以通过传入 XML 格式的配置文件来实现配置，文件大小限制为64KB。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

## 请求
### 请求示例

```sh
PUT /?cors HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: Auth String

```
> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
请求的请求体为跨域规则。

```http
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


具体的数据描述如下：

|节点名称（关键字）|父节点|描述|类型|必选|
|---|---|---|---|---|
|CORSConfiguration|无|说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule|Container|是|

Container 节点 CORSConfiguration 的内容：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| CORSRule           | CORSConfiguration | 说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule | Container | 是   |

Container 节点 CORSRule 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|---|---|---|---|---|
|ID|CORSConfiguration.CORSRule|配置规则的 ID，可选填|string|是|
|AllowedOrigin|CORSConfiguration.CORSRule|允许的访问来源，支持通配符`*`，格式为：`协议://域名[:端口]`，例如：`http://www.qq.com`|strings|是|
|AllowedMethod|CORSConfiguration.CORSRule|允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE|strings|是|
|AllowedHeader|CORSConfiguration.CORSRule|在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符`*`|strings|是|
|MaxAgeSeconds|CORSConfiguration.CORSRule|设置 OPTIONS 请求得到结果的有效期|integer|是|
|ExposeHeader|CORSConfiguration.CORSRule|设置浏览器可以接收到的来自服务器端的自定义头部信息|strings|是|


## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 文档。

#### 特有响应头
该请求操作无特殊的响应头部信息。

### 响应体
该请求响应体为空。

### 错误码

|错误码|描述|HTTP 状态码|
|---|---|---|
|SignatureDoesNotMatch|提供的签名不符合规则，返回该错误码|403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) |
|NoSuchBucket|如果试图添加的规则所在的 Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) |

## 实际案例

### 请求

```sh
PUT /?cors HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2017 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814927;32557710927&q-key-time=1484814927;32557710927&q-header-list=host&q-url-param-list=cors&q-signature=8b9f05dabce2578f3a79d732386e7cbade9033e3
Content-Type: application/xml
Content-Length: 280

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

### 响应

```sh
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 10 Mar 2017 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdiZWRfOWExZjRlXzQ2OWVfZGY0
```


