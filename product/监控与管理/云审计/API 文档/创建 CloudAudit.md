
## 接口描述
CreateAudit 用于创建云审计跟踪集。
接口访问域名：`cloudaudit.api.qcloud.com`

## 请求参数
以下请求参数列表仅列出了接口请求参数。

|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|IsMultiRegionAudit	|否|	Number	|是否开启多地域采集。0：不开启，1：开启|
|Name	|是|	String	|跟踪集名称，3-128字节，只能包含 ASCII 编码字母`a-z，A-Z`，数字`0-9`，下划线`_`|
|CosBucketName	|是|	String	|要投递的 COS Bucket 的名称，命名规范参照 COS 的命名要求|
|CosKeyPrefix	|否|	String	|COS Bucket 前缀，命名规范参照 COS|

>!此处每个用户只能创建1个跟踪集。


## 响应参数


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| IsMultiRegionAudit | Number | 是否开启多地域采集，1代表是，0代表否|
| Name | String | 跟踪集名称 |
| CosBucketName | String | 	COS Bucket 名称 |
| CosKeyPrefix | String | COS Bucket 前缀 |

## 实际案例
### 请求

```shell
{
   "IsMultiRegionAudit": "Number",
   "Name": "String",
   "CosBucketName": "String",
   "CosKeyPrefix": "String"
}
```

### 响应
```shell
{
   "IsMultiRegionAudit": "Number",
   "Name": "String",
   "CosBucketName": "String",
   "CosKeyPrefix": "String"
}
```
