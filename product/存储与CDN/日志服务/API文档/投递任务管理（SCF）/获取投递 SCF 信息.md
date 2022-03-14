## 功能描述

本接口用于获取指定投递策略的详细信息。

## 请求

### 请求行

```
GET /deliverfunction
```

### 请求示例

```
GET /deliverfunction?topic_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### 请求头

无特殊。

### 请求参数

| 字段名        |  类型  | 位置  |是否必须 |      含义                  |
|--------------|--------|------|--------|---------------------------|
| topic_id   | string | query  |  是      |查询的 topic id           |

## 响应

### 响应示例

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
    "topic_id": "yyyy-yy-yy-yy-yyyyyyyy",
    "names_pace": "test",
    "function_name": "myname",
    "qualifier": "$LATEST",
    "max_wait": 60,
    "max_size": 100,
    "effective" : true
  
}
```


### 响应头

无特殊。

### 响应参数

|  字段名     |  类型  | 是否必须 |        含义                    |
|------------|--------|---------|-------------------------------|
| topic_id   | string | 是      | 投递规则属于的 topic id          |
| name_spqce    | string | 是      | 命名空间               |
| function_name    | string | 是      | 函数名字                 |
| qualifier| string  | 是      | 函数版本                      |
| max_size| int| 否     | 投递最大消息数                 |
| max_wait  | int    | 否      | 投递最长等待时间，单位：秒          |
| effective  | bool  | 是      |          投递开关            |
 
