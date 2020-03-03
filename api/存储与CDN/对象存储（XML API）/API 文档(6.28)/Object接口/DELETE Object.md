## 功能描述

DELETE Object 接口请求可以删除一个指定的对象（Object）。该 API 的请求者需要对存储桶有写入权限。

#### 版本控制

如需删除对象的指定版本（包括删除标记，下同），请使用 versionId 请求参数指定对应的版本 ID （包括删除标记的版本 ID，下同），此时响应将返回 x-cos-version-id 响应头部，代表该请求操作删除的版本 ID。

如未指定 versionId 请求参数：
- 当版本控制为启用时，该 DELETE 操作将创建一个删除标记作为指定对象的最新版本，此时响应将返回 x-cos-version-id 响应头部，代表该请求操作创建的删除标记的版本 ID。
- 当版本控制为暂停时，该 DELETE 操作将创建一个版本 ID 为 null 的删除标记作为指定对象的最新版本，同时删除任何已存在的版本 ID 为 null 的其他版本（如有）。

当该 DELETE 操作创建或删除了删除标记，那么将返回 x-cos-delete-marker: true 响应头部，代表该 DELETE 操作创建或删除了指定对象的删除标记。

有关版本控制的启用或暂停状态说明，请参见 [版本控制概述](https://cloud.tencent.com/document/product/436/19883)。

## 请求

#### 请求示例

```shell
DELETE /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| versionId | 指定要删除的版本 ID | string | 否 |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**版本控制相关头部**

删除启用版本控制的存储桶内的对象或对象的指定版本将返回下列响应头部：

| 名称 | 描述 | 类型 |
| --- | --- | --- |
| x-cos-version-id | 对象的版本 ID 或删除标记的版本 ID | string |
| x-cos-delete-marker | <li>当使用 versionId 请求参数指定删除标记的版本 ID 时，将返回此响应头部且值为 true，代表删除的版本 ID 对应的是一个删除标记<br><li>当未使用 versionId 请求参数，且指定对象所在的存储桶启用了版本控制时，将返回此响应头部且值为 true，代表该删除请求创建了一个删除标记作为对象的最新版本 | boolean |

#### 响应体

此接口响应体为空。

#### 错误码

此接口无特殊错误信息，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：未启用版本控制

#### 请求

```shell
DELETE /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 14 Aug 2019 11:59:40 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565783980;1565791180&q-key-time=1565783980;1565791180&q-header-list=date;host&q-url-param-list=&q-signature=75ae614a90d55054f7dea2b5cdcfdeaa1f85****
Connection: close
```

#### 响应

```shell
HTTP/1.1 204 No Content
Content-Length: 0
Connection: close
Date: Wed, 14 Aug 2019 11:59:40 GMT
Server: tencent-cos
x-cos-request-id: NWQ1M2Y3YWNfMzdiMDJhMDlfODA1Yl8xZThj****
```

#### 案例二：启用版本控制（创建删除标记）

#### 请求

```shell
DELETE /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 14 Aug 2019 12:00:21 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565784021;1565791221&q-key-time=1565784021;1565791221&q-header-list=date;host&q-url-param-list=&q-signature=f5ee3ccd55378061f1890b9a2d3dd1af94f6****
Connection: close
```

#### 响应

```shell
HTTP/1.1 204 No Content
Content-Length: 0
Connection: close
Date: Wed, 14 Aug 2019 12:00:21 GMT
Server: tencent-cos
x-cos-delete-marker: true
x-cos-request-id: NWQ1M2Y3ZDVfN2RiNDBiMDlfMmMwNmVfMTc4****
x-cos-version-id: MTg0NDUxNzgyODk2ODc1NjY0NzQ
```

#### 案例三：永久删除指定版本

#### 请求

```shell
DELETE /exampleobject?versionId=MTg0NDUxNzgyODk3MDgyMzI4NDY HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 14 Aug 2019 12:00:32 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565784032;1565791232&q-key-time=1565784032;1565791232&q-header-list=date;host&q-url-param-list=versionid&q-signature=9553e1210ba22f0725e5ff7f9bb7c8760c58****
Connection: close
```

#### 响应

```shell
HTTP/1.1 204 No Content
Content-Length: 0
Connection: close
Date: Wed, 14 Aug 2019 12:00:32 GMT
Server: tencent-cos
x-cos-request-id: NWQ1M2Y3ZTBfODhjMjJhMDlfMWNkOF8xZDZi****
x-cos-version-id: MTg0NDUxNzgyODk3MDgyMzI4NDY
```

#### 案例四：永久删除指定删除标记

#### 请求

```shell
DELETE /exampleobject?versionId=MTg0NDUxNzgyODk2ODc1NjY0NzQ HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 14 Aug 2019 12:00:42 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565784042;1565791242&q-key-time=1565784042;1565791242&q-header-list=date;host&q-url-param-list=versionid&q-signature=14e18786f25e762fb11560ea788d5e07c375****
Connection: close
```

#### 响应

```shell
HTTP/1.1 204 No Content
Content-Length: 0
Connection: close
Date: Wed, 14 Aug 2019 12:00:42 GMT
Server: tencent-cos
x-cos-delete-marker: true
x-cos-request-id: NWQ1M2Y3ZWFfNzljMDBiMDlfMjkyMDJfMWRjNjVm****
x-cos-version-id: MTg0NDUxNzgyODk2ODc1NjY0NzQ
```
