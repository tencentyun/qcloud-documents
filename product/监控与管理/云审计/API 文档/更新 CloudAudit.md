
## 接口描述
UpdateAudit 用于更新云审计跟踪集，其中可用于更新指定日志文件中的一些设置，例如路径，COS Bucket 等设置，请注意跟踪集的名称是不能修改的。对路径的更改，不需要停止跟踪集服务。对 COS Bucket 的更改，如果该 COS Bucket 之前是跟踪集日志文件的目标，则可以更改成功。否则需要手动授权 COS 存储桶，使得跟踪集具有写权限才行。

接口访问域名：`cloudaudit.api.qcloud.com`


## 请求参数
以下请求参数列表仅列出了接口请求参数。

|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|IsMultiRegionAudit	|否|	Number	|是否开启多地域采集。0：不开启，1：开启|
|KmsKeyId	|否|	String	| Kms 的 scretId，用于数据加密|
|Name	|是|	String	|跟踪集的名称，3-128 字节，只能包含 ASCII 编码字母`a-z，A-Z`，数字`0-9`，下划线`_`|
|CosBucketName	|是|	String	|要投递的 COS Bucket 的名称，命名规范参照 COS 的命名要求|
|CosKeyPrefix	|否|	String	|COS Bucket前缀，命名规范参照 COS|
|CmqTopicName	|否|	String	|CMQ 主题名称，如果开启消息队列请填写，命名规范参照 CMQ 要求|

## 响应参数

|参数名称|类型|描述|
|---------|---------|--------|
|IsMultiRegionAudit	|	Number	|是否开启多地域采集，0：不开启，1：开启|
|KmsKeyId	|	String	|  Kms 的 scretId，用于数据加密|
|Name	|	String	|跟踪集的名称，3-128字节，只能包含 ASCII 编码字母`a-z，A-Z`，数字`0-9`，下划线`_`。|
|CosBucketName	|	String	|要投递的 COS Bucket 的名称，命名规范参照 COS 的命名要求|
|CosKeyPrefix	|	String	|COS Bucket前缀，命名规范参照 COS|
|CmqTopicResource|String|Cmq 主题资源|
|CmqTopicName	|	String	|CMQ 主题名称，如果开启消息队列请填写，命名规范参照 CMQ 要求|

## 实际案例
### 请求

```shell
{
   "IsMultiRegionAudit": "Number",
   "KmsKeyId": "String",
   "Name": "String",
   "CosBucketName": "String",
   "CosKeyPrefix": "String",
   "CosTopicName": "String"
}
```

### 响应
```shell
{
   "IsMultiRegionAudit": "Number",
   "KmsKeyId": "String",
   "Name": "String",
   "CosBucketName": "String",
   "CosKeyPrefix": "String",
   "CmqTopicResource": "String",
   "CmqTopicName": "String"
}
```
