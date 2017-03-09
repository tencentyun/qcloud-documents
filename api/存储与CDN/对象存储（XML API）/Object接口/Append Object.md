## 功能描述
Append请求可以将一个文件（Object）以分块追加的方式上传至 Bucket 中。使用Append Upload的文件必须事前被设定为Appendable。当Appendable的文件被执行Put Object的操作以后，文件被覆盖，属性改变为Normal。

文件属性可以在Head Object操作中被查询到，当您发起Head Object请求时，会返回自定义Header『x-cos-object-type』，该Header只有两个枚举值：Normal或者Appendable。

追加上传建议文件大小1M - 5G。如果position的值和当前Object的长度不致，COS会返回409错误。如果Append一个Normal的Object，COS会返回409 ObjectNotAppendable。

Appendable的文件不可以被复制，不参与版本管理，不参与生命周期管理，不可跨区域复制。

## 请求

### 请求语法

```http
POST /ObjectName?append&position=*position* HTTP/1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Content-Length: size
Content-Type: ContentType
Date: date
Authorization: auth
```

### 请求参数

| 名称       | 描述                                       | 必选   |
| -------- | ---------------------------------------- | ---- |
| Position | 追加操作的起始点，单位：字节。首次追加Position=0，后续追加，Position=当前文件content-length | 是    |

### 请求头部

#### 必选头部

| 名称             | 描述                             | 类型     | 必选   |
| -------------- | ------------------------------ | ------ | ---- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）。 | String | 是    |

#### 推荐使用头部

| 名称                  | 描述                                       | 类型     | 必选   |
| ------------------- | ---------------------------------------- | ------ | ---- |
| Cache-Control       | RFC 2616 中定义的缓存策略，将作为 Object 元数据返回。      | String | 否    |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为 Object 元数据返回。      | String | 否    |
| Content-Encoding    | RFC 2616 中定义的编码格式，将作为 Object 元数据返回。      | String | 否    |
| Content-MD5          | RFC 1864 中定义的 128-bit 内容 MD5 算法校验值。      | String | 否    |
| Content-Type        | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据返回。 | String | 否    |
| Expect              | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容。 | String | 否    |
| Expires             | RFC 2616 中定义的过期时间，将作为 Object 元数据返回。      | String | 否    |
| x-cos-content-sha1  | RFC 3174 中定义的 160-bit 内容 SHA-1 算法校验值。    | String | 否    |
| x-cos-meta-*        | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K。    | String | 否    |

#### 权限相关头部

| 名称                       | 描述                                       | 类型     | 必选   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | 允许用户自定义文件权限。<br/ >有效值：private，public-read，public-read-write | String | 否    |
| x-cos-grant-read         | 赋予被授权者读的权限<br/>格式x-cos-grant-read: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| x-cos-grant-write        | 赋予被授权者写的权限<br/>格式x-cos-grant-write: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| x-cos-grant-full-control | 赋予被授权者读写权限<br/>格式x-cos-grant-full-control: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |

### 请求内容

追加的文件内容

## 返回值

### 返回头部

| 名称                         | 描述                | 类型     |
| -------------------------- | ----------------- | ------ |
| x-cos-next-append-position | 下一次追加操作的起始点，单位：字节 | String |
| x-cos-content-sha1         | 分段的校验值            | String |
| ETag                       | 文件的唯一标识           | String |

### 返回内容

无返回内容

## 示例

### 请求

```HTTP
POST /coss3/app?append&position=0 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1484208848;32557104848&q-key-time=1484208848;32557104848&q-header-list=host&q-url-param-list=append;position&q-signature=855fe6b833fadf20570f7f650e2120e17ce8a2fe
Content-Length: 4096

[Object]
```

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 12 16:14:24 2017
ETag: 1ce5b469b7d6600ecc2fd112e570917b
Server: tencent-cos
x-cos-content-sha1: 1ceaf73df40e531df3bfb26b4fb7cd95fb7bff1d
x-cos-next-append-position: 4096
x-cos-request-id: NTg3NzNhZGZfMmM4OGY3X2I2Zl8xMTBm
```


