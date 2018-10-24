## Description

This API is used to get the information on a server group.

## Request

### Request example

```
GET /machinegroup?group_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /machinegroup
```

### Request header

No special response header is used except for the common response header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| group_id     | string | query| Yes | ID of the group to be queried |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
  "group_id": "xxxx-xx-xx-xx-xxxxxxxx",
  "group_name": "testname",
  "ips": [
    "10.10.10.10","10.10.10.11"
  ],
  "create_time": "2017-08-08 12:12:12"
}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| group_id   | string | Yes | Server group ID |
| group_name | string | Yes | Server group name |
| ips        | JsonArray| Yes | List of IPs under the server group |
| create_time| string | No | Creation time |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

