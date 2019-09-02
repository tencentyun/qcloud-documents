## 功能描述
PUT Object acl 接口用来对某个 Bucket 中的某个的 Object 进行 ACL 表的配置，您可以通过 Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-full-control" 传入 ACL 信息，或者通过 Body 以 XML 格式传入 ACL 信息。

## 请求
#### 请求示例

```shell
PUT /<ObjectKey>?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 文档。

#### 非公共头部

<table>
   <tr>
      <th>名称</th>
      <th>描述</th>
      <th>类型</th>
      <th>必选</th>
   </tr>
   <tr>
      <td nowrap="nowrap">x-cos-acl</td>
      <td>定义 Object 的 ACL 属性，有效值：private，public-read，default，默认值：default（继承 Bucket 权限）<br>注：当前访问策略条目限制为1000条，如果您不需要进行 Object ACL 控制，请填 default 或者此项不进行设置，默认继承 Bucket 权限</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td nowrap="nowrap">x-cos-grant-read</td>
      <td>赋予被授权者读的权限，格式：x-cos-grant-read: id="[OwnerUin]"</td>
      <td>String</td>
      <td>否</td>
   </tr>
   <tr>
      <td nowrap="nowrap">x-cos-grant-full-control</td>
      <td>赋予被授权者所有的权限，格式：x-cos-grant-full-control: id="[OwnerUin]"</td>
      <td>String</td>
      <td>否</td>
   </tr>
</table>


#### 请求体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
    <DisplayName>qcs::cam::uin/100000000001:uin/100000000001</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
           <URI>http://cam.qcloud.com/groups/global/AllUsers</URI>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
        <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
        <DisplayName>qcs::cam::uin/100000000001:uin/100000000001</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
     </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:---|
| AccessControlPolicy |无| 保存 GET Object acl 结果的容器 | Container |是|

Container 节点 AccessControlPolicy 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:---|
| Owner | AccessControlPolicy | Object 持有者信息 |  Container |是|
| AccessControlList | AccessControlPolicy | 被授权者信息与权限信息 |  Container |是|

Container 节点 Owner 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:---|
| ID | AccessControlPolicy.Owner |  Object 持有者 ID</br>格式为：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; <br>如果是主帐号，&lt;OwnerUin&gt; 和 &lt;SubUin&gt; 是同一个值 |  String |是|
| DisplayName | AccessControlPolicy.Owner |  Object 持有者的名称 |  String |是|

Container 节点 AccessControlList 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:---|
| Grant | AccessControlPolicy.AccessControlList | 单个 Object 的授权信息，一个 AccessControlList 可以拥有100条 Grant | Container    |是|

Container 节点 Grant 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:---|
| Grantee | AccessControlPolicy.AccessControlList.Grant | 说明被授权者的信息，type 类型可以为 RootAccount，Subaccount<br><li>当 type 类型为 RootAccount 时，ID 中指定的是主帐号<br><li>当 type 类型为 Subaccount 时，ID 中指定的是子帐号| Container    |是|
| Permission | AccessControlPolicy.AccessControlList.Grant | 指明授予被授权者的权限信息，枚举值：READ，FULL_CONTROL  | String    |是|

Container 节点 Grantee 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |必选|
| ------------ | ------------------------------------- | --------- |:--|:---|
|URI|  AccessControlPolicy.AccessControlList.Grant.Grantee| 指定所有用户|  String |是|
| ID | AccessControlPolicy.AccessControlList.Grant.Grantee | 用户的 ID，格式为：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; <br>如果是主帐号，&lt;OwnerUin&gt; 和 &lt;SubUin&gt; 是同一个值|  String |是|
| DisplayName | AccessControlPolicy.AccessControlList.Grant.Grantee |  用户的名称 |  String |是|


## 响应
#### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 文档。

#### 特有响应头
该请求操作无特殊的响应头部信息。

#### 响应体
该请求响应体为空。

#### 错误码
该响应可能会出现如下错误码信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

<table>
   <tr>
      <th>错误码</th>
      <th>描述</th>
      <th>HTTP 状态码</th>
   </tr>
   <tr>
      <td>SignatureDoesNotMatch</td>
      <td>提供的签名不符合规则，返回该错误码</td>
			<td nowrap="nowrap">403 <a href="https://tools.ietf.org/html/rfc7231#section-6.5.3">Forbidden</a></td>
   </tr>
   <tr>
      <td>NoSuchBucket</td>
      <td>如果试图添加的规则所在的 Bucket 不存在，返回该错误码</td>
			<td nowrap="nowrap">404 <a href="https://tools.ietf.org/html/rfc7231#section-6.5.4">Not Found</a></td>
   </tr>
   <tr>
      <td>MalformedXML</td>
      <td>XML 格式不合法，请跟 Restful API 文档仔细比对</td>
			<td nowrap="nowrap">400 <a href="https://tools.ietf.org/html/rfc7231#section-6.5.1">Bad Request</a></td>
   </tr>
   <tr>
      <td>InvalidRequest</td>
      <td>请求不合法，如果错误描述中显示"header acl and body acl conflict"，表示头部和 body 不能同时设置 acl 参数</td>
			<td nowrap="nowrap">400 <a href="https://tools.ietf.org/html/rfc7231#section-6.5.1">Bad Request</a></td>
   </tr>
</table>

## 实际案例

#### 请求

```shell
PUT /exampleobject?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 25 Feb 2017 04:10:22 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484724784;32557620784&q-key-time=1484724784;32557620784&q-header-list=host&q-url-param-list=acl&q-signature=785d9075b8154119e6a075713c1b9e56ff0bddfc
Content-Length: 229
Content-Type: application/x-www-form-urlencoded

<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
    <DisplayName>qcs::cam::uin/100000000001:uin/100000000001</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
           <URI>http://cam.qcloud.com/groups/global/AllUsers</URI>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
        <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
        <DisplayName>qcs::cam::uin/100000000001:uin/100000000001</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
     </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 25 Feb 2017 04:10:22 GMT\
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw
```
