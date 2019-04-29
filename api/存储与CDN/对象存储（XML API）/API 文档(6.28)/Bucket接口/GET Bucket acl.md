## 功能描述
GET Bucket acl 接口用来获取存储桶的访问权限控制列表。

## 请求
### 请求示例

```
GET /?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节）

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应
### 响应头
#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```
<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/1250000000:uin/1250000000</ID>
    <DisplayName>qcs::cam::uin/1250000000:uin/1250000000</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:type=\"CanonicalUser\">
        <ID>qcs::cam::uin/1250000000:uin/1250000000</ID>
        <DisplayName>qcs::cam::uin/1250000000:uin/1250000000</DisplayName>
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

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| AccessControlPolicy |无| 保存 Get Bucket ACL 结果的容器 | Container |

Container 节点 AccessControlPolicy 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Owner | AccessControlPolicy | Bucket 持有者信息 |  Container |
| AccessControlList | AccessControlPolicy | 被授权者信息与权限信息 |  Container |

Container 节点 Owner 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ID | AccessControlPolicy.Owner |  Bucket 持有者 ID，</br>格式：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; 如果是根帐号，&lt;OwnerUin&gt; 和 &lt;SubUin&gt; 是同一个值 |  String |
| DisplayName | AccessControlPolicy.Owner |  Bucket 持有者的名称 |  String |

Container 节点 AccessControlList 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Grant | AccessControlPolicy.AccessControlList | 单个 Bucket 的授权信息。一个 AccessControlList 可以拥有100条 Grant | Container    |

Container 节点 Grant 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Grantee | AccessControlPolicy.AccessControlList.Grant | 说明被授权者的信息。type 类型可以为 RootAccount， Subaccount；当 type 类型为 RootAccount 时，ID 中指定的是根帐号;当 type 类型为 Subaccount 时，ID 中指定的是子帐号  | Container    |
| Permission | AccessControlPolicy.AccessControlList.Grant | 指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL  | String    |

Container 节点 Grantee 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | AccessControlPolicy.Owner | 用户的 ID，如果是根帐号，格式为：qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt; 或  qcs::cam::anyone:anyone （指代所有用户）如果是子帐号，格式为： qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;|  String |
| DisplayName | AccessControlPolicy.Owner |  用户的名称 |  String |

### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 章节。


## 实际案例

### 请求
``` 
GET /?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b40652
```
### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 266
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZmNw==
<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/1250000000:uin/1250000000</ID>
    <DisplayName>qcs::cam::uin/1250000000:uin/1250000000</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:type=\"CanonicalUser\">
        <ID>qcs::cam::uin/1250000000:uin/1250000000</ID>
        <DisplayName>qcs::cam::uin/1250000000:uin/1250000000</DisplayName>
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

