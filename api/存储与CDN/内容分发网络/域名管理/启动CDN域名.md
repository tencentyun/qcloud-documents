## 接口描述

**OnlineHost** 启动指定域名的加速服务。

请求域名：<font style="color:red">cdn.api.qcloud.com</font>
>!
+ 一次支持一个域名的启动操作。
+ 仅当域名状态为“已关闭”时，才可进行启动操作。
+ 调用频次限制为100次/分钟。
+ 接口已支持子账号调用，权限配置请参见 [权限配置示例](https://cloud.tencent.com/document/product/228/14867)。

[查看调用示例](https://cloud.tencent.com/document/product/228/1734)

## 入参说明

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 。其中，此接口的 Action 字段为 OnlineHost。

| 参数名称   | 是否必选 | 类型     | 描述           |
| ------ | ---- | ------ | ------------ |
| host   | 否    | String | 需要启动的加速域名。    |
| hostId | 否    | Int    | 需要启动的加速域名 ID。 |

### 详细说明

+ 可使用接口 [根据域名查询域名信息](https://cloud.tencent.com/doc/api/231/3938) 、[查询域名信息](https://cloud.tencent.com/doc/api/231/3937) 获取 host 对应的 ID。
+ host 与 hostId 必须指定其中一个查询。

## 出参说明

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。<br/>详情请参见错误码页面 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。<br/>详情请参见错误码页面 [业务错误码](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。 |

## 调用案例

### 示例参数 

```
hostId：1234
```

### GET 请求

GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=OnlineHost
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&hostId=1234
```

### POST 请求
POST 请求时，参数填充在 HTTP Request-body 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'OnlineHost',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'hostId' => 1234
)
```

### 结果示例
```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

```json
{
    "code": 4000,
    "message": "(9177)域名已上线 cdn host online[host online]",
    "codeDesc": 9177
}
```




