## 功能描述
PUT Object acl 接口用来对某个 Bucket 中的某个的 Object 进行 ACL 表的配置，您可以通过 Header:"x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"，"x-cos-grant-full-control" 传入 ACL 信息，或者通过 Body 以 XML 格式传入 ACL 信息。

>**注意：**
>- Header 和 Body 只能选择其中一种，否则响应返回会冲突。
>- PUT Object acl 是一个覆盖操作，传入新的 ACL 将覆盖原有 ACL。
>- 只有 Bucket 持有者才有权操作。


### 版本

启用多版本情况下，PUT 操作将为当前版本对象设置 ACL。要设置不同版本的 ACL，请使用 versionId 子资源。


### 细节分析
1. 既可以通过头部设置，也可以通过 xml body 设置，只使用一种方法。
2. ACL 策略数上限1000，建议用户不要每个上传文件都设置 ACL。
3. 把文件夹设置成私有后，给该文件夹下的文件及文件夹设置公有属性，不会生效。

## 请求
请求示例:
```
PUT /{ObjectName}/?acl HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String

<AccessControlPolicy>
```
> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行

```
PUT /{ObjectName}/?acl HTTP/1.1
```

该 API 接口接受 `PUT` 请求。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 非公共头部


名称|类型|必选|描述
---|---|---|---
x-cos-acl|string|否|定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read。
x-cos-grant-read|string|否|赋予被授权者读的权限。格式：x-cos-grant-read: id=" ",id=" "；当需要给子账户授权时， id = "qcs::cam::uin/<OwnerUin>:uin/<SubUin>"，当需要给根账户授权时， id = "qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
x-cos-grant-write|string|否|赋予被授权者写的权限。格式：x-cos-grant-write: id=" ",id=" "；当需要给子账户授权时， id = "qcs::cam::uin/<OwnerUin>:uin/<SubUin>"，当需要给根账户授权时， id = "qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
x-cos-grant-full-control|string|否|赋予被授权者写的权限。格式：x-cos-grant-full-control: id=" ",id=" "；当需要给子账户授权时， id = "qcs::cam::uin/<OwnerUin>:uin/<SubUin>"，当需要给根账户授权时， id = "qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"


### 请求体
请求的请求体为 ACL 配置规则。
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<AccessControlPolicy/>
```


具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
AccessControlPolicy|无|保存 GET Bucket acl 结果的容器|Container|是



## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头
名称|类型|必选|描述
---|---|---|---
x-cos-version-id|string|否|当启用多版本时，将返回正在设置ACL 的对象版本。

### 响应体
该请求响应体为空。

### 错误码

错误码|描述|HTTP 状态码
---|---|---
SignatureDoesNotMatch|提供的签名不符合规则，返回该错误码|403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|如果试图添加的规则所在的 Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
MalformedXML|XML 格式不合法，请跟 Restful API 文档仔细比对|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidRequest|请求不合法，如果错误描述中显示"header acl and body acl conflict"，那么表示不能头部和 body 都有 acl 参数。|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)


## 实际案例

### 请求

```
PUT /test?acl HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 25 Feb 2017 04:10:22 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484724784;32557620784&q-key-time=1484724784;32557620784&q-header-list=host&q-url-param-list=acl&q-signature=785d9075b8154119e6a075713c1b9e56ff0bddfc
Content-Length: 229
Content-Type: application/x-www-form-urlencoded

<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/12345:uin/12345</ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:type=\"CanonicalUser\">
        <ID>qcs::cam::uin/12345:uin/12345</ID>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:type=\"Group\">
        <URI>http://cam.qcloud.com/groups/global/AllUsers</URI>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

### 响应:

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 25 Feb 2017 04:10:22 GMT\
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw
```


