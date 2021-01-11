## 功能描述

本接口用于获取消费组游标。

## 请求

#### 请求示例

```shell
GET /consumergroupcursor?topic_id=xxxx-xx-xx-xx-xxxx&consumer_group=cls_demo_consumer_group&partition_id=1 HTTP/1.1
Host: <Region>.cls.tencentyun.com
Authorization: <AuthorizationString>
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名         | 类型   | 位置  | 是否必须 | 含义                                                     |
| -------------- | ------ | ----- | -------- | -------------------------------------------------------- |
| topic_id       | string | query | 是       | 消费组所属的日志主题 ID                                  |
| consumer_group | string | query | 是       | 消费组名称                                               |
| partition_id   | int    | query | 否       | 主题分区编号（如果不指定，则返回该主题下所有分区的游标） |

## 响应

#### 响应示例

未指定 partition_id 响应回包：

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
    "cursors":[
        {
            "consumer_id":"cls-demo_consumer_id",
            "cursor":"FAjUjMtmELBovQRogYkBuq",
            "partition_id":1,
            "update_time":1573645058
        },
        {
            "consumer_id":"cls-demo_consumer_id",
            "cursor":"FAjUjMtmELBovQRogYkBuqg",
            "partition_id":2,
            "update_time":1573645058
        }
    ]
}
```

指定 partition_id 响应回包：

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
    "consumer_id":"cls-demo_consumer_id",
    "cursor":"FAjUjMtmELBovQRog",
    "partition_id":1,
    "update_time":1573645058
}
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

| 字段名       | 类型      | 是否必有 | 含义                    |
| ------------ | --------- | -------- | ----------------------- |
| partition_id | string    | 是       | 主题分区编号            |
| cursor       | string    | 是       | 游标值                  |
| update_time  | long long | 是       | 游标更新的时间          |
| consumer_id  | string    | 是       | 该分区被分配的消费者 ID |

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

