## 1. 接口描述
 
本接口(GetRedisBackupList)用于查询 Redis 实例的备份列表。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>

- 目前备份只保留7天，所以只能查询到最近7天以内的备份，包括用户发起的手动备份和凌晨的系统备份。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='https://cloud.tencent.com/document/product/213/6976' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的 Action 字段为GetRedisBackupList。

| 参数名称 | 是否必选  | 类型 | 描述 |
|:---------|---------|---------|---------|
| limit | 是 | Int | 分页大小。 |
| offset | 是 | Int | 当前页码，默认为0。 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset进行分页查询；例如查询第110~149 这40条记录，则可以设置 offset=110 limit=40。 |
| redisId | 是 | String | 待操作的实例ID，可通过 [DescribeRedis](/document/product/239/1384) 接口返回值中的 redisId 获取。|
| beginTime | 否 | String | 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。 |
| endTime | 否 | String | 结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|:---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| totalCount | Int | 备份总数 |
| data | Object | 实例的备份列表详情 |


其中，data 表示实例的备份列表详情，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|:---------|---------|---------|
| data.redisBackupSet | Array | 实例的备份数组 |

其中，redisBackupSet 表示实例的备份数组，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|:---------|---------|---------|
| startTime | String | 开始备份的时间 |
| backupId | String | 备份ID |
| backupType | String | 备份类型。<br>manualBackupInstance：用户发起的手动备份；<br>systemBackupInstance：凌晨系统发起的备份 |
| status | Int | 备份状态。 <br>1:"备份被其它流程锁定"; <br>2:"备份正常，没有被任何流程锁定"; <br>-1:"备份已过期"；<br>3:"备份正在被导出"; <br>4:"备份导出成功" |
| remark | String | 备份的备注信息 |
| locked | Int | 备份是否被锁定，0：未被锁定；1：已被锁定 |

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|

## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=GetRedisBackupList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&limit=10
&offset=0
&redisId=crs-izbob1wh
&beginTime=2017-02-08 16:46:34
&endTime=2017-02-08 19:09:26
</pre>
返回示例如下：
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 2,
    "data": {
        "redisBackupSet": [
            {
                "startTime": "2017-02-08 16:46:34",
                "backupId": "19266626-eddb-11e6-890a-525400394272",
                "backupType": "manualBackupInstance",
                "status": 2,
                "remark": "testAPI",
                "locked": 0
            },
            {
                "startTime": "2017-02-08 19:09:26",
                "backupId": "0f87ffc6-edef-11e6-b88e-525400394272",
                "backupType": "systemBackupInstance",
                "status": 2,
                "remark": "",
                "locked": 0
            }
        ]
    }
}

```
