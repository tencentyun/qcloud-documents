## 功能描述

GET Object 接口请求可以将 COS 存储桶中的对象（Object）下载至本地。该 API 的请求者需要对目标对象有读取权限，或者目标对象向所有人开放了读取权限（公有读）。

> !
>- 如果使用了 `response-*` 请求参数，那么该请求操作不支持匿名请求，必须携带签名。
>- 当通过 COS 控制台 [设置回源](https://cloud.tencent.com/document/product/436/13310) ，但未开启**同步回源**时，需注意，COS 从用户配置的源站拉取数据时，发起 GET Object 请求将返回 302 并重定向到设置的回源地址（如果该回源地址是不受信任的，强烈建议在使用 SDK 或自行调用 API 时，不要直接跟随 302，而应该由业务后端验证回源地址的合法性后再去请求回源地址，否则可能产生 SSRF 等安全风险，例如回源到一个内网地址）。
>

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=GetObject&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


#### 版本控制

当启用版本控制时，该 GET 操作可以使用 versionId 请求参数指定要返回的版本 ID，此时将返回对象的指定版本。若指定版本为删除标记，则返回 HTTP 响应码404（Not Found），否则将返回指定对象的最新版本。

#### 归档类型

如果该 GET 请求操作的对象为**归档存储和深度归档存储类型**，且没有使用 [POST Object restore](https://cloud.tencent.com/document/product/436/12633) 进行恢复（或恢复后的副本已被过期删除），那么该请求将返回 HTTP 响应码403（Forbidden），同时在响应体中包含错误信息，其中错误码（Code）为 InvalidObjectState，表示对象的当前状态无法被 GET 请求操作，需要先经过恢复。

## 请求

#### 请求示例

```shell
GET /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

| 名称                         | 描述                                                         | 类型   | 是否必选 |
| ---------------------------- | ------------------------------------------------------------ | ------ | -------- |
| response-cache-control       | 设置响应中的 Cache-Control 头部的值                          | string | 否       |
| response-content-disposition | 设置响应中的 Content-Disposition 头部的值                    | string | 否       |
| response-content-encoding    | 设置响应中的 Content-Encoding 头部的值                       | string | 否       |
| response-content-language    | 设置响应中的 Content-Language 头部的值                       | string | 否       |
| response-content-type        | 设置响应中的 Content-Type 头部的值                           | string | 否       |
| response-expires             | 设置响应中的 Expires 头部的值                                | string | 否       |
| versionId                    | 当启用版本控制时，指定要下载的版本 ID，如不指定则下载对象的最新版本 | string | 否       |

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述                                                         | 类型    | 是否必选 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------- | -------- |
| Range                                                        | RFC 2616 中定义的字节范围，范围值必须使用 bytes=first-last 格式且仅支持单一范围，不支持多重范围。first 和 last 都是基于0开始的偏移量。<br>例如 bytes=0-9，表示下载对象的开头10个字节的数据；bytes=5-9，表示下载对象的第6到第10个字节。此时返回 HTTP 状态码206（Partial Content）及 Content-Range 响应头部。<br>如果 first 超过对象的大小，则返回 HTTP 状态码416（Requested Range Not Satisfiable）错误。如果不指定，则表示下载整个对象 | string  | 否       |
| If-Modified-Since                                            | 当对象在指定时间后被修改，则返回对象，否则返回 HTTP 状态码为304（Not Modified） | string  | 否       |
| If-Unmodified-Since                                          | 当对象在指定时间后未被修改，则返回对象，否则返回 HTTP 状态码为412（Precondition Failed） | string  | 否       |
| If-Match                                                     | 当对象的 ETag 与指定的值一致，则返回对象，否则返回 HTTP 状态码为412（Precondition Failed） | string  | 否       |
| If-None-Match                                                | 当对象的 ETag 与指定的值不一致，则返回对象，否则返回 HTTP 状态码为304（Not Modified） | string  | 否       |
| x-cos-traffic-limit                                          | 针对本次下载进行流量控制的限速值，必须为数字，单位默认为 bit/s。限速值设置范围为819200 - 838860800，即100KB/s - 100MB/s，如果超出该范围将返回400错误 | integer | 否       |

**服务端加密相关头部**

如果指定的对象使用了服务端加密且加密方式为 SSE-C 时，则需要指定服务端加密的相关头部来解密对象，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7728#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述                                                         | 类型   |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| Cache-Control                                                | RFC 2616 中定义的缓存指令，仅当对象元数据包含此项或通过请求参数指定了此项时才会返回该头部 | string |
| Content-Disposition                                          | RFC 2616 中定义的文件名称，仅当对象元数据包含此项或通过请求参数指定了此项时才会返回该头部 | string |
| Content-Encoding                                             | RFC 2616 中定义的编码格式，仅当对象元数据包含此项或通过请求参数指定了此项时才会返回该头部 | string |
| Content-Range                                                | RFC 2616 中定义的返回内容的字节范围，仅当请求中指定了 Range 请求头部时才会返回该头部 | string |
| Expires                                                      | RFC 2616 中定义的缓存失效时间，仅当对象元数据包含此项或通过请求参数指定了此项时才会返回该头部 | string |
| x-cos-meta-\*                                                | 包括用户自定义元数据头部后缀和用户自定义元数据信息           | string |
| x-cos-storage-class                                          | 对象存储类型，枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 MAZ_STANDARD、MAZ_STANDARD_IA、INTELLIGENT_TIERING、MAZ_INTELLIGENT_TIERING、STANDARD_IA、ARCHIVE、DEEP_ARCHIVE。仅当对象不是标准存储（STANDARD）时才会返回该头部 | enum   |
|  x-cos-storage-tier  |  当对象的存储类型为智能分层存储时，该头部表示对象所处的存储层，有效值：FREQUENT、INFREQUENT。  |  enum  |

**版本控制相关头部**

启用版本控制的存储桶内的对象将返回下列响应头部：

| 名称             | 描述          | 类型   |
| ---------------- | ------------- | ------ |
| x-cos-version-id | 对象的版本 ID | string |

**服务端加密相关头部**

如果指定的对象使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

此接口请求的响应体为对象（文件）内容。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例（未启用版本控制）

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 09:35:16 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586511316;1586518516&q-key-time=1586511316;1586518516&q-header-list=date;host&q-url-param-list=&q-signature=1bd1898e241fb978df336dc68aaef4c0acae****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Accept-Ranges: bytes
Date: Fri, 10 Apr 2020 09:35:16 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 09:35:05 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MDNkZDRfZDgyNzVkNjRfN2Q5M18xOWVi****



[Object Content]
```

#### 案例二：通过请求参数指定响应头部

#### 请求

```shell
GET /exampleobject?response-content-type=application%2Foctet-stream&response-cache-control=max-age%3D86400&response-content-disposition=attachment%3B%20filename%3Dexample.jpg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 09:35:17 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586511317;1586518517&q-key-time=1586511317;1586518517&q-header-list=date;host&q-url-param-list=response-cache-control;response-content-disposition;response-content-type&q-signature=4fcea9f80bc67fe475dff746eca0b9abff6a****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Content-Length: 16
Connection: close
Accept-Ranges: bytes
Cache-Control: max-age=86400
Content-Disposition: attachment; filename=example.jpg
Date: Fri, 10 Apr 2020 09:35:17 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 09:35:05 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MDNkZDVfNjZjODJhMDlfMTY2MDdfMThm****



[Object Content]
```

#### 案例三：通过请求头指定查询条件并返回 HTTP 状态码为304（Not Modified）

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 29 Jul 2020 06:51:49 GMT
If-None-Match: "ee8de918d05640145b18f70f4c3aa602"
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1596005509;1596012709&q-key-time=1596005509;1596012709&q-header-list=date;host;if-none-match&q-url-param-list=&q-signature=20e39095b9f22ae1279bec2a3375b527c32d****
Connection: close
```

#### 响应

```shell
HTTP/1.1 304 Not Modified
Content-Type: image/jpeg
Content-Length: 0
Connection: close
Date: Wed, 29 Jul 2020 06:51:49 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWYyMTFjODVfOGZiNzJhMDlfNDcxZjZfZDY2****
```

#### 案例四：通过请求头指定查询条件并返回 HTTP 状态码为412（Precondition Failed）

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 29 Jul 2020 06:51:50 GMT
If-Match: "aa488bb80185a6be87f4a7b936a80752"
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1596005510;1596012710&q-key-time=1596005510;1596012710&q-header-list=date;host;if-match&q-url-param-list=&q-signature=1437a0d094c4e0f8e26909d35b2cca83dcbf****
Connection: close
```

#### 响应

```shell
HTTP/1.1 412 Precondition Failed
Content-Type: application/xml
Content-Length: 480
Connection: close
Date: Wed, 29 Jul 2020 06:51:50 GMT
Server: tencent-cos
x-cos-request-id: NWYyMTFjODZfOGRjOTJhMDlfMmIyMWVfOTJl****



<?xml version='1.0' encoding='utf-8' ?>
<Error>
			<Code>PreconditionFailed</Code>
			<Message>Precondition not match.</Message>
			<Resource>examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Resource>
			<RequestId>NWYyMTFjODZfOGRjOTJhMDlfMmIyMWVfOTJl****</RequestId>
			<TraceId>OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OTdjMDczODYwZjM5YTU3ZmZmOWI5MmY4NjkxY2I3MGNiNjkyOWZiNzUxZjg5MGY2OWU4NmI0YWMwNTlhNTExYWU=</TraceId>
</Error>
```

#### 案例五：使用服务端加密 SSE-COS

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 09:36:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586511360;1586518560&q-key-time=1586511360;1586518560&q-header-list=date;host&q-url-param-list=&q-signature=6f9ec1af1aa86abd5b484b41ae1378850ad2****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Accept-Ranges: bytes
Date: Fri, 10 Apr 2020 09:36:00 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 09:35:49 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MDNlMDBfMzdiMDJhMDlfYTgyNl8xNjA2****
x-cos-server-side-encryption: AES256



[Object Content]
```

#### 案例六：使用服务端加密 SSE-KMS

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 09:36:11 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586511371;1586518571&q-key-time=1586511371;1586518571&q-header-list=date;host&q-url-param-list=&q-signature=bdadbe917a50feeb8dddf8c75642be172720****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Accept-Ranges: bytes
Date: Fri, 10 Apr 2020 09:36:11 GMT
ETag: "840af7c921f4b3230049af8663145bd0"
Last-Modified: Fri, 10 Apr 2020 09:36:01 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MDNlMGJfZGEyNzVkNjRfZDgxY18xYTBj****
x-cos-server-side-encryption: cos/kms
x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****



[Object Content]
```

#### 案例七：使用服务端加密 SSE-C

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 09:36:23 GMT
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key: MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586511383;1586518583&q-key-time=1586511383;1586518583&q-header-list=date;host;x-cos-server-side-encryption-customer-algorithm;x-cos-server-side-encryption-customer-key;x-cos-server-side-encryption-customer-key-md5&q-url-param-list=&q-signature=7da5c304f9439df949b6550ab23aea67a5f0****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Accept-Ranges: bytes
Date: Fri, 10 Apr 2020 09:36:23 GMT
ETag: "582d9105f71525f3c161984bc005efb5"
Last-Modified: Fri, 10 Apr 2020 09:36:12 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MDNlMTdfNzBiODJhMDlfZTVmMV8xNDAy****
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==



[Object Content]
```

#### 案例八：下载对象最新版本（启用版本控制）

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 12:30:02 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586521802;1586529002&q-key-time=1586521802;1586529002&q-header-list=date;host&q-url-param-list=&q-signature=51b3c33f4cfae5d7b31ad61a974db7374f39****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 26
Connection: close
Accept-Ranges: bytes
Date: Fri, 10 Apr 2020 12:30:02 GMT
ETag: "22e024392de860289f0baa7d6cf8a549"
Last-Modified: Fri, 10 Apr 2020 12:29:52 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 11596229263574363878
x-cos-request-id: NWU5MDY2Y2FfMzFiYjBiMDlfMjE2NzVfMTgz****
x-cos-version-id: MTg0NDUxNTc1NTE5MTc1NjM4MDA



[Object Content Version 2]
```

#### 案例九：下载对象指定版本（启用版本控制）

#### 请求

```shell
GET /exampleobject?versionId=MTg0NDUxNTc1NjIzMTQ1MDAwODg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 09:36:45 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586511405;1586518605&q-key-time=1586511405;1586518605&q-header-list=date;host&q-url-param-list=versionid&q-signature=31aeb69334b973ef7406300a182de0645c91****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Accept-Ranges: bytes
Date: Fri, 10 Apr 2020 09:36:45 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 09:36:35 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MDNlMmRfNzBiODJhMDlfZTYwZl8xM2Fh****
x-cos-version-id: MTg0NDUxNTc1NjIzMTQ1MDAwODg



[Object Content]
```

#### 案例十：指定 Range 请求头部下载部分内容

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 12:32:37 GMT
Range: bytes=8-14
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586521957;1586529157&q-key-time=1586521957;1586529157&q-header-list=date;host;range&q-url-param-list=&q-signature=719273479357f4b4b4c7d4f5ceb631753101****
Connection: close
```

#### 响应

```shell
HTTP/1.1 206 Partial Content
Content-Type: image/jpeg
Content-Length: 7
Connection: close
Accept-Ranges: bytes
Content-Range: bytes 8-14/16
Date: Fri, 10 Apr 2020 12:32:37 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 12:32:25 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MDY3NjVfY2VjODJhMDlfOWVlZl8xNmMy****



Content
```

#### 案例十一：下载未经恢复的归档（ARCHIVE）存储类型的对象

#### 请求

```shell
GET /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 26 Dec 2019 11:57:24 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1577361444;1577368644&q-key-time=1577361444;1577368644&q-header-list=date;host&q-url-param-list=&q-signature=d975dc7097b2dbffcf2ba001e6dec25dd80a****
Connection: close

```

#### 响应

```shell
HTTP/1.1 403 Forbidden
Content-Type: application/xml
Content-Length: 513
Connection: close
Date: Thu, 26 Dec 2019 11:57:24 GMT
Server: tencent-cos
x-cos-request-id: NWUwNGEwMjRfZDcyNzVkNjRfNjZlM183Zjcx****
x-cos-storage-class: ARCHIVE



<?xml version='1.0' encoding='utf-8' ?>
<Error>
			<Code>InvalidObjectState</Code>
			<Message>The operation is not valid for the object storage class.</Message>
			<Resource>examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Resource>
			<RequestId>NWUwNGEwMjRfZDcyNzVkNjRfNjZlM183Zjcx****</RequestId>
			<TraceId>OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OTBjNjIyOGVlZmJlNDg4NDQ1MzAzMjA2ZDg4OGQ3MDhlMjIzYjI1ZWUwODY5YjdlMTBjY2EwNTgyZWMyMjc0Mjc=</TraceId>
</Error>
```

