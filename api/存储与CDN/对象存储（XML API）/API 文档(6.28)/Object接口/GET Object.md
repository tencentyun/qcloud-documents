## 功能描述

GET Object 接口请求可以将 COS 存储桶中的对象（Object）下载至本地。该 API 的请求者需要对目标对象有读取权限，或者目标对象向所有人开放了读取权限（公有读）。

>? 如果使用了 response-* 请求参数，那么该请求操作不支持匿名请求，必须携带签名。

#### 版本控制

当启用版本控制时，该 GET 操作返回对象的最新版本。要返回对象的历史版本，请使用 versionId 请求参数。

## 请求

#### 请求示例

```shell
GET /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| response-cache-control | 设置响应中的 Cache-Control 头部的值 | string | 否 |
| response-content-disposition | 设置响应中的 Content-Disposition 头部的值 | string | 否 |
| response-content-encoding | 设置响应中的 Content-Encoding 头部的值 | string | 否 |
| response-content-language | 设置响应中的 Content-Language 头部的值 | string | 否 |
| response-content-type | 设置响应中的 Content-Type 头部的值 | string | 否 |
| response-expires | 设置响应中的 Expires 头部的值 | string | 否 |
| versionId | 当启用版本控制时，指定要下载的对象的版本 ID，若不指定则下载对象的最新版本 | string | 否 |

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| Range | RFC 2616 中定义的字节范围，范围值必须使用 bytes=first-last 格式，first 和 last 都是基于0开始的偏移量。例如 bytes=0-9，表示下载对象的开头10个字节的数据，此时返回 HTTP 状态码206（Partial Content）及 Content-Range 响应头部。如果不指定，则表示下载整个对象 | string | 否 |
| If-Modified-Since | 当对象在指定时间后被修改，则返回对象，否则返回 HTTP 状态码为304（Not Modified） | string | 否 |
| If-Unmodified-Since | 当对象在指定时间后未被修改，则返回对象，否则返回 HTTP 状态码为412（Precondition Failed） | string | 否 |
| If-Match | 当对象的 ETag 与指定的值一致，则返回对象，否则返回 HTTP 状态码为412（Precondition Failed） | string | 否 |
| If-None-Match | 当对象的 ETag 与指定的值不一致，则返回对象，否则返回 HTTP 状态码为304（Not Modified） | string | 否 |

**服务端加密相关头部**

如果指定的对象使用了服务端加密且加密方式为 SSE-C 时，则需要指定服务端加密的相关头部来解密对象，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7728#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

| 名称 | 描述 | 类型 |
| --- | --- | --- |
| Cache-Control | RFC 2616 中定义的缓存指令，仅当对象元数据包含此项或通过请求参数指定了此项时才会返回该头部 | string |
| Content-Disposition | RFC 2616 中定义的文件名称，仅当对象元数据包含此项或通过请求参数指定了此项时才会返回该头部 | string |
| Content-Encoding | RFC 2616 中定义的编码格式，仅当对象元数据包含此项或通过请求参数指定了此项时才会返回该头部 | string |
| Content-Range | RFC 2616 中定义的返回内容的字节范围，仅当请求中指定了 Range 请求头部时才会返回该头部 | string |
| Expires | RFC 2616 中定义的缓存失效时间，仅当对象元数据包含此项或通过请求参数指定了此项时才会返回该头部 | string |
| x-cos-meta-\* | 包括用户自定义元数据头部后缀和用户自定义元数据信息 | string |
| x-cos-storage-class | 对象存储类型。枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 STANDARD_IA，ARCHIVE。仅当对象不是标准存储（STANDARD）时才会返回该头部 | Enum |

**版本控制相关头部**

启用版本控制的存储桶内的对象将返回下列响应头部：

| 名称 | 描述 | 类型 |
| --- | --- | --- |
| x-cos-version-id | 对象的版本 ID | string |

**服务端加密相关头部**

如果指定的对象使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

此接口请求的响应体为对象（文件）内容。

#### 错误码

此接口无特殊错误信息，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例（未启用版本控制）

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 04 Jul 2019 11:33:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1562239980;1562247180&q-key-time=1562239980;1562247180&q-header-list=date;host&q-url-param-list=&q-signature=fa5552e4c84ab474e9b66bcecbefcb5c15d9****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 13
Connection: close
Accept-Ranges: bytes
Date: Thu, 04 Jul 2019 11:33:00 GMT
ETag: "b62e10bcab55a88240bd9c436cffdcf9"
Last-Modified: Thu, 04 Jul 2019 11:32:55 GMT
Server: tencent-cos
x-cos-request-id: NWQxZGUzZWNfN2RiZTBiMDlfM2EzZF8yMGYx****

[Object Content]
```

#### 案例二：通过请求参数指定响应头部

#### 请求

