## 功能描述

本接口用于获取日志主题信息。

### 请求示例

```
GET /topic?topic_id=xxxx-xx-xx-xx-yyyyyyyy HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
```

### 请求行

```
GET /topic
```

### 请求头

除公共头部外，无特殊请求头部。

### 请求参数

| 字段名   | 类型   | 位置  | 是否必须 | 含义            |
| -------- | ------ | ----- | ---- | --------------- |
| topic_id | string | query | 是   | 查询的 topic id |

## 响应

### 响应示例

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
  "logset_id": "xxxx-xx-xx-xx-xxxxxxxx",
  "topic_id": "xxxx-xx-xx-xx-yyyyyyyy",
  "topic_name": "testname",
  "log_path": "/abc/log/test.log",
  "wild_path":"/data/nginx/log/**/access.log",
  "collection": true,
  "index": true,
  "log_type": "delimiter_log",
  "extract_rule": {
      "time_key": "date",
      "time_format": "%Y-%m-%d %H:%M:%S",
      "delimiter": "|",
      "log_regex": ".*",
      "beginning_regex": "^",
      "keys": ["date","","content"],
      "filter_keys": [],
      "filter_regex": []
  },
  "create_time": "2017-08-08 12:12:12"
}
```

### 响应头

除公共响应头部外，无特殊响应头部。

### 响应参数

| 字段名        | 类型       | 是否必须 | 含义                                                         |
| ------------- | ---------- | ---- | ------------------------------------------------------------ |
| logset_id     | string     | 是   | 日志集的 ID                                                  |
| topic_id      | string     | 是   | 日志主题的 ID                                                |
| topic_name    | string     | 是   | 日志主题的名字                                               |
| path          | string     | 是   | 旧版日志文件路径                                                |
| wild_path	    | string	   | 是	 | 新版通配符日志文件路径，以/\*\*/分隔文件目录和文件名，和旧版path只会存在一个  |
| collection    | bool       | 是   | 是否开启采集                                                 |
| index         | bool       | 是   | 是否开启索引                                                 |
| log_type      | string     | 是   | 采集的日志类型，`json_log`代表 json 格式日志，`delimiter_log`代表分隔符格式日志，`minimalist_log`代表极简日志，`regex_log`、`multiline_log`代表多行日志，`fullregex_log`代表完整正则 |
| extract_rule  | JsonObject | 是   | 提取规则                                                     |
| machine_group | JsonObject | 否   | 采集机器组信息                                               |
| create_time   | string     | 否   | 创建时间                                                     |

extract_rule 格式如下：

| 字段名          | 类型              | 是否必须 | 含义                                                        |
| --------------- | ----------------- | -------- | ----------------------------------------------------------- |
| time_key        | string            | 否       | 时间字段的 key 名字                                           |
| time_format     | string            | 否       | 时间字段的格式，参考 C 语言的`strftime`函数对于时间的格式说明 |
| delimiter       | string            | 否       | 分隔符类型日志的分隔符                                      |
| log_regex       | string            | 否       | 多行日志类型的 整条日志匹配规则                             |
| beginning_regex | string            | 否       | 多行日志类型的 行首匹配规则                                 |
| keys            | JsonArray(string) | 否       | 提取的每个字段的 key 名字                                     |
| filter_keys     | JsonArray(string) | 否       | 需要过滤日志的 key                                           |
| filter_regex    | JsonArray(string) | 否       | 上述字段 filter_keys 对应的值，个数与 filter_keys 相同，一一对应        |

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。
