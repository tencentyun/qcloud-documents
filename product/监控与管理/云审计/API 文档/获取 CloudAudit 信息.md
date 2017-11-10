# 获取 CloudAudit 信息
## 接口描述
  DescribeAudits 用于获取 CloudAudit 信息。
## 请求参数
|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|auditNameList|	是|	array	|auditName 列表|
## 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| auditLists | Array | 跟踪集数组 |

其中 auditList 的参数如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| IsMultiRegionAudit | number | 是否开启多地域查询（0 代表否，1 代表是） |
| KmsKeyId | string | Kms 密钥 ID |
| Name | string | audit 名称 |
| CosBucketName | string | COS Bucket 名称 |
| CosKeyPrefix | string | COS Bucket 前缀|
| CmqTopicName | string | Cmq 主题名称 |
| Status | number | 	audit 状态，0 代表关闭、1 代表开启 |


## 实际案例
### 请求

```
{
   "auditNameList": [ "string" ]
}
```
### 响应

```
{
   "auditLists": [ 
      { 
         "IsMultiRegionAudit": number,
         "KmsKeyId": "string",
         "Name": "string",
         "CosBucketName": "string",
         "CosKeyPrefix": "string",
         "CmqTopicName": "string",
         "Status":0
      }
   ]
}
```


