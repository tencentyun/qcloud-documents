## Description
This API (DELETE Bucket tagging) is used to delete the tags of a bucket.

## Request
#### Request example:

```
DELETE /?tagging HTTP 1.1
Host:<bucketname-APPID>.cos.<Region>.myqcloud.com
Date:date
Authorization: Auth
```
> Authorization: Auth String (for more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778))


### Request line

```
DELETE /?tagging HTTP/1.1
```

This API allows `DELETE` request.


### Request header

#### Common header

This request operation is implemented using common request headers. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728 "Common Request Headers").

#### Non-common header


No special request header is used for this request operation.

### Request body
The request body is empty.
## Response
### Response header

#### Common response header

This response uses common response headers. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729 "Common Request Headers").

#### Special response header

No special response header is used for this request operation.

### Response body
The response body is empty.

### Error codes
The following describes some special and common errors that may occur with this request:

Error Code | Description | HTTP Status Code
---|---|---
None|A null is returned for the response body upon a successful deletion | 204 [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)
NoSuchBucket|This error code is returned if the bucket accessed does not exist | 404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## Example

### Request

```
DELETE /?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: chengwus3sdktj-1251668577.cos.ap-beijing.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4LYUE&q-sign-time=1516362480;1517362530&q-key-time=1516362480;1517362530&q-url-param-list=tagging&q-header-list=host&q-signature=8f80220c5699bb02d3b0956951d6105510020d54
```

### Response

```
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 19 Jan 2018 11:49:05 GMT
Server: tencent-cos
x-cos-request-id: NWE2MWRiMzFfOGViMjM1MGFfNTdkMV81NDIyYg==
```



