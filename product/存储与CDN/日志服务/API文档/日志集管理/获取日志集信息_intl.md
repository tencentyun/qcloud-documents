## Description

This API is used to get the information on a logset.

## Request

### Request example

```
GET /logset?logset_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /logset
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| logset_id    | string | query| Yes | ID of the logset to be queried |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
  "logset_id": "xxxx-xx-xx-xx-xxxxxxxx",
  "logset_name": "testname",
  "period": 15,
  "create_time": "2017-08-08 12:12:12"
}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| logset_id  | string | Yes | Logset ID |
| logset_name| string | Yes | Logset name |
| period     | int    | Yes | Retention period (in days) |
| create_time| string | No | Creation time |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

