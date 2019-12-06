## 1. 接口描述

本接口（GetOvCdnHyStat）用于查询海外 CDN 回源质量详细信息，包括流量，带宽，速度，回源失败明细，4xx次数明细，每五分钟一个统计点，一天共有288个统计点。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>

[调用Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 GetOvCdnHyStat。

| 参数名称 | 是否必选 | 类型   | 描述                   |
| ------- | ------- | ------ | -------------------- |
| host    | 是      | String | 海外 CDN 域名             |
| view    | 是      | String | usage 表示查询流量，带宽和速度；fails 表示查询回源失败明细；4xx表示查询4xx错误码明细 |
| date    | 是      | String | 查询日期，如2017-08-08        |

## 3. 输出参数

| 参数名称  | 类型   | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Array  | 结果数据，详细说明见下文                             |

#### data 字段说明

| 参数名称        | 类型    | 描述                                       |
| -------------- | ------ | ---------------------------------------- |
| start_datetime | String | 统计起始时间，若填入查询日期2017-08-08，则起始时间为2017-08-08 00:00:00 |
| end_datetime   | String | 统计结束时间，若填入查询日期2017-08-08，则结束时间为2017-08-08 23:55:00                        |
| period         | String | 统计周期，默认5分钟                          |
| time_date      | Array  | 结果数据，详细说明见下文 |

#### time_date 字段说明

**参数 view 为 usage 时**：

| 参数名称      | 类型   | 描述                                       |
| ------------ | ----- | ---------------------------------------- |
| hy_bandwidth | Array | 各个周期的回源带宽峰值，单位为 bps |
| hy_flux      | Array | 各个周期的回源总流量，单位为 Byte                |
| hy_speed     | Array | 各个周期的回源速度，单位为 bit/s               |

**参数 view 为 fails 时**：

| 参数名称               | 类型    | 描述                                       |
| --------------------- | ------ | ---------------------------------------- |
| hy_count              | Array  | 各个周期的回源请求数 |
| hy_fail               | Array  | 各个周期的回源失败数                          |
| hy_origin_close       | Array  | 各个周期的源站关闭次数                          |
| hy_timeout            | Array  | 各个周期的回源超时次数
| hy_http_error         | Array  | 各个周期的回源协议错误次数
| hy_5xx                | Array  | 各个周期的回源5xx错误次数
| hy_fail_ratio         | Array  | 各个周期的回源失败率
| hy_origin_close_ratio | Array  | 各个周期的源站关闭比例
| hy_timeout_ratio      | Array  | 各个周期的回源超时比例
| hy_http_error_ratio   | Array  | 各个周期的回源协议错误比例
| hy_5xx_ratio          | Array  | 各个周期的回源5xx错误比例

**参数view为4xx时**：

| 参数名称 | 类型  | 描述                                       |
| ------- | ----- | ---------------------------------------- |
| hy_404  | Array | 各个周期的404错误次数 |
| hy_4xx  | Array | 各个周期的4xx错误次数                          |

**注意事项**：

- 未在上述文档中说明的字段为**无效字段**，可直接忽略。

## 4. 示例

### 4.1 输入示例

> host：www.test.com
> view : usage
> date : 2017-08-09

### 4.2 GET 请求

GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetOvCdnHyStat
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462434006
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
&view=usage
&date=2017-08-09
```

### 4.3 POST 请求

POST 请求时，参数填充在 HTTP Request-body 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'GetOvCdnHyStat',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'host' => 'www.test.com',
  'view' => 'usage',
  'date' => 2017-08-09
)
```

### 4.4 返回结果示例

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "start_datetime": "2017-08-09 00:00:00",
        "end_datetime": "2017-08-09 23:55:00",
        "period": 5,
        "time_data": {
            "hy_bandwidth": [
                721428,
                715591,
				...
            ],
            "hy_flux": [
                27053573,
                26834677,
				...
            ],
            "hy_speed": [
                15490.630196656,
                11586.793285294,
				...
            ]
        }
    }
}
```
