## Description

This API is used to search for the log content according to specified criteria.

## Request

### Request Example

```
GET /searchlog?logset_id=xxxx-xx-xx-xx-xxxxxxxx&topic_ids=xxxx,xxxx&start_time=2017-08-22%2010%3A10%3A10&end_time=2017-08-23%2010%3A10%3A10&query=&limit=10&context=xxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
```

### Request Line

```
GET /searchlog
```

### Request Header

No special requirements

### Request Parameters

| Field Name | Type | Location | Required | Description |
| ---------- | ------ | ----- | ---- | --------------------------------------------------------- |
| logset_id | string | query | Yes | ID of the logset to be queried |
| topic_ids | string | query | Yes | IDs of topics to be queried, separated by "," |
| start_time | string | query | Yes | Start time of the log to be queried, format: YYYY-mm-dd HH:MM:SS |
| end_time | string | query | Yes | End time of the log to be queried, format: YYYY-mm-dd HH:MM:SS |
| query | string | query | Yes | Content to be queried |
| limit | int | query | Yes | Number of logs returned at a time |
| context | string | query | No | Load more for use. Transparently transmit the last returned context value, and obtain follow-up log content |

## Response

### Response Example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 53

{
    "context": "abcdefg",
    "listover": false,
    "results": [
    {
        "timestamp": "2017-07-14 20:43:00",
        "topic_id": "xxxx-xx-xx-xx-xxxxxxxx",
        "topic_name": "xxxxxxx",
        "content": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    },
    {
        "timestamp": "2017-07-14 20:42:00",
        "topic_id": "xxxx-xx-xx-xx-xxxxxxxx",
        "topic_name": "xxxxxxx",
        "content": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
    ]
}
```

### **Response Header**

No special requirements

## Response Parameters

| Field Name | Type | Required | Description |
| -------- | -------------------- | ---- | ------------------------- |
| context | string | Yes | context for loading follow-up content |
| listover | bool | Yes | Whether all searched results are returned |
| results | JsonArray(LogObject) | Yes | Log content information |

JsonArray(LogObject) is described as follows:

| Field Name | Type | Required | Description |
| ---------- | ------ | ---- | ------------------ |
| topic_id | string | Yes | ID of the topic to which the log belongs |
| topic_name | string | Yes | Name of the topic |
| timestamp  | string | Yes | Log time |
| content    | string | Yes   | Log content           |

## Error Codes

For more information, please see [Error Codes](/document/product/614/12402).

