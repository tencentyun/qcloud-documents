## Description
Put Object request allows you to upload a file (Oject) to the specified Bucket.

## Request

### Request Syntax

```Http
PUT /ObjectName HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: authorization string
```

### Request Parameter

No particular request parameters

### Request Header

#### Required Headers

| Name          | Description                               | Type     | Required   |
| -------------- | ------------------------------ | ------ | ---- |
| Content-Length | HTTP request content length defined in RFC 2616 (bytes).  | String | Yes |

#### Recommended Headers

| Name                | Description                                       | Type        | Required   |
| ------------------- | ---------------------------------------- | ------ | ---- |
| Cache-Control       | The caching policy defined in RFC 2616, which will be saved as Object metadata.       | String | No    |
| Content-Disposition | The file name defined in RFC 2616, which will be saved as Object metadata.       | String | No    |
| Content-Encoding    | The encoding format defined in RFC 2616, which will be saved as Object metadata.       | String | No    |
| Content-Type        | The content type defined in RFC 2616, which will be saved as Object metadata.  | String | No    |
| Expect              | If Expect:  100-continue is used, the request content will not be sent until the receipt of response from server.  | String | No    |
| Expires    | The expiration time defined in RFC 2616, which will be saved as Object metadata.       | String | No    |
| x-cos-content-sha1  | The 160-bit content SHA-1 algorithm check value defined in RFC 3174.     | String | No    |
|  x-cos-meta-*        | The header information allowed to be defined by users. This will be returned as Object metadata. The size is limited to 2K.     | String | No    |
| X-cos-storage-class | Set the storage class of Object. Enumerated values: Standard, Standard_IA, Nearline. The default is Standard (this is only supported for South China region) | String |No    |


#### Permission-related headers

| Name                | Description                                       | Type        | Required   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | Allow users to define file permissions. <br />Valid values: private, public-read | String | No    |
| X-cos-grant-read | Grant read permission to the authorized user <br /> Format: x-cos-grant-read:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |
| x-cos-grant-write        | Grant write permission to the authorized user <br /> Format: x-cos-grant-write:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |
| x-cos-grant-full-control | Grant read and write permissions to the authorized user <br /> Format: x-cos-grant-full-control:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |

### Request Content

File content

## Returned Value

### Response Header

| Name                                | Description                                       | Type        |
| ---- | ---------------------------------------- | ------ |
| ETag | Return the MD5 algorithm check value for the file. ETag value can be used to check whether the Object content has changed.  | String |

### Response Content

No response content

## Example

### Request

```HTTP
PUT /ObjectName HTTP/1.1
Host:zuhaotestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484639384;32557535384&q-key-time=1484639384;32557535384&q-header-list=host&q-url-param-list=&q-signature=5c07b7c67d56497d9aacb1adc19963135b7d00dc
Content-Length: 64

[Object]
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Tue Jan 17 15:50:02 2017
Etag: 020df6d63448ae38a1de7924a68ba1e2
x-cos-request-id: NTg3ZGNjYTlfNDUyMDRlXzUyOTlfMjRj
```


