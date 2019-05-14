## 1. 接口描述
本接口（QueryCdnIp）用于查询指定IP是否为CDN节点。

接口请求域名：cdn.api.qcloud.com

**接口说明：**
+ 支持多IP查询，一次最多可查询20个；


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.qcloud.com/doc/api/231/4473)页面。其中，此接口的Action字段为QueryCdnIp。

| 参数名称 | 是否必选 | 类型     | 描述                |
| ---- | ---- | ------ | ----------------- |
| ips  | 是    | String | 需要查询的IP，支持一个或多个查询 |


**注意事项：**

+ 多个IP时，查询方式如下，多个IP时使用英文逗号分隔：
```
ips=1.1.1.1,2.2.2.2
```

## 3. 输出参数
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Object | 返回结果数据                                   |

**data字段说明**

| 参数名称             | 类型    | 描述             |
| ---------------- | ----- | -------------- |
| last_update_time | int   | 最后一次更新的Unix时间戳 |
| list             | Array | 查询结果数组         |

**list字段说明**

| 参数名称      | 类型     | 描述                            |
| --------- | ------ | ----------------------------- |
| ip        | String | 查询的IP                         |
| platform  | String | 是否属于CDN节点，"yes"表示属于，"no"表示不属于 |
| prov_name | String | 节点所在省份                        |
| isp_name  | String | 节点运营商                         |

## 4. 示例
### 4.1 输入示例
> ips: 1.1.1.1,2.2.2.2

### 4.2 GET 请求
GET 请求需要将所有参数都加在 URL 后（逗号进行转码）：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=QueryCdnIp
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&ips=1.1.1.1%2C2.2.2.2
```

### 4.2 POST请求
POST 请求时，参数填充在 HTTP Requestbody 中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 formdata、xwwwformurlencoded 等格式，参数数组如下：

```
array (
	'Action' => 'QueryCdnIp',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'ips' => '1.1.1.1,2.2.2.2'
)
```

### 4.3 返回示例
>!示例中IP仅供参考。

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "last_update_time": 1477987948,
        "list": [
            {
                "ip": "2.2.2.2",
                "platform": "yes",
                "prov_name": "广东",
                "isp_name": "电信"
            },
            {
                "ip": "1.1.1.1",
                "platform": "no",
                "prov_name": "未知",
                "isp_name": "未知"
            }
        ]
    }
}
```
