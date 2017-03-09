## Description
Delete Bucket CORS is used to delete cross-domain access configurations.

## Request

### Request Syntax

```HTTP
DELETE /?cors HTTP 1.1
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
DELETE /?cors HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484816036;32557712036&q-key-time=1484816036;32557712036&q-header-list=host&q-url-param-list=cors&q-signature=e92eecbf0022fe7e5fd39b2c500b22da062be50a

```
### Response
```xml
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 405
Connection: keep-alive
Date: Thu Jan 19 16:54:04 2017
Server: tencent-cos
x-cos-request-id: NTg4MDdlYWNfOTgxZjRlXzZhYTlfZjAz
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODczNTBmNjMwZmQ0MTZkMjg0NjlkNTYyNmY4ZTRkZTk0N2M2MTdkZGZlMGNhOWQyYjk3MWNmNWNkYzFhMjQzNzRiZTE1NjgzNzFhOGI5M2EwZDMyNGM4Y2ZmMzhiNTllMjk=

```

