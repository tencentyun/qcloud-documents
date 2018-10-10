## Description

This API is used to modify a server group.

## Request

### Request example

```
PUT /machinegroup HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/json

{"group_id": "xxxx-xx-xx-xx-xxxxxxx", "group_name": "testname", "ips": []}
```

### Request line

```
PUT /machinegroup
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| group_id     | string | body | Yes | ID of the server group to be modified |
| group_name   | string | body | No | Name of the server group, which should be unique |
| ips          | JsonArray| body | No | List of IPs under the server group |

> **Note:**
>
> At least one of group_name and ips should be provided.

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

