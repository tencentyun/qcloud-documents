## Description

This API is used to obtain the list of shipping task information.

## Request

### Request example

```
GET /tasks?shipper_id=xx-xx-xx-xxxx&start_time=2017-10-10+00%3A00%3A00&end_time=2017-10-10+23%3A59%3A59 HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
```

### Request line

```
GET /tasks
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|---------------------------------|
| shipper_id   | string | query| Yes | ID of the shipping rule to be queried |
| start_time   | string | query| Yes | Start time of the shipping task to be queried. Tasks within the last 3 days can be queried. |
| end_time     | string | query| Yes | End time of the shipping task to be queried |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
  "tasks": [
    {
      "task_id": "xxxxx-xx-xx-xx",
      "shipper_id": "xxxxx-xx-xx-xx",
      "topic_id": "xxxxx-xx-xx-xx",
      "range_start": "2017-10-17 10:10:10",
      "range_end": "2017-10-17 10:10:10",
      "start_time": "2017-10-17 10:10:10",
      "end_time": "2017-10-17 10:10:10",
      "status": "success",
      "message": "success",
    }
  ]
}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|-------------|-----------|---------|-------------------------------|
| tasks       | JsonArray | Yes | Array of shipping task information |

TaskInfo is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| task_id    | string | Yes | Shipping task ID |
| shipper_id | string | Yes | Shipping rule ID |
| topic_id   | string | Yes | Log topic ID |
| range_start| string | Yes | Start time of this batch of logs to be shipped |
| range_end  | string | Yes | End time of this batch of logs to be shipped |
| start_time | string | Yes | Start time of this shipping task |
| end_time   | string | Yes | End time of this shipping task |
| status     | string | Yes | Result of this shipping task: "success", "running", "failed", "wait" |
| message    | string | Yes | Result details |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

