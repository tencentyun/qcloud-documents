## 功能描述
PUT Object acl 接口用来对某个存储桶中的某个的对象进行 ACL 表的配置，您可以通过 Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"，"x-cos-grant-full-control" 传入 ACL 信息，或者通过 Body 以 XML 格式传入 ACL 信息。
>**注意：**
>Header 和 Body 只能选择其中一种，否则响应返回会冲突。
>PUT Object acl 是一个覆盖操作，传入新的 ACL 将覆盖原有 ACL。
>只有 Bucket 持有者才有权操作。

---
### 版本

对象的 ACL 被设置为对象版本级别。默认情况下，PUT 操作为当前版本对象设置 ACL。要设置不同版本的 ACL，请使用 versionId 子资源。

---
### 细节分析
1. 既可以通过头部设置，也可以通过 xml body 设置，只使用一种方法。
2. ACL策略数上限1000，建议用户不要每个上传文件都设置 ACL。
3. 把文件夹设置成私有后，给该文件夹下的文件及文件夹设置公有属性，不会生效。

## 请求

语法示例：
```
PUT /ObjectName?acl HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-MD5: MD5
x-cos-acl: [对应权限]
x-cos-grant-read: id="",id=""
x-cos-grant-write: id="",id=""
x-cos-grant-full-control: id="",id=""
Authorization: Auth String
```
> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
~~~
PUT /ObjectName?acl HTTP/1.1
~~~
该 API 接口接受 PUT 请求。
### 请求头

**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

**非公共头部**
该请求操作的实现可以用 PUT 请求中的 x-cos-acl 头来设置 Object 访问权限。目前 Object 有三种访问权限：public-read-write，public-read 和 private。如果不设置，默认为 private 权限。也可以单独明确赋予用户读、写或读写权限。内容如下：
<style  rel="stylesheet"> table th:nth-of-type(1) {width: 200px;	}</style>

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| x-cos-acl | 定义 Object 的 ACL 属性。有效值：private，public-read-write，public-read；默认值：private | String|  否 |
| x-cos-grant-read | 赋予被授权者读的权限。格式：x-cos-grant-read: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  否 |
| x-cos-grant-write| 赋予被授权者写的权限。格式：x-cos-grant-write: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" |String |  否 |
| x-cos-grant-full-control | 赋予被授权者读写权限。格式：x-cos-grant-full-control: id=" ",id=" "；<br/>当需要给子账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"，<br/>当需要给根账户授权时，id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String|  否 |

### 请求体
该请求操作的实现也可以在请求体中帯特定请求参数来设置 Object 访问权限，但请求体帯参数方式和请求头帯 ObjectName?acl 子资源方式两者只能选一种。
帯所有节点的示例：
```
<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/<OwnerUin>:uin/<SubUin></ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
      <ID>qcs::cam::uin/<OwnerUin>:uin/<SubUin></ID>
      </Grantee>
      <Permission></Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::uin/<OwnerUin>:uin/<SubUin></ID>
      </Grantee>
      <Permission></Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```
具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| AccessControlPolicy |无| 保存 Get Object ACL 结果的容器 | Container |是|

Container 节点 AccessControlPolicy 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| Owner | AccessControlPolicy | Object 资源持有者信息 |  Container |是|
| AccessControlList | AccessControlPolicy | 被授权者信息与权限信息 |  Container |是|

Container 节点 Owner 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| ID | AccessControlPolicy.Owner |  Object 资源持有者 ID，</br>格式：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; 如果是根帐号，&lt;OwnerUin&gt; 和 &lt;SubUin&gt; 是同一个值 |  String |是|

Container 节点 AccessControlList 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:--|
| Grant | AccessControlPolicy.AccessControlList | 单个 Object 资源的授权信息。一个 AccessControlList 可以拥有 100 条 Grant | Container    |是|

Container 节点 Grant 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:--|
| Grantee | AccessControlPolicy.AccessControlList.Grant | 说明被授权者的信息。type 类型可以为 RootAccount， Subaccount；</br>当 type 类型为 RootAccount 时，在 ID 中指定根帐号;</br>当 type 类型为 Subaccount 时，在 ID 中指定子帐号  | Container    |是|
| Permission | AccessControlPolicy.AccessControlList.Grant | 指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL  | String    |是|

Container 节点 Grantee 的内容：<style  rel="stylesheet"> table th:nth-of-type(1) {width: 200px;	}</style>

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:--|
| ID | AccessControlPolicy.AccessControlList.Grant.Grantee | 用户的 ID，如果是根帐号，格式为：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt; 或 qcs::cam::anyone:anyone （指代所有用户）;如果是子帐号，格式为：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;|  String |是|


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

|错误码|HTTP状态码|描述|
|--|--|--|
|InvalidDigest|400 Bad Request|用户带的 Content-MD5 和 COS 计算 body 的 Content-MD5 不一致|
|MalformedXML|400 Bad Request|传入的 xml 格式有误，请跟 restful api 文档仔细比对|
|InvalidArgument|400 Bad Request|参数错误，具体可以参考错误信息|
|NoSuchKey|404 Not Found| Object 不存在|

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。
## 实际案例

### 请求
```
PUT /ObjectName?acl HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 25 Feb 2015 04:10:22 GMT 
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484724784;32557620784&q-key-time=1484724784;32557620784&q-header-list=host&q-url-param-list=acl&q-signature=785d9075b8154119e6a075713c1b9e56ff0bddfc
Content-Length: 229
Content-Type: application/x-www-form-urlencoded

<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/12345:uin/12345</ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::uin/12345:uin/12345</ID>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::anyone:anyone</ID>
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
Date: Fri, 25 Feb 2015 04:10:22 GMT 
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw

```
