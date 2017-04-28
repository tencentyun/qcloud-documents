## Description
Upload Part request is used to implement the multipart upload after initialization. The allowed number of parts is limited to 10000, and the size of part should be between 1 MB and 5 GB. Upload Part should be used with partNumber and uploadID. PartNumber is the part No. and supports out-of-order upload.

If the uploadID and partNumber are the same, the parts uploaded later will overwrite the parts uploaded earlier. A 404 error "NoSuchUpload" will be returned if the UploadID does not exist.

## Request

### Request Syntax

```http
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId HTTP 1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Content-Length: Size
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header

#### Required Headers

| Name          | Description                               | Type     | Required   |
| -------------- | ------------------------------ | ------ | ---- |
| Content-Length | HTTP request content length defined in RFC 2616 (bytes).  | String | Yes |

#### Recommended Headers

| Name      | Description                          | Type        | Required   |
| ------------------ | ---------------------------------------- | ------ | ---- |
| Expect             | If Expect:  100-continue is used, the request content will not be sent until the receipt of response from server.  | String | No    |
| x-cos-content-sha1 | The 160-bit content SHA-1 algorithm check value defined in RFC 3174.     | String | No    |

### Request Content

File content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

No response content

## Example

### Request

```Http
PUT /ObjectName?partNumber=1&uploadId=1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727403;32557623403&q-key-time=1484727403;32557623403&q-header-list=host&q-url-param-list=partNumber;uploadId&q-signature=bfc54518ca8fc31b3ea287f1ed2a0dd8c8e88a1d
Content-Length: 10485760

[Object]
```

### Response

```Http
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed Jan 18 16:17:03 2017
Etag: "e1e5b4965bc7d30880ed6d226f78a5390f1c09fc"
Server: tencent-cos
x-cos-request-id: NTg3ZjI0NzlfOWIxZjRlXzZmNGJfMWYy
```


