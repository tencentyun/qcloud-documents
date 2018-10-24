## Description

This API is used to get the log cursor under a specified log topic, and download collected logs.

## Request

### Request example

```
GET /cursor?topic_id=xxxxxxxx-xxxx-xxxx-xxxx&start=2017-12-28%2014%3A13%3A00 HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /cursor
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|--------|-----------------------------------------------|
| topic_id     | string | query| Yes | Log topic ID |
| start        | string | query| Yes | Start time of the log, which is accurate to minutes. Format: yyyy-mm-dd hh:mm:ss |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 23

{
    "cursor": "1212ssssxxxxxx"
}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|-------------|----------------------|---------|-------------------------------|
| cursor      | string               | Yes | Cursor |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

