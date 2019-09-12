## Description
Get Bucket request is identical to List Object request. It is used to list partial or all of the Objects under the Bucket. The caller of this API requires Read permission for the Bucket.

## Request

Syntax:
```
GET / HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
~~~
GET / HTTP/1.1
~~~
This API allows GET request.

### Request Parameters
Example of request line that contains all request parameters.
```
GET /?prefix=Prefix&delimiter=Delimiter&encoding-type=EncodingType&marker=Marker&max-keys=MaxKeys HTTP/1.1
```
See the details below: <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

| Parameter Name | Description | Required |
|:---|:-- |:--|
| prefix | Prefix match, used to specify the prefix address of the returned file | No |
| delimiter | Delimiter is a sign. If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed. If Prefix does not exist, the listing process starts from the beginning of the path | No |
| encoding-type | Specify the encoding method of the returned value. Available value: url | No |
| marker | Entries are listed using UTF-8 binary order by default, starting from the marker | No |
| max-keys | Maximum number of entries returned each time. Default is 1,000 | No |

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
<ListBucketResult>
  <Name></Name>
  <Encoding-Type></Encoding-Type>
  <Prefix></Prefix>
  <Marker></Marker>
  <MaxKeys></MaxKeys>
  <IsTruncated></IsTruncated>
  <NextMarker></NextMarker>
  <Contents>
    <Key></Key>
    <LastModified></LastModified>
    <ETag></ETag>
    <Size></Size>
    <Owner>
      <ID></ID>
     </Owner>
     <StorageClass></StorageClass>
  </Contents>
  <CommonPrefixes>
    <Prefix></Prefix>
  </CommonPrefixes>
</ListBucketResult>
```

Detailed data content is shown as below:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| ListBucketResult | None | Store all the information of Get Bucket request result | Container |

Content of Container node ListBucketResult:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Name | ListBucketResult | Provide the information of Bucket | String |
| Encoding-Type | ListBucketResult | Encoding method | String |
| Prefix | ListBucketResult | Prefix match, used to specify the prefix address of the file returned for response request | String |
| Marker | ListBucketResult | Entries are listed using UTF-8 binary order by default, starting from the marker | String |
| MaxKeys | ListBucketResult | Maximum number of entries of the result returned for response request each time | String |
| IsTruncated | ListBucketResult | Whether the response request entry is truncated. Boolean: true, false | Boolean |
| NextMarker | ListBucketResult | If the returned entry is truncated, the returned NextMarker indicates the beginning of the next entry | String |
| Contents | ListBucketResult | Metadata information | Container |
| CommonPrefixes | ListBucketResult | The same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix | Container |

Content of Container node Contents:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Key | ListBucketResult.Contents | Key of Object | String |
| LastModified | ListBucketResult.Contents | The last modification time of Object | Date |
| ETag | ListBucketResult.Contents | MD-5 algorithm check value of the file | String |
| Size | ListBucketResult.Contents | File size (in Byte) | String |
| Owner | ListBucketResult.Contents | Information of Bucket owner | Container |
| StorageClass | ListBucketResult.Contents | The storage class of Object. Enumerated values: STANDARD, STANDARD_IA, NEARLINE | String |

Content of Container node CommonPrefixes:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| Prefix |  ListBucketResult.Contents.CommonPrefixes | Single Common prefix  | Container    |

Content of Container node Owner:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | ListBucketResult.Contents.Owner | AppID of Bucket  | Container    |



## Practical Case

### Request
```
GET / HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213451;32557109451&q-key-time=1484213451;32557109451&q-header-list=host&q-url-param-list=&q-signature=0336a1fc8350c74b6c081d4dff8e7a2db9007dce
```

### Response
```
HTTP /1.1 200 OK
Content-Type: application/xml
Content-Length: 1132
Connection: keep-alive
Vary: Accept-Encoding
Date: Wed, 18 Oct 2014 22:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRjY2VfYmRjMzVfMTc5M182MmIyNg==

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
    <Name>zuhaotestnorth</Name>
    <Encoding-Type>url</Encoding-Type>
    <Prefix>ela</Prefix>
    <Marker/>
    <MaxKeys>1000</MaxKeys>
    <Delimiter>/</Delimiter>
    <IsTruncated>false</IsTruncated>
    <NextMarker>1234.txt</NextMarker>
    <Contents>
        <Key>testL</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>"79f2a852fac7e826c9f4dbe037f8a63b"</ETag>
        <Size>10485760</Size>
        <Owner>
	   <ID>1252375641</ID>
	</Owner>
	<StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testL1</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>"3f9a5dbff88b25b769fa6304902b5d9d"</ETag>
        <Size>10485760</Size>
        <Owner>
	  <ID>1252375642</ID>
	 </Owner>
	 <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testLLL</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>"39bfb88c11c65ed6424d2e1cd4db1826"</ETag>
        <Size>10485760</Size>
        <Owner>
	   <ID>1252375643</ID>
	 </Owner>
	 <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testLOL</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>"fb31459ad10289ff49327fd91a3e1f6a"</ETag>
        <Size>4</Size>
        <Owner>
	   <ID>1252375644</ID>
	 </Owner>
	 <StorageClass>STANDARD</StorageClass>
    </Contents>
</ListBucketResult>
```

