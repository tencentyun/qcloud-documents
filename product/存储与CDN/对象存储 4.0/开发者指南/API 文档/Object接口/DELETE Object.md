## 功能描述

DELETE Object 接口请求可以实现删除存储桶中的某个对象。该操作需要用户对存储桶有写权限。

### 版本
如存储桶启用了多版本功能，要删除特定版本，您需要指定被删除对象的版本 ID。否则将不删除对象。

### 细节分析

- 在 DELETE Object 请求中删除一个不存在的对象，将返回 `204 No Content`。
- DELETE Object 要求用户对该对象要有写权限。

## 请求

语法示例：
```
DELETE /ObjectName HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](/document/product/436/7778) 章节)

### 请求行
```
DELETE /ObjectName HTTP/1.1
```
该 API 接口接受 DELETE 请求。

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部

该请求操作无特殊的请求头部信息。


### 请求体

该请求的请求体空。

## 响应

### 响应头
#### 公共响应头 

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头

|名称|类型|描述|
|---|---|---|
|x-cos-delete-marker|Boolean|判断是否创建了删除标记，如是则返回 true,否则 false。|
|x-cos-version-id|string|如果不指定版本 ID 操作，将返回创建删除标记的版本 id，否则返回被删除对象的版本 ID。|

### 响应体

该请求的响应体为空。

### 错误分析

以下描述此请求可能会发生的一些特殊的且常见的错误情况：

|错误码|HTTP状态码|描述|
|--|--|--|
| NoSuchBucket |404 Not Found|Bucket 不存在| 

获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。
## 实际案例

### 请求 1
```
DELETE /123 HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213409;32557109409&q-key-time=1484213409;32557109409&q-header-list=host&q-url-param-list=&q-signature=1c24fe260ffe79b8603f932c4e916a6cbb0af44a

```

### 响应 1
```
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRjYTRfYmRjMzVfMzFhOF82MmM3Yg==

```

### 请求 2 永久删除指定版本的对象

```
DELETE /123 ?versionId=UIORUnfndfiufdisojhr398493jfdkjFJjkndnqUifhnw89493jJFJ HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213409;32557109409&q-key-time=1484213409;32557109409&q-header-list=host&q-url-param-list=&q-signature=1c24fe260ffe79b8603f932c4e916a6cbb0af44a

```

### 响应 2

```
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRjYTRfYmRjMzVfMzFhOF82MmM3Yg==
x-cos-version-id: UIORUnfndfiufdisojhr398493jfdkjFJjkndnqUifhnw89493jJFJ

```