## 1. 接口描述
本接口(ExportRedisBackup)用于导出 Redis 实例的备份。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>

- 导出备份为rdb格式的文件；
- 只有集群版实例才需要导出备份；
- 只有导出备份后，才能调用GetBackupDownloadUrl接口下载该备份;
- 只能导出备份状态为2的备份，可以通过[GetRedisBackupList](/document/product/239/8403)接口获取备份状态。


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='https://cloud.tencent.com/document/product/213/6976' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为ExportRedisBackup。

| 参数名称 | 是否必选  | 类型 | 描述 |
|:---------|---------|---------|---------|
| redisId | 是 | String | 待操作的实例ID，可通过 [DescribeRedis](/document/product/239/1384) 接口返回值中的 redisId 获取。|
| backupId | 是 | String | 备份ID，可通过 [GetRedisBackupList](/document/product/239/1384) 接口返回值中的 backupId 获取。 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| data | Object | 任务ID |

其中，data 表示任务ID，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|:---------|---------|---------|
| data.requestId | 任务ID | 任务ID，可通过 [DescribeTaskInfo](/document/product/239/1387) 接口查询任务执行状态|

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|
|10701|InstanceNotExists|没有找到serialId对应的实例|
|11213|BackupNotExists|根据backupId，没有找到实例对应的备份|
|11214|OnlyClusterInstanceCanExportBackup|只有集群版的实例才支持导出备份|
|10711|BackupStatusInvalid|备份状态无效（集群版只能导出状态为2的备份）|

## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=ExportRedisBackup
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&redisId=crs-j30wibe7
&backupId=3a07b27e-f744-11e6-babc-525400082493
</pre>
返回示例如下：
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
	 "data": {
        "requestId": 400151
    }
}
```
