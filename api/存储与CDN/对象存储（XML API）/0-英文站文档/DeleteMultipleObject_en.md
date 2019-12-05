## Description
Delete Multiple Object API request is used for batch deletion of files in specific Bucket. A maximum of 1,000 Objects are allowed to be deleted in batches at a time. COS provides two modes for returned results: Verbose and Quiet. Verbose mode returns the result of deletion of each Object, while Quiet mode only returns the information of the Objects with an error.
><font color="#0000cc">**Note:** </font>
>This request must be used with Content-MD5 to verify the integrity of Body.

## Request

Syntax:
```
POST /?delete HTTP/1.1
Host: <Bucketname>-<AppID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: Auth String

<Delete>
  <Quiet></Quiet>
  <Object>
    <Key></Key>
  </Object>
  <Object>
    <Key></Key>
  </Object>
  ...
</Delete>

```

> Authorization: Auth String (For more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778) chapter)

### Request Line
```
POST /?delete HTTP/1.1
```
This API allows POST request.

### Request Header

#### Common Header
This request operation is implemented using common request header. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728) chapter.

#### Non-common Header
**Required Header**
This request operation is implemented using the following required headers:
<style rel="stylesheet"> table th:nth-of-type(1) { width: 200px;	} </style>

| Name | Description | Type | Required |
|:---|:---|:---|:---|
| Content-Length | HTTP request content length defined in RFC 2616 (in bytes) | String | Yes |
| Content-MD5 | 128-bit content MD5 check value encoded using Base64, defined in RFC 1864. This header is used to check whether the file content has changed | String | Yes |

### Request Body
The specific nodes of the request body for this request are:
```
<Delete>
  <Quiet></Quiet>
  <Object>
    <Key></Key>
  </Object>
  <Object>
    <Key></Key>
  </Object>
  ...
</Delete>

```
Details are described below:

| Node Name (Keyword) | Parent Node | Description | Type | Required |
|:---|:---|:---|:---|:---|
| Delete | None | Indicate the method by which the result is returned for the deletion and the target Object | Container | Yes |
| Quiet | Delete | Boolean. Indicate whether the Quiet mode is enabled. <br> True means Quiet mode is enabled, and False means Verbose mode is enabled. The default is False | Boolean | No |
| Object |Delete | Provide the information of each target Object to be deleted | Container | Yes |
| Key | Delete.Object | Name of target Object file | String | Yes |


## Response

### Response Header
#### Common Response Header 
This response uses common response header. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729) chapter.
#### Specific Response Header
No particular response header for this request operation.

### Response Body
**application/xml** data is returned for the response body, including the complete node data, as show below:
```
<DeleteResult>
  <Deleted>
    <Key></Key>
  </Deleted>
  <Error>
    <Key></Key>
    <Code></Code>
    <Message></Message>
  </Error>
</DeleteResult>
```
See the details below:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:---|:---|:---|
| DeleteResult | None | Indicate the method by which the result is returned for the deletion and the target Object | Container | 

Content of Container node DeleteResult:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:---|:---|:---|
| Deleted | DeleteResult | Indicate the information of Object that has been deleted successfully | Boolean | 
| Error| DeleteResult | Indicate the information of Object that failed to be deleted | Container | 

Content of Container node Deleted:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:---|:---|:---|
| Key | DeleteResult.Deleted | Name of Object | String |

Content of Container node Error:

| Node Name (Keyword) | Parent Node | Description | Type |
|:---|:---|:---|:---|
| Key | DeleteResult.Error | Name of Object that failed to be deleted | String |
| Code | DeleteResult.Error | Error code for failed deletion | String |
| Message | DeleteResult.Error | Error message for failed deletion | String |

## Practical Case

### Request
```
POST /?delete HTTP/1.1
Host: lelu06-1252400000.cn-north.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9SmuG00&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=delete&q-header-list=host&q-signature=c54f22fd92232a76972ba599cba25a8a733d2fef
Content-MD5: yoLiNjQuvB7lu8cEmPafrQ==
Content-Length: 125

<Delete>
  <Quiet>true</Quiet>
  <Object>
    <Key>aa</Key>
  </Object>
  <Object>
    <Key>aaa</Key>
  </Object>
</Delete>

```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 17
Connection: keep-alive
Date: Tue, 22 Aug 2017 12:00:48 GMT
Server: tencent-cos
x-cos-request-id: NTk5YzFjZjBfZWFhZDM1MGFfMjkwZV9lZGM3ZQ==

<DeleteResult/>
```

### Request
```
POST /?delete HTTP/1.1
Host: lelu06-1252440000.cn-north.myqcloud.com
Date: Tue, 22 Aug 2017 12:16:35 GMT
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9SmuG00&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=delete&q-header-list=host&q-signature=c54f22fd92232a76972ba599cba25a8a733d2fef
Content-MD5: V0XuU8V7aqMYeWyD3BC2nQ==
Content-Length: 126

<Delete>
  <Quiet>false</Quiet>
  <Object>
    <Key>aa</Key>
  </Object>
  <Object>
    <Key>aaa</Key>
  </Object>
</Delete>

```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 111
Connection: keep-alive
Date: Tue, 22 Aug 2017 12:16:35 GMT
Server: tencent-cos
x-cos-request-id: NTk5YzIwYTNfMzFhYzM1MGFfMmNmOWZfZWVhNjQ=

<DeleteResult>
 <Deleted>
  <Key>aa</Key>
 </Deleted>
 <Deleted>
  <Key>aaa</Key>
 </Deleted>
</DeleteResult>

```


