## Description
List Multiparts Uploads is used to query multipart upload operations that are still in process. Up to 1000 such operations can be listed each time.

## Request

### Request Syntax

```Http
GET /?uploads HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### Request Parameter

| Name               | Description                                       | Type     | Required   |
| ---------------- | ---------------------------------------- | ------ | ---- |
| delimiter        | Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter will be grouped as the same type and defined Common Prefix, then all Common Prefixes will be listed. If Prefix doesn't exist, the listing process will start from the beginning of the path | String | No    |
| encoding-type    | Indicate the encoding method of the returned value                               | String | No    |
| Prefix           | Prefix match, used to specify the prefix address of the returned file                       | String | No    |
| max-uploads      | Max number of entries returned each time, default is 1000                       | String | No    |
| key-marker       | Used together with upload-id-marker<Br/>If upload-id-marker is not specified, entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed<Br/>If upload-id-marker is specified, besides the above entries, those whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed.  | String | No    |
| upload-id-marker | Used together with key-marker<Br/>If key-marker is not specified, upload-id-marker will be ignored<Br/>If key-marker is specified, entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed, and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed.  | String | No    |

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

| Name                                | Description                                       | Type        |
| --------------------------------- | ---------------------------------------- | --------- |
| ListMultipartUploadsResult        | Describe information regarding all multipart upload operations                            | Container |
| Bucket                            | The target Bucket for multipart upload operations<br/>Parent node: ListMultipartUploadsResult | String    |
| Encoding-type                     | Indicate the encoding method of the returned value<br/>Parent node: ListMultipartUploadsResult | String    |
| KeyMarker                         | Entries will be listed starting from this key value<br/>Parent node: ListMultipartUploadsResult | String    |
| UploadIdMarker                    | Entries will be listed starting from this UploadId value<br/>Parent node: ListMultipartUploadsResult | String    |
| NextKeyMarker                     | If the returned entry is truncated, the returned NextKeyMarker indicates the beginning of the next entry<br/>Parent node: ListMultipartUploadsResult | String    |
| NextUploadIdMarker                | If the returned entry is truncated, the returned UploadId indicates the beginning of the next entry<br/>Parent node: ListMultipartUploadsResult | String    |
| MaxUploads                        | Maximum number of entries returned at a time<br/>Parent node: ListMultipartUploadsResult | String    |
| IsTruncated                       | Indicate whether the returned entry is truncated. Boolean: True, False<br/>Parent node: ListMultipartUploadsResult | Boolean    |
| Upload                            | Information regarding each Upload<br/>Parent node: ListMultipartUploadsResult | Container |
| Key                               | Object name<br/>Parent node: Upload                 | Integer   |
| UploadID                          | Indicate the ID of the current multipart upload<br/>Parent node: Upload               | Integer   |
| StorageClass                      | Indicate the storage class of uploaded parts; enumerated values include Standard, Standard_IA, Nearline <br/>Parent node: Upload | String    |
| Initiator                         | Indicate the information of the initiator of current upload. Child node includes UID<br/>Parent node: Upload   | Container |
| UID                               | Developer's APPID<br/>Parent node: Initiator, Owner         | String    |
| Owner                             | Indicate the information of the owner of these uploaded parts. Child node includes UID<br/>Parent node: Upload   | Container |
| Initiated                         | Start time of the multipart upload<br/>Parent node: Upload                 | Date      |
| ListMultipartUploadsResult.Prefix | Prefix match, used to specify the prefix address of the returned file<br/>Parent node: ListMultipartUploadsResult | String    |
| delimiter                         | Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter will be grouped as the same type and defined Common Prefix, then all Common Prefixes will be listed. If Prefix doesn't exist, the listing process will start from the beginning of the path<br/>Parent node: ListMultipartUploadsResult | String    |
| CommonPrefixs                     | The same paths between Prefix and delimiter are grouped as the same type and defined Common Prefix<br/>Parent node: ListMultipartUploadsResult | Container |
| CommonPrefixs.Prefix              | Display detailed CommonPrefixs<br/>Parent node: CommonPrefixs | String    |

```XML
<ListMultipartUploadsResult>
  <Bucket></Bucket>
  <Encoding-type></Encoding-type>
  <KeyMarker></KeyMarker>
  <UploadIdMarker></UploadIdMarker>
  <NextKeyMarker></NextKeyMarker>
  <NextUploadIdMarker></NextUploadIdMarker>
  <MaxUploads></MaxUploads>
  <IsTruncated></IsTruncated>
  <Prefix></Prefix>
  <delimiter></delimiter>
  <Upload>
    <Key></Key>
    <UploadID></UploadID>
    <StorageClass></StorageClass>
    <Initiator>
      <UID></UID>
    </Initiator>
    <Owner>
      <UID></UID>
    </Owner>
    <Initiated></Initiated>
  </Upload>
  <CommonPrefixs>
    <Prefix></Prefix>
  </CommonPrefixs>
</ListMultipartUploadsResult>
```

## Example

### Request

```HTTP
GET /?uploads HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727508;32557623508&q-key-time=1484727508;32557623508&q-header-list=host&q-url-param-list=uploads&q-signature=5bd4759a7309f7da9a0550c224d8c61589c9dbbf
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1203
Date: Wed Jan 18 16:18:37 2017
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
			<UID/>
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
			<UID/>
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
			<UID/>
		</Initiator>
		<Owner>
			<UID>1251668577</UID>
		</Owner>
		<StorageClass>Standard</StorageClass>
		<Initiated>Wed Jan 18 16:14:30 2017</Initiated>
	</Upload>
</ListMultipartUploadsResult>
```


