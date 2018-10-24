## 功能描述

本接口用于根据指定的条件搜索日志内容。

## 请求

### 请求示例

```
GET /searchlog?logset_id=xxxx-xx-xx-xx-xxxxxxxx&topic_ids=xxxx,xxxx&start_time=2017-08-22%2010%3A10%3A10&end_time=2017-08-23%2010%3A10%3A10&query=&limit=10&context=xxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
```

### 请求行

```
GET /searchlog
```

### 请求头

无特殊

### 请求参数

| 字段名     | 类型   | 位置  | 必须 | 含义                                                      |
| ---------- | ------ | ----- | ---- | --------------------------------------------------------- |
| logset_id  | string | query | 是   | 要查询的logset id                                         |
| topic_ids  | string | query | 是   | 要查询的topic id组合，以,分隔                             |
| start_time | string | query | 是   | 要查询的日志的起始时间，格式 YYYY-mm-dd HH:MM:SS          |
| end_time   | string | query | 是   | 要查询的日志的结束时间，格式 YYYY-mm-dd HH:MM:SS          |
| query      | string | query | 是   | 要查询的内容                                              |
| limit      | int    | query | 是   | 单次要返回的日志条数                                      |
| context    | string | query | 否   | 加载更多使用，透传上次返回的context值，获取后续的日志内容 |

## 响应

### 响应示例

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

### **响应头**

无特殊

### 响应参数

| 字段名   | 类型                 | 必有 | 含义                      |
| -------- | -------------------- | ---- | ------------------------- |
| context  | string               | 是   | 由于加载后续内容的context |
| listover | bool                 | 是   | 搜过结果是否已经全部返回  |
| results  | JsonArray(LogObject) | 是   | 日志内容信息              |

其中，JsonArray(LogObject) 说明如下：

| 字段名     | 类型   | 必有 | 含义               |
| ---------- | ------ | ---- | ------------------ |
| topic_id   | string | 是   | 日志属于的topic id |
| topic_name | string | 是   | 日志主题的名字     |
| timestamp  | string | 是   | 日志时间           |
| content    | string | 是   | 日志内容           |

## 错误码

参见 [错误码](/document/product/614/12402)。