## Description
Get Bucket CORS is used to read cross-domain access configurations.

## Request

### Request Syntax

```HTTP
GET /?cors HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

| Name                | Description                                       | Type        | Required   |
| ----------------- | ---------------------------------------- | --------- | ---- |
| CORSConfiguration | Describe all information regarding cross-domain configurations, may contain up to 100 CORSRule entries            | Container | Yes    |
| CORSRule          | Information of a single configuration<br/>Parent node: CORSRule                 | Container | Yes    |
| ID                | Name of the rule, optional<br/>Parent node: CORSRule                | String    | No    |
| AllowedMethod     | Allowed HTTP operations, enumerated values include Get, Put, Head, Post, Delete<br/>Parent node: CORSRule | Enum      | Yes    |
| AllowedOrigin     | Allowed access source. Wildcard "*" is supported<br/>Parent node: CORSRule        | String    | Yes    |
| AllowedHeader     | When sending an OPTIONS request, notify the server end about which custom HTTP request headers are allowed to be used by subsequent requests<br/>Parent node: CORSRule | String    | No    |
| MaxAgeSeconds     | Configure the valid period for the results obtained by OPTIONS request<br/>Parent node: CORSRule   | Integer   | No    |
| ExposeHeadr       | Configure what kind of custom header information from the server end can be received by the browser<br/>Parent node: CORSRule | String    | No    |

```xml
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

## Example
### Request
```xml
GET /?cors HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484815944;32557711944&q-key-time=1484815944;32557711944&q-header-list=host&q-url-param-list=cors&q-signature=a2d28e1b9023d09f9277982775a4b3b705d0e23e

```
### Response
```xml
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 345
Connection: keep-alive
Date: Thu Jan 19 16:52:31 2017
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


