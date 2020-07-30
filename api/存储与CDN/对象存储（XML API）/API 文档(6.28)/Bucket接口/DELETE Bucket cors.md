## 功能描述

DELETE Bucket cors 请求用于删除存储桶的跨域资源共享（CORS）访问控制。

## 请求

#### 请求示例

```plaintext
DELETE /?cors HTTP/1.1
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

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
DELETE /?cors HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 09 Jul 2020 11:52:50 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1594295570;1594302770&q-key-time=1594295570;1594302770&q-header-list=date;host&q-url-param-list=cors&q-signature=1994d46c0ec515f5433016e17f0e49c72e4c****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 204 No Content
Connection: close
Date: Thu, 09 Jul 2020 11:52:50 GMT
Server: tencent-cos
x-cos-request-id: NWYwNzA1MTJfNjRiODJhMDlfMWMyMzlfMWMyNzhl****
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODczNTBmNjMwZmQ0MTZkMjg0NjlkNTYyNmY4ZTRkZTk0NzJmZTI0ZmJhYTZmZjYyNmU5ZGNlZDI5YjkyODkwYjNhYjJkOWQzYWJlOGRjYzY5N2ZlMGJhZjdlNDA4YjkzODc=
Content-Length: 0
```
