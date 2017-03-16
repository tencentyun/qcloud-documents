## Description
Get Bucket Tagging API is used to acquire tags of specified Bucket.

## Request

### Request Syntax

```HTTP
GET /?tagging HTTP 1.1
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

| Name      | Description                           | Type        |
| ------- | ---------------------------- | --------- |
| Tagging | Describe information regarding all TagSets and Tags            | Container |
| TagSet  | Describe information regarding a series of Tags<br/>Parent node: Tagging  | Container |
| Tag     | Describe information for a single Tag<br/>Parent node: TagSet | Container |
| Key     | Type name of Tag<br/>Parent node: Tag         | String    |
| Value   | Value of Tag<br/>Parent node: Tag            | String    |

```xml
<Tagging>
  <TagSet>
    <Tag>
      <Key></Key>
      <Value></Value>
    </Tag>
    <Tag>
      ...
    </Tag>
  </TagSet>
</Tagging>
```

## Example
### Request

```XML
GET /?tagging HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817283;32557713283&q-key-time=1484817283;32557713283&q-header-list=host&q-url-param-list=tagging&q-signature=b1da7bf83c43fd06fc4c5664ecb832b98966b193

```
### Response

```xml
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 96
Connection: keep-alive
Date: Thu Jan 19 17:14:51 2017
Server: tencent-cos
x-cos-request-id: NTg4MDgzOGJfOWExZjRlXzQ2YTBfZTY0

<Tagging>
	<TagSet>
		<Tag>
			<Key>1</Key>
			<Value>2</Value>
		</Tag>
	</TagSet>
</Tagging>

```

