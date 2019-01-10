## 功能描述

本接口用于获取指定日志主题的投递策略详细列表。

## 请求

### 请求示例

```shell
 GET /shippers?topic_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
 Host: <Region>.cls.myqcloud.com
 Authorization: <Authorization String>
```

### 请求行 

```shell
GET /shippers
```

### 请求头

除公共头部外，无特殊请求头部。

### 请求参数

| 字段名   | 类型   | 位置  | 是否必须 | 含义                          |
| -------- | ------ | ----- | -------- | ----------------------------- |
| topic_id | string | query | 是       | 查询的 Shipper 属于的 topic id |
| offset   | int    | query | 否       | 查询的起始位置，默认0         |
| count    | int    | query | 否       | 查询的个数，默认50，最大1000  |

## 响应

### 响应示例

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{
  "shippers": [
  {
    "shipper_id": "xxxx-xx-xx-xx-xxxxxxxx",
    "topic_id": "yyyy-yy-yy-yy-yyyyyyyy",
    "bucket": "test-1250000001",
    "prefix": "test",
    "shipper_name": "myname",
    "interval": 300,
    "max_size": 256,
    "effective": true,
    "filter_rules": [{
      "key": "",
      "regex": "",
      "value": ""
    }],
    "partition": "%Y%m%d",
    "compress": {
        "format": "none"
    },
    "content": {
        "format": "json"
    },
    "create_time": "2017-12-12 12:12:12"
  }
  ]
}
```

### 响应头

除公共响应头部外，无特殊响应头部。

### 响应参数

| 字段名   | 类型      | 是否必须 | 含义         |
| -------- | --------- | -------- | ------------ |
| shippers | JsonArray | 是       | 投递信息数组 |

ShipperInfo 格式如下： 

| 字段名       | 类型   | 是否必须 | 含义                                               |
| ------------ | ------ | -------- | -------------------------------------------------- |
| shipper_id   | string | 是       | 投递的 ID                                          |
| topic_id     | string | 是       | 投递规则属于的 topic id                            |
| bucket       | string | 是       | 投递的 bucket 地址                                 |
| prefix       | string | 是       | 投递的前缀目录                                     |
| shipper_name | string | 是       | 投递规则的名字                                     |
| interval     | int    | 是       | 投递的时间间隔，单位秒                            |
| max_size     | int    | 是       | 投递的文件的最大值，单位 MB                        |
| effective    | bool   | 是       | 是否生效                                           |
| filter_rules | array  | 是       | 投递日志的过滤规则                                 |
| create_time  | string | 是       | 投递日志的创建时间                                 |
| partition    | string | 是       | 投递日志的分区规则，支持 strftime 的时间格式表示 |
| compress     | object | 是       | 投递日志的压缩配置                                 |
| content      | object | 是       | 投递日志的内容格式配置                             |

filter_rules 格式如下：

| 字段名 | 类型   | 是否必须 | 含义                                                  |
| ------ | ------ | -------- | ----------------------------------------------------- |
| key    | string | 是       | 用来比较的 key，`__CONTENT__` 代表全文                |
| regex  | string | 是       | 比较内容的提取正则表达式                              |
| value  | string | 是       | 与上面 regex 提取出的内容比较的 value，如果一致则命中 |

compress格式如下：

| 字段名 | 类型   | 是否必须 | 含义                                       |
| ------ | ------ | -------- | ------------------------------------------ |
| format | string | 是       | 压缩格式，支持 gzip、lzop 和 none 不压缩 |

content 格式如下：

| 字段名   | 类型   | 是否必须 | 含义                        |
| -------- | ------ | -------- | --------------------------- |
| format   | string | 是       | 内容格式，支持 json、csv |
| csv_info | object | 否       | 内容格式为 csv 时返回       |

csv_info 格式如下：

| 字段名             | 类型          | 是否必须 | 含义                                             |
| ------------------ | ------------- | -------- | ------------------------------------------------ |
| print_key          | bool          | 是       | csv 首行是否打印 key                             |
| keys               | array（string） | 是       | 每列 key 的名字                                  |
| delimiter          | string        | 是       | 各字段间的分隔符                                 |
| escape_char        | string        | 是       | 若字段内容中包含分隔符，则使用该转义符包裹改字段 |
| non_existing_field | string        | 是       | 对于上面指定的不存在字段使用该内容填充           |

### 错误码

请查看 [错误码](https://cloud.tencent.com/document/product/614/12402) 文档。
