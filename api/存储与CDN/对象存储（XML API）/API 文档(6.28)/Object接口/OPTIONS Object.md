## 功能描述
OPTIONS Object 接口实现 Object 跨域访问配置的预请求。即在发送跨域请求之前会发送一个 OPTIONS 请求并带上特定的来源域，HTTP 方法和 Header 信息等给 COS，以决定是否可以发送真正的跨域请求。当 CORS 配置不存在时，请求返回403 Forbidden。可以通过 PUT Bucket cors 接口来开启 Bucket 的 CORS 支持。

## 请求
#### 请求示例

```shell
OPTIONS /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Origin: Origin
Access-Control-Request-Method: HTTPMethod
Access-Control-Request-Headers: RequestHeader
Authorization: Auth String
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

名称|类型|描述|是否必选
---|---|---|---
Origin|string|模拟跨域访问的请求来源域名|是
Access-Control-Request-Method|string|模拟跨域访问的请求 HTTP 方法|是
Access-Control-Request-Headers|string|模拟跨域访问的请求头部|否

#### 请求体

此接口无请求体。

## 响应
#### 响应头
#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该请求操作的特有响应头具体数据为：

|名称|类型|描述|
|---|---|---|
|Access-Control-Allow-Origin|string|模拟跨域访问的请求来源域名，当来源不允许的时候，此 Header 不返回|
|Access-Control-Allow-Methods|string|模拟跨域访问的请求 HTTP 方法，当请求方法不允许的时候，此 Header 不返回|
|Access-Control-Allow-Headers|string|模拟跨域访问的请求头部，当模拟任何请求头部不允许的时候，此 Header 不返回该请求头部|
|Access-Control-Expose-Headers|string|模拟跨域访问的请求 HTTP 方法，当请求方法不允许的时候，此 Header 不返回|
|Access-Control-Max-Age|string|设置 OPTIONS 请求得到结果的有效期|

#### 响应体
此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


## 实际案例

#### 请求

```shell
OPTIONS /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 12 Jan 2017 17:26:53 GMT
Origin: http://www.qq.com
Access-Control-Request-Method: PUT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3M****&q-sign-time=1487070734;32466654734&q-key-time=1487070734;32559966734&q-header-list=host&q-url-param-list=&q-signature=2ac3ada19910f44836ae0df72a0ec1003f34****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 16087
Connection: keep-alive
x-cos-request-id: NTg3NzRiZGRfYmRjMzVfM2Y2OF81N2Yz****
Date: Thu, 12 Jan 2017 17:26:53 GMT
ETag: \"9a4802d5c99dafe1c04da0a8e7e166bf\"
Access-Control-Allow-Origin: http://www.qq.com
Access-Control-Allow-Methods: PUT
Access-Control-Expose-Headers: x-cos-request-id
Server: tencent-cos
```
