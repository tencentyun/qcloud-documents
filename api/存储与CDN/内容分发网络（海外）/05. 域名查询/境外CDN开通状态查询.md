## 1. 接口描述
接口请求域名：`cdn.api.qcloud.com`
本接口（GetCdnOverseaOpenStat）用于查询当前帐号境外 CDN 服务的开通状态。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 GetCdnOverseaOpenStat。

## 3. 输出参数
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0 表示成功，其他值表示失败<br/>详情请参见见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) |
| message  | String | 模块错误信息描述，与接口相关                          |
| codeDesc | String | 英文错误信息，或业务侧错误码                         |
| data     | String | 计费类型说明，详情请参见下文 “data 字段说明”                                |

**data 字段说明**

| 参数名称    | 类型     | 描述          |
| ------- | ------ | ----------- |
| appId | String | 查询帐号的 AppId |
| openStatus | String | 境外 CDN 服务开通状态,<br>"approved"：审核通过，服务已开通；<br>"rejected"：已拒绝，服务未开通；<br>"checking"：审核中，服务未开通；<br>"unopen"：服务未开通 |

## 4. 示例
### 4.1 GET 请求
GET 请求需要将所有参数都加在 URL 后：：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnOverseaOpenStat
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
```

### 4.2 POST 请求
POST 请求时，参数填充在 HTTP Requestbody 中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
	'Action' => 'GetCdnOverseaOpenStat',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX'
)
```

### 4.3 返回示例
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": [{
		"appId": 123456789,
		"openStatus": "approved"
	}]

}

```
