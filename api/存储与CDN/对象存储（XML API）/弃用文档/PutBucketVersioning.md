## 功能描述

PUT Bucket Versioning 接口实现启用或者暂停存储桶的版本控制功能。
### 细节分析
1. 版本管理功能一经打开，只能暂停，不能关闭；
2. 可以设置版本管理状态为 Enabled 或者 Suspended，表示开启版本管理和暂停版本管理；
3. 设置版本版本管理，你需要有存储桶写权限。

## 请求

语法示例：
```
PUT /?versioning HTTP 1.1
Host: <Bucketname>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Authorization: Auth String
```
> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行

```
PUT /?versioning HTTP 1.1
```
该 API 接口接受 PUT 请求。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体

```
<VersioningConfiguration>
  <Status>Enabled</Status>
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
该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为空。
### 错误分析
以下描述此请求可能会发生的一些特殊的且常见的错误情况：

| 错误码             | HTTP状态码         |描述                                       | 
| -------------- | --------------------------------------- | -------------- |
| InvalidArgument | 400 Bad Request |如果开启版本管理的 xml body 为空，会返回 InvalidArgument  | 
| InvalidDigest   |400 Bad Request | 1. 携带的 Content-MD5 和服务端计算的请求 body 的不一致；<br>2. 开启版本管理的状态只有 Enabled 和 Suspended 两个合法值，如果写了其他状态，会返回 InvalidArgument | 

获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例
```
PUT /?versioning HTTP/1.1
Host: testbucket-1322448703.cos.cn-north.myqcloud.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Content-Type: application/xml
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9SmuG00&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versioning&q-header-list=host&q-signature=47ec2b80c73788ecd394d3b9ad90e120a32f9779
Content-Length: 83

<VersioningConfiguration>
    <Status>Enabled</Status>
</VersioningConfiguration>
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Aug 2017 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0ZThm
```
