## 功能描述

本接口用于获取日志主题的消费组列表。

## 请求

#### 请求示例

```shell
GET /consumergroups?topic_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.tencentyun.com
Authorization: <AuthorizationString>
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名   | 类型   | 位置  | 是否必须 | 含义              |
| -------- | ------ | ----- | -------- | ----------------- |
| topic_id | string | query | 是       | 查询日志主题的 ID |

## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
    "consumer_groups":[
        {
            "consumer_group":"cls-demo_consumer_group",
            "order":true,
            "timeout":3600
        }
    ]
}
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

| 字段名         | 类型   | 是否必有 | 含义                                                         |
| -------------- | ------ | -------- | ------------------------------------------------------------ |
| consumer_group | string | 是       | 消费组名称                                                   |
| timeout        | int    | 是       | 消费组超时时间，超过 timeout 秒后未收到任何心跳，系统会删除消费组 |
| order          | bool   | 是       | 是否按顺序消费                                               |

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

