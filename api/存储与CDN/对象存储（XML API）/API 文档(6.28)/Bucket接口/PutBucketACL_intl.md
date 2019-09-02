## Description
The PUT Bucket acl interface is used to write the acl table of the bucket. You can do this via Header:"x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos -grant-full-control" Pass in acl information, or pass acl information in XML format via Body.
**Notes:**
- The Header and Body cannot be selected at the same time.
- PUT Bucket acl  is an overlay operation, passing in a new acl will overwrite the original acl.
- Only Bucket creators are authorized to operate.

### Note
1. It can be set either by head or by XML body. It is recommended to use only one method.
2. You can set a folder in a private Bucket to public, then the files in the folder are public; but after the folder is set to private, the public properties set in the folder will not take effect.

## Request

Grammar example:
```
PUT /?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-MD5: MD5
X-cos-acl: [corresponding authority]
X-cos-grant-read: id="",id=""
X-cos-grant-write: id="",id=""
X-cos-grant-full-control: id="",id=""
Authorization: Auth String
```
> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request line
~~~
PUT /?acl HTTP/1.1
~~~

### Request header

**Public header**
The implementation of this request operation uses the public request header. For details on the public request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728) section.

**Non-public header** <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>
You can use the x-cos-acl header in the PUT request to set the Bucket access permissions. A Bucket has three access rights: public-read-write, public-read, and private. If not set, the default is private. It is also possible to explicitly give the user read, write or read and write permissions. The content is as follows:

|Name|Description|Type|Required|
|:---|:-- |:--|:--|
| x-cos-acl | Defines the acl attribute of an Object. Valid values: private, public-read-write, public-read; Default: private | String| No |
| x-cos-grant-read |Give the authorized person read access. Format: x-cos-grant-read: id="[OwnerUin]" | String |  No |
| x-cos-grant-write|Gives permission to the authorized person to write. Format: x-cos-grant-write: id="[OwnerUin]" |String |  No |
| x-cos-grant-full-control | Give the authorized person read and write permissions. Format: x-cos-grant-full-control: id="[OwnerUin]" | String| No |

### Request body
The implementation of the request operation can also set the Bucket access permission in the request body by using a specific request parameter, but only one of the request body parameter mode and the request header acl sub-resource mode can be selected.
Example of all nodes:
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
The specific data content is as follows:

|Node name (keyword)|Parent node|Description|Type|Required|
|:---|:-- |:--|:--|:--|
| AccessControlPolicy | None | Save GET Bucket acl Result Container | Container |Yes |

The contents of the Container node AccessControlPolicy:

|Node name (keyword)|Parent node|Description|Type|Required|
|:---|:-- |:--|:--|:--|
| Owner | AccessControlPolicy | Bucket Holder Information | Container |Yes |
| AccessControlList | AccessControlPolicy | Authorized Information and Permission Information | Container |Yes |

The contents of the Container node Owner:

|Node name (keyword)|Parent node|Description|Type|Required|
|:---|:-- |:--|:--|:--|
|ID | AccessControlPolicy.Owner | Bucket Holder ID,</br> Format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; If it is the root account, &lt;OwnerUin&gt; and &lt; SubUin&gt; is the same value | String |Yes|

The contents of the Container node AccessControlList:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:------------ |:-------------------- |:--------- |:--|:--|
| Grant | AccessControlPolicy.AccessControlList | Authorization information for a single Bucket. An AccessControlList can have 100 Grants | Container | Yes |

The contents of the Container node Grant:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:------------ |:--------------------------------|:---------|:--|:--|
|Grantee | AccessControlPolicy.AccessControlList.Grant | Authorized resource information. The type can be RootAccount, SubAccount;</br> When the type is RootAccount, you can fill in QQ in uin, you can fill in QQ in id, or you can use anyone (refer to all types of users) instead of uin/&lt; OwnerUin&gt; and uin/&lt;SubUin&gt;. </br>When the type is RootAccount, uin represents the root account account, Subaccount represents the sub-account account | Container | Yes |
|Permission | AccessControlPolicy.AccessControlList.Grant | Indicates the permission information granted to the authorized person. Values can be: READ, WRITE, FULL_CONTROL | String |Yes|

The contents of the Container node Grantee:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:------------ |:--------------------------------|:---------|:--|:--|
|ID | AccessControlPolicy.AccessControlList.Grant.Grantee | User ID,</br> Format: qcs::cam::uin/&lt;OwnerUin&gt;:uin/&lt;SubUin&gt; If it is the root account, &lt;OwnerUin&gt; and &lt;SubUin&gt; is the same value | String |Yes |



## Response

### Response header
#### Public response header
The response uses a common response header. See the [Public Response Header](https://cloud.tencent.com/document/product/436/7729) section for details on the public response header.
#### API-specific response header
There is no specific response header for this API.
### Response body
The response body returns empty.

### Error Codes
The following describes some special and common error conditions that can occur with this request:

|Error Code|HTTP Status Code|Description|
|------|------|------|
|InvalidDigest|400 Bad Request|User's Content-MD5 is inconsistent with the COS calculation body's Content-MD5|
|MalformedXM|400 Bad Request|The incoming XML format is incorrect, please compare it carefully with the restful API documentation|
|InvalidArgument|400 Bad Request|Parameter error, please refer to the error message for details|

## Sample Code

### Request
```
PUT /?acl HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 25 Feb 2017 04:10:22 GMT
Authorization: q-sign-algorithm = sha1 & q-ak = AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO & q-sign-time = 1484724784; 32557620784 & q-key-time = 1484724784; 32557620784 & q-header-list = host & q-url-param-list = acl & q-signature = 785d9075b8154119e6a075713c1b9e56ff0bddfc
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
