## 功能描述
Get Object ACL 接口用来获取某个 Bucket 下的某个 Object 的访问权限。只有 Bucket 的持有者才有权限操作。
## 请求

语法示例：
```
GET /ObjectName?acl HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth
```
> Authorization:  Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
~~~
GET /ObjectName?acl HTTP/1.1
~~~
#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 ObjectName?acl。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
**必选头部**
该请求操作的实现使用如下必选头部：

|参数名称|描述|类型|必选|
|:---|:-- |:--|:--|
| Authorization | 签名串 |String| 是 |


### 请求体
该请求的请求体为空。


## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应无特殊的响应头。
#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```
<AccessControlPolicy>
  <Owner>
    <ID>qcs::cam::uin/<OwnerUin>:uin/<SubUin></ID>
    <DisplayName>qcs::cam::uin/<OwnerUin>:uin/<SubUin></DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
      <ID>qcs::cam::uin/<OwnerUin>:uin/<SubUin></ID>
      <DisplayName>qcs::cam::uin/<OwnerUin>:uin/<SubUin></DisplayName>
      </Grantee>
      <Permission></Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::uin/<OwnerUin>:uin/<SubUin></ID>
        <DisplayName>qcs::cam::uin/<OwnerUin>:uin/<SubUin></DisplayName>
      </Grantee>
      <Permission></Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| AccessControlPolicy |无| 保存 Get Object ACL 结果的容器 | Container |

Container 节点 AccessControlPolicy 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Owner | AccessControlPolicy | Object 持有者信息 |  Container |
| AccessControlList | AccessControlPolicy | 被授权者信息与权限信息 |  Container |

Container 节点 Owner 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ID | AccessControlPolicy.Owner |  Object 持有者 ID，</br>格式：`qcs::cam::uin/<OwnerUin>:uin/<SubUin>` 如果是根帐号，<OwnerUin> 和 <SubUin> 是同一个值 |  String |
| DisplayName | AccessControlPolicy.Owner |  Object 持有者的名称 |  String |

Container 节点 AccessControlList 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Grant | AccessControlPolicy.AccessControlList | 单个 Object 的授权信息。一个 AccessControlList 可以拥有 100 条 Grant | Container    |

Container 节点 Grant 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Grantee | AccessControlPolicy.AccessControlList.Grant | 被授权者信息。type 类型可以为 RootAccount， Subaccount；</br>当 type 类型为 RootAcount 时，可以在 uin 中填写 QQ，也可以用 anyone（指代所有类型用户）代替 `uin/<OwnerUin>`。</br>当 type 类型为 RootAccount 时，uin 代表根账户账号，Subaccount 代表子账户账号  | Container    |
| Permission | AccessControlPolicy.AccessControlList.Grant | 指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL  | String    |

Container 节点 Grantee 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | AccessControlPolicy.Owner | 用户的 ID，</br>格式：`qcs::cam::uin/<OwnerUin>:uin/<SubUin> `如果是根帐号，<OwnerUin> 和 <SubUin> 是同一个值|  String |
| DisplayName | AccessControlPolicy.Owner |  用户的名称 |  String |


## 实际案例

### 请求
```
GET /ObjectName?acl HTTP/1.1
Host: zuhaotestnorth-1251668577.cn-north.myqcloud.com
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
    <ID>qcs::cam::uin/12345:uin/12345</ID>
    <DisplayName>qcs::cam::uin/12345:uin/12345</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::uin/12345:uin/12345</ID>
        <DisplayName>qcs::cam::uin/12345:uin/12345</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="RootAccount">
        <ID>qcs::cam::uin/54321:uin/54321</ID>
        <DisplayName>qcs::cam::uin/54321:uin/54321</DisplayName>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```


