## Description
DELETE Bucket lifecycle is used to delete the life cycle configuration of the Bucket. If the Bucket does not have a lifecycle rule configured, it will return NoSuchLifecycleConfiguration.

##Request
Grammar example:
```
DELETE /?lifecycle HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
>Authorization: Auth String , see the section [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details.

### Request line

```
DELETE /?lifecycle HTTP/1.1
```

The API interface accepts a `DELETE` request.


### Request header

#### Common headers

The implementation of this request operation uses the common request header. For details on the common request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728 "Common Request Header") section.

#### Non-common header


The request operation has no special request header information.

### Request body
The request request body is empty.
## Response
### Response header

#### Common response header

The response uses a common response header. For a detailed description of the public response header, see the [Common Response Header](https://cloud.tencent.com/document/product/436/7729 "Common Response Header") section.

#### Unique response header


The request operation has no special response header information.

### Response
The request response body is empty.

### Error codes

Error code|Description|Status Code
---|---|---
None|Deleted successfully. The response body returns empty |204 [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)
NoSuchBucket|The Bucket does not exist |404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## Sample Code

### Request

```
DELETE /?lifecycle HTTP/1.1
Host:lifecycletest-73196696.cos.ap-beijing.myqcloud.com
Date: Wed, 16 Aug 2017 12:59:09 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1502859472;1502939472&q-key-time=1502859472;1502939472&q-header-list=host&q-url-param-list=lifecycle&q-signature=49c1414c700643f11139219384332a3ec4e9485b
```

### Response

```
HTTP /1.1 204 No Content
Content-Type: application/xml
Date: Wed, 16 Aug 2017 12:59:09 GMT
Server: tencent-cos
X-cos-request-id: NTk5NDQxOWNfMjQ4OGY3Xzc3NGRfMjE=
```