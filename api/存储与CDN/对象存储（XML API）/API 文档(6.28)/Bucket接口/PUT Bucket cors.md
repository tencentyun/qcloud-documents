## 功能描述
PUT Bucket cors 接口用于请求设存储桶的跨域资源共享权限，您可以通过传入 XML 格式的配置文件来实现配置，文件大小限制为64KB。默认情况下，存储桶持有者直接有权限使用该 API 接口，存储桶持有者也可以将权限授予其他用户。

## 请求
#### 请求示例

```sh
PUT /?cors HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: Auth String

```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。
#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。



#### 请求体
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

|节点名称（关键字）|父节点|描述|类型|是否必选|
|---|---|---|---|---|
|CORSConfiguration|无|说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule|Container|是|

Container 节点 CORSConfiguration 的内容：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| CORSRule           | CORSConfiguration | 说明跨域资源共享配置的所有信息，最多可以包含100条 CORSRule | Container | 是   |

Container 节点 CORSRule 的内容：

|节点名称（关键字）|父节点|描述|类型|是否必选|
|---|---|---|---|---|
|ID|CORSConfiguration.CORSRule|配置规则的 ID，可选填|string|否|
|AllowedOrigin|CORSConfiguration.CORSRule|允许的访问来源，支持通配符`*`，格式为：`协议://域名[:端口]`，例如：`http://www.qq.com`|strings|是|
|AllowedMethod|CORSConfiguration.CORSRule|允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE|strings|是|
|AllowedHeader|CORSConfiguration.CORSRule|在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符`*`|strings|是|
|MaxAgeSeconds|CORSConfiguration.CORSRule|设置 OPTIONS 请求得到结果的有效期|integer|是|
|ExposeHeader|CORSConfiguration.CORSRule|设置浏览器可以接收到的来自服务器端的自定义头部信息|strings|是|


## 响应
#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体
该请求响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```sh
PUT /?cors HTTP/1.1
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Content-MD5: q+xJ56ypmuOSKbkohlpZIg==
Content-Type: application/xml
Authorization: q-sign-algorithm=sha1&q-ak=AKIDVMyLTL4B8rVt52LTozzPZBYffPs9****&q-sign-time=1578385303;1578392503&q-key-time=1578385303;1578392503&q-header-list=content-md5;content-type;host&q-url-param-list=cors&q-signature=730a82c7afed2a6c051870d54895193235e8****
Content-Length: 385

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

#### 响应

```sh
HTTP/1.1 200 OK
content-length: 0
connection: close
date: Tue, 07 Jan 2020 08:21:44 GMT
server: tencent-cos
x-cos-request-id: NWUxNDNmOThfNWFiMjU4NjRfMWIxYl9lYWY1****
```

