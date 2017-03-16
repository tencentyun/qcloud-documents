## Description
List Parts is used to query uploaded parts in a specific multipart upload.

## Request

### Request Syntax

```Http
GET /ObjectName?uploadId=UploadId HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### Request Parameter

| Name                | Description                                       | Type        | Required   |
| ------------------ | --------------------------------- | ------ | ---- |
| UploadID           | Indicate the ID of current multipart upload                       | String | Yes |
| Encoding-type      | Indicate the encoding method of the returned value                               | String | No    |
| max-parts      | Maximum number of entries returned at a time; The default is 1000                       | String | No    |
| part-number-marker | Entries are listed in UTF-8 binary order by default, starting from marker         | String | No    |

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

No request content

## Returned Value

### Response Header

No response headers

### Response Content

| Name                             | Description                                       | Type        |
| -------------------- | ---------------------------------------- | --------- |
| ListPartsResult      | Provide all the information of current multipart upload. Child nodes include: Bucket, Encoding-type, Key, UploadID, Initiator, Owner, PartNumberMarker, NextPartNumberMarker, MaxParts, IsTruncated, Part | Container |
| Bucket | The target Bucket of multipart upload <br/>Parent node: ListPartsResult    | String    |
| Encoding-type      | Indicate the encoding method of the returned value<br/>Parent node: ListPartsResult       | String    |
| Key                  | Name of Object<br/>Parent node: ListPartsResult        | String    |
| UploadID           | Indicate the ID of the current multipart upload<br/>Parent node: ListPartsResult      | Container    |
| Initiator            | Indicate the information of the initiator of current upload. Child node: UID <br/> Parent node: ListPartsResult | Container |
| UID                  | APPID of developer                                 | String    |
| Owner                | Indicate the information of the owner of these parts. Child node: UID<br/>parent node: ListPartsResult | Container |
| StorageClass | Indicate the storage class of these parts; enumerated values: Standard, Standard_IA, Nearline <br/> Parent node: ListPartsResult | String |
| PartNumberMarker     | Entries are listed in UTF-8 binary order by default, starting from marker<br/>Parent node: ListBucketResult | String    |
| NextPartNumberMarker | If the returned entry is truncated, the returned NextMarker indicates the beginning of the next entry<br/>Parent node: ListPartsResult | String    |
|MaxParts             | Maximum number of entries returned at a time<br/>Parent node: ListPartsResult      | String    |
| IsTruncated          | Indicate whether the returned entry is truncated. Boolean: True, False<br/>Parent node: ListPartsResult | Boolen    |
| Part                 | Indicate the information of each part<br/>Parent node: ListPartsResult | Container |
| PartNumber           | Part No.<br/> Parent node: Part                        | String    |
| LastModified          | Indicate the last modification time of the part<br/>Parent node: Part                    | Date      |
| Etag                 | SHA-1 algorithm check value of part<br/>Parent node: Part              | String    |
| Size                 | Size of part (in bytes)<br/>Parent node: Part                  | String    |

```XML
<ListPartsResult>
  <Bucket></Bucket>
  <Encoding-type></Encoding-type>
  <Key></Key>
  <UploadID></UploadID>
  <Initiator>
    <UID></UID>
  </Initiator>
  <Owner>
    <UID></UID>
  </Owner>
  <StorageClass></StorageClass>
  <PartNumberMarker></PartNumberMarker>
  <NextPartNumberMarker></NextPartNumberMarker>
  <MaxParts></MaxParts>
  <IsTruncated></IsTruncated>
  <Part>
    <PartNumber></PartNumber>
    <LastModified></LastModified>
    <Etag></Etag>
    <Size></Size>
  </Part>
</ListPartsResult>
```

## Example

### Request

```HTTP
GET /coss3/test10M_2?uploadId=14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0&max-parts=1 HTTP/1.1
Host:burning-1251668577.cn-east.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1484643123;1484646723&q-key-time=1484643123;1484646723&q-header-list=host&q-url-param-list=max-parts;uploadId&q-signature=b8b4055724e64c9ad848190a2f7625fd3f9d3e87
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 661
Connection: keep-alive
Date: Tue Jan 17 16:52:08 2017
x-cos-request-id: NTg3ZGRiMzhfMmM4OGY3XzdhY2NfYw==

<ListPartsResult>
	<Bucket>burning</Bucket>
	<Encoding-type/>
	<Key>test10M_2</Key>
	<UploadId>14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0</UploadId>
	<Initiator>
		<UID/>
	</Initiator>
	<Owner>
		<UID>1251668577</UID>
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
