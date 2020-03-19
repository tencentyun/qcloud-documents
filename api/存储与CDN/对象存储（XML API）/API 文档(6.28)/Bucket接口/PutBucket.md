## 功能描述

PUT Bucket 接口请求可以在指定账号下创建一个存储桶。该 API 接口不支持匿名请求，您需要使用带 Authorization 签名认证的请求才能创建新的 Bucket 。创建存储桶的用户默认成为存储桶的持有者。

> ? 
>
> - 创建存储桶时，如果没有指定访问权限，则默认使用私有读写（private）权限。
> - 如需为创建的新存储桶配置多 AZ，请在请求中添加以下：
```
<CreateBucketConfiguration>
     <BucketAZConfig>MAZ|OAZ</BucketAZConfig>
</CreateBucketConfiguration>
```

## 请求

#### 请求示例

```shell
PUT / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: 0
Authorization: Auth String
```

> ? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

| 名称                     | 描述                                                         | 类型   | 是否必选 |
| ------------------------ | ------------------------------------------------------------ | ------ | -------- |
| x-cos-acl                | 定义存储桶的访问控制列表（ACL）属性。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E9.A2.84.E8.AE.BE.E7.9A.84-acl) 文档中存储桶的预设 ACL 部分，如 private，public-read 等，默认为 private | Enum   | 否       |
| x-cos-grant-read         | 赋予被授权者读取存储桶的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-write        | 赋予被授权者写入存储桶的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-read-acp     | 赋予被授权者读取存储桶的访问控制列表（ACL）和存储桶策略（Policy）的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-write-acp    | 赋予被授权者写入存储桶的访问控制列表（ACL）和存储桶策略（Policy）的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-full-control | 赋予被授权者操作存储桶的所有权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"` | string | 否       |

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口的特殊错误信息如下所述，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

| 错误码                  | 描述                               | HTTP 状态码  |
| ----------------------- | ---------------------------------- | ------------ |
| BucketAlreadyExists     | 指定的存储桶已存在                 | 409 Conflict |
| BucketAlreadyOwnedByYou | 指定的存储桶已存在且由当前帐户创建 | 409 Conflict |

## 实际案例

#### 案例一：简单案例

#### 请求

```shell
PUT / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sun, 26 May 2019 14:51:38 GMT
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558882298;1558889498&q-key-time=1558882298;1558889498&q-header-list=content-length;date;host&q-url-param-list=&q-signature=c25fd640274a6da2318935ceebfbcfba4598****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Sun, 26 May 2019 14:51:37 GMT
Server: tencent-cos
x-cos-request-id: NWNlYWE3ZjlfZDQyNzVkNjRfMzg1N18yNzFh****
```

#### 案例二：指定公有读并授权特定用户读取权限和写入对象

#### 请求

```shell
PUT / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 14 Jun 2019 13:48:59 GMT
x-cos-acl: public-read
x-cos-grant-write: id="100000000002"
x-cos-grant-read-acp: id="100000000002"
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1560520139;1560527339&q-key-time=1560520139;1560527339&q-header-list=content-length;date;host;x-cos-acl;x-cos-grant-read-acp;x-cos-grant-write&q-url-param-list=&q-signature=df03e7917270e0bf2b679bc6f99793bd0c63****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Fri, 14 Jun 2019 13:49:00 GMT
Server: tencent-cos
x-cos-request-id: NWQwM2E1Y2NfZjBhODBiMDlfOTM1YV83NDRi****
```
