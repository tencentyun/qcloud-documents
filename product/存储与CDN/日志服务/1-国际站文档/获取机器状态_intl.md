## Description

This API is used to get the status of a server under the specified server group.

### Request example

```
GET /machines?group_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /machines
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
  "machines": [
    {"ip": "10.10.10.10","status": 0},
    {"ip": "10.10.10.11","status": 1}
  ]
}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|-------------|-----------|---------|-------------------------------|
| machines    |JsonArray  | Yes | Array of server information |

MachineInfo is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| ip         | string | Yes | Server IP |
| status     | int    | Yes | 0: Exceptional; 1: Normal |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

