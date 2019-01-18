## Description

This API is used to delete a server group.

## Request

### Request example

```
DELETE /machinegroup?group_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
DELETE /machinegroup
```

### Request header

No special response header is used except for the common response header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| group_id     | string | query| Yes | ID of the server group to be deleted |

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

