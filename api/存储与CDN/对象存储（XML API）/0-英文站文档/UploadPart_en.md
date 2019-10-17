## Description
Upload Part request is used to implement the multipart upload after initialization. The allowed number of parts is limited to 10,000, and the size of part should be between 1 MB and 5 GB.
You can obtain an uploadid when you use the API "Initiate Multipart Upload" to initiate multipart upload. This ID exclusively identifies this multipart data, and the relative position of this multipart in the entire file. Upload Part should be used with partNumber and uploadId. partNumber is the part No. and supports out-of-order upload.
If the uploadId and partNumber are the same, the parts uploaded later will overwrite the parts uploaded earlier. A 404 error "NoSuchUpload" will be returned if the uploadId does not exist.

## Request

Syntax:
```
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: Size
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
```
This API allows PUT request.

### Request Parameters
Example of request line that contains all request parameters. <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>
```
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
```
See the details below:

| Parameter Name | Description | Type | Required |
|:---|:---|:---|:---|
| partNumber | Indicate the No. of current multipart upload | String | Yes |
| uploadId | Indicate the ID of current multipart upload.<br>You can obtain an uploadid when you use the API "Initiate Multipart Upload" to initiate multipart upload. This ID exclusively identifies this multipart data, and the relative position of this multipart in the entire file | String | Yes |

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
**Required Header**
The following required request header is needed for the implementation of request operation. Details are shown below:

| Name | Description | Type | Required |
|:---|:---|:---|:---|
| Content-Length | HTTP request content length defined in RFC 2616 (in bytes) | String | Yes |

**Recommended Header**
The following recommended request headers are recommended for implementation of this request operation. Details are shown below:

| Name | Description | Type | Required |
|:---|:---|:---|:---|
| Expect | HTTP request content length defined in RFC 2616 (in bytes) | String | Yes |
| Content-MD5 | 128-bit content MD5 check value encoded using Base64, defined in RFC 1864. This header is used to check whether the file content has changed | String | No |

### Request Body
The request body of this request is null.

## Response

### Response Header
#### Common Response Header 
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this response.

### Response Body
The response body of this response is null.

## Practical Case

### Request
```
PUT /ObjectName?partNumber=1&uploadId=1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Jan 2017 16:17:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727403;32557623403&q-key-time=1484727403;32557623403&q-header-list=host&q-url-param-list=partNumber;uploadId&q-signature=bfc54518ca8fc31b3ea287f1ed2a0dd8c8e88a1d
Content-Length: 10485760

[Object]
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 18 Jan 2017 16:17:03 GMT
Etag: "e1e5b4965bc7d30880ed6d226f78a5390f1c09fc"
Server: tencent-cos
x-cos-request-id: NTg3ZjI0NzlfOWIxZjRlXzZmNGJfMWYy

```

