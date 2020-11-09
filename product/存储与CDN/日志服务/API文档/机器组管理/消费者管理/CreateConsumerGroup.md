## 功能描述

本接口用于创建消费组。

## 请求

#### 请求示例

```shell
POST /consumergroup?topic_id=xxxx-xx-xx-xx-xxxx HTTP/1.1
Host: <Region>.cls.tencentyun.com
Content-Type: application/json
Authorization: <AuthorizationString>

{"consumer_group": "cls_demo_consumer_group", "timeout": 3600, "order": false}
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名         | 类型   | 位置  | 是否必须 | 含义                                                         |
| -------------- | ------ | ----- | -------- | ------------------------------------------------------------ |
| topic_id       | string | query | 是       | 日志主题 ID，在该日志主题下创建消费组                        |
| consumer_group | string | body  | 是       | 消费组名称，字符长度为1至255个字符，允许的字符为 a-z、A-Z、0-9、_、- |
| timeout        | int    | body  | 是       | 消费组超时时间（单位：秒），超过 timeout 秒后未收到任何心跳，系统会删除消费组 |
| order          | bool   | body  | 是       | 该配置会影响主题分区分裂/合并时的消费行为：<br><li>true：按顺序消费<br><li>false：不按顺序消费 |



## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 0
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

无。

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

