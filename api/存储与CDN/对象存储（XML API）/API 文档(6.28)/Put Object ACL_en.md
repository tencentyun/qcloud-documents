## Description
The API Put Object ACL is used to configure ACL for an Object in a Bucket. You can import ACL information either by using Header: "x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos-grant-full-control", or by using body in XML format.
>**Note:**
>Header and Body cannot be used simultaneously. Otherwise, an error indicating a conflict will be returned by the response.
> Importing new ACL using Put Object ACL operation will overwrite existing ACL.
> Only the Bucket owner is allowed to perform the action.


## Request

Syntax:
```
PUT /ObjectName?acl HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-MD5: MD5
x-cos-acl: [Corresponding permission]
x-cos-grant-read: id="",id=""
x-cos-grant-write: id="",id=""
x-cos-grant-full-control: id="",id=""
Authorization: Auth String
```
> Authorization:  Auth String (For more information, please see [Request Signature](https://www.qcloud.com/document/product/436/7778) chapter)

### Request Line
~~~
PUT /ObjectName?acl HTTP/1.1
~~~
This API allows PUT request.
### Request Header

**Common Header**
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://www.qcloud.com/document/product/436/7728) chapter.

**Non-common Header**
This request operation is implemented using header x-cos-acl in request PUT to set the access permission of Object. Object supports three access permissions: public-read-write, public-read and private. The default permission is private if not set. Users can also be clearly granted with permission of read, write or read-write separately. See the details below:
<style  rel="stylesheet"> table th:nth-of-type(1) {width:  200px;	}</style>

| Name | Description | Type | Required |
|:---|:-- |:--|:--|
| x-cos-acl | Define the ACL attribute of Object. Valid values: private, public-read-write, public-read. Default value: private | String |  No |
| x-cos-grant-read | Grant read permission to the authorized user. Format: x-cos-grant-read:  id=" ", id=" "<br/>When you need to authorize a sub-account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"<br/>When you need to authorize the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  No |
| x-cos-grant-write | Grant write permission to the authorized user. Format: x-cos-grant-write:  id=" ", id=" "<br/>When you need to authorize a sub-account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"<br/>When you need to authorize the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  No |
| x-cos-grant-full-control | Grant read-write permission to the authorized user. Format: x-cos-grant-full-control:  id=" ", id=" "<br/>When you need to authorize a sub-account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"<br/>When you need to authorize the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  No |

### Request Body
This request operation can also be implemented using request body with specific request parameter to set Object access permissions. However, only one can be used between "request body with specific request parameter" and "request header with ObjectName?acl sub-resource".
Example of request body with all nodes:
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
Detailed data content is shown as below:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| AccessControlPolicy | None | Container for saving results of Get Object ACL | Container | Yes |

Content of Container node AccessControlPolicy:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| Owner | AccessControlPolicy | Information of Object resource owner | Container | Yes |
| AccessControlList | AccessControlPolicy | Information of authorized account and permissions | Container | Yes |

Content of Container node Owner:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| ID | AccessControlPolicy.Owner | ID of Object owner. </br>Format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; in case of root account, &lt;OwnerUin&gt; and &lt;SubUin&gt; are of the same value | String | Yes |

Content of Container node AccessControlList:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        | Required |
| ------------ | ------------------------------------- | --------- |:--|:--|
| Grant | AccessControlPolicy.AccessControlList | A single Object resource authorization information entry. Each AccessControlList can contain 100 Grant entries | Container | Yes |

Content of Container node Grant:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        | Required |
| ------------ | ------------------------------------- | --------- |:--|:--|
| Grantee | AccessControlPolicy.AccessControlList.Grant | Provide the information of the authorized user. "type" can be RootAccount or Subaccount. </br>In case of RootAccount, ID is specified as root account. </br>In case of Subaccount, ID is specified as sub-account | Container | Yes |
| Permission | AccessControlPolicy.AccessControlList.Grant | Indicate the information of permissions granted to the authorized user. Enumerated values: READ, WRITE, FULL_CONTROL | String | Yes |

Content of Container node Grantee: <style  rel="stylesheet"> table th:nth-of-type(1) {width:  200px;	}</style>

| Node Name (Keyword)          | Parent Node | Description                                    | Type        | Required |
| ------------ | ------------------------------------- | --------- |:--|:--|
| ID | AccessControlPolicy.AccessControlList.Grant.Grantee | User ID. In case of root account, format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt; or qcs::cam::anyone:anyone (all users). In case of sub-account, format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; | String | Yes |


## Response

### Response Header
#### Common Response Header
This response uses common response header. For more information, please see [Common Response Headers](https://www.qcloud.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this response.
### Response Body
Null is returned for the response body.

## Practical Case

### Request
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

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 25 Feb 2015 04:10:22 GMT 
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw

```

