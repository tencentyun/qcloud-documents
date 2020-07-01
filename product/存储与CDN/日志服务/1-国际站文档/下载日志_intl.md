## Description

This API is used to download logs using cursor.

## Request

### Request example

```
GET /log?topic_id=xxxxxxxx-xxxx-xxxx-xxxx&cursor=xxxxxx&count=10 HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
```

### Request line

```
GET /log
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|--------|-----------------------------------------------|
| topic_id     | string | query| Yes | Log topic ID |
| cursor       | string | query| Yes | The cursor got via the API "Get Log Cursor" |
| count        | string | query| Yes | Number of logs to be downloaded, which is limited to 1,000 |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/x-protobuf
Content-Length: 23
x-cls-cursor: xxxxxx
x-cls-count:10

<LogGroupList content packaged as a pb file>
```

### Response header

| Header Name | Description |
|------------------------|--------------------------------|
| x-cls-cursor           | The current log cursor, which can be used to download logs next time |
| x-cls-count            | Number of logs downloaded for the current request |

### Response parameters

The packaged content of the LogGroupList object. For more information on pd file, please see the API [Upload Structured Logs](https://cloud.tencent.com/document/product/614/16873).

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

