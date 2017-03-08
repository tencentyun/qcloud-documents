## Description
Get Bucket Location API is used to acquire information of the region to which a Bucket belongs. Only the Bucket owner is allowed to read the information.

## Request

### Request Syntax

```HTTP
GET /?location HTTP 1.1
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

| Name                 | Description                                       | Content     |
| ------------------ | ---------------------------------------- | ------ |
| LocationConstraint | Region to which the Bucket belongs, enumerated values include china-east, china-south, china-north, china-west, singapore | String |


## Example
### Request
```xml
GET /?location HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817522;32557713522&q-key-time=1484817522;32557713522&q-header-list=host&q-url-param-list=location&q-signature=ceb96fc929663dd4d2e6dc0aeb304cdde6761ed0

```
### Response
```xml
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 92
Connection: keep-alive
Date: Thu Jan 19 17:18:49 2017
Server: tencent-cos
x-cos-request-id: NTg4MDg0NzlfNDYyMDRlXzM0OWFfZjFk

<LocationConstraint>singapore</LocationConstraint>
```


