## Description
The POST Object restore API can recover an object of type `archived` by COS archive. The recovered readable object is temporary. You can set the time to keep it readable and then delete the temporary copy. You can use the Days parameter to specify the expiration time of the temporary object. If this time is exceeded and you do not initiate any copying, extension, etc., the temporary object will be automatically deleted by the system. The temporary object is only a copy of the archive type object, and the archived source object will always exist during this period.

## Request
Request example:
```
POST /ObjectName?restore HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String

Request body
 ```
> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request line

```
POST /{ObjectName}?restore HTTP/1.1
```

The API accepts `POST` requests.


### Request header

#### Common header

The implementation of this request operation uses the common request header. For details on the common request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728 "Common Request Header") section.

#### Non-common header


The request operation has no special request header information.

### Request body
The implementation of the request operation requires a request body.
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<Days>0</Days>
<CASJobParameters>
  <Tier>string</Tier>
</CASJobParameters>
```


The specific data is described as follows:

Node Name (Keyword)|Parent Node|Description|Type|Required
---|---|---|---|---
Days|None|Set the expiration time of the temporary copy|integer|

## Response
### Response header

#### Common response header

The response uses a common response header. For a detailed description of the common response header, see the [Common Response Header](https://cloud.tencent.com/document/product/436/7729 "Common Response Header")
#### API-specific response header


The request operation has no special response header information.

### Responsive body
The request response body is empty.

### Error Codes

Error Code|Description|HTTP Status Code
---|---|---
None|Restoration success|202 [Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)
RestoreAlreadyInProgress| Object is already in recovery |409 [Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)


## Sample Code

### Request

```
POST /arvin/arvin6.txt?restore HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff4500557e0ea057
Host:arvin1-7319456.cn-north.myqcloud.com
Content-Length: 105
Content-Type: application/x-www-form-urlencoded
```

### Response

```
HTTP/1.1 202 Accepted
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-cos
X-cos-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=
```