## 功能描述

本接口用于上传日志到指定的日志主题。

## 请求

### 请求示例

```
POST /structuredlog?topic_id=xxxxxxxx-xxxx-xxxx-xxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/x-protobuf

<LogGroupList 的pb格式打包内容>
```
#### PB 描述文件

```
package cls;
message Log
{
    message Content
    {
        required string key   = 1;
        required string value = 2;
    }
    required int64   time     = 1; // UNIX Time Format
    repeated Content contents = 2;
}
message LogGroup
{
    repeated Log    logs        = 1;
    optional string contextFlow = 2; // 保持上下文用的UID
    optional string filename    = 3; // 文件名
    optional string source      = 4; // 日志来源，一般使用机器IP
}
message LogGroupList
{
    repeated LogGroup logGroupList = 1;
}
```

### 请求行

```
POST /structuredlog
```

### 请求头

除公共头部外，无特殊请求头部。

### 请求参数

| 字段名        |  类型  | 位置  |必须 |      含义                                      |
|--------------|--------|------|--------|-----------------------------------------------|
| topic_id     | string | query| 是     |日志上报到的日志主题 ID                            |
| logGroupList | message|  pb | 是     |日志内容相关                                     |

LogGroup 说明：

| 字段名        |      含义                                      |
|--------------|-----------------------------------------------|
| logs         |日志内容                                        |
| contextFlow  |保持上下文用的 UID                                |
| filename     |文件名                                          |
| source       |日志来源，一般使用机器 IP                          |

Log 说明：

| 字段名        |      含义                                      |
|--------------|-----------------------------------------------|
| time         |日志时间，UNIX 时间戳，单位：秒。请注意部分语言得到的是毫秒级，需要转换 |
| contents     |日志内容                                        |

Content 说明：

| 字段名        |      含义                                      |
|--------------|-----------------------------------------------|
| key          |字段的 key，不能以 ```_```开头                    |
| value        |字段的值                                        |

## 响应

### 响应示例

```
HTTP/1.1 200 OK
Content-Length: 0
```

### 响应头

除公共响应头部外，无特殊响应头部。

### 响应参数

无

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。
