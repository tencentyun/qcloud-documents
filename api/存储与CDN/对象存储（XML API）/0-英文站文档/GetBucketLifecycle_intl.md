## Description
GET Buket lifecycle is used to query the life cycle configuration of the Bucket. If the Bucket does not have a lifecycle rule configured, it will return `NoSuchLifecycleConfiguration`.

## Request
Grammar example:
```
GET /?lifecycle HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
> Authorization: Auth String (see [Request Signature](https://cloud.tencent.com/document/product/436/7778) for details)

### Request Line
```
GET /?lifecycle HTTP/1.1
```
The API accepts `GET` requests.

### Request header

#### Public Header
The implementation of this request operation uses the public request header. For details on the public request header, see the [Common Request Header](https://cloud.tencent.com/document/product/436/7728) section.

#### Non-public Header
The request operation has no special request header information.

### Request Body
The request body of the request is empty.

## Response

### Response Header
#### Public Response Header
The response uses a common response header. See the [Public Response Header](https://cloud.tencent.com/document/product/436/7729) section for details on the public response header.

#### API-specific Response Header
There is no specific response header for this response.

### Response Body
The content and meaning of each element in the response body is the same as that of the PUT Buket lifecycle. For details, see [PUT Bucket lifecycle]() request body node description.

### Error Codes
The following describes some of the common mistakes and the special circumstances of this request may occur:

|Error Code|HTTP Status Code|Description|
| ------- | -------- | -------- |
|NoSuchBucket|404 Not Found|The  Bucket does not exist|
|NoSuchLifecycleConfiguration|404 Not Found|Lifecycle configuration does not exist. |

For more information on COS error codes, or a list of all product errors, please see the [Error Codes](https://cloud.tencent.com/document/product/436/7730) documentation.

## Sample Code

### Request
```
GET /?lifecycle HTTP/1.1
Host: lifecycletest-73196696.cos.ap-beijing.myqcloud.com
Date: Wed, 16 Aug 2017 12:23:54 GMT
Authorization: q-sign-algorithm = sha1 & q-ak = AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM & q-sign-time = 1502857357; 1502937357 & q-key-time = 1502857357; 1502937357 & q-header-list = host & q-url-param-list = lifecycle & q-signature = da155cda3461bee7422ee95367ac8013ef847e02

```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 312
Date: Wed, 16 Aug 2017 12:23:54 GMT
Server: tencent-cos
X-cos-request-id: NTk5NDM5NWFfMjQ4OGY3Xzc3NGRfMjA=

<LifecycleConfiguration>
  <Rule>
    <ID> id1 </ ID>
    <Filter>
       <Prefix>documents/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <Days>100</Days>
      <StorageClass>STANDARD_IA</StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID>id2</ID>
    <Filter>
       <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>10</Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
```
