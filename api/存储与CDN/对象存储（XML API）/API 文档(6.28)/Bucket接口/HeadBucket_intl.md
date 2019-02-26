## Description
The HEAD Bucket request can confirm whether the Bucket exists and whether the user has permission to access it. The HEAD permissions are the same as Read. When the Bucket exists, an HTTP status code of 200 is returned; when the Bucket has no access, an HTTP status code of 403 is returned; and when the Bucket does not exist, an HTTP status code of 404 is returned.
>Remarks: At present, APIs to obtain Bucket attributes are not available.

## Request

Grammar example:
```
HEAD / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request Line
```
HEAD / HTTP/1.1
```
The API accepts a `HEAD` request.

### Request Header

#### Public header
The implementation of this request operation uses the public request header. For details on the public request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728) section.

#### Non-public header
The request operation has no special request header information.

### Request body
The request body of the request is empty.

## Response

### Response header
#### Public response header
The response uses a common response header. See the [Public Response Header](https://cloud.tencent.com/document/product/436/7729) section for details on the public response header.
#### API-specific response header
There is no specific response header for this API.

### Response body
The response body returns empty.

## Sample Code

### Request
```
HEAD / HTTP/1.1
Host: zuhaotestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Thu, 27 Oct 2015 20:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484640517;32557536517&q-key-time=1484640517;32557536517&q-header-list=host&q-url-param-list=&q-signature=7bedc2f84a0a3d29df85fe727d0c1e388c410376
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Thu, 27 Oct 2015 20:32:00 GMT
X-cos-request-id: NTg3ZGQxNDNfNDUyMDRlXzUyOWNfMjY5

```

