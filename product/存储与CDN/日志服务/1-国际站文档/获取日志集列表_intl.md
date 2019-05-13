## Description

This API is used to get the list of logset information.

## Request

### Request example

```
GET /logsets HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /logsets
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
  "logsets": [
    {
    "logset_id": "xxxx-xx-xx-xx-xxxxxxxx",
    "logset_name": "testname",
    "period": 15,
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
| logsets     | JsonArray | Yes | Array of logset information |

LogsetInfo is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| logset_id  | string | Yes | Logset ID |
| logset_name| string | Yes | Logset name |
| period     | int    | Yes | Retention period (in days) |
| create_time| string | No | Creation time |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

