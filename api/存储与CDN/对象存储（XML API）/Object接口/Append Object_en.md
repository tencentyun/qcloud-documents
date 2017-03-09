## Description
Append request is used to upload a file (Object) to Bucket via multipart upload method. A file must be configured Appendable before it can be uploaded using Append. If you commence Put Object operation to an Appendable file, the file will be overwritten and its attribute will change to Normal.

You can query the attribute of the file using Head Object operation. When you initiate Head Object request, the custom Header [x-cos-object-type] will be returned, which only contains two enumerated values: Normal or Appendable.

Recommended size of the appended file is 1M - 5G. COS will return 409 error if the value of position and the length of current Object are inconsistent. COS will return "409 ObjectNotAppendable" if you try to Append a Normal Object.

Appendable files cannot be copied, are not involved in versioning, life cycle management and cannot be replicated across domains.

## Request

### Request Syntax

```http
POST /ObjectName?append&position=*position* HTTP/1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Content-Length: size
Content-Type: ContentType
Date: date
Authorization: auth
```

### Request Parameter

| Name       | Description                                       | Required   |
| -------- | ---------------------------------------- | ---- |
| Position | Start point of the append operation. Unit: byte. Position=0 for initial append. Position=content-length of the current file for subsequent append | Yes    |

### Request Header

#### Required Headers

| Name          | Description                               | Type     | Required   |
| -------------- | ------------------------------ | ------ | ---- |
| Content-Length | HTTP request content length defined in RFC 2616 (bytes).  | String | Yes |

#### Recommended Headers

| Name                | Description                                       | Type        | Required   |
| ------------------- | ---------------------------------------- | ------ | ---- |
| Cache-Control       | The caching policy defined in RFC 2616, which will be returned as Object metadata.       | String | No    |
| Content-Disposition | The file name defined in RFC 2616, which will be returned as Object metadata.       | String | No    |
| Content-Encoding    | The encoding format defined in RFC 2616, which will be returned as Object metadata.       | String | No    |
| Content-MD5          | 128-bit content MD5 algorithm check value defined in RFC 1864.       | String | No    |
| Content-Type        | The content type defined in RFC 2616 (MIME), which will be returned as Object metadata.  | String | No    |
| Expect              | If Expect:  100-continue is used, the request content will not be sent until the receipt of response from server.  | String | No    |
| Expires    | The expiration time defined in RFC 2616, which will be returned as Object metadata.       | String | No    |
| x-cos-content-sha1  | The 160-bit content SHA-1 algorithm check value defined in RFC 3174.     | String | No    |
|  x-cos-meta-*        | The header information allowed to be defined by users. This will be returned as Object metadata. The size is limited to 2K.     | String | No    |

#### Permission-related headers

| Name                | Description                                       | Type        | Required   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | Allow users to define file permissions. <br/ >Valid values: private, public-read, public-read-write | String | No    |
| x-cos-grant-read         | Grant read permission to the authorized account <br/> Format: x-cos-grant-read:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |
| x-cos-grant-write        | Grant write permission to the authorized account <br/> Format: x-cos-grant-write:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |
| x-cos-grant-full-control | Grant read and write permissions to the authorized account <br/> Format: x-cos-grant-full-control:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |

### Request Content

Appended file content

## Returned Value

### Response Header

| Name                         | Description                | Type     |
| -------------------------- | ----------------- | ------ |
| x-cos-next-append-position | Start point of the next append operation. Unit: byte | String |
| x-cos-content-sha1         | Check value of the segment            | String |
| ETag                       | Unique tag of the file           | String |

### Response Content

No response content

## Example

### Request

```HTTP
POST /coss3/app?append&position=0 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1484208848;32557104848&q-key-time=1484208848;32557104848&q-header-list=host&q-url-param-list=append;position&q-signature=855fe6b833fadf20570f7f650e2120e17ce8a2fe
Content-Length: 4096

[Object]
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 12 16:14:24 2017
ETag: 1ce5b469b7d6600ecc2fd112e570917b
Server: tencent-cos
x-cos-content-sha1: 1ceaf73df40e531df3bfb26b4fb7cd95fb7bff1d
x-cos-next-append-position: 4096
x-cos-request-id: NTg3NzNhZGZfMmM4OGY3X2I2Zl8xMTBm
```



