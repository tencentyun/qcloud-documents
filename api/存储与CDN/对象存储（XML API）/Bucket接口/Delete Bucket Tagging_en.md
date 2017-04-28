## Description
Delete Bucket Tagging API is used to delete tags of specified Bucket.

## Request

### Request Syntax

```HTTP
DELETE /?tagging HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

No response content

## Example
### Request
```xml
DELETE /?tagging HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817338;32557713338&q-key-time=1484817338;32557713338&q-header-list=host&q-url-param-list=tagging&q-signature=fa13dedef474fe2034d2bb5b93b3afeffb225e5a

```
### Response
```xml
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 17:15:46 2017
Server: tencent-cos
x-cos-request-id: NTg4MDgzYzJfOWIxZjRlXzZmM2JfZWUw

```

