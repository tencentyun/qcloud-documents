## 功能描述
Append Object 接口请求可以将一个 Object（文件）以分块追加的方式上传至指定 Bucket 中。Object 属性为 Appendable 时，才能使用 Append Object 接口上传。
Object 属性可以在 Head Object 操作中查询到，发起 Head Object 请求时，会返回自定义 Header 的『x-cos-object-type』，该 Header 只有两个枚举值：Normal 或者 Appendable。通过 Append Object 操作创建的 Object 类型为 Appendable 文件；通过 Put Object 上传的 Object 是 Normal 文件。
当 Appendable 的 Object 被执行 Put Object 的请求操作以后，原 Object 被覆盖，属性改变为 Normal 。
追加上传的 Object 建议大小 1M-5G。如果 Position 的值和当前 Object 的长度不致，COS 会返回 409 错误。如果 Append 一个 Normal 属性的文件，COS 会返回 409 ObjectNotAppendable。
>**注意：**
> Appendable 的文件不可以被复制，不参与版本管理，不参与生命周期管理，不可跨区域复制。

## 请求

语法示例：
```
POST /ObjectName?append&position=*position* HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Content-Length: size
Content-Type: ContentType
Date: GMT Date
Authorization: Auth String

```

> Authorization: Auth String (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
~~~
POST /ObjectName?append&position=*position* HTTP/1.1
~~~
该 API 接口接受 POST 请求。
#### 请求参数
<style rel="stylesheet"> table th:nth-of-type(1) { width: 200px;	} </style>

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| position | 追加操作的起始点，单位：字节。<br/>首次追加 position=0，后续追加 position= 当前 Object 的 content-length| Integer| 是 |

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
**必选头部**
该请求操作的实现需要使用 Content-Length 必选头部。

|节点名称（关键字）|描述|类型|必选|
|:---|:-- |:--|:--|
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）。 | String |是 |


**推荐头部**
该请求操作的实现可以用一些推荐使用的请求头来自定义通过 Append Object 操作创建的 Object，推荐请求头内容如下：

|节点名称（关键字）|描述|类型|必选|
|:---|:-- |:--|:--|
| Cache-Control       | RFC 2616 中定义的缓存策略，将作为 Object 元数据返回。      | String | 否    |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为 Object 元数据返回。      | String | 否    |
| Content-Encoding    | RFC 2616 中定义的编码格式，将作为 Object 元数据返回。      | String | 否    |
| Content-MD5          | RFC 1864 中定义的 128-bit 内容 MD5 算法校验值。      | String | 否    |
| Content-Type        | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据返回。 | String | 否    |
| Expect              | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容。 | String | 否    |
| Expires             | RFC 2616 中定义的过期时间，将作为 Object 元数据返回。      | String | 否    |
| x-cos-content-sha1  | RFC 3174 中定义的 160-bit 内容 SHA-1 算法校验值。    | String | 否    |
| x-cos-meta-`*`        | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制 2K。    | String | 否    |

**权限相关头部**
该请求操作的实现可以用 POST 请求中的 x-cos-acl 头来设置文件访问权限。目前 Object 访问权限有三种：public-read-write，public-read和private。如果不设置，默认为 private 权限。也可以单独明确赋予用户读、写或读写权限。内容如下：
>了解更多 ACL 请求可详细请参见 [Put Bucket ACL](https://www.qcloud.com/document/product/436/7737) 文档。

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| x-cos-acl | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | String|  否 |
| x-cos-grant-read | 赋予被授权者读的权限。格式：x-cos-grant-read: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  否 |
| x-cos-grant-write| 赋予被授权者写的权限。格式：x-cos-grant-write: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" |String |  否 |
| x-cos-grant-full-control | 赋予被授权者读写权限。格式：x-cos-grant-full-control: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String|  否 |

### 请求体
该请求的请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应包含如下响应头。

| 节点名称（关键字）                       | 描述                | 类型     |
| -------------------------- | ----------------- | ------ |
| x-cos-next-append-position | 下一次追加操作的起始点，单位：字节 | String |
| x-cos-content-sha1         | 分段的校验值            | String |
| ETag                       | 文件的唯一标识           | String |

#### 响应体
该响应体返回为空。

## 实际案例

### 请求
```
POST /coss3/app?append&position=0 HTTP/1.1
Host: zuhaotestnorth-1251668577.cn-north.myqcloud.com
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
ETag: 1ce5b469b7d6600ecc2fd112e570917b
Server: tencent-cos
x-cos-content-sha1: 1ceaf73df40e531df3bfb26b4fb7cd95fb7bff1d
x-cos-next-append-position: 4096
x-cos-request-id: NTg3NzNhZGZfMmM4OGY3X2I2Zl8xMTBm

```

