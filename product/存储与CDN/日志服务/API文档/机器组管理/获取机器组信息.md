## 功能描述

本接口用于获取机器组信息。

## 请求

### 请求示例

```
GET /machinegroup?group_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### 请求行

```
GET /machinegroup
```

### 请求头

除公共响应头部外，无特殊响应头部。

### 请求参数

| 字段名        |  类型  | 位置  | 必须 |      含义                       |
|--------------|--------|------|---------|--------------------------------|
| group_id     | string | query| 是      |查询的 group id                   |

## 响应

### 响应示例

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
  "group_id": "xxxx-xx-xx-xx-xxxxxxxx",
  "group_name": "testname",
  "ips": [
    "10.10.10.10","10.10.10.11"
  ],
  "create_time": "2017-08-08 12:12:12"
}
```

### 响应头

除公共响应头部外，无特殊响应头部。

### 响应参数

|  字段名     |  类型  | 必有 |        含义                   |
|------------|--------|---------|-------------------------------|
| group_id   | string | 是      | 机器组的 ID                  |
| group_name | string | 是      | 机器组的名字                    |
| ips        | JsonArray| 是    | 机器组下的 IP 列表            |
| create_time| string | 否      | 创建时间                       |

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。
