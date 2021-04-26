## 功能描述

本接口根据时间获取对应主题分区的游标（cursor），该游标用于获取对应主题分区上的日志数据。

## 请求

#### 请求示例

```shell
GET /cursor?topic_id=xxxxxxxx-xxxx-xxxx-xxxx&partition_id=1&from=end HTTP/1.1
Host: <Region>.cls.tencentyun.com
Authorization: <AuthorizationString>
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 参数名       | 类型   | 位置  | 是否必须 | 描述                                                         |
| ------------ | ------ | ----- | -------- | ------------------------------------------------------------ |
| topic_id     | string | query | 是       | 日志主题 ID                                                  |
| partition_id | int    | query | 是       | 主题分区编号                                                 |
| from         | string | query | 是       | from 用于标识实时消费的开始时间，支持三种类型：<br />1. "UNIX 时间戳（秒）"，表示从指定 UNIX 时间开始消费日志<br />2. "start"，表示从主题分区生命周期的开始时间开始消费日志<br />3. "end"，表示从主题分区生命周期的结束时间（当前时间）消费日志 |

##### 主题分区生命周期说明

主题分区的数据生命周期由 CLS 后台系统设置，不低于1天（不同的日志主题下的主题分区数据生命周期会不同）。

例如，当前时间为2019-10-10 12:00:00，则每个主题分区中数据可以被消费的时间范围（以服务端时间为准）为：[2019-10-09 12:00:00, 2019-10-10 12:00:00)。

通过 from 可以在主题分区中定位实时消费的起始位置，假设主题分区的生命周期为 [start_time, end_time)：
- 当`from（UNIX 时间戳）≤ start_time 或 from = "start"`，接口返回时间点为 start_time 所对应的游标位置。
- 当`from（UNIX 时间戳）≥ end_time 或 from = "end"`，接口返回在当前时间点下，下一条将被写入的游标位置（当前该游标位置上无数据）。
- 当`from（UNIX 时间戳）> start_time and from（UNIX 时间戳）< end_time`，接口返回第一个服务端接收时间大于等于from（UNIX 时间戳）的数据包对应的游标位置。



## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 23

{"cursor": "MTQ0NzI5OTYwNjg5NjYzMjM1Ng=="}
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

| 字段名 | 类型   | 是否必有 | 含义         |
| ------ | ------ | -------- | ------------ |
| cursor | string | 是       | 返回的游标值 |

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

