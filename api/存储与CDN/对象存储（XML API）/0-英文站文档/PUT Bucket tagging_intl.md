## Description
COS supports setting a tag for an existing bucket. This API (PUT Bucket tagging) is used to set a tag for a bucket, and supports adding a key-value pair to an existing bucket as a tag.

## Request
#### Request example:

```
PUT /?tagging HTTP 1.1
Host:<bucketname-APPID>.cos.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```
> Authorization: Auth String (for more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778))

### Request header

#### Common header

This request operation is implemented using common request headers. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728 "Common Request Headers").

#### Non-common header

No special request header is used for this request operation.

### Request body
A collection of tags to be set.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<Tagging>
  <TagSet>
    <Tag>
      <Key>string</Key>
      <Value>string</Value>
    </Tag>
  </TagSet>
</Tagging>
```

The detailed data are described as follows:

Node Name (Keyword) | Parent Node | Description | Type | Required
---|---|---|---|---
Tagging| None | A collection of tags |Container|Yes

Content of Container node Tagging:

Node Name (Keyword) | Parent Node | Description | Type | Required
---|---|---|---|---
TagSet|Tagging|A collection of tags |Container|Yes

Content of Container node TagSet:

Node Name (Keyword) | Parent Node | Description | Type | Required
---|---|---|---|---
Tag|Tagging.TagSet|A collection of tags (10 tags at most) |Containers|Yes

Content of Container node Tag:

Node Name (Keyword) | Parent Node | Description | Type | Required
---|---|---|---|---
Key|Tagging.TagSet.Tag|Tag key, with a length limited to 128 characters comprised of letters, numbers, spaces, +, -, _, =, ., :, and / |string|Yes
Value|Tagging.TagSet.Tag|Tag value, with a length limited to 256 characters comprised of letters, numbers, spaces, +, -, _, =, ., :, and / |string|Yes


## Response
### Response header

#### Common response header

This response uses common response headers. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729 "Common Request Headers").

#### Special response header


No special response header is used for this request operation.

### Response body
The response body is empty.

### Error codes
The following describes some special and common errors that may occur with this request:

Error Code | Description | HTTP Status Code
---|---|---
None|A null is returned for the response body upon a successful configuration | 204 [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)
SignatureDoesNotMatch|This error code is returned if the signature provided is invalid | 403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|This error code is returned if the bucket to which a rule should be added does not exist | 404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
MalformedXML|XML format is invalid. See restful API documentation for details. | 400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
BadRequest|This error code is returned if the number of tags allowed for a bucket exceeds the limit (10 tags at most). | 400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidTag|Tag key and tag value contain a reserved string cos: | 400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidTag|Tag key exceeds 128 characters or tag value exceeds 256 characters | 400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidTag|Tag key and tag value contain invalid characters. Both of them only support letters, numbers, spaces, +, -, _, =, ., :, and / | 400[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidTag|Tag key and tag value contain invalid characters. Both of them only support letters, numbers, spaces, +, -, _, =, ., :, and / | 400[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)


## Example

### Request

```
PUT /?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: chengwus3sdktj-1251668577.cos.ap-beijing.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4LYUE&q-sign-time=1516361923;1517361973&q-key-time=1516361923;1517361973&q-url-param-list=tagging&q-header-list=content-md5;host&q-signature=71251feb4501494edcfbd01747fa873003759404
Content-Md5: LIbd5t5HLPhuNWYkP6qHcQ==
Content-Length: 127
Content-Type: application/xml

<Tagging>
    <TagSet>
        <Tag>
            <Key>age</Key>
            <Value>18</Value>
        </Tag>
        <Tag>
            <Key>name</Key>
            <Value>xiaoming</Value>
        </Tag>
    </TagSet>
</Tagging>
```

### Response

```
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 19 Jan 2018 11:40:22 GMT
Server: tencent-cos
x-cos-request-id: NWE2MWQ5MjZfMTBhYzM1MGFfMTA5ODVfMTVjNDM=
```

