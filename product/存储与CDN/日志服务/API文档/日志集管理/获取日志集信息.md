## 功能描述

本接口用于获取日志集信息。

## 请求

### 请求示例

```
GET /logset?logset_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### 请求行

```
GET /logset
```

### 请求头

除公共头部外，无特殊请求头部。

### 请求参数

| 字段名        |  类型  | 位置  | 必须 |      含义                       |
|--------------|--------|------|---------|--------------------------------|
| logset_id    | string | query| 是      |查询的 logset id |

## 响应

### 响应示例

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
  "logset_id": "xxxx-xx-xx-xx-xxxxxxxx",
  "logset_name": "testname",
  "period": 15,
  "create_time": "2017-08-08 12:12:12"
}
```

### 响应头

除公共响应头部外，无特殊响应头部。

### 响应参数

|  字段名     |  类型  | 必有 |        含义                    |
|------------|--------|---------|-------------------------------|
| logset_id  | string | 是      | 日志集的 ID                  |
| logset_name| string | 是      | 日志集的名字                    |
| period     | int    | 是      | 保存周期（天）                  |
| create_time| string | 否      | 创建时间                       |

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。
