## Description
The GET Bucket location API is used to obtain the location information of the Bucket. The GET operation uses the location sub-resource to return the location of the Bucket. Only the Bucket holder has the operation permission of the API.

## Request
Request example:
```
GET /?location HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request line

```
GET /?location HTTP/1.1
```

The API accepts `GET` requests.


### Request header

#### Public header

The implementation of this request operation uses the common request header. For details on the common request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728 "Common Request Header").

#### Non-common head

The request operation has no special request header information.

### Request body
The request request body is empty.
## Response
### Response header

#### Common response header

The response uses a common response header. For a detailed description of the public response header, see the [Common Response Header](https://cloud.tencent.com/document/product/436/7729 "Common Response Header") section.

#### API response header

The request operation has no special response header information.

### Response body
The response body is empty if the upload is successful.
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<LocationConstraint>string</LocationConstraint>
```

The specific data is described as follows:

Node Name|Parent Node|Description|Type|Required
---|---|---|---|---
LocationConstraint|None|Describes the location of the bucket. For the enumerated values, see [Availability Zones](https://cloud.tencent.com/document/product/436/6224) documents, such as: ap-beijing, ap-hongkong, eu- Frankfurt et al |String| Yes

###Error Codes

Error Code|Description|HTTP Status Code
---|---|---
SignatureDoesNotMatch| Does not match the rule |403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|The Bucket does not exist|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## Sample Code

### Request

```
GET /?location HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm = sha1 & q-ak = AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO & q-sign-time = 1484817522; 32557713522 & q-key-time = 1484817522; 32557713522 & q-header-list = host & q-url-param-list = location & q-signature = ceb96fc929663dd4d2e6dc0aeb304cdde6761ed
```

### Response

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 92
Connection: keep-alive
Date: Wed, 18 Oct 2014 22:32:00 GMT
Server: tencent-cos
X-cos-request-id: NTg4MDg0NzlfNDYyMDRlXzM0OWFfZjFk

<LocationConstraint>cos.ap-beijing</LocationConstraint
```