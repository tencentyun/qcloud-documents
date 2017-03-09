## Description
Delete Object request is used for deletion of one file (Object).

## Request

### Request Syntax

```Http
DELETE /ObjectName HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Content-Length:length
Authorization: auth
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

```HTTP
DELETE /123 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213409;32557109409&q-key-time=1484213409;32557109409&q-header-list=host&q-url-param-list=&q-signature=1c24fe260ffe79b8603f932c4e916a6cbb0af44a
```

### Response

```HTTP
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 12 17:30:12 2017
Server: tencent-cos
x-cos-request-id: NTg3NzRjYTRfYmRjMzVfMzFhOF82MmM3Yg==
```


