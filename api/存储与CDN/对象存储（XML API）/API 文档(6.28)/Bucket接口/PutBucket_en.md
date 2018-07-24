## Description
Put Bucket request is used to create a Bucket under specified account. The API does not support anonymous requests. To create a Bucket, you should use a request authenticated by Authorization signature. By creating the Bucket, you become the bucket owner.

## Request

Syntax:
```
PUT / HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
~~~
PUT / HTTP/1.1
~~~
This API allows PUT request.

### Request Header

**Common Header**
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

**Non-common Header**
This request operation is implemented using header x-cos-acl in request Put to set the access permission of Bucket. Bucket supports three access permissions: public-read-write, public-read and private. The default permission is private if not set. Users can also be clearly granted with permission of read, write or read-write separately. See the details below:
> For more information on ACL, please see [Put Bucket ACL](https://cloud.tencent.com/document/product/436/7737).

| Name | Description | Type | Required |
|:---|:-- |:--|:--|
| x-cos-acl | Define the ACL attribute of Object. Valid values: private, public-read-write, public-read. Default value: private | String | No |
| x-cos-grant-read |赋予被授权者读的权限。格式：x-cos-grant-read: id="[OwnerUin]" | String |  No |
| x-cos-grant-write| 赋予被授权者写的权限。格式：x-cos-grant-write: id="[OwnerUin]" |String |  No |
| x-cos-grant-full-control | 赋予被授权者所有的权限。格式：x-cos-grant-full-control: id="[OwnerUin]" | String|  No |

### Request Body
The request body of this request is null.

## Response

### Response Header
#### Common Response Header
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this response.
### Response Body
Null is returned for the response body.

## Practical Case

### Request
```
PUT / HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Thu, 12 Jan 2016 19:12:22 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484708728;32557604728&q-key-time=1484708728;32557604728&q-header-list=host&q-url-param-list=&q-signature=b394a86624cbcc705b11bc6fc505843c5e2dd9c9
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu, 12 Jan 2016 19:12:22 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZWRiODJfOWIxZjRlXzZmNDBfMTUz

```


