## Description

Delete Object request is used to download a file (Object) locally. This action requires that the user has the read permission for the target Object or the read permission for the target Object has been made available for everyone (public-read).

## Request

### Request Syntax

```http
GET /ObjectName Http/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: authorization string(公有读无需此头部，若携带也无效)
Range: bytes=byte_range
```

### Request Parameter

| Name                | Description                                       | Type        | Required   |
| ---------------------------- | -------------------------------- | ------ | ---- |
| response-content-type        | Set the Content-Type parameter in the response header.         | String | No    |
| response-content-language    | Set the Content-Language parameter in the response header.     | String | No    |
| response-expires             | Set the Content-Expires parameter in the response header.      | String | No    |
| response-cache-control       | Set the Cache-Control parameter in the response header.        | String | No    |
| response-content-disposition | Set the Content-Disposition parameter in the response header.  | String | No    |
| response-content-encoding   | Set the Content-Encoding parameter in the response header.     | String | No    |

### Request Header

#### Recommended Headers

| Name                | Description                                       | Type        | Required   |
| ----------------- | ---------------------------------------- | ------ | ---- |
| Range             |The specified range of file download defined in RFC 2616 (in bytes).      | String | No    |
| If-Modified-Since | Return the contents of the file if the file is modified later than the specified time. Otherwise 304 is returned (not modified).  | String | No    |

### Request Content

No request content

## Returned Value

### Response Header

| Name                  | Description                                       | Type     |
| ------------------- | ---------------------------------------- | ------ |
| x-cos-meta-*        | User-defined metadata                                | String |
| X-cos-object-type | Indicate whether the Object is appendable for upload. Enumerated values: normal or appendable | string |
| X-cos-storage-class | The storage class of Object. Enumerated values: Standard, Standard_IA, Nearline | String |


### Response Content

File content

## Example

### Request

```HTTP
GET /123 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484212200;32557108200&q-key-time=1484212200;32557108200&q-header-list=host&q-url-param-list=&q-signature=11522aa3346819b7e5e841507d5b7f156f34e639
```

### Response

```HTTP
HTTP/1.1 200 OK
Date: Thu, 12 Jan 2017 09:10:22 GMT
Content-Type: application/octet-stream
Content-Length: 16087
Connection: keep-alive
Accept-Ranges: bytes
Content-Disposition: attachment; filename*="UTF-8''123"
Content-Range: bytes 0-16086/16087
ETag: "9a4802d5c99dafe1c04da0a8e7e166bf"
Last-Modified: Wed, 11 Jan 2017 15:30:07 GMT
x-cos-object-type: normal
x-cos-request-id: NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ==

[Object]
```


