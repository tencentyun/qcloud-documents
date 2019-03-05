## 功能描述

DELETE Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）删除。该操作需要请求者对 Bucket 有 WRITE 权限。

### 细节分析

- 在 DELETE Object 请求中删除一个不存在的 Object，仍然认为是成功的，返回`204 No Content`。
- DELETE Object 要求用户对该 Object 要有写权限。

## 请求

### 请求示例
```shell
DELETE /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Authorization: Auth String
```

> Authorization: Auth String （详情请参阅 [请求签名](/document/product/436/7778) 文档）。

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。


### 请求体

该请求的请求体空。

## 响应

### 响应头
#### 公共响应头 

该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头

该请求操作无特殊的响应头。

### 响应体

该请求的响应体为空。

### 错误分析

以下描述此请求可能会发生的一些特殊的且常见的错误情况：

|错误码|HTTP状态码|描述|
|--|--|--|
| NoSuchBucket |404 Not Found|Bucket 不存在| 

获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。
## 实际案例

### 请求
```shell
DELETE /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213409;32557109409&q-key-time=1484213409;32557109409&q-header-list=host&q-url-param-list=&q-signature=1c24fe260ffe79b8603f932c4e916a6cbb0af44a
```

### 响应
```shell
HTTP /1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRjYTRfYmRjMzVfMzFhOF82MmM3Yg==
```
