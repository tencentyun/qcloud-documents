## Description
Complete Multipart Upload API request is used to complete the entire multipart upload. You must use this API to complete the multipart upload operation of the entire file when you have uploaded all parts using Upload Parts. When using this API, you need to provide the PartNumber and ETag for every part in request Body, to verify the accuracy of parts.
The merging of parts is required and takes several minutes, thus COS returns status code 200 immediately when the merging process begins. During merging, COS may returns blank information periodically to keep the connection active, until the merging process completes, upon which the COS will return the content of the merged parts in Body.
When this API is called, "400 EntityTooSmall" is returned if the uploaded part is smaller than 1 MB.
"400 InvalidPart" is returned if the numbers of uploaded parts are discontinuous.
"400 InvalidPartOrder" is returned if the part information entries in the request Body are not sorted in ascending order according to their numbers.
"404 NoSuchUpload" is returned if the UploadId does not exist when this API is called.
><font color="#0000cc">**Note:** </font>
>It is recommended that you complete multipart upload in time or abort the upload operation for the reason that parts that have been uploaded but not aborted can take up storage, incurring cost.

## Request

Syntax:
```
POST /ObjectName?uploadId=UploadId HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-length: Size
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
POST /ObjectName?uploadId=UploadId HTTP/1.1
```
This API allows POST request.
#### Request parameter <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>
Example of request line that contains all request parameters.
```
POST /ObjectName?uploadId=UploadId HTTP/1.1
```
See the details below:

| Parameter Name | Description | Type | Required |
|:---|:-- |:--|:--|
| uploadId | Indicate the ID of current multipart upload. <br>You can obtain an uploadid when you use the API "Initiate Multipart Upload" to initiate multipart upload. This ID exclusively identifies this multipart data, and the relative position of this multipart in the entire file | String | Yes |

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
No particular request header information for this request operation.

### Request Body
The specific nodes of the request body for this API request are:
```
<CompleteMultipartUpload>
  <Part>
    <PartNumber></PartNumber>
    <ETag></ETag>
  </Part>
  ...
</CompleteMultipartUpload>
```

Detailed data content is shown as below:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| CompleteMultipartUpload | None | Used to describe all information of the current multipart upload operation | Container | Yes |

Content of Container node CompleteMultipartUpload:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| Part |CompleteMultipartUpload| Used to describe information of every part in the current multipart upload operation | Container | Yes |

Content of Container node Part:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| PartNumber | CompleteMultipartUpload.Part | Part number | String | Yes |
| ETag | CompleteMultipartUpload.Part | MD5 algorithm check value for every part file | String | Yes |
## Response

### Response Header
#### Common Response Header 
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this response.

### Response Body
**application/xml** data is returned for the response body, including the complete node data, as show below:
```
<CompleteMultipartUploadResult>
  <Location></Location>
  <Bucket></Bucket>
  <Key></Key>
  <ETag></ETag>
</CompleteMultipartUploadResult>
```
Detailed data content is shown as below:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| CompleteMultipartUploadResult | None | Indicate all the returned information | Container |

Content of Container node CompleteMultipartUploadResult:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Location |CompleteMultipartUploadResult | Domain name for public network access of the created Object | URL |
| Bucket |CompleteMultipartUploadResult| The target Bucket for multipart upload | String |
| Key |CompleteMultipartUploadResult| Name of Object | String |
| ETag |CompleteMultipartUploadResult| MD5 algorithm check value for the merged file | String |

## Practical Case

### Request
```
POST /ObjectName?uploadId=1484728886e63106e87d8207536ae8521c89c42a436fe23bb58854a7bb5e87b7d77d4ddc48 HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Jan 2017 16:17:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484729794;32557625794&q-key-time=1484729794;32557625794&q-header-list=host&q-url-param-list=uploadId&q-signature=23627c8fddb3823cce4257b33c663fd83f9f820d
Content-Length: 155
Content-Type: application/x-www-form-urlencoded
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 277
Connection: keep-alive
Date: Wed, 18 Jan 2017 16:17:03 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjJlMjVfNDYyMDRlXzM0YzRfMjc1

<CompleteMultipartUploadResult>
    <Location>arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com/ObjectName</Location>
    <Bucket>arlenhuangtestsgnoversion</Bucket>
    <Key>ObjectName</Key>
    <ETag>"3a0f1fd698c235af9cf098cb74aa25bc"</ETag>
</CompleteMultipartUploadResult>

```

