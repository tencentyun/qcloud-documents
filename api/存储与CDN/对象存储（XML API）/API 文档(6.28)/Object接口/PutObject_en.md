## Description
Put Object request allows you to upload a local file (Object) to the specified Bucket. This action requires that the user has the WRITE permission for the Bucket.
## Request

Syntax:
```
PUT /<ObjectName> HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
PUT /<ObjectName> HTTP/1.1
```
This API allows PUT request.

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
**Required Header**

The following required headers are needed for the implementation of request operation: <style rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

| Name | Description | Type | Required |
|:---|:-- |:---|:-- |
| Content-Length | HTTP request content length defined in RFC 2616 (in bytes) | String | Yes |

**Recommended Header**
The following recommended request headers are recommended for implementation of this request operation:

| Name | Description | Type | Required |
|:---|:-- |:---|:-- |
| Cache-Control | The caching policy defined in RFC 2616, which will be saved as Object metadata. | String | No |
| Content-Disposition | The file name defined in RFC 2616, which will be saved as Object metadata. | String | No |
| Content-Encoding | The encoding format defined in RFC 2616, which will be saved as Object metadata. | String | No |
| Content-Type | The content type defined in RFC 2616, which will be saved as Object metadata. | String | No |
| Expect | If Expect: 100-continue is used, the request content will not be sent until the receipt of response from server. | String | No |
| Expires | The expiration time defined in RFC 2616, which will be saved as Object metadata. | String | No |
| x-cos-meta-* | The header information allowed to be defined by users, which will be returned as Object metadata. The size is limited to 2 KB. | String | No |
| X-cos-storage-class | Set the storage class of Object. Enumerated values: STANDARD, STANDARD_IA. The default is STANDARD (this is only supported for South China region) | String | No |

**Permission-related headers**
This request operation is implemented using header x-cos-acl in request Put to set the access permission of Object. Three access permissions are available: public-read-write, public-read and private. The default permission is private if not set. Users can also be clearly granted with permission of read, write or read-write separately. See the details below:
> For more information on ACL, please see [Put Bucket ACL](https://cloud.tencent.com/document/product/436/7737).

| Name | Description | Type | Required |
|:---|:-- |:--|:--|
| x-cos-acl | Define the ACL attribute of Object. Valid values: private, public-read-write, public-read. Default value: private | String | No |
| x-cos-grant-read |Give the authorized person read access. Format: x-cos-grant-read: id="[OwnerUin]" | String |  No |
| x-cos-grant-write|Gives permission to the authorized person to write. Format: x-cos-grant-write: id="[OwnerUin]" |String |  No |
| x-cos-grant-full-control | Give the authorized person read and write permissions. Format: x-cos-grant-full-control: id="[OwnerUin]" | String| No |

### Request Body
The request body of this request is file Object.

## Response

### Response Header
#### Common Response Header
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
The response header of the request operation is as follows:

| Name | Description | Type |
|:---|:-- |:-- |
| ETag | Return the MD5 algorithm check value for the file. ETag value can be used to check whether the Object is corrupted in the upload process. | String |

### Response Body
Null is returned for the response body.

## Practical Case

### Request
```
PUT /filename.jpg HTTP/1.1
Host: zuhaotestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2015 20:32:00 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484639384;32557535384&q-key-time=1484639384;32557535384&q-header-list=host&q-url-param-list=&q-signature=5c07b7c67d56497d9aacb1adc19963135b7d00dc
Content-Length: 64

[Object]
```

### Response
```
HTTP /1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Wed, 28 Oct 2015 20:32:00 GMT
Etag: 020df6d63448ae38a1de7924a68ba1e2
x-cos-request-id: NTg3ZGNjYTlfNDUyMDRlXzUyOTlfMjRj

```

