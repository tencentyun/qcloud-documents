## Description

This API is used to get the list of log topic information.

## Request

### Request example

```
GET /topics?logset_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /topics
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
  "topics": [
    {
    "logset_id": "xxxx-xx-xx-xx-xxxxxxxx",
    "topic_id": "xxxx-xx-xx-xx-yyyyyyyy",
    "topic_name": "testname",
    "path": "/abc/log/test.log",
    "collection": true,
    "index": true,
    "log_type": "delimiter_log",
    "extract_rule": {
          "time_key": "data",
          "time_format": "%Y-%m-%d %H:%M:%S",
          "delimiter": "|",
          "keys": ["data","","content"],
          "filter_keys": [],
          "filter_regex": [],
      },
    "machine_group": {
        "group_id": "xxxx-xx-xx-xx-oooooooo",
        "group_name": "name",
      },
    "create_time": "2017-08-08 12:12:12"
    }
  ]
}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|-------------|-----------|---------|-------------------------------|
| topics      | JsonArray | Yes | Array of log topic information |

TopicInfo is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| logset_id  | string | Yes | Logset ID |
| topic_id   | string | Yes | Log topic ID |
| topic_name | string | Yes | Log topic name |
| path       | string | Yes | Log file path |
| collection | bool   | Yes | Indicates whether to enable collection |
| index      | bool   | Yes | Indicates whether to enable index |
| log_type   | string | Yes | Type of log to be collected. ```Json_log```: Log in JSON format; ```delimiter_log```: Log in separator-based format; ```minimalist_log```: Minimalist log |
| extract_rule| JsonObject| Yes | Extraction rule |
| machine_group|JsonObject| No | Information of the server group on which logs are collected |
| create_time| string | No | Creation time |

extract_rule is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| time_key   | string | No | Key of the time field |
| time_format| string | No | Format of the time field. For a description of time format, please see ```strftime``` function in C programming language. |
| delimiter  | string | No | The separator for separator-based logs |
| keys       | JsonArray(string) | No | Key of each extracted field |
| filter_keys| JsonArray(string)| No | Log keys to be filtered |
| filter_regex| JsonArray(string) | No | Values corresponding to the above keys. The number of values equals to that of the filter_keys. A value corresponds to a key. |

machine_group is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| group_id   | string | Yes | Server group ID |
| group_name | string | Yes | Server group name |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

