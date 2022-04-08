## Description
The HEAD Object API request can obtain the metadata of the Object, and the HEAD permission is the same as the GET permission.

###Version

By default, the HEAD operation retrieves metadata from the current version of the object. To retrieve metadata from a different version, use the versionId subresource.

## Request
Request example:
```
HEAD /<ObjectName> HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request line

```
HEAD /{ObjectName} HTTP/1.1
```

The API accepts a `HEAD` request.


### Request header

#### Common header

The implementation of this request operation uses the common request header. For details on the common request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728 "Common Request Header") section.

#### Non-common header

Name|Type|Required|Description
---|---|---|---
If-Modified-Since|string|No|When the Object is modified after the specified time, the metadata corresponding to the Object is returned, otherwise it returns 304


### Request body
The request request body is empty.
## Response
### Response header

#### Common response header

The response uses a common response header. For a detailed description of the common response header, see the [Common Response Header](https://cloud.tencent.com/document/product/436/7729 "Common Response Header") section.

#### API response header

The response header specific data for this request operation include:

|Name|Type|Description|
|---|---|---|
|x-cos-meta- *|string|User-defined meta|
|x-cos-object-type|string| It indicates whether an Object can be additionally uploaded. Values can be: normal or appendable|
|x-cos-storage-class|string|Object storage level, Values can be: STANDARD, STANDARD_IA|
|x-cos-version-id|string|The version ID of the returned object. |
|x-cos-server-side -encryption|string|If the object is stored by COS-managed server-side encryption, the response will contain the value of this header and the encryption algorithm used, AES256|


### Response Body
The request response body is empty.

## Sample Code

### Request

```
HEAD /123 HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Thu, 12 Jan 2017 17:26:53 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213210;32557109210&q-key-time=1484213210;32557109210&q-header-list=host&q-url-param-list=&q-signature=ac61b8eb61964e7e6b935e89de163a479a25c210
```

### Response

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 16087
Connection: keep-alive
Date: Thu, 12 Jan 2017 17:26:53 GMT
ETag: \"9a4802d5c99dafe1c04da0a8e7e166bf\"
Last-Modified: Wed, 11 Jan 2017 07:30:07 GMT
Server: tencent-cos
X-cos-object-type: normal
X-cos-request-id: NTg3NzRiZGRfYmRjMzVfM2Y2OF81N2YzNA==
X-cos-storage-class: STANDARD
```