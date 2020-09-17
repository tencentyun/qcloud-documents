## 功能描述

本接口用于修改消费组。

## 请求

#### 请求示例

```shell
PUT /consumergroup?topic_id=xxxx-xx-xx-xx-xxxxxxxx&consumer_group=xxxxx HTTP/1.1
Host: <Region>.cls.tencentyun.com
Content-Type: application/json
Authorization: <AuthorizationString>

{"timeout": 3600, "order": true}
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名         | 类型   | 位置  | 是否必须 | 含义                                                         |
| -------------- | ------ | ----- | -------- | ------------------------------------------------------------ |
| topic_id       | string | query | 是       | 消费组所属的日志主题 ID                                      |
| consumer_group | string | query | 是       | 消费组名称                                                   |
| timeout        | int    | body  | 否       | 消费组超时时间，超过 timeout 秒未收到任何心跳，系统将删除消费组 |
| order          | bool   | body  | 否       | 是否按顺序消费                                               |

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

