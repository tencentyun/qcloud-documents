## 功能描述

本接口用于合并一个读写态的主题分区，合并时指定一个主题分区 ID，日志服务会自动合并范围右相邻的分区。

## 请求

#### 请求示例

```shell
POST /partitions?topic_id=xxxx-xx-xx-xx-xxxx&partition_id=2&action=merge HTTP/1.1
Host: <Region>.cls.tencentyun.com
Authorization: <AuthorizationString>
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名       | 类型   | 位置  | 是否必须 | 说明                                                         |
| ------------ | ------ | ----- | -------- | ------------------------------------------------------------ |
| topic_id     | string | query | 是       | 分区所属的日志主题 ID                                       |
| partition_id | int    | query | 是       | 需合并的主题分区编号，日志服务会自动合并范围右相邻的分区。<br>例如，若2、3是两个相邻的 readwrite 分区，paritition_id=2时，会将2、3分区合并，同时2、3分区类型变成 readonly，合并的后的分区类型为 readwrite，partition_id=4 |
| action       | string | query | 是       | 操作类型，action 需要设置为：merge                         |

## 响应

#### 响应示例

```shell
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 21

{
    "partitions":[
        {
           "partition_id": 2,
            "status": "readonly",
            "inclusive_begin_key": "000000000000000000000000000000000000",
            "exclusive_end_key": "7fffffffffffffffffffffffffffffffffff",
            "create_time": "2019-01-14 19:25:41"
        },
        {
            "partition_id": 3,
            "status": "readonly",
            "inclusive_begin_key": "7fffffffffffffffffffffffffffffffffff",
            "exclusive_end_key": "ffffffffffffffffffffffffffffffffffff",
            "create_time": "2019-01-14 19:25:41"
        },
        {
            "partition_id": 4,
            "status": "readwrite",
            "inclusive_begin_key": "000000000000000000000000000000000000",
            "exclusive_end_key": "ffffffffffffffffffffffffffffffffffff",
            "create_time": "2019-01-14 19:33:41"
        }
    ]
}
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

| 字段名              | 类型   | 说明                                                |
| ------------------- | ------ | --------------------------------------------------- |
| partition_id        | int    | 主题分区编号                                        |
| status              | string | 主题分区状态：<br><li>readwrite：读写态<br><li>readonly：只读态 |
| inclusive_begin_key | string | 主题分区范围的起始位置                              |
| exclusive_end_key   | string | 主题分区范围的结束位置                              |
| create_time         | string | 主题分区的创建时间                                  |



## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

