## Description
Initiate Multipart Upload request is used for the initialization of multipart upload. After the execution of this request, Upload ID will be returned for the subsequent Upload Part requests.

## Request

### Request Syntax

```http
POST /Object?uploads HTTP 1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header

#### Recommended Headers

| Name                | Description                                       | Type        | Required   |
| ------------------- | ---------------------------------------- | ------ | ---- |
| Cache-Control       | The caching policy defined in RFC 2616, which will be saved as Object metadata.       | String | No    |
| Content-Disposition | The file name defined in RFC 2616, which will be saved as Object metadata.       | String | No    |
| Content-Encoding    | The encoding format defined in RFC 2616, which will be saved as Object metadata.       | String | No    |
| Content-Type        | The content type defined in RFC 2616, which will be saved as Object metadata.  | String | No    |
| Expires    | The expiration time defined in RFC 2616, which will be saved as Object metadata.       | String | No    |
|  x-cos-meta-*        | The header information allowed to be defined by users. This will be returned as Object metadata. The size is limited to 2K.     | String | No    |
| X-cos-storage-class | Set the storage class of Object. Enumerated values: Standard, Standard_IA, Nearline. The default is Standard (this is only supported for South China region) | String |No    |

#### Permission-related headers

| Name                | Description                                       | Type        | Required   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | Allow users to define file permissions. <br />Valid values: private, public-read | String | No    |
| X-cos-grant-read | Grant read permission to the authorized user <br /> Format x-cos-grant-read:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |
| x-cos-grant-write        | Grant write permission to the authorized user <br /> Format: x-cos-grant-write:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |
| x-cos-grant-full-control | Grant read and write permissions to the authorized user <br /> Format: x-cos-grant-full-control:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers

### Response Content

| Name                            | Description            | Type        |
| ----------------------------- | ------------- | --------- |
| InitiateMultipartUploadResult | Indicate all the returned information | Container |
| Bucket                        | The target Bucket of upload in parts | String    |
| Key                           | Name of Object    | String    |
|UploadId                      | ID used in subsequent uploads   | String    |

```xml
<InitiateMultipartUploadResult>
  <Bucket></Bucket>
  <Key></Key>
  <UploadId></UploadId>
</InitiateMultipartUploadResult>
```

## Example

### Request

```HTTP
POST /ObjectName?uploads HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727259;32557623259&q-key-time=1484727259;32557623259&q-header-list=host&q-url-param-list=uploads&q-signature=b5f46c47379aeaee74be7578380b193c01b28045
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Wed Jan 18 16:14:30 2017
Server: tencent-cos
x-cos-request-id: NTg3ZjIzZTZfOWIxZjRlXzZmMzhfMWRj

<InitiateMultipartUploadResult>
	<Bucket>arlenhuangtestsgnoversion</Bucket>
	<Key>ObjectName</Key>
	<UploadId>1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e</UploadId>
</InitiateMultipartUploadResult>
```


