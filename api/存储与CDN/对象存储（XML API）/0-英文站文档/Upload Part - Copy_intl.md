## Description
The Upload Part - Copy request implements copying the a file part from the source path to the target path. Use `x-cos-copy-source` to specify the source file, use `x-cos-copy-source-range` to specify byte range (the part size can be 5 MB - 5 GB).

###Version
When the bucket is enabled for multiple versions, x-cos-copy-source identifies the current version of the object being copied. If the current version is a delete tag and x-cos-copy-source does not specify a version, COS considers the object deleted and returns a 404 error. If you specify versionId in x-cos-copy-sourceand and versionId is the delete tag, COS returns an HTTP 400 error because the delete tag is not allowed as the version of x-cos-copy-source.

## Request
Request example:

```
PUT http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com

X-cos-copy-source: string
X-cos-copy-source-range: string
x-cos-copy-source-If-Modified-Since: string
x-cos-copy-source-If-Unmodified-Since: string
x-cos-copy-source-If-Match: string
x-cos-copy-source-If-None-Match: string
X-cos-storage-class: STANDARD
X-cos-acl: public-read
X-cos-grant-read: id="qcs::cam::uin/\<OwnerUin>:uin/<SubUin>"
X-cos-grant-write: id="qcs::cam::uin/\<OwnerUin>:uin/<SubUin>".
X-cos-grant-full-control: id="qcs::cam::uin/\<OwnerUin>:uin/<SubUin>"

Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request line

```
PUT /{ObjectName} HTTP/1.1
```

The API accepts `PUT` requests.

#### Request Parameters

Name|Type|Required|Description
---|---|---|---
partNumber|string|Yes| The sequence number of the file part|
uploadId|string|Yes|To upload a file part, you must first initialize part upload. Then an uploadId is returned, which need to be added to the part upload request.

### Request Headers

#### Common Headers

The implementation of this request operation uses the common request headers. For details on the common request headers, see [Common Request Header](https://cloud.tencent.com/document/product/436/7728 "Common Request Header").

#### Non-common Headers


|Name|Description|Type|Required|
|---|---|---|---|
|x-cos-copy-source|Source file URL path, which can be specified by the versionid sub-resource |string|Yes
|x-cos-copy-source-range|The byte range of the source file, the range value must be in the bytes=first-last format, first and last are offsets based on 0 |string|No|
|x-cos-copy-source-If-Modified-Since|When an Object is modified after a specified time, the operation is performed, otherwise it returns 412. It can be used with x-cos-copy-source-If-None-Match. Conflict occurs for usage with other conditions |string|No|
|x-cos-copy-source-If-Unmodified-Since|When the Object has not been modified after the specified time, the operation is performed, otherwise it returns 412. It can be used with x-cos-copy-source-If-Match. Conflict occurs for usage with other conditions|string|No|
|x-cos-copy-source-If-Match|When the Etag of the Object matches the given, the operation is performed, otherwise 412 is returned. It can be used with x-cos-copy-source-If-Unmodified-Since. Conflict occurs for usage with other conditions |string|No|
|x-cos-copy-source-If-None-Match|When the Etag of the Object is inconsistent with the given, the operation is performed, otherwise it returns 412. It can be used with x-cos-copy-source-If-Modified-Since. Conflict occurs for usage with other conditions|string|No|
|x-cos-storage-class|Sets the storage level of the Object. Values: STANDARD, STANDARD_IA, ARCHIVE, default: STANDARD|string|No|
|x-cos-acl| Defines the ACL property of the Object. Valid values: private, public-read-write, public-read; default: private|string|no|
|x-cos-grant-read|Grant READ access to the specified persons. Format: x-cos-grant-read: id=" ",id=" ";<br>For sub-account, id="qcs::cam::uin/\<OwnerUin>:uin/<SubUin>",<br>For root account, id="qcs::cam::uin/\<OwnerUin>:uin/\<OwnerUin>"|string|No|
|x-cos-grant-write| Grant WRITE access to the specified persons. Format: x-cos-grant-write: id=" ",id=" ";<br>For a sub-account, id="qcs::cam::uin/\<OwnerUin>:uin/<SubUin>",<br>For a root account, id="qcs::cam::uin/\<OwnerUin>:uin/\<OwnerUin>"|String|No|
|x-cos-grant-full-control|Grant READ and WRITE access to the specified persons. Format: x-cos-grant-full-control: id=" ",id=" ";<br>For a sub-account, id="qcs::cam::uin/\<OwnerUin>:uin / <SubUin> ",<br>For a root account, id =" qcs :: cam :: uin / \ <OwnerUin>: uin / \ <OwnerUin> "| string | No |
|x-cos-copy-source-range|The byte range of the source file, the range value must be in the bytes=first-last format, and both first and last are offsets based on 0. For example, bytes=0-9 means that you want to copy the first 10 bytes of data in the source file. If not specified, it means copying the entire file. |Integer|No|

### Request body
The request request body is empty.
## Response
### Response Headers

#### Common Response Headers

The response uses common response headers. For a detailed description of the common response header, see [Common Response Header](https://cloud.tencent.com/document/product/436/7729 "Common Response Header").

#### API Response Headers
Name|Description|Type
---|---|---
X-cos-copy-source-version-id|Copy the version of the source object if multiple versions have been enabled on the source bucket. |string
 X-cos-server-side-encryption | If the object is stored by COS-managed server-side encryption, the response will contain the value of this header and the encryption algorithm used, AES256. | String

### Response Body
The copy is successful and the response body is returned.
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<ETag>string</ETag>
<LastModified>string</LastModified>
```

The specific data is described as follows:

Node Name (Keyword)|Parent Node|Description|Type|
---|---|---|---
ETag|None|Returns the MD5 algorithm check value of the file. The value of ETag can be used to check if the contents of the Object have been changed |string|

## Sample Code

### Request

```
PUT /jimmy/test.file2?partNumber=1&uploadId=1505706248ca8373f8a5cd52cb129f4bcf85e11dc8833df34f4f5bcc456c99c42cd1ffa2f9 HTTP/1.1
User-Agent: curl/7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.19.7 NSS/3.13.1.0 zlib/1.2.3 libidn/1.18 libssh2/1.2.2
Accept: */*
X-cos-copy-source:jimmyyantest-1251668577.cos.ap-shanghai.myqcloud.com/test.file1
X-cos-copy-source-range: bytes=10-100
Host: jimmyyantest-1251668577.cos.ap-shanghai.myqcloud.com
Authorization: q-sign-algorithm = sha1 & q-ak = AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn & q-sign-time = 1507530223; 1508530223 & q-key-time = 1507530223; 1508530223 & q-header-list = & q-url-param-list = & q-signature = d02640c0821c49293e5c289fa07290e6b2f05cb2
```

### Response

```
HTTP /1.1 200 OK
Content-Type: application/xml
Content-Length: 133
Connection: keep-alive
Date: Mon, 04 Sep 2017 04:45:45 GMT
Server: tencent-cos
X-cos-request-id: NTlkYjFjYWJfMjQ4OGY3MGFfNGIzZV9k

<CopyPartResult>
    <ETag>"ba82b57cfdfda8bd17ad4e5879ebb4fe"</ETag>
    <LastModified>2017-09-04T04:45:45</LastModified>
</CopyPartResult>
```