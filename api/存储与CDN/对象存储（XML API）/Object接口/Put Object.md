## 功能描述
Put Object请求可以将一个文件（Oject）上传至指定Bucket。

## 请求

### 请求语法

```Http
PUT /ObjectName HTTP/1.1
Host:<BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Authorization: authorization string
```

### 请求参数

无特殊请求参数

### 请求头部

#### 必选头部

| 名称             | 描述                             | 类型     | 必选   |
| -------------- | ------------------------------ | ------ | ---- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）。 | String | 是    |

#### 推荐使用头部

| 名称                  | 描述                                       | 类型     | 必选   |
| ------------------- | ---------------------------------------- | ------ | ---- |
| Cache-Control       | RFC 2616 中定义的缓存策略，将作为 Object 元数据保存。      | String | 否    |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为 Object 元数据保存。      | String | 否    |
| Content-Encoding    | RFC 2616 中定义的编码格式，将作为 Object 元数据保存。      | String | 否    |
| Content-Type        | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存。 | String | 否    |
| Expect              | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容。 | String | 否    |
| Expires             | RFC 2616 中定义的过期时间，将作为 Object 元数据保存。      | String | 否    |
| x-cos-content-sha1  | RFC 3174 中定义的 160-bit 内容 SHA-1 算法校验值。    | String | 否    |
| x-cos-meta-*        | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K。    | String | 否    |
| x-cos-storage-class | 设置Object的存储级别，枚举值：Standard，Standard_IA，Nearline，默认值：Standard（目前只支持华南园区） | String | 否    |


#### 权限相关头部

| 名称                       | 描述                                       | 类型     | 必选   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | 允许用户自定义文件权限。<br />有效值：private，public-read | String | 否    |
| x-cos-grant-read         | 赋予被授权者读的权限<br />格式x-cos-grant-read: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| x-cos-grant-write        | 赋予被授权者写的权限<br />格式x-cos-grant-write: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| x-cos-grant-full-control | 赋予被授权者读写权限<br />格式x-cos-grant-full-control: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |

### 请求内容

文件内容

## 返回值

### 返回头部

| 名称   | 描述                                       | 类型     |
| ---- | ---------------------------------------- | ------ |
| ETag | 返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化。 | String |

### 返回内容

无返回内容

## 示例

### 请求

```HTTP
PUT /ObjectName HTTP/1.1
Host:zuhaotestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484639384;32557535384&q-key-time=1484639384;32557535384&q-header-list=host&q-url-param-list=&q-signature=5c07b7c67d56497d9aacb1adc19963135b7d00dc
Content-Length: 64

[Object]
```

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Tue Jan 17 15:50:02 2017
Etag: 020df6d63448ae38a1de7924a68ba1e2
x-cos-request-id: NTg3ZGNjYTlfNDUyMDRlXzUyOTlfMjRj
```

