## 接口描述
**QueryCdnIp** 查询指定 IP 是否属于腾讯云 CDN 节点，及其服务状态。

请求域名：<font style="color:red">cdn.api.qcloud.com</font>

>!
+ 支持多 IP 查询，使用英文逗号分隔，最多可一次提交20个进行查询
+ 调用频次限制为3000次/分钟
+ 无需授权，开通 CDN 服务后可直接使用


[查看调用示例](https://cloud.tencent.com/document/product/228/1734)

## 入参说明
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 QueryCdnIp。

| 参数名称 | 是否必选 | 类型     | 描述                |
| ---- | ---- | ------ | ----------------- |
| ips  | 是    | String | 需要查询的 IP，支持一个或多个查询 |

## 出参说明
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。<br/>详见错误码页面 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。<br/>详见错误码页面 [业务错误码](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) |
| data     | Object | 返回结果数据                                   |

#### 详细说明

#### data

| 参数名称             | 类型    | 描述             |
| ---------------- | ----- | -------------- |
| last_update_time | int   | 最后一次更新的 Unix 时间戳 |
| list             | Array | 查询结果数组         |

#### list

| 参数名称      | 类型     | 描述                                       |
| --------- | ------ | ---------------------------------------- |
| ip        | String | 查询的 IP                                   |
| platform  | String | 是否属于 CDN 节点<br/>"yes"：属于腾讯云 CDN<br/>"no"：不属于腾讯云 CDN |
| prov_name | String | 节点所在省份                                   |
| isp_name  | String | 节点运营商                                    |
| status    | String | 节点运行状态<br/>"on"：表示节点正常服务中<br/>"off"：表示节点未在服务中 |

## 调用案例
### 示例参数

```
ips：1.1.1.1,2.2.2.2
```

### GET 请求
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

### POST请求
POST 请求时，参数填充在HTTP Request body中，请求地址：
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

### 返回示例
注意：示例中 IP 仅供参考。
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
                "isp_name": "电信",
                "status":"off"
            },
            {
                "ip": "1.1.1.1",
                "platform": "no",
                "prov_name": "未知",
                "isp_name": "未知",
                "status":"on"
            }
        ]
    }
}
```


