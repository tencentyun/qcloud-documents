## 功能描述
PUT Bucket 接口请求可以在指定账号下创建一个 Bucket。该 API 接口不支持匿名请求，您需要使用帯 Authorization 签名认证的请求才能创建新的 Bucket 。创建  Bucket 的用户默认成为 Bucket 的持有者。
### 细节分析
1. 创建 Bucket 时，如果没有指定访问权限，则默认使用私有读写（private）权限。

## 请求

语法示例：
```
PUT / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
~~~
PUT / HTTP/1.1
~~~
该 API 接口接受 PUT 请求。

### 请求头

**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

**非公共头部**
该请求操作的实现可以用 PUT 请求中的 x-cos-acl 头来设置 Bucket 访问权限。目前有三种 Bucket 的访问权限：public-read-write，public-read 和 private。如果不设置，默认为 private 权限。也可以单独明确赋予用户读、写或读写权限。内容如下：
>了解更多 acl 请求可详细请参见 [Put Bucket ACL](https://cloud.tencent.com/document/product/436/7737) 文档。

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| x-cos-acl | 定义 Object 的 acl 属性。有效值：private，public-read-write，public-read；默认值：private | String|  否 |
| x-cos-grant-read | 赋予被授权者读的权限。格式：x-cos-grant-read: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  否 |
| x-cos-grant-write| 赋予被授权者写的权限。格式：x-cos-grant-write: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" |String |  否 |
| x-cos-grant-full-control | 赋予被授权者读写权限。格式：x-cos-grant-full-control: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String|  否 |

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。
### 响应体
该响应体返回为空。
### 错误分析
以下描述此请求可能会发生的一些特殊的且常见的错误情况：

|错误码|HTTP 状态码|描述|
|--------|--------|--------------|
| BucketAlreadyExists |409 Conflict|当请求创建的 Bucket 已经存在，并且请求创建的用户就是拥有者| 
| InvalidBucketName | 400 Bad Request|Bucket 的命名不规范 具体原因可参考 message 的描述|
| InvalidRequest | 400 Bad Request|Bucket 的命名不规范 具体原因可参考 message 的描述| 
如果 Bucket 设置的 ACL 不正确，也会导致创建 Bucket 失败，同时会返回 “Failed to set access control authority for the bucket” 的错误信息。具体错误原因，可根据返回的错误码参考 [Put Bucket ACL](https://cloud.tencent.com/document/product/436/7737) 相关的文档

获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求
```
PUT / HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Thu, 12 Jan 2016 19:12:22 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484708728;32557604728&q-key-time=1484708728;32557604728&q-header-list=host&q-url-param-list=&q-signature=b394a86624cbcc705b11bc6fc505843c5e2dd9c9
```

### 响应
```
HTTP /1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu, 12 Jan 2016 19:12:22 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZWRiODJfOWIxZjRlXzZmNDBfMTUz

```

