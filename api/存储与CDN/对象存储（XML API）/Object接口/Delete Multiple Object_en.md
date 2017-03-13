## Description
Delete Multiple Object request is used for batch deletion of files. A maximum of 1000 files are allowed to be deleted at a time. COS provides two modes for returned results: Verbose and Quiet. Verbose mode will return the result of deletion of each Object, while Quiet mode only returns the information of the Objects with an error.

This request must be used with x-cos-sha1 to verify the integrity of Body.

## Request

### Request Syntax

```Http
POST /?delete HTTP/1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date: date
Content-Length:length
Content-Type:application/xml
Content-MD5:MD5
Authorization: authorization string

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

### Request Parameter

No particular request parameters

### Request Header

#### Required Headers

| Name             | Description                               | Type     | Required   |
| -------------- | -------------------------------- | ------ | ---- |
| Content-Length | HTTP request content length defined in RFC 2616 (bytes).    | String | Yes |
| Content-MD5 | 128-bit content MD5 algorithm check value defined in RFC 1864.  | String | Yes |

### Request Content

| Name             | Description                               | Type     | Required   |
| ------ | ---------------------------------------- | --------- | ---- |
| Delete | Indicate the method by which the result is returned for the deletion and the target Object | Container | Yes |
| Quiet | Boolean.Indicate whether the Quiet mode is enabled. True means Quiet mode is enabled, and False means Verbose mode is enabled. The default is False. <Br/> Parent node: Delete | Boolean   | No    |
| Object | Provide the information of each target file to be deleted | Container | Yes |
| Key    | Target file name                                    | String    | Yes    |

```xml
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


## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers.

### Response Content

| Name      | Description                               | Type        |
| ------------ | ------------------------------------- | --------- |
| DeleteResult | Indicate the returned result of the deletion                           | Container |
| Deleted      | Indicate the information of Object that has been deleted successfully <Br/> Parent node: DeleteResult | Container |
| Key          | Name of Object<Br/>Parent node: Deleted, Error       | String    |
| Error      | Indicate the information of Object that failed to be deleted<Br/> Parent node: DeleteResult | Container |
| Code         | Error code for failed deletion                              | String    |
| Message | Message indicating the deletion error                                | String    |

```xml
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
## Example
### Request
```http
POST /coss3/?delete HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Content-MD5:35385efb5ba5134bffb192bfa17c3d5e
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1487065662;32466649662&q-key-time=1487065662;32559961662&q-header-list=host&q-url-param-list=delete&q-signature=286ef48c81f1652c37c635f0fb7db7a2150aa5ba
Content-Length: 75
Content-Type: application/x-www-form-urlencoded
```
### Response
```http
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 79
Connection: keep-alive
Date: Tue Feb 14 17:49:12 2017
Server: tencent-cos
x-cos-request-id: NThhMmQyOTdfMmM4OGY3XzZjZGFfY2Mx

<DeleteResult>
	<Deleted>
		<Key>ObjectName</Key>
	</Deleted>
</DeleteResult>

```


