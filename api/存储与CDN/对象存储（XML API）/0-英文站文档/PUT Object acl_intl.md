## Description
The PUT Object acl API is used to configure the ACL table for an Object in a bucket. You can do this via Header: "x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos-grant-full-control" to pass in ACL information, or pass ACL information in XML format via Body.

## Request
Request example:
```
PUT /{ObjectName}/?acl HTTP/1.1
Host: .cos..myqcloud.com
Date: GMT Date
Authorization: Auth String


```
> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)


### Request Headers

#### Common Headers

The implementation of this request operation uses the common request header. For details on the common request headers, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728 "Common Request Header").

#### Non-common Headers


Name|Description|Type|Required
---|---|---|---
X-cos-acl|Defines the ACL property of the Object. Valid values: private, public-read-write, public-read.|string|No
x-cos-grant-read |Give the authorized person read access. Format: x-cos-grant-read: id="[OwnerUin]" | String |  No 
x-cos-grant-write|Gives permission to the authorized person to write. Format: x-cos-grant-write: id="[OwnerUin]" |String |  No 
x-cos-grant-full-control | Give the authorized person read and write permissions. Format: x-cos-grant-full-control: id="[OwnerUin]" | String| No 


### Request Body
The requested request body is an ACL configuration rule.
```xml


```


The specific data is described as follows:

Node Name (Keyword)|Parent Node|Description|Type|Required
---|---|---|---|---
AccessControlPolicy|None|Save GET Bucket acl result container|Container|



## Response
### Response Headers

#### Common Response Headers

The response uses common response headers. For a detailed description of the common response headers, see the [Common Response Header](https://cloud.tencent.com/document/product/436/7729 "Common Response Header").

#### API-Specific Response Header


The request operation has no special response header information.

### Responsive body
The request response body is empty.

### Error Codes

Error Code|Description|HTTP Status Code
---|---|---
SignatureDoesNotMatch| The signature provided does not match the rule |403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|The Bucket where the rule you are trying to add does not exist |404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
MalformedXML|XML format invalid |400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
The InvalidRequest| Request is invalid. If "header acl and body acl conflict" is displayed in the error message, then the header and body cannot have acl parameters. |400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)


## Sample Code

### Request

```
PUT /test?acl HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 25 Feb 2017 04:10:22 GMT
Authorization: q-sign-algorithm = sha1 & q-ak = AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO & q-sign-time = 1484724784; 32557620784 & q-key-time = 1484724784; 32557620784 & q-header-list = host & q-url-param-list = acl & q-signature = 785d9075b8154119e6a075713c1b9e56ff0bddfc
Content-Length: 229
Content-Type: application/x-www-form-urlencoded


  
    qcs::cam::uin/12345:uin/12345
  
  
    
      
        qcs::cam::uin/12345:uin/12345
      
      FULL_CONTROL
    
    
      
        http://cam.qcloud.com/groups/global/AllUsers
      
      READ
    
  

```

### Response:

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 25 Feb 2017 04:10:22 GMT\
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw
```
