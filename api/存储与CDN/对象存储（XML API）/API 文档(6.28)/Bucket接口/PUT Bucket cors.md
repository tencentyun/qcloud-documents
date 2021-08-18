## 功能描述

PUT Bucket cors 请求用于为存储桶配置跨域资源共享（CORS）访问控制，您可以通过传入 XML 格式的配置文件来实现配置，文件大小限制为64KB。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=PutBucketCors&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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
PUT /?cors HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-Length: Content Length
Content-MD5: MD5
Authorization: Auth String

[Request Body]
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

提交 **application/xml** 请求数据，包含完整的存储桶跨域资源共享（CORS）配置信息。

```plaintext
<CORSConfiguration>
	<CORSRule>
		<AllowedOrigin>string</AllowedOrigin>
		<AllowedMethod>enum</AllowedMethod>
		<AllowedMethod>enum</AllowedMethod>
		<AllowedHeader>string</AllowedHeader>
		<AllowedHeader>string</AllowedHeader>
		<ExposeHeader>string</ExposeHeader>
		<ExposeHeader>string</ExposeHeader>
		<MaxAgeSeconds>integer</MaxAgeSeconds>
	</CORSRule>
	<CORSRule>
		<ID>string</ID>
		<AllowedOrigin>string</AllowedOrigin>
		<AllowedOrigin>string</AllowedOrigin>
		<AllowedMethod>enum</AllowedMethod>
		<AllowedMethod>enum</AllowedMethod>
		<AllowedHeader>string</AllowedHeader>
		<ExposeHeader>string</ExposeHeader>
		<ExposeHeader>string</ExposeHeader>
		<MaxAgeSeconds>integer</MaxAgeSeconds>
	</CORSRule>
</CORSConfiguration>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| CORSConfiguration | 无 | 包含 PUT Bucket cors 操作的所有请求信息 | Container | 否 |

**Container 节点 CORSConfiguration 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| CORSRule | CORSConfiguration | 说明单条跨域资源共享（CORS）配置的所有信息，最多可以包含100条 CORSRule | Container | 是 |

**Container 节点 CORSRule 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| AllowedOrigin | CORSConfiguration.CORSRule | 允许的访问来源，单条 CORSRule 可以配置多个 AllowedOrigin。<br><li>配置支持 `*`，表示全部域名都允许，但不推荐。<br><li>支持单个具体域名，例如 `http://www.example.com`。<br><li>支持 `*` 通配符，通配符可出现在任何位置，包括协议、域名和端口，可匹配0个或多个字符，但是只能有一个 `*`。请谨慎使用通配符，因为可能意外匹配到非预期的来源<br><li>注意不要遗漏协议名 http 或 https，若端口不是默认的80(http)或443(https)，还需要带上端口，例如 `https://example.com:8443`。 | string | 是 |
| AllowedMethod | CORSConfiguration.CORSRule | 允许的 HTTP 操作方法（Method），对应 CORS 请求响应中的 Access-Control-Allow-Methods 头部，单条 CORSRule 可以配置多个 AllowedMethod。枚举值：PUT、GET、POST、DELETE、HEAD。 | enum | 是 |
| AllowedHeader | CORSConfiguration.CORSRule | 在发送预检（OPTIONS）请求时，浏览器会告知服务端接下来的正式请求将使用的自定义 HTTP 请求头部，此配置用于指定允许浏览器发送 CORS 请求时携带的自定义 HTTP 请求头部，不区分英文大小写，单条 CORSRule 可以配置多个 AllowedHeader。<br><li>可以配置`*`，代表允许所有头部，为了避免遗漏，推荐配置为`*`。<br><li>如果不配置为`*`，那么在预检（OPTIONS）请求中 Access-Control-Request-Headers 头部出现的每个 Header，都必须在 AllowedHeader 中有对应项。 | string | 是 |
| ExposeHeader | CORSConfiguration.CORSRule | 允许浏览器获取的 CORS 请求响应中的头部，不区分大小写，单条 CORSRule 可以配置多个 ExposeHeader。<br><li>默认情况下浏览器只能访问简单响应头部：Cache-Control、Content-Type、Expires、Last-Modified，如果需要访问其他响应头部，需要添加 ExposeHeader 配置。<br><li>不支持配置为 `*`，必须明确配置具体的 Header。<br><li>根据浏览器的实际需求确定，默认推荐填写 ETag，可参考各 API 文档的响应头部分及 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。 | string | 是 |
| MaxAgeSeconds | CORSConfiguration.CORSRule | 跨域资源共享配置的有效时间，单位为秒，在有效时间内，浏览器无须为同一请求再次发起预检（OPTIONS）请求，对应 CORS 请求响应中的 Access-Control-Max-Age 头部，单条 CORSRule 只能配置一个 MaxAgeSeconds。 | integer | 是 |
| ID | CORSConfiguration.CORSRule | 单条 CORSRule 配置的 ID，用于在 GET Bucket cors 时查找指定 CORSRule。可选填，单条 CORSRule 最多配置一个 ID。 | string | 否 |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
PUT /?cors HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 09 Jul 2020 11:15:01 GMT
Content-Type: application/xml
Content-Length: 1185
Content-MD5: ZNkhBxyjkaZcs1j7/cIE2A==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1594293301;1594300501&q-key-time=1594293301;1594300501&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=cors&q-signature=2ec71624468abfbd5c8ea2679e1365b29f3a****
Connection: close

<CORSConfiguration>
	<CORSRule>
		<AllowedOrigin>*</AllowedOrigin>
		<AllowedMethod>GET</AllowedMethod>
		<AllowedMethod>HEAD</AllowedMethod>
		<AllowedHeader>Range</AllowedHeader>
		<AllowedHeader>x-cos-server-side-encryption-customer-algorithm</AllowedHeader>
		<AllowedHeader>x-cos-server-side-encryption-customer-key</AllowedHeader>
		<AllowedHeader>x-cos-server-side-encryption-customer-key-MD5</AllowedHeader>
		<ExposeHeader>Content-Length</ExposeHeader>
		<ExposeHeader>ETag</ExposeHeader>
		<ExposeHeader>x-cos-meta-author</ExposeHeader>
		<MaxAgeSeconds>600</MaxAgeSeconds>
	</CORSRule>
	<CORSRule>
		<ID>example-id</ID>
		<AllowedOrigin>https://example.com</AllowedOrigin>
		<AllowedOrigin>https://example.net</AllowedOrigin>
		<AllowedMethod>PUT</AllowedMethod>
		<AllowedMethod>GET</AllowedMethod>
		...
		<AllowedMethod>HEAD</AllowedMethod>
		<AllowedHeader>*</AllowedHeader>
		<ExposeHeader>Content-Length</ExposeHeader>
		<ExposeHeader>ETag</ExposeHeader>
		<ExposeHeader>x-cos-meta-author</ExposeHeader>
		<MaxAgeSeconds>600</MaxAgeSeconds>
	</CORSRule>
</CORSConfiguration>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Thu, 09 Jul 2020 11:15:01 GMT
Server: tencent-cos
x-cos-request-id: NWYwNmZjMzVfMzFiYjBiMDlfZjgzYV8xZDky****
```
