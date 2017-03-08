## Description
Options Object is used to implement a pre-request for cross-domain access. That is , an OPTIONS request is sent to the server to verify whether cross-domain operations are possible.

When the CORS configuration does not exist, 403 Forbidden is returned for the request.

## Request

### Request Syntax

```HTTP
OPTIONS /ObjectName HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Origin:Origin
Access-Control-Request-Method:HTTPMethod
Access-Control-Request-Headers:RequestHeader
```

### Request Parameter

No particular request parameters

### Request Header

#### Required Headers

| Name               | Description                                       | Type     | Required   |
| ----------------------------- | --------------- | ------ | ---- |
| Origin                        | Simulate the domain from which the request for cross-domain access is sent | String | Yes    |
| Access-Control-Request-Method | Simulate the HTTP method of the request for cross-domain access | String | Yes    |

#### Recommended Headers

| Name               | Description                                       | Type     | Required   |
| ------------------------------ | ----------- | ------ | ---- |
| Access-Control-Request-Headers | Simulate the header of the request for cross-domain access | String | No    |


### Request Content

No request content

## Returned Value

### Response Header

| Name                             | Description                                       | Type        |
| ----------------------------- | ---------------------------------------- | ------ |
| Access-Control-Allow-Origin   | Simulate the domain from which the request for cross-domain access is sent. If the origin is not allowed, the header will not be returned.       | String |
| Access-Control-Allow-Methods  | Simulate the HTTP method of the request for cross-domain access. If the method is not allowed, the header will not be returned.   | String |
| Access-Control-Allow-Headers  | Simulate the header of the request for cross-domain access. If the simulation of any request header is not allowed, the header will not be returned.  | String |
| Access-Control-Expose-Headers | Returned headers supported by cross-domain request, separated by commas | String |
| Access-Control-Max-Age        | Set the validity period within which the result of OPTIONS request should be returned | String |

### Response Content

No response content

## Example

### Request
```http
OPTIONS /coss3/ObjectName HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Origin:http://www.qq.com
Access-Control-Request-Method:PUT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1487070734;32466654734&q-key-time=1487070734;32559966734&q-header-list=host&q-url-param-list=&q-signature=2ac3ada19910f44836ae0df72a0ec1003f34324b

```
### Response
```http
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Headers: x-cos-meta-test
Access-Control-Allow-Methods: PUT
Access-Control-Allow-Origin: http://www.qq.com
Access-Control-Expose-Headers: x-cos-meta-test1
Access-Control-Max-Age: 500
Date: Tue Feb 14 19:13:51 2017
Server: tencent-cos
x-cos-request-id: NThhMmU2NmZfMmM4OGY3XzZjZGFfMTkzNw==
```

