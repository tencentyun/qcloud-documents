## 功能描述
Put Object请求可以将一个文件（Oject）上传至指定Bucket。

## 请求

### 请求语法

```Http
PUT /ObjectName HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
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
| x-cos-meta-         | 允许用户自定义的头部信息，将作为 Object 元数据返回。           | String | 否    |


#### 权限相关头部

| 名称                       | 描述                                       | 类型     | 必选   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | 允许用户自定义文件权限。<br />有效值：private，public-read | String | 否    |
| X-cos-grant-read         | 赋予被授权者读的权限<br />格式X-cos-grant-read: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| X-cos-grant-write        | 赋予被授权者写的权限<br />格式X-cos-grant-write: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| X-cos-grant-full-control | 赋予被授权者读写权限<br />格式X-cos-grant-full-control: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |

### 请求内容

文件内容

## 返回值

### 返回头部

| 名称   | 描述                                       | 类型     |
| ---- | ---------------------------------------- | ------ |
| ETag | 返回文件的 SHA-1 算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化。 | String |

### 返回内容

无返回内容