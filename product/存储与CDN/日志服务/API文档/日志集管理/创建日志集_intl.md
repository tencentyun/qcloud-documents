## Description

This API is used to create a logset. The ID of the new logset is returned.

## Request

### Request example

```
POST /logset HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/json

{"logset_name": "testname","period": 15}
```

### Request line

```
POST /logset
```

### Request header

No special response header is used except for the common response header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| logset_name  | string | body | Yes | Name of the logset, which should be unique |
| period       | int    | body | Yes | Logset retention period (in days), which is limited to 90 days |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{"logset_id": "xxxx-xx-xx-xx-xxxxxxxx"}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|-------------|-----------|---------|-------------------------------|
| logset_id   | string    | Yes | Logset ID |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

