## Description
Complete Multipart Upload is used to complete the entire multipart upload. You can use this API to complete the upload operation when you have uploaded all parts using Upload Parts. When using this API, you need to provide the PartNumber and ETag for every part in Body, to verify the accuracy of parts.

Merging the parts will take several minutes, thus COS will immediately return status code 200 when the merging process starts. When merging, COS will return blank information periodically to keep the connection active, until the merging process completes, upon which the COS will return the content of the merged parts in Body.

When calling this request, a return of "400 EntityTooSmall" means the uploaded part is smaller than 1 MB; "400 InvalidPart" means the numbers of uploaded parts are discontinuous; "400 InvalidPartOrder" means the part information entries in the request Body are not sorted in ascending order according to their numbers; "404 NoSuchUpload" means the UploadId does not exist.

It is recommended that you complete multipart upload in time or abort the upload operation for the reason that parts that have been uploaded but not aborted will take up storage, incurring cost.

## Request

### Request Syntax

```http
POST /ObjectName?uploadId=UploadId HTTP 1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Content-length: Size
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header
No particular request headers

### Request Content

| Name                      | Description                 | Type        | Required   |
| ----------------------- | ------------------ | --------- | ---- |
| CompleteMultipartUpload | Used to describe all information of the current multipart upload operation    | Container | Yes    |
| Part                    | Used to describe information of every part in the current multipart upload operation  | Container | Yes    |
| PartNumber              | Part number                | String    | Yes    |
| ETag                    | The SHA-1 algorithm check value for every part file | String    | Yes    |

```xml
<CompleteMultipartUpload>
  <Part>
    <PartNumber></PartNumber>
    <ETag></ETag>
  </Part>
  ...
</CompleteMultipartUpload>
```

## Returned Value

### Response Header

No particular response headers

### Response Content

| Name                      | Description               | Type        |
| ----------------------- | ---------------- | --------- |
| CompleteMultipartUpload | Indicate all the returned information         | Container |
| Location                | External network access domain of the created Object | URI       |
| Bucket                  | Target Bucket of the multipart upload operation    | String    |
| Key                     | Object name        | String    |
| ETag                    | MD5 algorithm check value for the merged file  | String    |

```xml
<CompleteMultipartUpload>
  <Location></Location>
  <Bucket></Bucket>
  <Key></Key>
  <ETag></ETag>
</CompleteMultipartUpload>
```

## Example

### Request

```HTTP
POST /ObjectName?uploadId=1484728886e63106e87d8207536ae8521c89c42a436fe23bb58854a7bb5e87b7d77d4ddc48 HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484729794;32557625794&q-key-time=1484729794;32557625794&q-header-list=host&q-url-param-list=uploadId&q-signature=23627c8fddb3823cce4257b33c663fd83f9f820d
Content-Length: 155
Content-Type: application/x-www-form-urlencoded
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 277
Connection: keep-alive
Date: Wed Jan 18 16:58:13 2017
Server: tencent-cos
x-cos-request-id: NTg3ZjJlMjVfNDYyMDRlXzM0YzRfMjc1

<CompleteMultipartUpload>
	<Location>http://arlenhuangtestsgnoversion-1251668577.cossgp.myqcloud.com/ObjectName</Location>
	<Bucket>arlenhuangtestsgnoversion</Bucket>
	<Key>ObjectName</Key>
	<ETag>"3a0f1fd698c235af9cf098cb74aa25bc"</ETag>
</CompleteMultipartUpload>
```


