# 创建 CloudAudit
## 接口描述
CreateAudit 用于创建云审计（CloudAudit）。
## 请求参数
以下请求参数列表仅列出了接口请求参数。

|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|IsMultiRegionAudit	|否|	number	|是否开启多地域采集(0 不开启，1 开启)|
|KmsKeyId	|否|	string	| KMS 的 scretId 用于数据加密|
|Name	|是|	string	|CloudAudit 的名字，3-128 字节，只能包含 ASCII 编码字母（a-z,A-Z），数字（0-9），下划线（_）|
|CosBucketName	|是|	string	|要投递的 COSBUCKET 的名称（命名规范参照 COS 的命名要求）|
|CosKeyPrefix	|否|	string	|COS 存储桶的前缀（命名规范参照 COS）|
|CmqTopicName	|否|	string	|Cmq 的名字，如果开启消息队列请填写（命名规范参照 CMQ 要求）|
> **注意：**
> 此处每个用户只能创建 50 个 CloudAudit 。


## 响应参数


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| IsMultiRegionAudit | number | 是否开启多地域采集（1 代表是，0 代表否） |
| KmsKeyId | string | Kms 秘钥 ID |
| Name | string | CloudAudit 名称 |
| CosBucketName | string | 	COS Bucket 名称 |
| CosKeyPrefix | string | COS Bucket 前缀 |
| CmqTopicName | string | CMQ 主题名称 |

## 实际案例
### 请求

```
{
   "IsMultiRegionAudit": number,
   "KmsKeyId": "string",
   "Name": "string",
   "CosBucketName": "string",
   "CosKeyPrefix": "string",
   "CosTopicName": "string"
}
```
### 响应

```
{
   "IsMultiRegionAudit": number,
   "KmsKeyId": "string",
   "Name": "string",
   "CosBucketName": "string",
   "CosKeyPrefix": "string",
   "CmqTopicName": "string"
}
```

