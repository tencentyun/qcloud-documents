## Description
This API (GET Bucket tagging) is used to query a collection of tags for a bucket.

## Request
#### Request example:

```
GET /?tagging HTTP 1.1
Host:<bucketname-APPID>.cos.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```
> Authorization: Auth String (for more information, please see [Request Signature](https://cloud.tencent.com/document/product/436/7778))


### Request line

```
GET /?tagging HTTP/1.1
```

This API allows `GET` request.


### Request header

#### Common header

This request operation is implemented using common request headers. For more information, please see [Common Request Headers](https://cloud.tencent.com/document/product/436/7728 "Common Request Headers").

#### Non-common header

No special request header is used for this request operation.

### Request body
The request body is empty.

## Response
### Response header

#### Common response header

This response uses common response headers. For more information, please see [Common Response Headers](https://cloud.tencent.com/document/product/436/7729 "Common Request Headers").

#### Special response header

No special response header is used for this request operation.

### Response body
Tags obtained successfully.

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


### Error codes
The following describes some special and common errors that may occur with this request:

Error Code | Description | HTTP Status Code
---|---|---
SignatureDoesNotMatch|This error code is returned if the signature provided is invalid | 403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|This error code is returned if the bucket accessed does not exist | 404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
NoSuchTagSet|The bucket contains no tags | 404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## Example

### Request

```
GET /?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: chengwus3sdktj-1251668577.cos.ap-beijing.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4LYUE&q-sign-time=1516362321;1517362371&q-key-time=1516362321;1517362371&q-url-param-list=tagging&q-header-list=host&q-signature=167efc9cf30b79f74a75fde96669e6fd943fe099
```

### Response

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 202
Connection: keep-alive
Date: Fri, 19 Jan 2018 11:46:24 GMT
Server: tencent-cos
x-cos-request-id: NWE2MWRhOTBfOGViMjM1MGFfNTdmNl81NDhhYg==

<?xml version='1.0' encoding='utf-8' ?>
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

