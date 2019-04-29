## 1. API Description
This API (ManualBackupInstance) is used to back up a CRS instance manually.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

- Please do not call this API frequently. The number of calls is limited to 24 each day, otherwise the operation will fail.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is ManualBackupInstance.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| redisId | Yes | String | ID of instance to work with. This can be obtained from redisId in the returned values of API [DescribeRedis](/document/product/239/1384). |
| remark | No | String | Remarks of backup |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Object | Task ID |

Parameter data indicates the task ID, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.requestId | Task ID | Task ID. You can use the API [DescribeTaskInfo](/document/product/239/1387) to query the task execution status |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |
| 10701 | InstanceNotExists | No instance can be found for the serialId |
| 10707 | InstanceLockedError | The operation is impossible because the instance is locked |
| 10702 | InstanceStatusAbnormal | The operation is impossible due to an abnormal instance status. For example, the instance has a status of "in process" or "isolated" or "deleted" |

## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=ManualBackupInstance
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&redisId=crs-izbob1wh
&remark=test_api
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
    "data": {
        "requestId": 375062
    }
}

```
