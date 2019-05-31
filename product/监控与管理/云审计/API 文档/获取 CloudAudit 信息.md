
## 接口描述
DescribeAudits 用于获取跟踪集信息。
接口访问域名：`cloudaudit.api.qcloud.com`


## 请求参数
|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|auditNameList|	是|	Array	|auditName 列表|


## 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| auditLists | Array | 跟踪集列表 |

其中 auditList 的参数如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| IsMultiRegionAudit | Number | 是否开启多地域查询。0 代表否，1 代表是 |
| KmsKeyId | String | Kms 密钥 ID |
| Name | String | Audit 名称 |
| CosBucketName | String | COS Bucket 名称 |
| CosKeyPrefix | String | COS Bucket 前缀|
| CmqTopicName | String | CMQ 主题名称 |
| Status | Number | 	Audit 状态，0 代表关闭，1 代表开启 |


## 实际案例
### 请求

```
{
   "auditNameList": [ "String" ]
}
```
### 响应

```
{
   "auditLists": [
      {
         "IsMultiRegionAudit": "Number",
         "KmsKeyId": "String",
         "Name": "String",
         "CosBucketName": "String",
         "CosKeyPrefix": "String",
         "CmqTopicName": "String",
         "Status":0
      }
   ]
}
```
