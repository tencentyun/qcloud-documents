## 功能描述

本接口用于修改机器组。

## 请求

### 请求示例

```
PUT /machinegroup HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/json

{"group_id": "xxxx-xx-xx-xx-xxxxxxx", "group_name": "testname", "ips": ["10.10.10.10", "10.10.10.11"]}
```

### 请求行

```
PUT /machinegroup
```

### 请求头

除公共头部外，无特殊请求头部。

### 请求参数

| 字段名        |  类型  | 位置  | 必须 |      含义                       |
|--------------|--------|------|---------|--------------------------------|
| group_id     | string | body | 是      |要修改的机器组的 ID                |
| group_name   | string | body | 否      |机器组的名字，不能重名             |
| ips          | JsonArray| body | 否      |机器组下的 IP 列表                  |


>!group_name 和 ips 至少要提供一个。

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

请查看 [错误码](https://cloud.tencent.com/document/product/614/12402) 文档。

