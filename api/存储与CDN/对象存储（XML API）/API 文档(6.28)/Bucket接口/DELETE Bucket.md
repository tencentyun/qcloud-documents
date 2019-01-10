## 功能描述
DELETE Bucket 请求用于在指定账号下删除 Bucket。
>!删除存储桶前，请确保存储桶内的数据和未完成上传的分块数据已全部清空，否则会无法删除存储桶。

## 请求
### 请求示例
```
DELETE / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体为空。

### 错误分析
以下是此请求可能会发生的一些特殊的且常见的错误情况。如需获取更多关于 COS 的错误码的信息，请查阅 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

|错误码|HTTP 状态码|描述|
|-------|------|------|
|BucketNotEmpty|409 Conflict|不能删除一个非空的 Bucket|
|AccessDenied|403 Forbidden|删除 Bucket 同样需要携带签名，如果试图删除一个没有访问权限的 Bucket，就会返回该错误|
|NoSuchBucket|404 Not Found|如果删除一个不存在的 Bucket，就回返回该错误|


## 实际案例

### 请求
```
DELETE / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484708950;32557604950&q-key-time=1484708950;32557604950&q-header-list=host&q-url-param-list=&q-signature=2b27b72ad2540ff2dde341dc7579a66ee8cb2afc
```

### 响应
```
HTTP/1.1 204 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZWRjNjBfOTgxZjRlXzZhYjlfMTg0
```
