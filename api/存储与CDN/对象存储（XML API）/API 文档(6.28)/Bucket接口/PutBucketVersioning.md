## 功能描述
PUT Bucket versioning 接口实现启用或者暂停存储桶的版本控制功能。

### 细节分析

1. 如果您从未在存储桶上启用过版本控制，则 GET Bucket versioning 请求不返回版本状态值。
2. 开启版本控制功能后，只能暂停，不能关闭。
3. 设置版本控制状态值为 Enabled 或者 Suspended，表示开启版本控制和暂停版本控制。
4. 设置存储桶的版本控制功能，您需要有存储桶的写权限。

## 请求
### 请求示例

```shell
PUT /?versioning HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Authorization: Auth String
```

> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体

```shell
<VersioningConfiguration>
  <Status></Status>
</VersioningConfiguration>
```

具体的数据内容如下：

| 节点名称（关键字）                | 父节点               | 描述    | 类型   |
| --------------------------------------- | --------------------- | --------- | ------- |
| VersioningConfiguration |        无                                   |说明版本控制的具体信息    | Container    |
| Status                            |    VersioningConfiguration      | 说明版本是否开启，枚举值：Suspended\Enabled  | Enum         |

## 响应

### 响应头
#### 公共响应头 
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体为空。

### 错误分析
以下描述此请求可能会发生的一些特殊的且常见的错误情况。获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

| 错误码             | HTTP状态码         |描述                                       | 
| -------------- | --------------------------------------- | -------------- |
| InvalidArgument | 400 Bad Request |如果开启版本控制的 xml body 为空，会返回 InvalidArgument  | 
| InvalidDigest   |400 Bad Request | 1. 携带的 Content-MD5 和服务端计算的请求 body 的不一致；<br>2. 开启版本控制的状态只有 Enabled 和 Suspended 两个合法值，如果写了其他状态，会返回 InvalidArgument | 



## 实际案例
```shell
PUT /?versioning HTTP/1.1
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Content-Type: application/xml
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9Sm****&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versioning&q-header-list=host&q-signature=47ec2b80c73788ecd394d3b9ad90e120a32f****
Content-Length: 83

<VersioningConfiguration>
    <Status>Enabled</Status>
</VersioningConfiguration>
```

### 响应
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Aug 2017 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0****
```
