## 功能描述
Append Object 接口请求可以将一个对象以分块追加的方式上传至指定存储桶中。对象首次使用 Append Object 接口上传时，该对象的属性自动为 appendable ，使用其他接口上传时则属性自动为 normal （如果该对象已存在则属性会被覆盖为 normal），可以使用 Get Object 或 Head Object 接口获取 x-cos-object-type 响应头来判断对象属性。对象属性为 appendable 时才能使用本接口追加上传。
追加上传的对象每个分块最小为 4 KB， 建议大小 1 MB ~ 5 GB。 如果 Position 的值和当前对象的长度不一致， COS 会返回 409 错误。 如果追加一个 normal 属性的文件， COS 会返回 409 ObjectNotAppendable。 

## 请求
### 请求示例

**shell:** 

```shell
# You can also use curl
curl -X POST http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?append&position={position} \
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
POST http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?append&position={position} HTTP/1.1
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
POST /{ObjectName}?append&position={position} HTTP/1.1
```

该 API 接口接受 `POST` 请求。


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
x-cos-meta-*|string|否|允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制 2K
x-cos-storage-class|string|否|设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE，默认值：STANDARD
x-cos-acl|string|否|定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private
x-cos-grant-read|string|否|赋予被授权者读的权限。格式：x-cos-grant-read: id=" ",id=" "
x-cos-grant-write|string|否|赋予被授权者写的权限。格式：x-cos-grant-write: id=" ",id=" "
x-cos-grant-full-control|string|否|赋予被授权者读写权限。格式：x-cos-grant-full-control: id=" ",id=" "


### 请求体
请求的请求体为追加的 Object 文件内容。
## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详情，参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头

该请求操作的响应头具体数据为：

|名称|类型|描述|
|---|---|---|
|ETag|string|上传文件内容的 MD5 值|
|x-cos-next-append-position|string|下一次追加操作的起始点，单位：字节|


### 响应体
该请求响应体为空。

### 错误码

错误码|描述|http 状态码
---|---|---
InvalidArgument|如果请求中未携带 position 参数，会返回 400 Bad Request|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
SignatureDoesNotMatch|提供的签名不符合规则，返回该错误码|403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
InvalidObjectState|如果对一个非 appendable 的文件进行 append 操作，那么会返回 409 Confilct|409 [Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)
MissingContentLength|如果追加文件时，没有添加 Content-Length 头部，会返回该错误码|411 [Length Required](https://tools.ietf.org/html/rfc7231#section-6.5.10)
InvalidURI|对象 key 长度限制为 850，如果超过 850 会返回该错误|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)


## 实际案例

### 请求

```
POST /coss3/app?append&position=0 HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Tue, 16 Jan 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1484208848;32557104848&q-key-time=1484208848;32557104848&q-header-list=host&q-url-param-list=append;position&q-signature=855fe6b833fadf20570f7f650e2120e17ce8a2fe
Content-Length: 4096

[Object]
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Tue, 16 Jan 2016 21:32:00 GMT
ETag: \"1ce5b469b7d6600ecc2fd112e570917b\"
Server: tencent-cos
x-cos-content-sha1: 1ceaf73df40e531df3bfb26b4fb7cd95fb7bff1d
x-cos-next-append-position: 4096
x-cos-request-id: NTg3NzNhZGZfMmM4OGY3X2I2Zl8xMTBm
```
