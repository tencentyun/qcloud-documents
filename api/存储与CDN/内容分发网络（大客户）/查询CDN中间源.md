## 1. 接口描述

本接口（GetCdnMiddleSourceList）用于查询 CDN 所有中间源IP列表。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>

## 2. 输入参数

此接口无输入参数



## 3. 输出参数

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Array  | 返回结果，详细说明见下文                             |

#### data 字段说明

| 参数名称               | 类型    | 描述      |
| ------------------ | ----- | ------- |
| middle_source_list | Array | 中间源IP列表 |



## 4. 示例

### 4.1 GET 请求

GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnMiddleSourceList
&SecretId=XXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462431364
&Nonce=123465789
&Signature=XXXXXXXXXXXXXXXXXX
```

### 4.2 POST 请求

POST请求时，参数填充在 HTTP Request-body 中，请求地址：

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





### 4.3 返回结果示例

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





