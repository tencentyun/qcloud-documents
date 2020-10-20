## 功能描述

本接口用于分裂一个读写态的主题分区。

## 请求

#### 请求示例

```shell
POST /partitions?topic_id=xxxx-xx-xx-xx-xxxx&partition_id=1&split_key=7fffffffffffffffffffffffffffffffffff&action=split HTTP/1.1
Host: <Region>.cls.tencentyun.com
Authorization: <AuthorizationString>
```

#### 请求头

除公共头部外，无特殊请求头部。

#### 请求参数

| 字段名       | 类型   | 位置  | 是否必须 | 说明                                                         |
| ------------ | ------ | ----- | -------- | ------------------------------------------------------------ |
| topic_id     | string | query | 是       | 分区所属的日志主题 ID                                        |
| partition_id | int    | query | 是       | 需分裂的主题分区编号                                         |
| action       | string | query | 是       | 操作类型，action 需要设置为 split                            |
| split_key    | string | query | 否       | 分裂成两个时，可以指定主题分区的分裂位置，32位16进制字符串（不含0x部分）;当分裂成3个及以上时，按平均方式分裂，此参数不生效 |
| number       | int    | query | 否       | 分裂的个数，默认值为2                                        |

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
            "status": "readonly",
            "inclusive_begin_key": "000000000000000000000000000000000000",
            "exclusive_end_key": "ffffffffffffffffffffffffffffffffffff",
            "create_time": "2019-01-14 19:19:41"
        },
        {
           "partition_id": 2,
            "status": "readwrite",
            "inclusive_begin_key": "000000000000000000000000000000000000",
            "exclusive_end_key": "7fffffffffffffffffffffffffffffffffff",
            "create_time": "2019-01-14 19:25:41"
        },
        {
            "partition_id": 3,
            "status": "readwrite",
            "inclusive_begin_key": "7fffffffffffffffffffffffffffffffffff",
            "exclusive_end_key": "ffffffffffffffffffffffffffffffffffff",
            "create_time": "2019-01-14 19:25:41"
        }
    ]
}
```

#### 响应头

除公共响应头部外，无特殊响应头部。

#### 响应参数

| 字段名              | 类型   | 说明                                                         |
| ------------------- | ------ | ------------------------------------------------------------ |
| partition_id        | int    | 主题分区编号                                                 |
| status              | string | 主题分区状态：<br><li>readwrite：读写态<br><li>readonly：只读态 |
| inclusive_begin_key | string | 主题分区范围的起始位置                                       |
| exclusive_end_key   | string | 主题分区范围的结束位置                                       |
| create_time         | string | 主题分区的创建时间                                           |

## 错误码

参见 [错误码](https://cloud.tencent.com/document/product/614/12402)。

