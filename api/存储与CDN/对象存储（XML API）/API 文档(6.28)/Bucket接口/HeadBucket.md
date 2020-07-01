## 功能描述

HEAD Bucket 请求可以确认该存储桶是否存在，是否有权限访问。有以下几种情况：

- 存储桶存在且有读取权限，返回 HTTP 状态码为200。
- 无存储桶读取权限，返回 HTTP 状态码为403。
- 存储桶不存在，返回 HTTP 状态码为404。

## 请求

#### 请求示例

```plaintext
HEAD / HTTP/1.1
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

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

| 名称                 | 描述                                                         | 类型 |
| -------------------- | ------------------------------------------------------------ | ---- |
| x-cos-bucket-az-type | 存储桶 AZ 类型，当存储桶为多 AZ 存储桶时返回此头部，值固定为 MAZ。 | Enum |
| x-cos-bucket-region  | 存储桶所在地域。枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 文档，例如 ap-beijing，ap-hongkong，eu-frankfurt 等 | Enum |

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：单 AZ 存储桶

#### 请求

```plaintext
HEAD / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 28 May 2019 03:16:12 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1559013372;1559020572&q-key-time=1559013372;1559020572&q-header-list=date;host&q-url-param-list=&q-signature=9085930afacf1e8a0ade2697b69353b27901****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: close
Date: Tue, 28 May 2019 03:16:12 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWNlY2E3ZmNfZjhjMDBiMDlfMTBjOWRfZDcz****
```

#### 案例二：多 AZ 存储桶

#### 请求

```plaintext
HEAD / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 04 Jun 2020 06:43:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1591252983;1591260183&q-key-time=1591252983;1591260183&q-header-list=date;host&q-url-param-list=&q-signature=aa996608fe79d122ed9667d9db3caa262ed6****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: close
Date: Thu, 04 Jun 2020 06:43:03 GMT
Server: tencent-cos
x-cos-bucket-az-type: MAZ
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWVkODk3ZjdfZjI4NWQ2NF9hODhkXzRhNmQ0****
```
