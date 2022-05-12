## 功能描述

OPTIONS Object 用于跨域资源共享（CORS）的预检（Preflight）请求。当浏览器发起 CORS 请求时，浏览器会判断是否有必要发起预检请求，如有必要则浏览器会在发起 CORS 请求前自动发出预检请求，所以在正常情况下，前端开发者不需要自己去发起这样的请求。
- 如果指定存储桶存在 CORS 配置且预检条件符合存储桶的 CORS 配置，则 COS 正常返回，允许浏览器继续 CORS 请求。
- 如果指定存储桶不存在 CORS 配置或预检条件不符合存储桶的 CORS 配置，则 COS 返回 HTTP 403 Forbidden，此时浏览器将停止 CORS 请求并向前端抛出异常。
- 有关存储桶的 CORS 配置，可参见 [PUT Bucket cors](https://cloud.tencent.com/document/product/436/8279) 文档。


<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=OptionsObject&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

## 请求

#### 请求示例

```plaintext
OPTIONS /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Origin: Origin
Access-Control-Request-Method: RequestMethod
```

>!
>- 虽然上述示例指定了对象键（ObjectKey），但在实际使用过程中可针对存储桶域名下的任意资源（包含根目录）发起预检请求，例如 `OPTIONS / HTTP/1.1` 或者 `OPTIONS /?lifecycle HTTP/1.1` 等。
>- 预检请求由浏览器自动发出，因此预检请求无需也无法携带 Authorization 请求签名。
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> 

#### 请求参数

此接口的请求参数由浏览器自动根据跨域访问的目标资源决定，开发者无需关注。

#### 请求头

此接口的请求头由浏览器自动根据跨域访问的具体行为决定，开发者无需关注。

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| Origin | 发起 CORS 请求的域名。 | string | 是 |
| Access-Control-Request-Method | 发起 CORS 请求所用的方法（Method） | string | 是 |
| Access-Control-Request-Headers | 发起 CORS 请求时使用的 HTTP 请求头部，不区分英文大小写，可使用英文逗号(,)分隔多个头部 | string | 否 |

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口的响应头由浏览器自动识别处理并控制是否允许 CORS 请求，开发者无需关注。

| 名称 | 描述 | 类型 |
| --- | --- | --- |
| Access-Control-Allow-Origin | 允许发起 CORS 的域名，可能的值有以下两种：<br><li>`*`：代表允许所有域名<br><li>请求头 Origin 中指定的域名：代表允许指定域名 | string |
| Access-Control-Allow-Methods | 允许发起 CORS 请求所使用的方法（Method），可使用英文逗号(,)分隔多个方法 | string |
| Access-Control-Expose-Headers | 允许浏览器获取的 CORS 请求中的 HTTP 响应头部，不区分英文大小写，可使用英文逗号(,)分隔多个头部 | string |
| Access-Control-Max-Age | CORS 配置的有效时间，单位为秒，在有效时间内，浏览器无须为同一请求再次发起预检请求 | integer |

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

以下案例均由浏览器根据发起的 CORS 请求自动发起的预检请求，开发者无需关注。

#### 案例一：针对 PUT Object 发起预检请求

#### 请求

```plaintext
OPTIONS /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 09 Jul 2020 14:49:22 GMT
Origin: https://example.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-md5,content-type,x-cos-meta-author
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: content-md5,content-type,x-cos-meta-author
Access-Control-Allow-Methods: PUT,GET,POST,DELETE,HEAD
Access-Control-Allow-Origin: https://example.com
Access-Control-Expose-Headers: Content-Length,ETag,x-cos-meta-author
Access-Control-Max-Age: 600
Date: Thu, 09 Jul 2020 14:49:22 GMT
Server: tencent-cos
x-cos-request-id: NWYwNzJlNzJfODRjOTJhMDlfMjU0MWNfMTNmZDM5****
```

#### 案例二：针对 GET Object 时携带 Range 请求头部发起预检请求

#### 请求

```plaintext
OPTIONS /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 09 Jul 2020 14:49:22 GMT
Origin: https://example.com
Access-Control-Request-Method: GET
Access-Control-Request-Headers: range
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Access-Control-Allow-Headers: range,x-cos-server-side-encryption-customer-algorithm,x-cos-server-side-encryption-customer-key,x-cos-server-side-encryption-customer-key-md5
Access-Control-Allow-Methods: GET,HEAD
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Content-Length,ETag,x-cos-meta-author
Access-Control-Max-Age: 600
Date: Thu, 09 Jul 2020 14:49:22 GMT
Server: tencent-cos
x-cos-request-id: NWYwNzJlNzJfZDUyNzVkNjRfYTA2Ml8yNGEz****
```

#### 案例三：针对 PUT Bucket lifecycle 发起预检请求

#### 请求

```plaintext
OPTIONS /?lifecycle HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 09 Jul 2020 14:29:40 GMT
Origin: https://bar.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-md5,content-type
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: content-md5,content-type
Access-Control-Allow-Methods: PUT,GET,POST,DELETE,HEAD
Access-Control-Allow-Origin: https://bar.com
Access-Control-Expose-Headers: Content-Length,ETag,x-cos-meta-author
Access-Control-Max-Age: 600
Date: Thu, 09 Jul 2020 14:29:40 GMT
Server: tencent-cos
x-cos-request-id: NWYwNzI5ZDRfNjFiMDJhMDlfYzk2NF8xYmZl****
```

#### 案例四：指定存储桶不存在 CORS 配置或预检条件不符合存储桶的 CORS 配置

#### 请求

```plaintext
OPTIONS /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 09 Jul 2020 11:45:26 GMT
Origin: https://example.com
Access-Control-Request-Method: PUT
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 403 Forbidden
Content-Type: application/xml
Content-Length: 687
Connection: close
Date: Thu, 09 Jul 2020 11:45:26 GMT
Server: tencent-cos
x-cos-request-id: NWYwNzAzNTZfNzNjODJhMDlfMzRiM2ZfMThjMjk4****
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OWE4OGMxZjNjY2JiNTBmMTVmMWY1MzAzYzkyZGQ2ZWM4OWM4Y2M5MzI5ZmUzN2FjZDk1OTRjYWI5Yjg5OTJlZDA=

<?xml version='1.0' encoding='utf-8' ?>
<Error>
	<Code>AccessForbidden</Code>
	<Message>CORSResponse: This CORS request is not allowed. This is usually because the evalution of Origin, request method / Access-Control-Request-Method or Access-Control-Requet-Headers are not whitelisted by the resource&apos;s CORS spec</Message>
	<Resource>examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Resource>
	<RequestId>NWYwNzAzNTZfNzNjODJhMDlfMzRiM2ZfMThjMjk4****</RequestId>
	<TraceId>OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OWE4OGMxZjNjY2JiNTBmMTVmMWY1MzAzYzkyZGQ2ZWM4OWM4Y2M5MzI5ZmUzN2FjZDk1OTRjYWI5Yjg5OTJlZDA=</TraceId>
</Error>
```
