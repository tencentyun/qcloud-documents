## Description
List Multipart Uploads is used to query multipart upload operations that are still in process. Up to 1,000 such operations can be listed for each request.
## Request

Syntax:
```
GET /?uploads HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Parameters

See the details below: <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

| Name       | Description            | Type     | Required   |
| ---------------- | ------------------------------- | ------ | ---- |
| delimiter | Delimiter is a sign. Objects that contain the same string between the prefix , if specified, and the first occurrence of the delimiter after the prefix are grouped under a single result element: common prefix. If you don't specify the prefix parameter, the substring starts at the beginning of the path | String | No    |
| encoding-type | Indicate the encoding method of the returned value. Valid value: url                | String | No    |
| prefix | Specify that the returned Object key must be prefixed with Prefix. </br>Note that the returned key will still contain Prefix when querying with prefix | String | No    |
| max-uploads | Set the maximum number of multipart returned. Valid value: from 1 to 1,000. Default: 1,000                       | String | No    |
| key-marker       | Used together with upload-id-marker<Br/>If upload-id-marker is not specified, entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed<Br/>If upload-id-marker is specified, besides the above entries, those whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. | String | No    |
| upload-id-marker | Used together with key-marker<Br/>If key-marker is not specified, upload-id-marker will be ignored<Br/>If key-marker is specified, entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed, and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. | String | No    |

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
No particular response header for this response.

### Response Body
**application/xml** data is returned for the response body, including the complete node data, as show below:
```
<ListMultipartUploadsResult>
  <Bucket></Bucket>
  <Encoding-Type></Encoding-Type>
  <KeyMarker></KeyMarker>
  <UploadIdMarker></UploadIdMarker>
  <NextKeyMarker></NextKeyMarker>
  <NextUploadIdMarker></NextUploadIdMarker>
  <MaxUploads></MaxUploads>
  <IsTruncated></IsTruncated>
  <Prefix></Prefix>
  <Delimiter></Delimiter>
  <Upload>
    <Key></Key>
    <UploadID></UploadID>
    <StorageClass></StorageClass>
    <Initiator>
      <ID></ID>
	<DisplayName></DisplayName>
    </Initiator>
    <Owner>
      <ID></ID>
	<DisplayName></DisplayName>
    </Owner>
    <Initiated></Initiated>
  </Upload>
  <CommonPrefixs>
    <Prefix></Prefix>
  </CommonPrefixs>
