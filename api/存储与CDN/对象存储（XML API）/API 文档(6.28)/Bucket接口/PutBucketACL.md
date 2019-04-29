## 功能描述
PUT Bucket acl 接口用来写入 Bucket 的 acl 表，您可以通过 Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-full-control" 传入 acl 信息，或者通过 Body 以 XML 格式传入 acl 信息。

>!
>- Header 和 Body 只能选择其中一种，否则响应返回会冲突。
>- PUT Bucket acl 是一个覆盖操作，传入新的 acl 将覆盖原有 acl。
>- 只有 Bucket 创建者才有权限操作。

### 细节分析
1. 既可以通过头部设置，也可以通过 xml body 设置，建议只使用一种方法。
2. 私有 Bucket 可以给某个文件夹设置为公开，那么该文件夹下的文件都为公开；但是把文件夹设置成私有后，在该文件夹中设置的公开属性，不会生效。

## 请求
### 请求示例

```
PUT /?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
>Authorization: Auth String (详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档)


### 请求头

**公共头部**
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

**非公共头部** 
该请求操作的实现可以用 PUT 请求中的 x-cos-acl 头来设置 Bucket 访问权限。目前 Bucket 有三种访问权限：public-read-write，public-read 和 private。如果不设置，默认为 private 权限，也可以单独明确赋予用户读、写或读写权限。内容如下：

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| x-cos-acl | 定义 Bucket 的 acl 属性。有效值： private，public-read-write，public-read ；默认值：private | String|  否 |
| x-cos-grant-read |赋予被授权者读的权限。格式：x-cos-grant-read: id="[OwnerUin]" | String |  否 |
| x-cos-grant-write| 赋予被授权者写的权限。格式：x-cos-grant-write: id="[OwnerUin]" |String |  否 |
| x-cos-grant-full-control | 赋予被授权者所有的权限。格式：x-cos-grant-full-control: id="[OwnerUin]" | String|  否 |

### 请求体
该请求操作的实现也可以在请求体中带特定请求参数来设置 Bucket 访问权限，但请求体带参数方式和请求头带 acl 子资源方式两者只能选一种。
带所有节点的示例：
```
<AccessControlPolicy>
  <Owner>
      <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee>
      <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee>
      <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```
具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| AccessControlPolicy |无| 保存 GET Bucket acl 结果的容器 | Container |是|

Container 节点 AccessControlPolicy 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| Owner | AccessControlPolicy | Bucket 持有者信息 |  Container |是|
| AccessControlList | AccessControlPolicy | 被授权者信息与权限信息 |  Container |是|

Container 节点 Owner 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| ID | AccessControlPolicy.Owner | Bucket 持有者的 ID，</br>格式：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; 如果是主帐号，&lt;OwnerUin&gt; 和 &lt;SubUin&gt; 是同一个值 |  String |是|

Container 节点 AccessControlList 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:--|
| Grant | AccessControlPolicy.AccessControlList | 单个 Bucket 的授权信息，一个 AccessControlList 可以拥有100条 Grant | Container    |是|

Container 节点 Grant 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:--|
| Grantee | AccessControlPolicy.AccessControlList.Grant | 被授权者资源信息。type 类型可以为 RootAccount， SubAccount；</br>当 type 类型为 RootAccount 时，可以在 uin 中填写 QQ，可以在 ID 中 uin 填写 QQ，也可以用 anyone（指代所有类型用户）代替 uin/&lt;OwnerUin&gt; 和 uin/&lt;SubUin&gt;。</br>当 type 类型为 RootAccount 时，uin 代表主账号，Subaccount 代表子账号 | Container    |是|
| Permission | AccessControlPolicy.AccessControlList.Grant | 指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL  | String    |是|

Container 节点 Grantee 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:--|
| ID | AccessControlPolicy.AccessControlList.Grant.Grantee | 用户的 ID，</br>格式：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; 如果是主帐号，&lt;OwnerUin&gt; 和 &lt;SubUin&gt; 是同一个值 |  String |是|


## 响应

### 响应头
#### 公共响应头
该响应使用公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该响应无特殊的响应头。
### 响应体
该响应体返回为空。

### 错误分析
以下描述此请求可能会发生的一些特殊的且常见的错误情况：

|错误码|描述|HTTP 状态码|
|------|------|------|
|InvalidDigest|400 Bad Request|用户带的 Content-MD5 和 COS 计算 body 的 Content-MD5 不一致|
|MalformedXML|400 Bad Request|传入的 xml 格式有误，请跟 restful api 文档仔细比对|
|InvalidArgument|400 Bad Request|参数错误，具体可以参考错误信息|

## 实际案例

### 请求
```
PUT /?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 25 Feb 2017 04:10:22 GMT 
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484724784;32557620784&q-key-time=1484724784;32557620784&q-header-list=host&q-url-param-list=acl&q-signature=785d9075b8154119e6a075713c1b9e56ff0bddfc
Content-Length: 229
Content-Type: application/x-www-form-urlencoded

<AccessControlPolicy>
  <Owner>
      <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee>
      <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee>
      <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 25 Feb 2017 04:10:22 GMT 
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw

```

