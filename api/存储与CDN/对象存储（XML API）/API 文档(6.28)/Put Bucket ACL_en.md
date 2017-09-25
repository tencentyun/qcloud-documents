## Description
Put Bucket ACL API is used to write ACL for a Bucket. You can import ACL information either by using Header: "x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos-grant-full-control", or by using body in XML format.
><font color="#0000cc">**Note:** </font>
- Header and Body cannot be used simultaneously. Otherwise, an error indicating a conflict will be returned by the response.
- Importing new ACL using Put Bucket ACL operation will overwrite existing ACL.
- Only the Bucket creator is allowed to perform the action.


## Request

Syntax:
```
PUT /?acl HTTP/1.1
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
PUT /?acl HTTP/1.1
~~~

### Request Header

**Common Header**
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://www.qcloud.com/document/product/436/7728) chapter.

**Non-common Header** <style  rel="stylesheet"> table th:nth-of-type(1) { width:  200px; }</style>
This request operation is implemented using header x-cos-acl in request PUT to set the access permission of Bucket. Bucket supports three access permissions: public-read-write, public-read and private. The default permission is private if not set. Users can also be clearly granted with permission of read, write or read-write separately. See the details below:

| Name | Description | Type | Required |
|:---|:-- |:--|:--|
| x-cos-acl | Define the ACL attribute of Object. Valid values: private, public-read-write, public-read. Default value: private | String |  No |
| x-cos-grant-read | Grant read permission to the authorized user. Format: x-cos-grant-read:  id=" ", id=" "<br/>When you need to authorize a sub-account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"<br/>When you need to authorize the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  No |
| x-cos-grant-write | Grant write permission to the authorized user. Format: x-cos-grant-write:  id=" ", id=" "<br/>When you need to authorize a sub-account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt;"<br/>When you need to authorize the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  No |
| x-cos-grant-full-control | Grant read-write permission to the authorized user. Format: x-cos-grant-full-control:  id=" ", id=" "<br/>When you need to authorize a sub-account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&tl;SubUin&gt;"<br/>When you need to authorize the root account, id="qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;OwnerUin&gt;" | String |  No |

### Request Body
This request operation can also be implemented using request body with specific request parameter to set Bucket access permissions. However, only one can be used between "request body with specific request parameter" and "request header with acl sub-resource".
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
| AccessControlPolicy | None | Container for saving results of Get Bucket ACL | Container | Yes |

Content of Container node AccessControlPolicy:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| Owner | AccessControlPolicy | Information of Bucket owner | Container |Yes|
| AccessControlList | AccessControlPolicy | Information of authorized account and permissions | Container | Yes |

Content of Container node Owner:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| ID | AccessControlPolicy.Owner | ID of Bucket owner. </br>Format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; in case of root account, &lt;OwnerUin&gt; and &lt;SubUin&gt; are of the same value | String | Yes |

Content of Container node AccessControlList:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        | Required |
| ------------ | ------------------------------------- | --------- |:--|:--|
| Grant | AccessControlPolicy.AccessControlList | A single Bucket authorization information entry. Each AccessControlList can contain 100 Grant entries | Container | Yes |

Content of Container node Grant:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        | Required |
| ------------ | ------------------------------------- | --------- |:--|:--|
| Grantee | AccessControlPolicy.AccessControlList.Grant | Resource information of the authorized user. "type" can be RootAccount or SubAccount. </br>In case of RootAccount, you can enter QQ in "uin" or in "uin" of id; you can also use "anyone" ( all types of users) to replace uin/&lt;OwnerUin&gt; and uin/&lt;SubUin&gt;. </br>For type of RootAcount, uin represents root account, and SubAccount represents sub-account | Container | Yes |
| Permission | AccessControlPolicy.AccessControlList.Grant | Indicate the information of permissions granted to the authorized user. Enumerated values: READ, WRITE, FULL_CONTROL | String | Yes |

Content of Container node Grantee:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        | Required |
| ------------ | ------------------------------------- | --------- |:--|:--|
| ID | AccessControlPolicy.AccessControlList.Grant.Grantee | User ID. </br>Format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; in case of root account, &lt;OwnerUin&gt; and &lt;SubUin&gt; are of the same value| String | Yes |


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
PUT /?acl HTTP/1.1
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
Date: Fri, 25 Feb 2017 04:10:22 GMT 
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw

```


