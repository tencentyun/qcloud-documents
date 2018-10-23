## Description
List Parts is used to query the uploaded parts when uploading particular parts, which lists all the uploaded parts under a specified UploadId.

## Request

Syntax:
```
GET /ObjectName?uploadId=UploadId HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String

```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
GET /ObjectName?uploadId=UploadId HTTP/1.1
```
This API allows GET request.
### Request Parameters

See the details below: <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

| Parameter Name | Description | Type | Required |
|:---|:---|:---|:---|
| uploadId | Indicate the ID of current multipart upload. <br>You can obtain an uploadid when you use the API "Initiate Multipart Upload" to initiate multipart upload. This ID exclusively identifies this multipart data, and the relative position of this multipart in the entire file. | String | Yes |
| encoding-type | Indicate the encoding method of the returned value | String | No |
| max-parts | Maximum number of entries returned each time. Default is 1,000 | String | No |
| part-number-marker | Entries are listed in UTF-8 binary order by default, starting from marker | String | No |

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
<ListPartsResult>
  <Bucket></Bucket>
  <Encoding-type></Encoding-type>
  <Key></Key>
  <UploadId></UploadId>
  <Owner>
    <ID></ID>
    <DisplayName></DisplayName>
  </Owner>
  <PartNumberMarker></PartNumberMarker>
  <Initiator>
    <ID></ID>
    <DisplayName></DisplayName>
  </Initiator>
  <StorageClass></StorageClass>
  
  <NextPartNumberMarker></NextPartNumberMarker>
  <MaxParts></MaxParts>
  <IsTruncated></IsTruncated>
  <Part>
    <PartNumber></PartNumber>
    <LastModified></LastModified>
    <ETag></ETag>
    <Size></Size>
  </Part>
</ListPartsResult>
```
Detailed data content is shown as below:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| ListPartsResult | None | Indicate information of the current multipart upload operation | Container | Yes |

Content of Container node ListPartsResult:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Bucket | ListPartsResult | The target Bucket for multipart upload | String |
| Encoding-type | ListPartsResult | Indicate the encoding method of the returned value | String |
| Key | ListPartsResult | Name of Object | String |
| UploadId | ListPartsResult | Indicate the ID of current multipart upload | String |
| Initiator | ListPartsResult | Indicate the information of the initiator of current upload | Container |
| Owner | ListPartsResult| Indicate the information of the owner of these parts | Container |
| StorageClass | ListPartsResult | Indicate the storage class of uploaded parts; enumerated values include Standard, Standard_IA, nearline | String |
| PartNumberMarker | ListPartsResult | Entries are listed using UTF-8 binary order by default, starting from marker | String |
| NextPartNumberMarker | ListPartsResult | If the returned entry is truncated, the returned NextMarker indicates the beginning of the next entry | String |
| MaxParts | ListPartsResult | Maximum number of entries returned at a time | String |
| IsTruncated | ListPartsResult | Indicate whether the returned entry is truncated. Boolean: TRUE, FALSE | Boolean |
| Part | ListPartsResult | Indicate the information of each part | Container |

Content of Container node Initiator:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| ID | ListPartsResult.Initiator | Unique ID of the creator | String |
| DisplayName | ListPartsResult.Initiator | Name of creator | String |

Content of Container node Owner:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| ID | ListPartsResult.Owner | Unique ID of the user | String |
| DisplayName | ListPartsResult.Owner | Name of User | String |

Content of Container node Part:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| PartNumber | ListPartsResult.Part | Part number | String |
| LastModified | ListPartsResult.Part | The last modification time of part | Date |
| ETag | ListPartsResult.Part | MD-5 algorithm check value of Object | String |
| Size | ListPartsResult.Part | Party size (in bytes) | String |

## Practical Case

### Request
```
GET /coss3/test10M_2?uploadId=14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0&max-parts=1 HTTP/1.1
Host:burning-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Jan 2017 16:17:03 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1484643123;1484646723&q-key-time=1484643123;1484646723&q-header-list=host&q-url-param-list=max-parts;uploadid&q-signature=b8b4055724e64c9ad848190a2f7625fd3f9d3e87
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 661
Connection: keep-alive
Date: Wed, 18 Jan 2017 16:17:03 GMT
x-cos-request-id: NTg3ZGRiMzhfMmM4OGY3XzdhY2NfYw==

<ListPartsResult>
    <Bucket>burning</Bucket>
    <Encoding-type/>
    <Key>test10M_2</Key>
    <UploadId>14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0</UploadId>
    <Initiator>
        <ID>123456789</ID>
        <DisplyName>123456789</DisplyName>
    </Initiator>
    <Owner>
        <ID>qcs::cam::uin/156545789:uin/156545789</ID>
        <DisplyName>156545789</DisplyName>
    </Owner>
    <PartNumberMarker>0</PartNumberMarker>
    <Part>
        <PartNumber>1</PartNumber>
        <LastModified>Tue Jan 17 16:43:37 2017</LastModified>
        <ETag>"a1f8e5e4d63ac6970a0062a6277e191fe09a1382"</ETag>
        <Size>5242880</Size>
    </Part>
    <NextPartNumberMarker>1</NextPartNumberMarker>
    <StorageClass>Standard</StorageClass>
    <MaxParts>1</MaxParts>
    <IsTruncated>true</IsTruncated>
</ListPartsResult>
```

