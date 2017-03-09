## Description

Get Bucket request is identical to List Object request. It is used to list partial or all of the Objects under the Bucket. Read permission is required to initiate this request.

## Request

### Request Syntax

```Http
GET / HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### Request Parameter

| Name            | Description                                       | Type     | Required   |
| ------------- | ---------------------------------------- | ------ | ---- |
| prefix        | Prefix match, used to specify the prefix address of the returned file                       | String | No    |
| delimiter     | Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter will be grouped as the same type and defined Common Prefix, then all Common Prefixes will be listed. If Prefix doesn't exist, the listing process will start from the beginning of the path | String | No    |
| encoding-type | Specify the encoding method of the returned value                               | String | No    |
| marker        | Entries are listed using UTF-8 binary order by default, starting from the marker         | String | No    |
| max-keys      | Max number of entries returned each time, default is 1000                       | String | No    |

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

| Name                    | Description                                       | Type     |
| --------------------- | ---------------------------------------- | ------ |
| Name                  | Bucket name<br/>Parent node: ListBucketResult        | String |
| Prefix                | Prefix match, used to specify the prefix address of the returned file<br/>Parent node: ListBucketResult | String |
| Marker                | Entries are listed using UTF-8 binary order by default, starting from the marker<br/>Parent node: ListBucketResult | String |
| Maxkey                | Max number of entries returned each time<br/>Parent node: ListBucketResult     | String |
| IsTruncated           | Whether the returned entry is truncated. Boolean: True, False<br/>Parent node: ListBucketResult | Boolean |
| NextMarker            | If the returned entry is truncated, NextMarker represents the starting point of the next entry<br/>Parent node: ListBucketResult | String |
| CommonPrefixes        | The same paths between Prefix and delimiter are grouped as the same type and defined Common Prefix<br/>Parent node: ListBucketResult | String |
| Encoding-Type         | Encoding type of Delimiter, used for Marker, Prefix, NextMarker, Key<br/>Parent node: ListBucketResult | String |
| Content               | Meta data information<br/>Parent node: ListBucketResult           | XML    |
| Key                   | Object name<br/>Parent node: ListBucketResult.Contents | String |
| LastModified          | Last modification time of Object<br/>Parent node: ListBucketResult.Contents | Date   |
| Etag                  | SHA-1 algorithm check value of the file<br/>Parent node: ListBucketResult.Contents | String |
| Size                  | File size, measured in Byte<br/>Parent node: ListBucketResult.Contents | String |
| Owner                 | Bucket owner information<br/>Parent node: ListBucketResult.Contents | XML    |
| ID                    | Bucket UID. <br/>Parent node: ListBucketResult.Contents.Owner | String |
| CommonPrefixes.Prefix | A single Common Prefix<br/>Parent node: CommonPrefixes   |        |

```XML
<ListBucketResult>
  <Name></Name>
  <Prefix></Prefix>
  <Marker></Marker>
  <MaxKeys></MaxKeys>
  <IsTruncated></IsTruncated>
  <Contents>
    <Key></Key>
    <LastModified></LastModified>
    <ETag></ETag>
    <Size></Size>
    <Owner>
      <ID></ID>
     </Owner>
  </Contents>
  <CommonPrefixes>
    <Prefix></Prefix>
  </CommonPrefixes>
</ListBucketResult>
```

## Example

### Request

```HTTP
GET / HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213451;32557109451&q-key-time=1484213451;32557109451&q-header-list=host&q-url-param-list=&q-signature=0336a1fc8350c74b6c081d4dff8e7a2db9007dce
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1132
Connection: keep-alive
Vary: Accept-Encoding
Date: Thu Jan 12 17:30:54 2017
Server: tencent-cos
x-cos-request-id: NTg3NzRjY2VfYmRjMzVfMTc5M182MmIyNg==

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>zuhaotestnorth</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<Contents>
		<Key>testL</Key>
		<LastModified>Wed Jan 11 18:57:06 2017</LastModified>
		<ETag>"79f2a852fac7e826c9f4dbe037f8a63b"</ETag>
		<Size>10485760</Size>
	</Contents>
	<Contents>
		<Key>testL1</Key>
		<LastModified>Wed Jan 11 19:02:17 2017</LastModified>
		<ETag>"3f9a5dbff88b25b769fa6304902b5d9d"</ETag>
		<Size>10485760</Size>
	</Contents>
	<Contents>
		<Key>testLLL</Key>
		<LastModified>Wed Jan 11 16:36:08 2017</LastModified>
		<ETag>"39bfb88c11c65ed6424d2e1cd4db1826"</ETag>
		<Size>10485760</Size>
	</Contents>
	<Contents>
		<Key>testLOL</Key>
		<LastModified>Wed Jan 11 17:24:10 2017</LastModified>
		<ETag>"fb31459ad10289ff49327fd91a3e1f6a"</ETag>
		<Size>4</Size>
	</Contents>
	<Contents>
		<Key>tet</Key>
		<LastModified>Wed Jan 11 15:54:02 2017</LastModified>
		<ETag>"83b3ec25cc19626ac073297eba30fbc4"</ETag>
		<Size>10485760</Size>
	</Contents>
</ListBucketResult>
```


