## 1. 接口描述
 
本接口(GetRedisTaskList)用于 Redis 实例的任务列表。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='https://cloud.tencent.com/document/product/213/6976' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的 Action 字段为 GetRedisTaskList。

| 参数名称 | 是否必选  | 类型 | 描述 |
|:---------|---------|---------|---------|
| limit | 是 | Int | 分页大小 |
| offset | 是 | Int | 当前页码，默认为0。 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset进行分页查询；例如查询第110~149 这40条记录，则可以设置 offset=110 limit=40。 |
| redisId | 否 | String | 实例ID, 可通过 [DescribeRedis](/document/product/239/1384) 接口返回值中的 redisId 获取，支持按照实例ID筛选任务。|
| redisName | 否 | String | 实例名称，可通过 [DescribeRedis](/document/product/239/1384) 接口返回值中的 redisName 获取，支持按照实例名称筛选任务。 |
| beginTime | 否 | String | 开始时间，格式如：2017-02-08 16:46:34。 查询在 [beginTime, endTime] 时间段内提交的任务列表。 |
| endTime | 否 | String | 结束时间，格式如：2017-02-08 19:09:26。 查询在 [beginTime, endTime] 时间段内提交的任务列表。 |
| taskStatus | 否 | Array | 一个或者多个任务状态，n表示从0开始的数组下标。 支持按照任务状态筛选任务。 任务状态定义为 <br>0：待执行;<br>1：执行中;<br>2：成功;<br>3：失败;<br>-1：执行出错  |
| taskType | 否 | Array | 一个或者多个任务类型，n表示从0开始的数组下标。 支持按照任务类型筛选。 任务类型定义为 <br>task_importRdb：导入Rdb的任务；<br>task_exportBackup：导出备份的任务；<br>task_restoreBackup：恢复实例的任务；<br>task_restoreStream：回档实例的任务（集群版实例可回档3天内任意时间点，但是，最近10分钟的数据不可回档）；<br>task_backupInstance：备份实例的任务；<br>task_cleanInstance：清空实例的任务；<br>task_resizeInstance：升级实例的任务 |

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|:---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 错误信息描述, 成功时，该值为空 |
| codeDesc | String | 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。 |
| totalCount | Int | 任务总数 |
| data | Object | 任务列表详情 |


其中，data 表示任务列表详情，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|:---------|---------|---------|
| data.redisTaskSet | Array | 任务详情数组 |

其中，redisTaskSet 表示任务详情数组，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|:---------|---------|---------|
| startTime | String | 任务的提交时间，格式如： 2017-02-10 16:56:18 |
| taskName | String | 任务名称：<br>newInstance：新建实例；<br>resizeInstance：升级实例；<br>closeInstance：隔离实例；<br>cleanInstance：清空实例；<br>startInstance：解隔离实例；<br>deleteInstance：删除实例；<br>setPassword：设置实例密码；<br>importRdb：导入Rdb；<br>exportBackup：导出备份；<br>restoreBackup：恢复实例；<br>restoreStream：回档实例（集群版实例可回档3天内任意时间点，但是，最近10分钟的数据不可回档）；<br>backupInstance：备份实例 |
| redisName | String | 实例名称 |
| redisId | String | 实例ID |
| projectId | Int | 实例所属的项目ID |
| status | Int | 任务执行状态，0：待执行；1：执行中；2：成功；3：失败；-1 执行出错 |
| progress | Int | 任务执行进度，0：未完成；1：已完成 |

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|

## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=GetRedisTaskList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&limit=10
&offset=0
&beginTime=2016-12-28 00:03:52
&endTime=2017-02-11 00:03:52
&redisId=crs-izbob1wh
&redisName=测试API专用&taskStatus.0=2
&taskType.0=task_restoreBackup
&taskType.1=task_backupInstance
&taskType.2=task_cleanInstance
</pre>
返回示例如下：
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 9,
    "data": {
        "redisTaskSet": [
            {
                "startTime": "2017-02-10 16:56:18",
                "taskName": "restoreBackup",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-10 15:02:36",
                "taskName": "backupInstance",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-10 14:59:29",
                "taskName": "backupInstance",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-09 19:00:24",
                "taskName": "backupInstance",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 19:09:26",
                "taskName": "backupInstance",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 17:21:32",
                "taskName": "restoreBackup",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 16:46:34",
                "taskName": "backupInstance",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 15:38:16",
                "taskName": "cleanInstance",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 15:35:25",
                "taskName": "backupInstance",
                "redisName": "测试API专用",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            }
        ]
    }
}

```