```shell
GET /exampleobject?response-content-type=application%2Foctet-stream&response-cache-control=max-age%3D86400&response-content-disposition=attachment%3B%20filename%3Dexample.jpg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 04 Jul 2019 11:33:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1562239980;1562247180&q-key-time=1562239980;1562247180&q-header-list=date;host&q-url-param-list=response-cache-control;response-content-disposition;response-content-type&q-signature=a079419b6f0cd4ac1bc55bcdf14b54a4a9a3****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Content-Length: 13
Connection: close
Accept-Ranges: bytes
Cache-Control: max-age=86400
Content-Disposition: attachment; filename=example.jpg
Date: Thu, 04 Jul 2019 11:33:00 GMT
ETag: "b62e10bcab55a88240bd9c436cffdcf9"
Last-Modified: Thu, 04 Jul 2019 11:32:55 GMT
Server: tencent-cos
x-cos-request-id: NWQxZGUzZWNfNjI4NWQ2NF9lMWYyXzk1NjFj****

[Object Content]
```

#### 案例三：使用服务端加密 SSE-COS

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 04 Jul 2019 11:33:05 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1562239985;1562247185&q-key-time=1562239985;1562247185&q-header-list=date;host&q-url-param-list=&q-signature=c2f7fbaba0ad534483078eebef3ca4a829ae****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 13
Connection: close
Accept-Ranges: bytes
Date: Thu, 04 Jul 2019 11:33:06 GMT
ETag: "b62e10bcab55a88240bd9c436cffdcf9"
Last-Modified: Thu, 04 Jul 2019 11:33:00 GMT
Server: tencent-cos
x-cos-request-id: NWQxZGUzZjJfZGQyOTVkNjRfMjU0NF80MGVj****
x-cos-server-side-encryption: AES256

[Object Content]
```

#### 案例四：使用服务端加密 SSE-C

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 04 Jul 2019 11:33:11 GMT
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key: MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1562239991;1562247191&q-key-time=1562239991;1562247191&q-header-list=date;host;x-cos-server-side-encryption-customer-algorithm;x-cos-server-side-encryption-customer-key;x-cos-server-side-encryption-customer-key-md5&q-url-param-list=&q-signature=6e50f8adca0fb8040868ab05891abf6df2a8****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 13
Connection: close
Accept-Ranges: bytes
Date: Thu, 04 Jul 2019 11:33:11 GMT
ETag: "492b458ec33eaf0a824e7dd1bdd403b3"
Last-Modified: Thu, 04 Jul 2019 11:33:06 GMT
Server: tencent-cos
x-cos-request-id: NWQxZGUzZjdfZDkyNzVkNjRfZDA0Y185OGJj****
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==

[Object Content]
```

#### 案例五：下载对象最新版本（启用版本控制）

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 05 Jul 2019 03:30:31 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1562297431;1562304631&q-key-time=1562297431;1562304631&q-header-list=date;host&q-url-param-list=&q-signature=5bb216e0260589dc6a9986bf6caa3df18db4****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 15
Connection: close
Accept-Ranges: bytes
Date: Fri, 05 Jul 2019 03:30:31 GMT
ETag: "60c7644eb1ae8918a7fe7e13a352712c"
Last-Modified: Fri, 05 Jul 2019 03:30:26 GMT
Server: tencent-cos
x-cos-request-id: NWQxZWM0NTdfZGEyNzVkNjRfMjJhOV9hMWVk****
x-cos-version-id: MTg0NDUxODE3NzYyODMxOTg0OTg

[Object Content]
```

#### 案例六：下载对象指定版本（启用版本控制）

#### 请求

```shell
GET /exampleobject?versionId=MTg0NDUxODE3NzYyODg0ODI2MjA HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 05 Jul 2019 03:30:31 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1562297431;1562304631&q-key-time=1562297431;1562304631&q-header-list=date;host&q-url-param-list=versionid&q-signature=3ea1162e56d0b43f7398a39b99b72bbf58ad****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 13
Connection: close
Accept-Ranges: bytes
Date: Fri, 05 Jul 2019 03:30:31 GMT
ETag: "b62e10bcab55a88240bd9c436cffdcf9"
Last-Modified: Fri, 05 Jul 2019 03:30:21 GMT
Server: tencent-cos
x-cos-request-id: NWQxZWM0NTdfOTNjMjJhMDlfZDBjNV85ZTBh****
x-cos-version-id: MTg0NDUxODE3NzYyODg0ODI2MjA

[Object Content]
```

#### 案例七：指定 Range 请求头部下载部分内容

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 09 Aug 2019 04:02:17 GMT
Range: bytes=2-4
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565323337;1565330537&q-key-time=1565323337;1565330537&q-header-list=date;host;range&q-url-param-list=&q-signature=8b3b4427bbbe15c5cfba9c458c9b3c85d0e3****
Connection: close
```

#### 响应

```shell
HTTP/1.1 206 Partial Content
Content-Type: image/jpeg
Content-Length: 3
Connection: close
Accept-Ranges: bytes
Content-Range: bytes 2-4/13
Date: Fri, 09 Aug 2019 04:02:18 GMT
ETag: "b62e10bcab55a88240bd9c436cffdcf9"
Last-Modified: Fri, 09 Aug 2019 04:02:12 GMT
Server: tencent-cos
x-cos-request-id: NWQ0Y2YwNGFfNDhiNDBiMDlfMmU2ZTFfMTc0MGVl****

[Object Content]
```
