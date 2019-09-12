## Description
PUT Bucket cors API is used to set cross-origin resource sharing permission for your Bucket. You can do so by importing configuration files of XML format (file size limit: 64 KB). By default, the Bucket owner has the permission of this API and can grant it to others.

>**Note:**
> The rule permissions created via PUT Bucket cors override all current rules instead of adding a permission rule.

## Request

Syntax:
```
PUT /?cors HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: Auth String

<XML file>
```
> Authorization: Auth String (For more information, please see [Access Control](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
~~~
PUT /?cors HTTP/1.1
~~~ 
This API allows PUT request.
### Request Header

**Common Header**
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

**Non-common Header**
The implementing of this request operation needs the request header with Content-MD5 to verify the integrity of message, as follows:

| Name | Description | Type | Required |
|:---|:-- |:--|:--|
| Content-MD5 | 128-bit content MD5 algorithm check value defined in RFC 1864, which is used to verify that the request body was not corrupted in transit.  | String | Yes |

### Request Body
The implemented of this request operation requires request body. The following is an example of request body with all nodes:
```
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

The detailed data are described as follows: <style  rel="stylesheet"> table th:nth-of-type(1) { width:  200px; }</style>

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| CORSConfiguration | None | Provide all configuration information of cross-origin resource sharing, containing up to 100 CORSRule entries | Container | Yes |

Content of Container node CORSConfiguration:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| CORSRule | CORSConfiguration | Provide Information of a single configuration entry| Container | Yes |

Content of Container node CORSRule:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:-- |:--|:--|:--|
| ID | CORSConfiguration.CORSRule | ID of the configuration rule (optional) | String | No |
| AllowedOrigin | CORSConfiguration.CORSRule | Allowed access source. Wildcard "*" is supported. <br/>Format: protocol://domain name[:port], for example, `http://www.qq.com` | String | Yes |
| AllowedMethod | CORSConfiguration.CORSRule | Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE | Enum | Yes |
| AllowedHeader | CORSConfiguration.CORSRule | When sending an OPTIONS request, notify the server end about the custom HTTP request headers allowed to be used by subsequent requests. Wildcard "*" is supported.| String | No |
| MaxAgeSeconds | CORSConfiguration.CORSRule | Configure the valid period for the results obtained by OPTIONS request | Integer | No |
| ExposeHeader | CORSConfiguration.CORSRule | Configure the custom header information that can be received by browser from server end | String | No |


## Response

### Response Header
#### Common Response Header
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this response.
### Response Body
Null is returned for the response body.

## Practical Case

### Request
```
PUT /?cors HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2017 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814927;32557710927&q-key-time=1484814927;32557710927&q-header-list=host&q-url-param-list=cors&q-signature=8b9f05dabce2578f3a79d732386e7cbade9033e3
Content-Type: application/xml
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
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 10 Mar 2017 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdiZWRfOWExZjRlXzQ2OWVfZGY0

```


