## Description
Put Object - Copy request is used to copy a file from source path to the destination path. The recommended file size is 1M-5G. For any file above 5G, please use multipart upload (Upload - Copy). In the process of copying, file meta-attributes and ACLs can be modified.

Users can use this API to move or rename a file, modify file attributes and create a copy.

If the request is not executed, the relevant error code will be returned; If any error occurs during the execution of request, error code 200 and the error message will be returned.

(Currently this is only supported for South China region)

## Request

### Request Syntax

```HTTP
PUT /destinationObject HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Cache-Control:
Content-Disposition:
Content-Encoding:
Content-Length:
Content-Type:
Expect:
Expires:
Authorization: Auth
X-cos-copy-source:
x-cos-metadata-directive:
x-cos-copy-source-If-Modified-Since:
x-cos-copy-source-If-Unmodified-Since:
x-cos-copy-source-If-Match:
x-cos-copy-source-If-None-Match:
x-cos-storage-class:
```

### Request Parameter

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Header

#### Required Headers
| Name               | Description                                       | Type     | Required   |
| ----------------- | --------------------------------- | ------ | ---- |
| x-cos-copy-source | Absolute path of source file URL. You can specify the history version with the versionid sub-resource | String |Yes    |

#### Recommended Headers

| Name               | Description                                       | Type     | Required   |
| ------------------------------------- | ---------------------------------------- | ------ | ---- |
| X-cos-metadata-directive              | Indicate whether to copy metadata. Enumerated values: Copy, Replaced. The default is Copy. If it is marked as Copy, the copying action will be performed directly, with the user metadata in the Header ignored ; if it is marked as Replaced, the metadata will be modified based on the Header information. If the destination path and the source path are the same, that is, the user attempts to modify the metadata, the value must be Replaced | String | No |
|  x-cos-copy-source-If-Modified-Since   | The action is performed if the Object has been modified since the specified time, otherwise error code 412 will be returned. It can be used with x-cos-copy-source-If-None-Match. Using it with other conditions can cause a conflict.  | String | No    |
| x-cos-copy-source-If-Unmodified-Since | The action is performed if the Object has not been modified since the specified time, otherwise error code 412 will be returned. It can be used with x-cos-copy-source-If-Match. Using it with other conditions can cause a conflict.  | String | No    |
| x-cos-copy-source-If-Match | The action is performed if the Etag of Object is the same as the given one, otherwise error code 412 will be returned. It can be used with x-cos-copy-source-If-Unmodified-Since. Using it with other conditions can cause a conflict.  | String | No    |
| x-cos-copy-source-If-None-Match       | The action is performed if the Etag of Object is different from the given one, otherwise error code 412 will be returned. It can be used with x-cos-copy-source-If-Modified-Since. Using it with other conditions can cause a conflict.  | String | No    |
| x-cos-storage-class                   | storage class. Enumerated values: Standard, Standard_IA, Nearline; the default is Standard | String | No    |

#### Permission-related headers

| Name                | Description                                       | Type        | Required   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | Allow users to define file permissions. <br />Valid values: private, public-read. The default is private.  | String | No    |
| X-cos-grant-read         | Grant read permission to the authorized user <br /> Format: X-cos-grant-read:  uin=" ",uin=" " | String | No    |
| X-cos-grant-write        | Grant write permission to the authorized user <br /> Format: X-cos-grant-write:  uin=" ",uin=" " | String | No    |
| X-cos-grant-full-control | Grant read and write permissions to the authorized user <br /> Format: x-cos-grant-full-control:  uin=" ",uin=" " | String | No    |
| x-cos-meta-*             | Other custom file headers | String | No     |

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

| Name                                | Description                                       | Type        |
| ---------------- | ---------------------------------------- | ------ |
| CopyObjectResult | Return the information of result of copying | String |
| ETag             | Return the SHA-1 algorithm check value for the file. ETag value can be used to check whether the Object content has changed.  | String |
| LastModified     | Return the last modification time of the file, GMT format                         | String |
```XML
<CopyObjectResult>
  <ETag></ETag>
  <LastModified></LastModified>
</CopyObjectResult>
```
## Example

### Request
```http
PUT /coss3/destinationObject HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
X-cos-copy-source:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com/ObjectName
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1487063832;32466647832&q-key-time=1487063832;32559959832&q-header-list=host&q-url-param-list=&q-signature=a1c35e63125977022c7d8a81a5c7918c9c403f68

```

### Response
```http
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 198
Connection: keep-alive
Date: Tue Feb 14 17:22:01 2017
ETag: "72c1bc1feb83a71c229de411c947f110"
Server: tencent-cos
x-cos-request-id: NThhMmNjMzlfMmM4OGY3XzZjZGFfOGM1

```

