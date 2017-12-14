## 1. 接口描述

本接口（GetHostCertList）用于查询用户托管在腾讯云SSL上的HTTPS证书Id等信息，支持分页查询。

接口请求域名：<font style="color:red">cdn.api.cloud.tencent.com</font>

1) 单次最多查询1个域名对应的1个证书信息；

[调用Demo](https://www.cloud.tencent.com/document/product/228/1734)

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.cloud.tencent.com/doc/api/231/4473)页面。其中，此接口的Action字段为GetHostCertList。

| 参数名称      | 是否必选 | 类型     | 描述                                       |
| --------- | ---- | ------ | ---------------------------------------- |
| host    | 是   | String   | 域名                          |

## 3. 输出参数

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://www.cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关                           |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Array  | 结果数据，详细说明见下文                             |

#### data字段说明
| 参数名称  | 类型   | 描述                                 |
| -------- | ------ | ----------------------------------- |
| cert_list   | Array   | HTTPS证书数组，详细说明见下面|
| count    | String  | 返回的HTTPS证书总数    |

#### cert_list字段说明
| 参数名称     | 类型   | 描述                                 |
| ----------- | ------ | ----------------------------------- |
| cert_id     | String | 证书ID |
| alias | String | 证书备注信息 |
| expire_time | String | 证书过期时间 |
| subject_name | String | 证书关联的域名 |

## 4. 示例

### 4.1 输入示例

> host:www.test.com


### 4.2 GET 请求


GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.cloud.tencent.com/v2/index.php?
Action=GetCertificates
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462440051
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
```

### 4.3 POST 请求
POST请求时，参数填充在HTTP Request-body 中，请求地址：

```
https://cdn.api.cloud.tencent.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'GetCertificates',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462868615,
  'Nonce' => 520585444,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'host' => www.test.com,
)
```

### 4.4 返回结果示例

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "cert_list": [
            {
                "cert_id": "XXXX8XXX",
                "alias": "www.test.com",
                "expire_time": "2019-01-07 07:59:59",
                "subject_name": [
                    "www.test.com"
                ]
            }
        ],
        "count": 1
    }
}
```







