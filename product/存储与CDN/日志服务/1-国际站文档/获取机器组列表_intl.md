## Description

This API is used to get the list of server group information.

## Request

### Request example

```
GET /machinegroups HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /machinegroups
```

### Request header

No special request header is used except for the common header.

### Request parameters

None

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
  "machine_groups": [
    {
    "group_id": "xxxx-xx-xx-xx-xxxxxxxx",
    "group_name": "testname",
    "create_time": "2017-08-08 12:12:12"
    }
  ]
]
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|-------------|-----------|---------|-------------------------------|
| machine_groups|JsonArray| Yes | Array of server group information |

MachineGroupInfo is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| group_id   | string | Yes | Server group ID |
| group_name | string | Yes | Server group name |
| create_time| string | No | Creation time |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

