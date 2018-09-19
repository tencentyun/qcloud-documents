## Description
Initiate Multipart Upload request is used for the initialization of multipart upload. After the execution of this request, UploadId will be returned for the subsequent Upload Part requests.

## Request

Syntax:
```
POST /Object?uploads HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
POST /Object?uploads HTTP/1.1
```
This API allows POST request.

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
**Recommended Header**
This request operation is implemented using the following recommended request headers: <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

| Name | Description | Type | Required |
|:---|:---|:---|:---|
| Cache-Control | The caching policy defined in RFC 2616, which will be saved as Object metadata. | String | No |
| Content-Disposition | The file name defined in RFC 2616, which will be saved as Object metadata. | String | No |
| Content-Encoding | The encoding format defined in RFC 2616, which will be saved as Object metadata. | String | No |
| Content-Type | The content type defined in RFC 2616, which will be saved as Object metadata. | String | No |
| Expires | The file name defined in RFC 2616, which will be saved as Object metadata. | String | No |
| x-cos-meta-* | The header information allowed to be defined by users, which will be returned as Object metadata. The size is limited to 2K. | String | No |
| X-cos-storage-class | Set the storage class of Object. Enumerated values: Standard, Standard_IA, Nearline. The default is Standard (this is only supported for South China region) | String | No |

**Permission-related headers**
This request operation is implemented using header x-cos-acl in request PUT to set the access permission of Object. Object supports three access permissions: public-read-write, public-read and private. The default permission is private if not set. Users can also be clearly granted with permission of read, write or read-write separately. See the details below:
> For more information on ACL, please see [Put Bucket ACL](https://cloud.tencent.com/document/product/436/7737).

| Name | Description | Type | Required |
|:---|:-- |:--|:--|
| x-cos-acl | Define the ACL attribute of Object. Valid values: private, public-read-write, public-read. Default value: private | String | No |
| x-cos-grant-read |Give the authorized person read access. Format: x-cos-grant-read: id="[OwnerUin]" | String |  No |
| x-cos-grant-write|Gives permission to the authorized person to write. Format: x-cos-grant-write: id="[OwnerUin]" |String |  No |
| x-cos-grant-full-control | Give the authorized person read and write permissions. Format: x-cos-grant-full-control: id="[OwnerUin]" | String| No |

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
<InitiateMultipartUploadResult>
  <Bucket></Bucket>
  <Key></Key>
  <UploadId></UploadId>
</InitiateMultipartUploadResult>
```
Detailed data content is shown as below:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| InitiateMultipartUploadResult | None | Indicate all the returned information | Container |

Content of Container node InitiateMultipartUploadResult:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Bucket | InitiateMultipartUploadResult | The target Bucket of multipart upload | Container |
| Key | InitiateMultipartUploadResult | Name of Object | Container |
| UploadId | InitiateMultipartUploadResult | ID used in subsequent uploads | Container |

## Practical Case

### Request
```
POST /ObjectName?uploads HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727259;32557623259&q-key-time=1484727259;32557623259&q-header-list=host&q-url-param-list=uploads&q-signature=b5f46c47379aeaee74be7578380b193c01b28045

```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjIzZTZfOWIxZjRlXzZmMzhfMWRj

<InitiateMultipartUploadResult>
    <Bucket>arlenhuangtestsgnoversion</Bucket>
    <Key>ObjectName</Key>
    <UploadId>1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e</UploadId>
</InitiateMultipartUploadResult>
```

