## Description
Put Bucket Tagging API is used to tag specified Bucket. Tags are used to organize and manage relevant Buckets. Status code 400 will be returned if the request sets different Values for the same Key. Status code 204 will be returned if the request succeeds.

## Request

### Request Syntax

```HTTP
PUT /?tagging HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Content-Type:application/xml
Authorization: Auth

[XML]
```

### Request Parameter

No particular request parameters

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

| Name      | Description                          | Type        | Required   |
| ------- | --------------------------- | --------- | ---- |
| Tagging | Describe information regarding all TagSets and Tags           | Container | Yes    |
| TagSet  | Describe information regarding a series of Tags<br/>Parent node: Tagging | Container | Yes    |
| Tag     | Describe information for a single Tag<br/>Parent node: TagSet   | Container | Yes    |
| Key     | Type name of Tag<br/>Parent node: Tag        | String    | Yes    |
| Value   | Value of Tag<br/>Parent node: Tag           | String    | Yes    |

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

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

No response content

## Example
### Request
```xml
PUT /?tagging HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817032;32557713032&q-key-time=1484817032;32557713032&q-header-list=host&q-url-param-list=tagging&q-signature=0a99e59b753c26b807e4b372560b0d026d26af26
Content-Type:application/xml
Content-Length: 75

<Tagging>
  <TagSet>
    <Tag>
      <Key>1</Key>
      <Value>2</Value>
    </Tag>
  </TagSet>
</Tagging>
```
### Response
```xml
HTTP/1.1 204
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 17:12:29 2017
Server: tencent-cos
x-cos-request-id: NTg4MDgyZmRfOTkxZjRlXzEwNjRfZWI2

```


