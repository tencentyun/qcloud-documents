## Description
Put Bucket CORS is used to set up cross-domain access configurations. You can do so by importing configuration files of XML format (file size limit: 64 KB).

## Request

### Request Syntax

```HTTP
PUT /?cors HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date: date
Content-Length: length
Content-Type:application/xml
Content-MD5:MD5
Authorization: Auth

<XML 文件>
```

### Request Parameter

No particular request parameters

### Request Header

#### Required Headers

| Name          | Description                               | Type     | Required   |
| ----------- | -------------------------------- | ------ | ---- |
| Content-MD5 | 128-bit content MD5 algorithm check value defined in RFC 1864.  | String | Yes |

### Request Content

| Name                | Description                                       | Type        | Required   |
| ----------------- | ---------------------------------------- | --------- | ---- |
| CORSConfiguration | Describe all information regarding cross-domain configurations, may contain up to 100 CORSRule entries            | Container | Yes    |
| CORSRule          | Information of a single configuration<br/>Parent node: CORSRule                 | Container | Yes    |
| ID                | Name of the rule, optional<br/>Parent node: CORSRule                | String    | No    |
| AllowedMethod     | Allowed HTTP operations, enumerated values include Get, Put, Head, Post, Delete<br/>Parent node: CORSRule | Enum      | Yes    |
| AllowedOrigin     | Allowed access source. Wildcard "*" is supported. The protocol, port and domain must be consistent<br/>Parent node: CORSRule | String    | Yes    |
| AllowedHeader     | When sending an OPTIONS request, notify the server end about which custom HTTP request headers are allowed to be used by subsequent requests. Wildcard "*" is supported<br/>Parent node: CORSRule | String    | No    |
| MaxAgeSeconds     | Configure the valid period for the results obtained by OPTIONS request<br/>Parent node: CORSRule   | Integer   | No    |
| ExposeHeadr       | Configure what kind of custom header information from the server end can be received by the browser<br/>Parent node: CORSRule | String    | No    |

```xml
<CORSConfiguration>
  <CORSRule>
    <ID></ID>
    <AllowedOrigin></AllowedOrigin>
      ...
    <AllowedMethod></AllowedMethod>
      ...
    <AllowedHeader></AllowedHeader>
      ...
    <MaxAgeSeconds></MaxAgeSeconds>
    <ExposeHeader></ExposeHeader>
      ...
  </CORSRule>
  <CORSRule>
    ...
  </CORSRule>
  ...
</CORSConfiguration>
```

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

No response content

## Example

### Request
```XML
PUT /?cors HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814927;32557710927&q-key-time=1484814927;32557710927&q-header-list=host&q-url-param-list=cors&q-signature=8b9f05dabce2578f3a79d732386e7cbade9033e3
Content-Type:application/xml
Content-Length: 280

<CORSConfiguration>
  <CORSRule>
    <ID>1234</ID>
    <AllowedOrigin>http://www.qq.com</AllowedOrigin>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedHeader>x-cos-meta-test</AllowedHeader>
    <MaxAgeSeconds>500</MaxAgeSeconds>
    <ExposeHeader>x-cos-meta-test1</ExposeHeader>
  </CORSRule>
</CORSConfiguration>
```
### Response
```XML
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 16:42:21 2017
Server: tencent-cos
x-cos-request-id: NTg4MDdiZWRfOWExZjRlXzQ2OWVfZGY0

```

