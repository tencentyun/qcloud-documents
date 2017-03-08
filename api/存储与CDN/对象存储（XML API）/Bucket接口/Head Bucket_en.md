## Description

Head Bucket request is used to determine whether the Bucket and the permission to access the Bucket exist. Head and Read have the same permission. HTTP status code 200 will be returned if the Bucket exists, 403 if there is no permission, and 404 if the Bucket does not exist.

## Request

### Request Syntax

```http
HEAD / Http/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
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
HEAD / HTTP/1.1
Host:zuhaotestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484640517;32557536517&q-key-time=1484640517;32557536517&q-header-list=host&q-url-param-list=&q-signature=7bedc2f84a0a3d29df85fe727d0c1e388c410376
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Tue Jan 17 16:09:39 2017
x-cos-request-id: NTg3ZGQxNDNfNDUyMDRlXzUyOWNfMjY5
```


