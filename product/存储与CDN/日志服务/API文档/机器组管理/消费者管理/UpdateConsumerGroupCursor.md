## 功能描述

本接口用于更新消费组游标。

## 请求

#### 请求示例

```shell
PUT /consumergroupcursor?topic_id=xxxx-xx-xx-xx-xxxx&consumer_group=cls_demo_consumer_group&partition_id=1 HTTP/1.1
Host: <Region>.cls.tencentyun.com
Content-Type: application/json
Authorization: <AuthorizationString>

{"consumer_id": "cls_demo_consumer_1", "cursor": "FAjUjMtmELBo"}
```

#### 请求行

```shell
PUT  /consumergroupcursor
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名         | 类型   | 位置  | 是否必须 | 含义                    |
| -------------- | ------ | ----- | -------- | ----------------------- |
| topic_id       | string | query | 是       | 消费组所属的日志主题 ID |
| consumer_group | string | query | 是       | 消费组名称              |
| partition_id   | int    | query | 是       | 主题分区编号            |
| consumer_id    | string | body  | 否       | 消费者名称              |
| cursor         | string | body  | 是       | 游标值                  |



## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

无。

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

