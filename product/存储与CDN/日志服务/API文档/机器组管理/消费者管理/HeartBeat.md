## 功能描述

本接口用于消费者上传心跳。

## 请求

#### 请求示例

```shell
POST /consumerheartbeat?topic_id=xxxx-xx-xx-xx-xxxx HTTP/1.1
Host: <Region>.cls.tencentyun.com
Content-Type: application/json
Authorization: <AuthorizationString>

{"consumer_group": "cls_demo_consumer_group", "consumer_id": "consumer_id", "partition_id_list": []}
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名            | 类型   | 位置  | 是否必须 | 含义                    |
| ----------------- | ------ | ----- | -------- | ----------------------- |
| topic_id          | string | query | 是       | 消费组所属日志主题的 ID |
| consumer_group    | string | body  | 是       | 消费组名称              |
| consumer_id       | string | body  | 是       | 消费者名称              |
| partition_id_list | array  | body  | 是       | 消费者消费的分区列表    |



## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
    "partition_id_list":[
        4,
        5
    ]
}
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

| 字段名            | 类型  | 是否必有 | 含义                     |
| ----------------- | ----- | -------- | ------------------------ |
| partition_id_list | array | 是       | 该消费者可消费的分区列表 |

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

