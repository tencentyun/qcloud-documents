## Description
GET Object acl API is used to obtain access permission of an Object under a Bucket. Only the Bucket owner is allowed to perform the action.
## Request

Syntax:
```
GET /ObjectName?acl HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
~~~
GET /ObjectName?acl HTTP/1.1
~~~
This API allows GET request.

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
**Required header**
This request operation is implemented using the following required headers:

| Name | Description | Type | Required |
|:---|:-- |:--|:--|
| Authorization | Signature string | String | Yes |

### Request Body
The request body of this request is null.

## Response

### Response Header
#### Common Response Header 
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this response.
### Response Body
**application/xml** data is returned for the response body, including the complete node data, as show below:

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

Detailed data content is shown as below:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| AccessControlPolicy | None | Container for saving results of GET Object acl | Container |

Content of Container node AccessControlPolicy:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Owner | AccessControlPolicy | Information of Object owner |  Container |
| AccessControlList | AccessControlPolicy | Information of authorized account and permissions |  Container |

Content of Container node Owner:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| ID | AccessControlPolicy.Owner |  Object owner ID. </br>Format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; in case of root account, &lt;OwnerUin&gt; and &lt;SubUin&gt; use the same value |  String |
| DisplayName | AccessControlPolicy.Owner | Name of Object owner |  String |

Content of Container node AccessControlList:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| Grant | AccessControlPolicy.AccessControlList | A single Object authorization information entry. Each AccessControlList can contain 100 Grant entries | Container    |

Content of Container node Grant:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| Grantee | AccessControlPolicy.AccessControlList.Grant | Provide the information of the authorized user. Type can be RootAccount and Subaccount. In case of RootAccount, ID is specified as root account. In case of Subaccount, ID is specified as sub-account  | Container    |
| Permission | AccessControlPolicy.AccessControlList.Grant | Indicate the information of permissions granted to the authorized user. Enumerated value: READ, WRITE, FULL_CONTROL  | String    |

Content of Container node Grantee:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | AccessControlPolicy.Owner | User ID. In case of root account, format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt; or qcs::cam::anyone:anyone (referring to all users). In case of sub-account, format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;|  String |
| DisplayName | AccessControlPolicy.Owner | Name of user |  String |


## Practical Case

### Request
```
GET /ObjectName?acl HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b40652
```

### Response
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
        <DisplayName>qcs::cam::anyone:anyone</DisplayName>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```



