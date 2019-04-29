## Description
DELETE Bucket cors API request is used to delete configuration information of cross-domain access.
## Request

Syntax:
```
DELETE /?cors HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778))

### Request Line
```
DELETE /?cors HTTP/1.1
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
Null is returned for the response body.

## Practical Case

### Request
```
DELETE /?cors HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Tue, 23 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484816036;32557712036&q-key-time=1484816036;32557712036&q-header-list=host&q-url-param-list=cors&q-signature=e92eecbf0022fe7e5fd39b2c500b22da062be50a
```

### Response
```
HTTP /1.1 204 No Content
Content-Type: application/xml
Content-Length: 405
Connection: keep-alive
Date: Tue, 23 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdlYWNfOTgxZjRlXzZhYTlfZjAz
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODczNTBmNjMwZmQ0MTZkMjg0NjlkNTYyNmY4ZTRkZTk0N2M2MTdkZGZlMGNhOWQyYjk3MWNmNWNkYzFhMjQzNzRiZTE1NjgzNzFhOGI5M2EwZDMyNGM4Y2ZmMzhiNTllMjk=

```

