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

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| versionId | 当启用版本控制时，指定要查询的版本 ID，如不指定则查询对象的最新版本 | string | 否 |

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| If-Modified-Since | 当对象在指定时间后被修改，则返回 HTTP 状态码为200（OK），否则返回 HTTP 状态码为304（Not Modified） | string | 否 |
| If-Unmodified-Since | 当对象在指定时间后未被修改，则返回 HTTP 状态码为200（OK），否则返回 HTTP 状态码为412（Precondition Failed） | string | 否 |
| If-Match | 当对象的 ETag 与指定的值一致，则返回 HTTP 状态码为200（OK），否则返回 HTTP 状态码为412（Precondition Failed） | string | 否 |
| If-None-Match | 当对象的 ETag 与指定的值不一致，则返回 HTTP 状态码为200（OK），否则返回 HTTP 状态码为304（Not Modified） | string | 否 |

**服务端加密相关头部**

如果指定的对象使用了服务端加密且加密方式为 SSE-C 时，则需要指定服务端加密的相关头部来解密对象，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7728#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述 | 类型 |
| --- | --- | --- |
| Cache-Control | RFC 2616 中定义的缓存指令，仅当对象元数据包含此项时才会返回该头部 | string |
| Content-Disposition | RFC 2616 中定义的文件名称，仅当对象元数据包含此项时才会返回该头部 | string |
| Content-Encoding | RFC 2616 中定义的编码格式，仅当对象元数据包含此项时才会返回该头部 | string |
| Expires | RFC 2616 中定义的缓存失效时间，仅当对象元数据包含此项时才会返回该头部 | string |
| x-cos-meta-\* | 包括用户自定义元数据头部后缀和用户自定义元数据信息 | string |
| x-cos-storage-class | 对象存储类型，枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 STANDARD_IA，ARCHIVE。仅当对象不是标准存储（STANDARD）时才会返回该头部 | Enum |

#### 归档类型对象相关头部

当对象为归档类型且使用 POST Object restore 请求进行恢复操作时，该 HEAD 请求将返回下列响应头部：

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述 | 类型 |
| --- | --- | --- |
| x-cos-restore | 指示当前恢复操作的状态：<br><li>当恢复操作正在进行中时，该响应头部的值为`ongoing-request="true"`<li>当对象已经恢复时，该响应头部包含 COS 即将删除临时副本的时间，例如`ongoing-request="false", expiry-date="Tue, 19 Nov 2019 16:00:00 GMT"` | string
| x-cos-restore-status | 当恢复操作正在进行中时返回该响应头部，指示当前的恢复模式和恢复操作请求时间，例如`tier="bulk"; request-date="Mon, 18 Nov 2019 09:34:50 GMT"`，有关恢复模式请参见 [POST Object restore](https://cloud.tencent.com/document/product/436/12633#.E8.AF.B7.E6.B1.82) | string

**版本控制相关头部**

启用版本控制的存储桶内的对象将返回下列响应头部：

| 名称 | 描述 | 类型 |
| --- | --- | --- |
| x-cos-version-id | 对象的版本 ID | string |

**服务端加密相关头部**

如果指定的对象使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

此接口响应体为空。

#### 错误码

此接口无特殊错误信息，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 09 Aug 2019 10:21:01 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565346061;1565353261&q-key-time=1565346061;1565353261&q-header-list=date;host&q-url-param-list=&q-signature=82f401cf54cd6ad0331d1c0b8c827bf8f2f9****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 13
Connection: close
Date: Fri, 09 Aug 2019 10:21:01 GMT
ETag: "b62e10bcab55a88240bd9c436cffdcf9"
Last-Modified: Fri, 09 Aug 2019 10:20:56 GMT
Server: tencent-cos
x-cos-request-id: NWQ0ZDQ5MGRfNmRjMDJhMDlfOThjMl8xNzE2****
```
