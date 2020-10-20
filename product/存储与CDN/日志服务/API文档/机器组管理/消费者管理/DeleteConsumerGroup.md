## 功能描述

本接口用于删除消费组。

## 请求

#### 请求示例

```shell
DELETE /consumergroup?topic_id=xxxx-xx-xx-xx-xxxx&consumer_group=cls_demo_consumer_group HTTP/1.1
Host: <Region>.cls.tencentyun.com
Authorization: <AuthorizationString>
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名         | 类型   | 位置  | 是否必须 | 含义                      |
| -------------- | ------ | ----- | -------- | ------------------------- |
| topic_id       | string | query | 是       | 消费组所属的日志主题的 ID |
| consumer_group | string | query  | 是       | 消费组名称                |

## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Length: 0
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

无。

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

