## Description
Abort Multipart Upload is used to abort a multipart upload operation and delete parts that are already uploaded. When Abort Multipart Upload is called, the Upload Parts returns failure to any request that is using the Upload Parts. "404 NoSuchUpload" is returned if the UploadID does not exist.

><font color="#0000cc">**Note:** </font>
>It is recommended that you complete multipart upload in time or abort the upload operation for the reason that parts that have been uploaded but not aborted can take up storage, incurring cost.

## Request

Syntax:
```
DELETE /ObjectName?uploadId=UploadId HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
DELETE /ObjectName?uploadId=UploadId HTTP/1.1
```
This API allows DELETE request.
### Request Parameters
Example of request line that contains all request parameters.
```
DELETE /ObjectName?uploadId=UploadId HTTP/1.1
```
See the details below: <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

| Parameter Name | Description | Type | Required |
|---|---|---|---|
| UploadID | Indicate the ID of current multipart upload. <br>You can obtain an uploadid when you use the API "Initiate Multipart Upload" to initiate multipart upload. This ID exclusively identifies this multipart data, and the relative position of this multipart in the entire file | String | Yes |

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
No particular request header information for this request operation.


### Request Body
The request body of this request is null.

## Response

### Response Header
#### Common Response Header 
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this request operation.


### Response Body
The response body of this request is null.


## Practical Case

### Request
```
DELETE /ObjectName?uploadId=1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Tue, 26 Oct 2013 21:22:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484728626;32557624626&q-key-time=1484728626;32557624626&q-header-list=host&q-url-param-list=uploadId&q-signature=2d3036b57cade4a257b48a3a5dc922779a562b18

```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Tue, 26 Oct 2013 21:22:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjI5MzlfOTgxZjRlXzZhYjNfMjBh

```

