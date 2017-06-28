## 功能描述
Put Bucket 接口请求可以在指定账号下创建一个 Bucket（不支持匿名访问）。该 API 接口不支持匿名请求，您需要使用帯 Authorization 签名认证的请求才能创建新的 Bucket 。创建  Bucket 的用户默认成为 Bucket 的持有者。

## 请求

语法示例：
```
PUT / HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

> Authorization:  Auth (详细参见 [访问控制](http://gggggggg) 章节)

### 请求行
~~~
PUT / HTTP/1.1
~~~
该 API 接口接受 PUT 请求。

### 请求头

**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见[公共请求头部]()章节。

**非公共头部**
该请求操作的实现可以用 Put 请求中的 x-ocs-acl 头来设置 Bucket 访问权限。目前 Bucket 有三种访问权限：public-read-write，public-read和private。如果不设置，默认为 private 权限。也可以单独明确赋予用户读、写或读写权限。内容如下：

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| x-cos-acl | 设置 Bucket 访问权限。有效值：private，public-read-write，public-read；默认值：private | String|  否 |
| x-cos-grant-read | 赋予被授权者读的权限。格式：x-cos-grant-read: uin=" ",uin=" "；</br> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String |  否 |
| x-cos-grant-write| 赋予被授权者写的权限。格式：x-cos-grant-write: uin=" ",uin=" "；</br>当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" |String |  否 |
| x-cos-grant-full-control | 赋予被授权者读写权限。格式：x-cos-grant-full-control: uin=" ",uin=" "；</br>当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String|  否 |

### 请求体
该请求的请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见[公共响应头部]()章节。
**特有响应头**
该响应无特殊有响应头。
#### 响应体
该响应体返回为空。

## 实际案例

### 请求
```
PUT / HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484708728;32557604728&q-key-time=1484708728;32557604728&q-header-list=host&q-url-param-list=&q-signature=b394a86624cbcc705b11bc6fc505843c5e2dd9c9
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed Jan 18 11:05:42 2017 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZWRiODJfOWIxZjRlXzZmNDBfMTUz

```

