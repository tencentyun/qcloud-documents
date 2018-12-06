## Description

This API is used to modify a logset.

## Request

### Request example

```
PUT /logset HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/json

{"logset_id": "xxxx-xx-xx-xx-xxxxxxx","logset_name": "testname","period": 15}
```

### Request line

```
PUT /logset
```

### Request header

No special response header is used except for the common response header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| logset_id    | string | body | Yes | ID of the logset to be modified |
| logset_name  | string | body | No | Name of the logset, which should be unique |
| period       | int    | body | No | Logset retention period (in days), which is limited to 90 days |

> **Note:**
>
> At least one of logset_name and period should be provided.

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

