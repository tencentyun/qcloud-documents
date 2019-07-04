## Description

This API is used to retry a failed shipping task.

## Request


### Request example

```
PUT /task HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/json

{
  "shipper_id": "xxxxxx-xx-xx-xx-xxxxxxxx",
  "task_id": "xxxxxx-xx-xx-xx-xyyyyyyy",
}
```
### Request line

```
PUT /task
```
### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| shipper_id   | string | body | Yes | Shipping rule ID |
| task_id      | string | body | Yes | Shipping task ID |

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

