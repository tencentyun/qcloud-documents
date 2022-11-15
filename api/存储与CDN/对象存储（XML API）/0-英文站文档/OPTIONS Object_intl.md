## Description
The OPTIONS Object API is used to pre-request an Object cross-origin access configuration. That is, before the cross-origin request is sent, an OPTIONS request is sent to COS. The request contains specific source domain, HTTP method, and header information. nt to determine whether a true cross-origin request can be sent. When the CORS configuration does not exist, the request returns 403 Forbidden. The Bucket's CORS support can be enabled via the PUT Bucket cors interface.

## Request
Request example:
```
OPTIONS /<ObjectName> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request line

```
OPTIONS /{ObjectName} HTTP/1.1
```

The API interface accepts `OPTIONS` requests.


### Request header

#### Common header

The implementation of this request operation uses the common request header. For details on the common request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728 "Common Request Header").

#### Non-common header


Name|Type|Required|Description
---|---|---|---
Origin|string| Yes | request source domain name for cross-origin access
Access-Control-Request-Method|string| Yes | request to simulate cross-origin access HTTP method
Access-Control-Request-Headers|string|No|Simulate the request header for cross-origin access


### Request body
The request request body is empty.
## Response
### Response header

#### Public response header

The response uses a common response header. For a detailed description of the public response header, see the [Common Response Header](https://cloud.tencent.com/document/product/436/7729 "Common Response Header") section.

#### API-specific response header


The response header specific data for this request operation is:

|Name|Type|Description|
|---|---|---|
|Access-Control-Allow-Origin|string| simulates the request source domain name for cross-origin access, this header does not return when the source does not allow |
|Access-Control-Allow-Methods|string|Simulates requests for cross-origin access HTTP methods, this header does not return when the request method does not allow |
|Access-Control-Allow-Headers|string| simulates the request header for cross-origin access. When simulating any request header is not allowed, this header does not return the request header |
|Access-Control-Expose-Headers|string|Simulates requests for cross-origin access HTTP methods, this header does not return when the request method does not allow |
|Access-Control-Max-Age|string|Set the validity period of the OPTIONS request to get results |

### Response body
The request response body is empty.

## Sample Code

### Request

```
OPTIONS /coss3/ObjectName HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Thu, 12 Jan 2017 17:26:53 GMT
Origin: http://www.qq.com
Access-Control-Request-Method: PUT
Authorization: q-sign-algorithm = sha1 & q-ak = AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn & q-sign-time = 1487070734; 32466654734 & q-key-time = 1487070734; 32559966734 & q-header-list = host & q-url-param-list = & q-signature = 2ac3ada19910f44836ae0df72a0ec1003f34324b
```

### Response

```
OPTIONS /<ObjectName> HTTP/1.1
Host: <Bucketname>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Origin: Origin
Access-Control-Request-Method: HTTPMethod
Access-Control-Request-Headers: RequestHeader
Authorization: Auth String
```