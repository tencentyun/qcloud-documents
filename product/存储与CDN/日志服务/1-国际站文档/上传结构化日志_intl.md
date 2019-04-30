## Description

This API is used to upload logs to the specified log topic.

## Request

### Request example

```
POST /structuredlog?topic_id=xxxxxxxx-xxxx-xxxx-xxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/x-protobuf

<LogGroupList content packaged as a pd file>
```
#### PB description file

```
package cls;
message LogTime in milliseconds is returned 
{
    message Content
    {
        required string key   = 1;
        required string value = 2;
    }
    required int64   time     = 1; // UNIX Time Format
    repeated Content contents = 2;
}
message LogGroup
{
    repeated Log    logs        = 1;
    optional string contextFlow = 2; // UID used to keep the context consistent
    optional string filename    = 3; // File name
    optional string source      = 4; // Log source, which is generally a server IP
}
message LogGroupList
{
    repeated LogGroup logGroupList = 1;
}
```

### Request line

```
POST /structuredlog
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|--------|-----------------------------------------------|
| topic_id     | string | query| Yes | ID of the log topic to which logs are reported |
| logGroupList | message|  pb | Yes | Description of log attributes |

LogGroup description:

| Field Name | Description |
|--------------|-----------------------------------------------|
| logs         | Log content |
| contextFlow  | UID used to keep the context consistent |
| filename     | File name |
| source       | Log source, which is generally a server IP |

Log description:

| Field Name | Description |
|--------------|-----------------------------------------------|
| time         | Log time (in sec), which is expressed as a UNIX timestamp. Note: Time in milliseconds is returned for some languages, which needs to be converted |
| contents     | Log content |

Content description:

| Field Name | Description |
|--------------|-----------------------------------------------|
| key          | Field key, which cannot start with ```_``` |
| value        | Field value |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Length: 0
```

### Response header

No special response header is used except for the common response header.

### Response parameters

None

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

