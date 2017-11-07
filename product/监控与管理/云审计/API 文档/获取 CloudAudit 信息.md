# 获取 CloudAudit 信息
## 接口描述
  DescribeAudits 用于获取 CloudAudit 信息。
## 请求参数
|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|auditNameList|	是|	array	|auditName 列表|


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
   "auditList": [ 
      { 
         "IsMultiRegionTrail": number,
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


