## 功能描述
GET Object acl 接口用来获取某个存储桶下的某个对象的访问权限，只有存储桶的持有者才有权限操作。

### 版本
默认情况下，该 GET 操作返回对象的当前版本。您如果需要返回不同的版本，请使用 versionId 子资源。

## 请求
### 请求示例
```shell
GET /<ObjectKey>?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
>Authorization: Auth String (详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档)。

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部
**必选头部**
该请求操作的实现使用如下必选头部：

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| Authorization | 签名串 |String| 是 |

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该响应无特殊的响应头。
### 响应体
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

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| AccessControlPolicy |无| 保存 GET Object acl 结果的容器 | Container |

Container 节点 AccessControlPolicy 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Owner | AccessControlPolicy | Object 持有者信息 |  Container |
| AccessControlList | AccessControlPolicy | 被授权者信息与权限信息 |  Container |

Container 节点 Owner 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ID | AccessControlPolicy.Owner |  Object 持有者 ID，</br>格式为：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; 如果是主帐号，&lt;OwnerUin&gt; 和 &lt;SubUin&gt; 是同一个值 |  String |
| DisplayName | AccessControlPolicy.Owner |  Object 持有者的名称 |  String |

Container 节点 AccessControlList 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Grant | AccessControlPolicy.AccessControlList | 单个 Object 的授权信息。一个 AccessControlList 可以拥有 100 条 Grant | Container    |

Container 节点 Grant 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Grantee | AccessControlPolicy.AccessControlList.Grant | 说明被授权者的信息。type 类型可以为 RootAccount，Subaccount；当 type 类型为 RootAccount 时，ID 中指定的是主帐号;当 type 类型为 Subaccount 时，ID 中指定的是子帐号| Container    |
| Permission | AccessControlPolicy.AccessControlList.Grant | 指明授予被授权者的权限信息，枚举值：READ，FULL_CONTROL  | String    |

Container 节点 Grantee 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
|URI|  AccessControlPolicy.AccessControlList.Grant.Grantee| 指定所有用户|  String |
| ID | AccessControlPolicy.AccessControlList.Grant.Grantee | 用户的 ID，格式为：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; 如果是主帐号，&lt;OwnerUin&gt; 和 &lt;SubUin&gt; 是同一个值。|  String |
| DisplayName | AccessControlPolicy.AccessControlList.Grant.Grantee |  用户的名称 |  String |


## 实际案例

### 请求
```shell
GET /exampleobject?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB&q-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b4065
```

### 响应
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 266
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZmNw==

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
