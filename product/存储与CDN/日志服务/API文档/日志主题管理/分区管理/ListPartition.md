## 功能描述

本接口用于获取主题分区信息列表。

## 请求

#### 请求示例

```shell
GET /partitions?topic_id=xxxx-xx-xx-xx-xxxx HTTP/1.1
Host: <Region>.cls.tencentyun.com
Authorization: <AuthorizationString>
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 参数名   | 类型   | 位置  | 是否必须 | 描述        |
| -------- | ------ | ----- | -------- | ----------- |
| topic_id | string | query | 是       | 日志主题 ID |

## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 21

{
    "partitions":[
        {
            "partition_id": 1,
            "status": "readwrite",
            "inclusive_begin_key": "000000000000000000000000000000000000",
            "exclusive_end_key": "a00000000000000000000000000000000000",
            "create_time": "2019-01-14 19:19:41"
        },
        {
           "partition_id": 2,
            "status": "readwrite",
            "inclusive_begin_key": "a00000000000000000000000000000000000",
            "exclusive_end_key": "ffffffffffffffffffffffffffffffffffff",
            "create_time": "2019-01-14 19:19:41"
        }
    ]
}
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

| 字段名              | 类型   | 是否必须 | 说明                                                |
| ------------------- | ------ | -------- | --------------------------------------------------- |
| partition_id        | int    | 是       | 主题分区编号                                        |
| status              | string | 是       | 主题分区状态：<br><li>readwrite：读写态<br><li>readonly：只读态 |
| inclusive_begin_key | string | 是       | 主题分区范围的起始位置                              |
| exclusive_end_key   | string | 是       | 主题分区范围的结束位置                              |
| create_time         | string | 是       | 主题分区的创建时间                                  |



## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

