## Description
Delete Bucket API request is used to delete a Bucket under a specified account. The Bucket must be empty before it can be deleted. The Bucket can be deleted only if its content is removed.
## Request

Syntax:
```
DELETE / HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
DELETE / HTTP/1.1
```
This API allows DELETE request.

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
No particular request header information for this request operation.

### Request Body
The request body of this request is null.

## Response

### Response Header
#### Common Response Header
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this response.

### Response Body
Null is returned for the response body, 

## Practical Case

### Request
```
DELETE / HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484708950;32557604950&q-key-time=1484708950;32557604950&q-header-list=host&q-url-param-list=&q-signature=2b27b72ad2540ff2dde341dc7579a66ee8cb2afc

```

### Response
```
HTTP /1.1 204 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZWRjNjBfOTgxZjRlXzZhYjlfMTg0

```

