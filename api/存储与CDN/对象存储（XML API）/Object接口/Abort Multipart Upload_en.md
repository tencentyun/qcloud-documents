## Description
Abort Multipart Upload is used to abort a multipart upload operation and delete parts that are already uploaded. When Abort Multipart Upload is called, the Upload Parts will return failure to any request that is using the Upload Parts. "404 NoSuchUpload" will be returned if the UploadID does not exist.

It is recommended that you complete multipart upload in time or abort the upload operation for the reason that parts that have been uploaded but not aborted will take up storage, incurring cost.

## Request

### Request Syntax

```http
DELETE /ObjectName?uploadId=UploadId HTTP 1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
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

```HTTP
DELETE /ObjectName?uploadId=1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484728626;32557624626&q-key-time=1484728626;32557624626&q-header-list=host&q-url-param-list=uploadId&q-signature=2d3036b57cade4a257b48a3a5dc922779a562b18
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed Jan 18 16:37:13 2017
Server: tencent-cos
x-cos-request-id: NTg3ZjI5MzlfOTgxZjRlXzZhYjNfMjBh
```


