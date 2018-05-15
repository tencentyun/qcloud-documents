## 功能描述 
PUT Object 接口为简单上传接口，可以将本地的小于 5 GB 的文件（Object）上传至指定 Bucket 中，大于 5 GB 的文件请使用分片接口上传（Upload Part）。该操作需要请求者对 Bucket 有 WRITE 权限。
### 细节分析
1. 需要有 Bucket 的写权限；
2. 如果请求头的 Content-Length 值小于实际请求体（body）中传输的数据长度，COS 仍将成功创建文件，但 Object 大小只等于 Content-Length 中定义的大小，其他数据将被丢弃；
3. 如果试图添加的 Object 的同名文件已经存在，那么新上传的文件，将覆盖原来的文件，成功时返回 200 OK。

## 请求

语法示例：
```
PUT /<ObjectName> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
```
PUT /<ObjectName> HTTP/1.1
```
该 API 接口接受 PUT 请求。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
**必选头部**

该请求操作需要用到如下必选请求头：<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

| 名称             | 描述                            | 类型     | 必选   |
| :------------- | :---------------------------- | :----- | :--- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节） | String | 是    |

**推荐头部**
该请求操作推荐使用如下推荐请求头：

| 名称                  | 描述                                       | 类型     | 必选   |
| :------------------ | :--------------------------------------- | :----- | :--- |
| Cache-Control       | RFC 2616 中定义的缓存策略，将作为 Object 元数据保存       | String | 否    |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为 Object 元数据保存       | String | 否    |
| Content-Encoding    | RFC 2616 中定义的编码格式，将作为 Object 元数据保存       | String | 否    |
| Content-Type        | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存 | String | 否    |
| Expect              | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容 | String | 否    |
| Expires             | RFC 2616 中定义的过期时间，将作为 Object 元数据保存       | String | 否    |
| x-cos-meta- *       | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制 2K    | String | 否    |
| x-cos-storage-class | 设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA，默认值：STANDARD | String | 否    |
| Content-MD5         | RFC 1864 中定义对消息内容（不包括头部）计算 MD5 值获得 128 比特位数字，对该数字进行 base64 编码为一个消息的 Content-MD5 值。该请求头可用于检查数据是否与发送时一致。虽然该请求头是可选的，但我们建议使用该请求头进行端到端检查 | String | 否    |

**权限相关头部**
该请求操作的实现可以用 PUT 请求中的 x-cos-acl 头来设置 Object 访问权限。有三种访问权限：public-read-write，public-read 和 private。如果不设置，默认为 private 权限。也可以单独明确赋予用户读、写或读写权限。内容如下：
>了解更多 ACL 请求可详细请参见 [PUT Bucket ACL](https://cloud.tencent.com/document/product/436/7737) 文档。

| 名称                       | 描述                                       | 类型     | 必选   |
| :----------------------- | :--------------------------------------- | :----- | :--- |
| x-cos-acl                | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | String | 否    |
| x-cos-grant-read         | 赋予被授权者读的权限。格式：x-cos-grant-read: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String | 否    |
| x-cos-grant-write        | 赋予被授权者写的权限。格式：x-cos-grant-write: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String | 否    |
| x-cos-grant-full-control | 赋予被授权者读写权限。格式：x-cos-grant-full-control: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String | 否    |

**服务端加密相关头部**

该请求操作指定腾讯云 COS 在数据存储时，应用数据加密的保护策略。腾讯云 COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用腾讯云 COS 主密钥对数据进行 AES-256 加密。如果您需要对数据启用服务端加密，则需传入以下头部：

| 名称                           | 描述                                       | 类型     | 必选     |
| ---------------------------- | ---------------------------------------- | ------ | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务端加密的方式。<br/>使用 COS 主密钥加密填写：AES256 | String | 如需加密，是 |

### 请求体

该请求的请求体为 Object 文件内容。

## 响应

### 响应头
#### 公共响应头
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该请求操作的响应头具体数据为：

| 名称   | 描述                                       | 类型     |
| :--- | :--------------------------------------- | :----- |
| ETag | 返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 在上传过程中是否有损坏 | String |

**服务端加密相关响应**

如果在上传时指定使用了服务端加密，响应头部将会包含如下信息：

| 名称                           | 描述                                       | 类型     |
| ---------------------------- | ---------------------------------------- | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务端加密的方式。<br/>使用 COS 主密钥加密：AES256 | String |

### 响应体

该响应体返回为空。
### 错误分析
以下描述此请求可能会发生的一些特殊的且常见的错误情况：

| 错误码                  | 描述                  | HTTP状态码                                  |
| -------------------- | ------------------- | ---------------------------------------- |
| InvalidDigest        | 400 Bad Request     | 如果用户上传文件时携带 Content-MD5 头部，COS 会校验 body 的 Md5 和用户携带的 MD5 是否一致，如果不一致将返回 InvalidDigest |
| KeyTooLong           | 400 Bad Request     | 上传文件时携带的以x-cos-meta开头的自定义头部，每个自定义头部的key和value加起来不能超过4k，否则返回 KeyTooLong 错误 |
| MissingContentLength | 411 Length Required | 如果上传文件时，没有添加 Content-Length 头部，会返回该错误码   |
| NoSuchBucket         | 404 Not Found       | 如果试图添加的 Object 所在的 Bucket 不存在，返回 404 Not Found 错误，错误码：NoSuchBucket |
| EntityTooLarge       | 400 Bad Request     | 如果添加的文件长度超过5G，会返回 EntityTooLarge，并返回错误信息`“Your proposed upload exceeds the maximum allowed object size”` |
| InvalidURI           | 400 Bad Request     | 对象 key 长度限制为 850，如果超过 850 会返回 InvalidURI |

获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

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
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Wed, 28 Oct 2015 20:32:00 GMT
Etag: 020df6d63448ae38a1de7924a68ba1e2
x-cos-request-id: NTg3ZGNjYTlfNDUyMDRlXzUyOTlfMjRj

```