</ListMultipartUploadsResult>
```
Detailed data content is shown as below:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| ListMultipartUploadsResult | Indicate information of all multipart upload operations | Container |

Content of Container node ListMultipartUploadsResult:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Bucket | ListMultipartUploadsResult | The target Bucket for multipart upload | String |
| Encoding-Type | Indicate the encoding method of the returned value. Valid value: url | String | 
| KeyMarker | ListMultipartUploadsResult| Entries will be listed starting from this key value | String |
| UploadIdMarker | ListMultipartUploadsResult| Entries will be listed starting from this UploadId value | String |
| NextKeyMarker | ListMultipartUploadsResult | If the returned entry is truncated, the returned NextKeyMarker indicates the beginning of the next entry | String |
| NextUploadIdMarker | ListMultipartUploadsResult | If the returned entry is truncated, the returned UploadId indicates the beginning of the next entry | String |
| MaxUploads | ListMultipartUploadsResul | Set the maximum number of multipart returned. Valid value: from 1 to 1,000 | String |
| IsTruncated | ListMultipartUploadsResult | Indicate whether the returned entry is truncated. Boolean: TRUE, FALSE | Boolean |
| Prefix | ListMultipartUploadsResult | Specify the returned Object key must be prefixed with Prefix. </br>Note that the returned key will still contain Prefix when querying with prefix | String |
| delimiter | ListMultipartUploadsResult | Delimiter is a sign. Objects that contain the same string between the prefix , if specified, and the first occurrence of the delimiter after the prefix are grouped under a single result element: common prefix. If you don't specify the prefix parameter, the substring starts at the beginning of the path | String |
| Upload | ListMultipartUploadsResult | Information regarding each Upload | Container |
| CommonPrefixs | The same paths between prefix and delimiter are grouped as the same type and defined Common Prefix | Container |

Content of Container node Upload:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Key | ListMultipartUploadsResult.Upload | Name of Object | String |
| UploadID | ListMultipartUploadsResult.Upload | Indicate the ID of current multipart upload | String |
| StorageClass | ListMultipartUploadsResult.Upload | Indicate the storage class of uploaded parts; enumerated values include STANDARD, STANDARD_IA, NEARLINE | String |
| Initiator | ListMultipartUploadsResult.Upload | Indicate the information of the initiator of current upload | Container |
| Owner | ListMultipartUploadsResult.Upload | Indicate the information of the owner of these parts | Container |
| Initiated | ListMultipartUploadsResult.Upload | Start time of the multipart upload | Date |

Content of Container node Initiator:

| Node Name (Keyword)    | Parent Node | Description       | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | ListMultipartUploadsResult.Upload.Initiator |  CAM ID | String  |
| DisplayName | ListMultipartUploadsResult.Upload.Initiator | UIN | String  |

Content of Container node Owner:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | ListMultipartUploadsResult.Upload.Initiator |  CAM ID | String  |
| DisplayName | ListMultipartUploadsResult.Upload.Initiator | UIN | String  |

Content of Container node CommonPrefixs:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| Prefix | ListMultipartUploadsResult.CommonPrefixs | Display detailed CommonPrefixs | String |

## Practical Case

### Request
```
GET /?uploads HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Jan 2015 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727508;32557623508&q-key-time=1484727508;32557623508&q-header-list=host&q-url-param-list=uploads&q-signature=5bd4759a7309f7da9a0550c224d8c61589c9dbbf

```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1203
Date: Wed, 18 Jan 2015 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjI0ZGRfNDQyMDRlXzNhZmRfMjRl

<ListMultipartUploadsResult>
    <Bucket>arlenhuangtestsgnoversion</Bucket>
    <Encoding-Type/>
    <KeyMarker/>
    <UploadIdMarker/>
    <MaxUploads>1000</MaxUploads>
    <Prefix/>
    <Delimiter>/</Delimiter>
    <IsTruncated>false</IsTruncated>
    <Upload>
        <Key>Object</Key>
        <UploadID>1484726657932bcb5b17f7a98a8cad9fc36a340ff204c79bd2f51e7dddf0b6d1da6220520c</UploadID>
        <Initiator>
           <UIN>14847266009/14847266009<UIN/>
        </Initiator>
        <Owner>
            <UID>1251668577</UID>
        </Owner>
        <StorageClass>Standard</StorageClass>
        <Initiated>Wed Jan 18 16:04:17 2017</Initiated>
    </Upload>
    <Upload>
        <Key>Object</Key>
        <UploadID>1484727158f2b8034e5407d18cbf28e84f754b791ecab607d25a2e52de9fee641e5f60707c</UploadID>
        <Initiator>
            <UIN>14847266009/14847266009<UIN/>
        </Initiator>
        <Owner>
            <UID>1251668577</UID>
        </Owner>
        <StorageClass>Standard</StorageClass>
        <Initiated>Wed Jan 18 16:12:38 2017</Initiated>
    </Upload>
    <Upload>
        <Key>ObjectName</Key>
        <UploadID>1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e</UploadID>
        <Initiator>
            <UIN>14847266009/14847266009<UIN/>
        </Initiator>
        <Owner>
            <UID>1251668577</UID>
        </Owner>
        <StorageClass>Standard</StorageClass>
        <Initiated>Wed Jan 18 16:14:30 2017</Initiated>
    </Upload>
</ListMultipartUploadsResult>

```

