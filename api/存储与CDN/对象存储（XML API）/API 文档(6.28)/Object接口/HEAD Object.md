## 功能描述

HEAD Object 接口请求可以判断指定对象是否存在和有权限，并在指定对象可访问时获取其元数据。该 API 的请求者需要对目标对象有读取权限，或者目标对象向所有人开放了读取权限（公有读）。

#### 版本控制

当启用版本控制时，该 HEAD 操作可以使用 versionId 请求参数指定要返回的版本 ID，此时将返回指定版本的元数据，如指定版本为删除标记则返回 HTTP 响应码404（Not Found），否则将返回最新版本的元数据。

## 请求

#### 请求示例

```shell
HEAD /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> ? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

| 名称      | 描述                                                         | 类型   | 是否必选 |
| --------- | ------------------------------------------------------------ | ------ | -------- |
| versionId | 当启用版本控制时，指定要查询的版本 ID，如不指定则查询对象的最新版本 | string | 否       |

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述                                                         | 类型   | 是否必选 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | -------- |
| If-Modified-Since                                            | 当对象在指定时间后被修改，则返回 HTTP 状态码为200（OK），否则返回 HTTP 状态码为304（Not Modified） | string | 否       |
| If-Unmodified-Since                                          | 当对象在指定时间后未被修改，则返回 HTTP 状态码为200（OK），否则返回 HTTP 状态码为412（Precondition Failed） | string | 否       |
| If-Match                                                     | 当对象的 ETag 与指定的值一致，则返回 HTTP 状态码为200（OK），否则返回 HTTP 状态码为412（Precondition Failed） | string | 否       |
| If-None-Match                                                | 当对象的 ETag 与指定的值不一致，则返回 HTTP 状态码为200（OK），否则返回 HTTP 状态码为304（Not Modified） | string | 否       |

**服务端加密相关头部**

如果指定的对象使用了服务端加密且加密方式为 SSE-C 时，则需要指定服务端加密的相关头部来解密对象，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7728#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述                                                         | 类型   |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| Cache-Control                                                | RFC 2616 中定义的缓存指令，仅当对象元数据包含此项时才会返回该头部 | string |
| Content-Disposition                                          | RFC 2616 中定义的文件名称，仅当对象元数据包含此项时才会返回该头部 | string |
| Content-Encoding                                             | RFC 2616 中定义的编码格式，仅当对象元数据包含此项时才会返回该头部 | string |
| Expires                                                      | RFC 2616 中定义的缓存失效时间，仅当对象元数据包含此项时才会返回该头部 | string |
| x-cos-meta-\*                                                | 包括用户自定义元数据头部后缀和用户自定义元数据信息           | string |
| x-cos-storage-class                                          | 对象存储类型，枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 MAZ_STANDARD，STANDARD_IA，ARCHIVE。仅当对象不是标准存储（STANDARD）时才会返回该头部 | Enum   |

#### 归档类型对象相关头部

当对象为归档类型且使用 POST Object restore 请求进行恢复操作时，该 HEAD 请求将返回下列响应头部：

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述 | 类型 |
| --- | --- | --- |
| x-cos-restore | 指示当前恢复操作的状态：<br><li>当恢复操作正在进行中时，该响应头部的值为`ongoing-request="true"`<li>当对象已经恢复时，该响应头部包含 COS 即将删除临时副本的时间，例如`ongoing-request="false", expiry-date="Tue, 19 Nov 2019 16:00:00 GMT"` | string
| x-cos-restore-status | 当恢复操作正在进行中时返回该响应头部，指示当前的恢复模式和恢复操作请求时间，例如`tier="bulk"; request-date="Mon, 18 Nov 2019 09:34:50 GMT"`，有关恢复模式请参见 [POST Object restore](https://cloud.tencent.com/document/product/436/12633#.E8.AF.B7.E6.B1.82) | string

**版本控制相关头部**

启用版本控制的存储桶内的对象将返回下列响应头部：

| 名称             | 描述          | 类型   |
| ---------------- | ------------- | ------ |
| x-cos-version-id | 对象的版本 ID | string |

**服务端加密相关头部**

如果指定的对象使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

此接口响应体为空。

#### 错误码

此接口无特殊错误信息，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例（未启用版本控制）

#### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:17:36 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542656;1586549856&q-key-time=1586542656;1586549856&q-header-list=date;host&q-url-param-list=&q-signature=cde88925e00d1c90ba74985ca43b610bdf6b****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Date: Fri, 10 Apr 2020 18:17:36 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 18:17:25 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MGI4NDBfNjFjODJhMDlfMzY2NjVfMjNi****
```

#### 案例二：使用服务端加密 SSE-COS

#### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:18:19 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542699;1586549899&q-key-time=1586542699;1586549899&q-header-list=date;host&q-url-param-list=&q-signature=6a6d4dd5b5a9e6379f300715985bfb60b947****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Date: Fri, 10 Apr 2020 18:18:19 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 18:18:08 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MGI4NmJfNmRjMDJhMDlfZGQwNl8xZmE4****
x-cos-server-side-encryption: AES256
```

#### 案例三：使用服务端加密 SSE-KMS

#### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:18:30 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542710;1586549910&q-key-time=1586542710;1586549910&q-header-list=date;host&q-url-param-list=&q-signature=7c8a1c93b9701e653c2ab00419f976397d00****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Date: Fri, 10 Apr 2020 18:18:30 GMT
ETag: "00ca268468481b847fc2d8a9bd84578d"
Last-Modified: Fri, 10 Apr 2020 18:18:19 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MGI4NzZfN2FjODJhMDlfMjU3N18xYTEz****
x-cos-server-side-encryption: cos/kms
x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****
```

#### 案例四：使用服务端加密 SSE-C

#### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:18:41 GMT
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key: MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542721;1586549921&q-key-time=1586542721;1586549921&q-header-list=date;host;x-cos-server-side-encryption-customer-algorithm;x-cos-server-side-encryption-customer-key;x-cos-server-side-encryption-customer-key-md5&q-url-param-list=&q-signature=99ad258fc295f43feb0546bb2346c8269dc5****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Date: Fri, 10 Apr 2020 18:18:41 GMT
ETag: "582d9105f71525f3c161984bc005efb5"
Last-Modified: Fri, 10 Apr 2020 18:18:31 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MGI4ODFfN2NiODJhMDlfMmFmYTVfMWRh****
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
```

#### 案例五：请求对象最新版本（启用版本控制）

#### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:19:15 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542755;1586549955&q-key-time=1586542755;1586549955&q-header-list=date;host&q-url-param-list=&q-signature=7909dc19780873dfaa51c8b238254098ca1a****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 26
Connection: close
Date: Fri, 10 Apr 2020 18:19:15 GMT
ETag: "22e024392de860289f0baa7d6cf8a549"
Last-Modified: Fri, 10 Apr 2020 18:19:04 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 11596229263574363878
x-cos-request-id: NWU5MGI4YTNfZDZjODJhMDlfYmU0MV8xM2Y5****
x-cos-version-id: MTg0NDUxNTc1MzA5NjQ2ODI5MTg
```

#### 案例六：请求对象指定版本（启用版本控制）

#### 请求

```shell
HEAD /exampleobject?versionId=MTg0NDUxNTc1MzA5NzU4ODg1Mjg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:19:04 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542744;1586549944&q-key-time=1586542744;1586549944&q-header-list=date;host&q-url-param-list=versionid&q-signature=1307acd3e8649087c738ecca452a54fa5a79****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Date: Fri, 10 Apr 2020 18:19:04 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 18:18:53 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MGI4OThfN2RiNDBiMDlfMTk1MTBfMWZj****
x-cos-version-id: MTg0NDUxNTc1MzA5NzU4ODg1Mjg
```

#### 案例七：归档存储正在恢复中

#### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 27 Dec 2019 08:19:35 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1577434775;1577441975&q-key-time=1577434775;1577441975&q-header-list=date;host&q-url-param-list=&q-signature=72408a09a5fc00d77d389559a0cfa5c98e31****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 13
Connection: close
Date: Fri, 27 Dec 2019 08:19:35 GMT
ETag: "b62e10bcab55a88240bd9c436cffdcf9"
Last-Modified: Fri, 27 Dec 2019 08:19:23 GMT
Server: tencent-cos
x-cos-request-id: NWUwNWJlOTdfN2VjODJhMDlfOGI1N18yYjYz****
x-cos-restore: ongoing-request="true"
x-cos-restore-status: tier="expedited"; request-date="Fri, 27 Dec 2019 08:19:29 GMT"
x-cos-storage-class: ARCHIVE
```

#### 案例八：归档存储已恢复

#### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 02 Jan 2020 18:09:51 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1577988591;1577995791&q-key-time=1577988591;1577995791&q-header-list=date;host&q-url-param-list=&q-signature=ff23b3a44945f019916450add646e963c29b****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 16
Connection: close
Date: Fri, 10 Apr 2020 18:17:36 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Last-Modified: Fri, 10 Apr 2020 18:17:25 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 16749565679157681890
x-cos-request-id: NWU5MWRiZjFfMmViMDJhMDlfNjIwOF8zNTU0****
x-cos-restore: ongoing-request="false", expiry-date="Mon, 13 Apr 2020 16:00:00 GMT"
x-cos-storage-class: ARCHIVE
```
