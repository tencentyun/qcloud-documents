## Description
Get Service API is used to obtain the list of all Buckets under the current account. This API requires Authorization signature for verification and can only obtain the Bucket list under the account to which the AccessID in signature belongs.

## Request

### Request Syntax

```HTTP
GET / HTTP 1.1
Host:service.cos.myqcloud.com
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

| Name                                | Description                                       | Type        |
| ---------------------- | ---------------------------------------- | --------- |
| ListAllMyBucketsResult | List all the information returned for the request                              | Container |
| Owner | Provide the informaiton of owner of Bucket<br/>Parent node: ListAllMyBucketsResult | Contianer |
| UIN                    | UIN of owner of Bucket<br/>Parent node: ListAllMyBucketsResult.Owner | String    |
| Buckets                | List all the information of returned list of Buckets<br/>Parent node: ListAllMyBucketsResult | Contianer |
| Bucket                 | Information of a single Bucket<br/>Parent node: ListAllMyBucketsResult.Buckets | Contianer |
| Name                   | Name of Bucket<br/>Parent node: ListAllMyBucketsResult.Buckets.Bucket | String    |
| CreateDate             | Date on which the Bucket was created. It takes an ISO8601 format, for example, 2016-11-09T08:46:32.000Z<br/>Parent node: ListAllMyBucketsResult.Buckets.Bucket | Date      |

```XML
<ListAllMyBucketsResult>
  <Owner>
    <UIN></UIN>
  </Owner>
  <Buckets>
    <Bucket>
      <Name></Name>
      <CreateDate></CreateDate>
    </Bucket>
   ...
  </Buckets>
</ListAllMyBucketsResult>
```

## Example

### Request

```XML

GET / HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817623;32557713623&q-key-time=1484817623;32557713623&q-header-list=host&q-url-param-list=&q-signature=9ef0c2ad86045f67d03b43cc4359ef861605390e
> 

```

### Response

```XML

HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 428
Connection: keep-alive
Date: Thu Jan 19 17:20:30 2017
Server: tencent-cos
x-cos-request-id: NTg4MDg0ZGVfOTkxZjRlXzEwOGVfZjdh

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>arlenhuangtestsgnoversion</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<Contents>
		<Key>ObjectName</Key>
		<LastModified>Wed Jan 18 16:58:13 2017</LastModified>
		<ETag>"3a0f1fd698c235af9cf098cb74aa25bc"</ETag>
		<Size>10485760</Size>
	</Contents>
</ListBucketResult>

```



