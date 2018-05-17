## 功能描述
Put Object 接口请求可以将本地的文件（Object）上传至指定 Bucket 中。该操作需要请求者对 Bucket 有 WRITE 权限。

## 请求
#### 请求语法示例

**shell:** 

```shell
# You can also use curl
curl -X PUT http://{bucket}.cos.{region}.myqcloud.com/{ObjectName} \
  -H 'Content-Length: string' \
  -H 'Content-Disposition: string' \
  -H 'Content-Encoding: string' \
  -H 'Content-Type: string' \
  -H 'Expect: string' \
  -H 'Expires: string' \
  -H 'x-cos-meta-*: string' \
  -H 'x-cos-storage-class: STANDARD' \
  -H 'Content-MD5: string' \
  -H 'x-cos-acl: public-read' \
  -H 'x-cos-grant-read: string' \
  -H 'x-cos-grant-write: string' \
  -H 'x-cos-grant-full-control: string' \
  -H 'Content-Type: */*' \
  -H 'Accept: application/xml'

```

**http:** 

```http
PUT http://{bucket}.cos.{region}.myqcloud.com/{ObjectName} HTTP/1.1
Host: 
Content-Type: */*
Accept: application/xml
Content-Length: string
Content-Disposition: string
Content-Encoding: string
Content-Type: string
Expect: string
Expires: string
x-cos-meta-*: string
x-cos-storage-class: STANDARD
Content-MD5: string
x-cos-acl: public-read
x-cos-grant-read: string
x-cos-grant-write: string
x-cos-grant-full-control: string


```

### 请求行

```
PUT /{ObjectName} HTTP/1.1
```

该 API 接口接受 `PUT` 请求。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 非公共头部


名称|类型|必选|描述
---|---|---|---
Content-Disposition|string|否|RFC 2616 中定义的文件名称，将作为 Object 元数据保存
Content-Encoding|string|否|RFC 2616 中定义的编码格式，将作为 Object 元数据保存
Expect|string|否|当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容
Expires|string|否|RFC 2616 中定义的缓存策略，将作为 Object 元数据保存
x-cos-meta-*|string|否|允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制 2KB
x-cos-storage-class|string|否|设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE，默认值：STANDARD
x-cos-acl|string|否|定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private
x-cos-grant-read|string|否|赋予被授权者读的权限。格式：x-cos-grant-read: id=" ",id=" "
x-cos-grant-write|string|否|赋予被授权者写的权限。格式：x-cos-grant-write: id=" ",id=" "
x-cos-grant-full-control|string|否|赋予被授权者读写权限。格式：x-cos-grant-full-control: id=" ",id=" "


### 请求体
请求的请求体为 Object 文件内容。
## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头


该请求操作的响应头具体数据为：

|名称|类型|描述|
|---|---|---|
|ETag|string|上传文件内容的MD5值|

### 响应体
该请求响应体为空。

### 错误码

错误码|描述|http 状态码
---|---|---
SignatureDoesNotMatch|提供的签名不符合规则，返回该错误码|403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|如果试图添加的 Object 所在的 Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
MissingContentLength|如果上传文件时，没有添加 Content-Length 头部，会返回该错误码|411 [Length Required](https://tools.ietf.org/html/rfc7231#section-6.5.10)
InvalidURI|对象 key 长度限制为 850，如果超过 850 会返回该错误|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
EntityTooLarge|如果添加的文件长度超过 5G，会返回该错误|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidDigest|如果用户上传文件时携带 Content-MD5 头部，COS 会校验 body 的 Md5 和用户携带的 MD5 是否一致，如果不一致将返回该错误|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
KeyTooLong|上传文件时携带的以 x-cos-meta 开头的自定义头部，每个自定义头部的 key 和 value 加起来不能超过 4k，否则返回该错误|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)


## 实际案例

### 请求

```
PUT /filename.jpg HTTP/1.1
Host: zuhaotestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2015 20:32:00 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484639384;32557535384&q-key-time=1484639384;32557535384&q-header-list=host&q-url-param-list=&q-signature=5c07b7c67d56497d9aacb1adc19963135b7d00dc
Content-Length: 64

[Object]
```

### 响应

```
HTTP/1.1200 OK
Content-Type: application/xml
Content-Length: 0
Date: Wed,16 Aug201711: 59: 33 GMT
Server: tencent-cos
x-cos-request-id: NTk5NDMzYTRfMjQ4OGY3Xzc3NGRfMWY=
```


