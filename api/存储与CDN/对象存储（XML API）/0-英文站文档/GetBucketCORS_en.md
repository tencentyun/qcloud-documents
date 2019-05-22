## Description
The API Get Bucket CORS helps Bucket owner configure the information of cross-origin resource shared on the Bucket. (CORS is short for cross-origin resource sharing, which is based on W3C standards). By default, the Bucket owner has the permission of this API and can grant it to others.

## Request

Syntax:
```
GET /?cors HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization:  Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
~~~
GET /?cors HTTP/1.1
~~~
This API allows GET request.

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
<CORSConfiguration>
  <CORSRule>
    <ID></ID>
    <AllowedOrigin></AllowedOrigin>
    <AllowedMethod></AllowedMethod>
    <AllowedHeader></AllowedHeader>
    <MaxAgeSeconds></MaxAgeSeconds>
    <ExposeHeader></ExposeHeader>
  </CORSRule>
  <CORSRule>
    ...
  </CORSRule>
  ...
</CORSConfiguration>
```
Detailed data content is shown as below: <style  rel="stylesheet"> table th:nth-of-type(1) { width:  200px; }</style>

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| CORSConfiguration | None | Provide all configuration information of cross-origin resource sharing, containing up to 100 CORSRule entries | Container |

Content of Container node CORSConfiguration:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| CORSRule | CORSConfiguration | A single configuration information entry |  Container |

Content of Container node CORSRule:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| ID | CORSConfiguration.CORSRule | ID of the configuration rule (Optional) |  String |
| AllowedOrigin | CORSConfiguration.CORSRule | Allowed access source. Wildcard "*" is supported</br>Format: protocol://domain name[:port], such as: `http://www.qq.com` | String |
| AllowedMethod | CORSConfiguration.CORSRule | Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE | Enum |
| AllowedHeader | CORSConfiguration.CORSRule | When sending an OPTIONS request, notify the server end about which custom HTTP request headers are allowed to be used by subsequent requests. Wildcard "*" is supported |  String |
| MaxAgeSeconds | CORSConfiguration.CORSRule | Configure the valid period for the results obtained by OPTIONS request | Integer |
| ExposeHeader | CORSConfiguration.CORSRule | Configure the custom header information from server end that can be received by browser | String |

## Practical Case

### Request
```
GET /?cors HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484815944;32557711944&q-key-time=1484815944;32557711944&q-header-list=host&q-url-param-list=cors&q-signature=a2d28e1b9023d09f9277982775a4b3b705d0e23e
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 345
Connection: keep-alive
Date: Wed, 28 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdlNGZfNDYyMDRlXzM0YWFfZTBh

<CORSConfiguration> 
  <CORSRule> 
    <ID>1234</ID>  
    <AllowedOrigin>http://www.qq.com</AllowedOrigin>  
    <AllowedMethod>PUT</AllowedMethod>  
    <AllowedHeader>x-cos-meta-test</AllowedHeader>  
    <ExposeHeader>x-cos-meta-test1</ExposeHeader>  
    <MaxAgeSeconds>500</MaxAgeSeconds> 
  </CORSRule> 
</CORSConfiguration>
```


