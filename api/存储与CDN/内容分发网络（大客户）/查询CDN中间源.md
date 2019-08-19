## 接口描述

**GetCdnMiddleSourceList** 用于查询 CDN 所有回源层 IP 列表。

请求域名：<font style="color:red">cdn.api.qcloud.com</font>

## 入参说明

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 GetCdnMiddleSourceList。

| 参数名称 | 是否必选 | 类型   | 描述                                                         |
| -------- | -------- | ------ | ------------------------------------------------------------ |
| format   | 否       | String | 显示格式，不填充时默认返回 ip_list<br/>"ip_block"：以 IP C 段格式返回<br/>"ip_list"：以详细 IP 模式返回 |

## 出参说明

| 参数名称 | 类型   | 描述                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                               |
| codeDesc | String | 英文错误信息，或业务侧错误码。                               |
| data     | Array  | 返回结果<br/>"middle_source_list"：中间源列表                |

## 调用案例

### GET 请求

GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnMiddleSourceList
&SecretId=XXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462431364
&Nonce=123465789
&Signature=XXXXXXXXXXXXXXXXXX
```

### POST 请求

POST 请求时，参数填充在 HTTP Request-body 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'GetCdnMiddleSourceList',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462866050,
  'Nonce' => 1130670281,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
)
```

### 结果示例

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "middle_source_list": [
			"1.1.1.1",
            "2.2.2.2",
            ...
        ]
    }
}
```





