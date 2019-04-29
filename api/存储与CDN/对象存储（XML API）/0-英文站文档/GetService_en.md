## Description
The API Get Service is used to obtain all Bucket lists of the requester. The API does not support anonymous requests. To obtain Bucket list, you should use a request authenticated by Authorization signature. In addition, this API can only obtain the Bucket list under the account to which the AccessID in signature belongs.

## Request

Syntax:
```
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
~~~
GET / HTTP/1.1
~~~
This API allows GET request.

### Request Header

**Common Header**
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.
**Non-common header**
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
<ListAllMyBucketsResult>
  <Owner>
    <ID></ID>
    <DisplayName></DisplayName>
  </Owner>
  <Buckets>
    <Bucket>
      <Name></Name>
      <Location></Location>
      <CreateDate></CreateDate>
    </Bucket>
   ...
  </Buckets>
</ListAllMyBucketsResult>
```


Detailed data content is shown as below:
<style rel="stylesheet">
table th:nth-of-type(1) {
width: 150px;	
}
</style>

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| ListAllMyBucketsResult | No | List all the information returned for the request | Container |

Content of Container node ListAllMyBucketsResult:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:-- |:--|:--|
| Owner | ListAllMyBucketsResult | Provide the information of Bucket owner | Container |
| Buckets | ListAllMyBucketsResult | List all the information of Bucket lists returned for the request | Container |


Content of Container node Owner:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| ID  | ListAllMyBucketsResult.Owner | ID of Bucket owner     | String    |
| DisplayName  | ListAllMyBucketsResult.Owner | Name information of Bucket owner     | String    |

Content of Container node Buckets:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| Bucket  | ListAllMyBucketsResult.Buckets | Information of a single Bucket  | Container    |

Content of Container node Bucket:

| Node Name (Keyword)          | Parent Node | Description                                    | Type        |
| ------------ | ------------------------------------- | --------- |:--|
| Name      | ListAllMyBucketsResult.Buckets.Bucket | Name of Bucket                               | String    |
| Location        | ListAllMyBucketsResult.Buckets.Bucket  | Region in which Bucket resides. For enumerated values, please see the document [Available Regions](https://cloud.tencent.com/document/product/436/6224), such as: ap-beijing, ap-hongkong, eu-frankfurt, etc. | String    |
| CreateDate          | ListAllMyBucketsResult.Buckets.Bucket | Date on which the Bucket was created. It takes an ISO8601 format, for example, 2016-11-09T08:46:32.000Z  | Date   |



## Practical Case

### Request
```
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: Thu, 12 Jan 2016 19:12:22 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1489110340;32468694340&q-key-time=1489110340;32562006340&q-header-list=host&q-url-param-list=&q-signature=cb46d5ce6daed2d3dc0db7130a57193497605620
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 19935
Connection: keep-alive
Date: Thu, 12 Jan 2016 19:12:22 GMT
Server: tencent-cos
x-cos-request-id: NThjMjA1NGFfNTViMjM1XzI0NWRfMjA4OGIx

<ListAllMyBucketsResult>
    <Owner>
	 <ID>qcs::cam::uin/1147518609:uin/1147518609</ID>
	 <DisplayName>1147518609</DisplayName>
    </Owner>
    <Buckets>
        <Bucket>
            <Name>01</Name>
            <Location>ap-beijing</Location>
            <CreateDate>2016-09-13 15:20:15</CreateDate>
        </Bucket>
        <Bucket>
            <Name>0111</Name>
            <Location>ap-hongkong</Location>
            <CreateDate>2017-01-11 17:23:51</CreateDate>
        </Bucket>
        <Bucket>
            <Name>1201new</Name>
            <Location>eu-frankfurt</Location>
            <CreateDate>2016-12-01 09:45:02</CreateDate>
        </Bucket>
   </Buckets>
</ListAllMyBucketsResult>
```


