## Description
Get Object API request is used to download one file (Object) in Bucket of COS to the local computer. This action requires that the user has the read permission for the target Object or the read permission for the target Object has been made available for everyone (public-read).

## Request

Syntax:
```
GET /<ObjectName> HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
GET /<ObjectName> HTTP/1.1
```
This API allows GET request.
#### Request parameter<style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>
Example of request line that contains all request parameters.
```
GET /<ObjectName>&response-content-type=ContentType&response-content-language=ContentLanguage&response-expires=ContentExpires&response-cache-control=CacheControl&response-content-disposition=ContentDisposition&response-content-encoding=ContentEncoding HTTP/1.1
```
See the details below:

| Parameter Name | Description | Type | Required |
|:---|:-- |:---|:-- |
| response-content-type | Set the Content-Type parameter in the response header. | String | No |
| response-content-language | Set the Content-Language parameter in the response header. | String | No |
| response-expires | Set the Content-Expires parameter in the response header. | String | No |
| response-cache-control | Set the Cache-Control parameter in the response header. | String | No |
| response-content-disposition | Set the Content-Disposition parameter in the response header. | String | No |
| response-content-encoding | Set the Content-Encoding parameter in the response header. | String | No |

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
The following recommended request headers are recommended for implementation of this request operation:

| Name | Description | Type | Required |
|:---|:-- |:---|:-- |
| Range | The specified range of file download defined in RFC 2616 (in bytes) | String | No |
| If-Unmodified-Since | Return the contents of the file if the file is modified earlier than or equal to the specified time. If not, 412 (precondition failed) is returned | String | No |
| If-Modified-Since | If Object is modified after the specified time, the Object meta information is returned, otherwise 304 is returned | String | No |
| If-Match | File is returned if Etag is identical to the specified content. If not, 412 (precondition failed) is returned | String | No |
| If-None-Match | File is returned if Etag is not identical to the specified content. If not, 304 (not modified) is returned | String | No |

### Request Body
The request body of this request is null.

## Response

### Response Header
#### Common Response Header 
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
The response header of the request operation is as follows:

| Parameter Name | Description | Type |
|:---|:-- |:-- |
| x-cos-meta-* | User-defined metadata | String |
| X-cos-object-type | Indicate whether the Object is appendable for upload. Enumerated values: normal or appendable |String|
| X-cos-storage-class | The storage class of Object. Enumerated values: STANDARD, STANDARD_IA, NEARLINE | String |

### Response Body
Content of Object is returned for the response body.

## Practical Case

### Request
```
GET /123 HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484212200;32557108200&q-key-time=1484212200;32557108200&q-header-list=host&q-url-param-list=&q-signature=11522aa3346819b7e5e841507d5b7f156f34e639
```

### Response
```
HTTP/1.1 200 OK
Date: Wed, 28 Oct 2014 22:32:00 GMT
Content-Type: application/octet-stream
Content-Length: 16087
Connection: keep-alive
Accept-Ranges: bytes
Content-Disposition: attachment; filename="filename.jpg"
Content-Range: bytes 0-16086/16087
ETag: "9a4802d5c99dafe1c04da0a8e7e166bf"
Last-Modified: Wed, 28 Oct 2014 20:30:00 GMT
x-cos-object-type: normal
x-cos-request-id: NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ==
x-cos-storage-class: STANDARD

[Object]
```

