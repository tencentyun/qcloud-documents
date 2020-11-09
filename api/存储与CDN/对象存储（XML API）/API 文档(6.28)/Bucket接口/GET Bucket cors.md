## 功能描述

GET Bucket cors 请求用于查询存储桶的跨域资源共享（CORS）访问控制。

## 请求

#### 请求示例

```plaintext
GET /?cors HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

查询成功，返回 **application/xml** 数据，包含完整的存储桶跨域资源共享（CORS）配置信息。

```plaintext
<?xml version='1.0' encoding='utf-8' ?>
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

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| CORSConfiguration | 无 | 保存 GET Bucket cors 结果的所有信息 | Container |

**Container 节点 CORSConfiguration 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| CORSRule | CORSConfiguration | 说明单条跨域资源共享（CORS）配置的所有信息 | Container |

**Container 节点 CORSRule 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| AllowedOrigin | CORSConfiguration.CORSRule | 允许的访问来源，可能为 `*` 或包含 `*` 的通配格式，单条 CORSRule 可以配置多个 AllowedOrigin | string |
| AllowedMethod | CORSConfiguration.CORSRule | 允许的 HTTP 操作方法（Method），对应 CORS 请求响应中的 Access-Control-Allow-Methods 头部，单条 CORSRule 可以配置多个 AllowedMethod。枚举值：PUT、GET、POST、DELETE、HEAD | enum |
| AllowedHeader | CORSConfiguration.CORSRule | 允许浏览器发送 CORS 请求时携带的自定义 HTTP 请求头部，不区分英文大小写，可能为 `*`，单条 CORSRule 可以配置多个 AllowedHeader。 | string |
| ExposeHeader | CORSConfiguration.CORSRule | 允许浏览器获取的 CORS 请求响应中的头部，不区分英文大小写，单条 CORSRule 可以配置多个 ExposeHeader。 | string |
| MaxAgeSeconds | CORSConfiguration.CORSRule | 跨域资源共享配置的有效时间，单位为秒，对应 CORS 请求响应中的 Access-Control-Max-Age 头部，单条 CORSRule 只能配置一个 MaxAgeSeconds | integer |
| ID | CORSConfiguration.CORSRule | 单条 CORSRule 配置的 ID，该节点的存在与否取决于使用 PUT Bucket cors 设置存储桶跨域资源共享配置时是否指定了 ID，单条 CORSRule 最多配置一个 ID | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
GET /?cors HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 09 Jul 2020 11:15:12 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1594293312;1594300512&q-key-time=1594293312;1594300512&q-header-list=date;host&q-url-param-list=cors&q-signature=8c00249260b2535056d2ef8fc43ecd675515****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1196
Connection: close
Date: Thu, 09 Jul 2020 11:15:12 GMT
Server: tencent-cos
x-cos-request-id: NWYwNmZjNDBfN2ViMTJhMDlfZDNjOV8xYjdk****

<?xml version='1.0' encoding='utf-8' ?>
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
		<AllowedOrigin>https://example-1.com</AllowedOrigin>
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
