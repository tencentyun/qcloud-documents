## 功能描述

本接口用于上传日志至指定的日志主题。目前仅支持写入 PB 格式日志数据，本文也将对 PB 格式进行说明。

## 请求

**请求行**

```
POST /log
```

**请求示例**

```
POST /log HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/x-protobuf

<日志内容打包的pb格式内容>
```
**PB描述文件**

PB（Protocol Buffer）是 Google 开发的用于结构化数据交换格式，作为腾讯云日志服务标准写入格式。因此用于写入日志数据前，需要将日志原始数据序列化为 PB 数据流后通过 API 写入服务端。PB 格式示例如下：

```
package cls
message Log
{
    optional uint64 time = 1; // UNIX Time Format
    required string topic_id = 2;
    required bytes content = 3;
}
```

**请求头**

除公共头部外，无特殊请求头部。

**请求参数**

| 字段名      | 类型     | 位置   | 是否必须 | 含义                     |
| -------- | ------ | ---- | ---- | ---------------------- |
| time     | uint64 | body | 否    | 日志时间，不指定，则使用服务器收到请求的时间 |
| topic_id | string | body | 是    | 日志上报到的日志主题id           |
| content  | string | body | 是    | 日志内容                   |

**返回示例**

```
HTTP/1.1 200 OK
Content-Length: 0

```

**响应头**

除公共响应头部外，无特殊响应头部。

**返回内容说明**

无

**错误码**

见错误码说明文档。
