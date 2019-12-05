## Description

This API is used to modify a log topic.

## Request

### Request example

```
PUT /topic HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/json

{
  "topic_id": "xxxxxx-xx-xx-xx-xxxxxxxx",
  "topic_name": "testname",
  "path": "/data/nginx/log/access.log",
  "group_id": "xxxxxx-yy-xx-xx",
  "collection": false,
  "log_type": "delimiter_log",
  "extract_rule": {
      "time_key": "data",
      "time_format": "%Y-%m-%d %H:%M:%S",
      "delimiter": "|",
      "keys": ["data","","content"],
      "filter_keys": [],
      "filter_regex": [],
  }
}
```

### Request line

```
PUT /topic
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|---------|--------------------------------|
| topic_id     | string | body | Yes | Log topic ID |
| topic_name   | string | body | No | Log topic name |
| path         | string | body | No | Path of the log that needs to be collected for the log topic |
| group_id     | string | body | No | The server group from which logs are collected |
| collection   | bool   | body | No | Indicates whether to enable collection |
| log_type     | string | body | No | Type of log to be collected. ```Json_log```: Log in JSON format; ```delimiter_log```: Log in separator-based format; ```minimalist_log```: Minimalist log |
| extract_rule | JsonObject| body| No | Extraction rule |

extract_rule is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| time_key   | string | No | Key of the time field. time_key and time_format must come in pairs. |
| time_format| string | No | Format of the time field. For a description of time format, please see ```strftime``` function in C programming language. |
| delimiter  | string | No | The separator for separator-based logs. This is valid only when ```log_type``` is ```delimiter_log```. |
| keys       | JsonArray(string) | No | Key of each extracted field. Empty key means to discard the field. This is valid only when ```log_type``` is ```delimiter_log```. JSON key is used for ```json_log```. |
| filter_keys| JsonArray(string)| No | Log keys to be filtered. The number of keys is limited to 5. |
| filter_regex| JsonArray(string) | No | Value corresponding to the above key. The number of values equals to that of the filter_keys. A value corresponds to a key. Logs that match the rule are collected. |

> **Note:**
>
>  At least one of the followings should be provided: topic_name, path, group_id, collection and (log_type+extract_rule). 

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

