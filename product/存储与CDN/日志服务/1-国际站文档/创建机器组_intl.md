## Description

This API is used to create a server group. The ID of the new server group is returned.

## Request

### Request example

```
POST /machinegroup HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/json

{"group_name": "testname", "ips": ["10.10.10.10", "10.10.10.11"]}
```

### Request line

```
POST /machinegroup
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| group_name   | string | body | Yes | Name of the server group, which should be unique |
| ips          | JsonArray| body| Yes | List of IPs under the server group |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{"group_id": "xxxx-xx-xx-xx-xxxxxxxx"}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|-------------|-----------|---------|-------------------------------|
| group_id    | string    | Yes | Server group ID |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

