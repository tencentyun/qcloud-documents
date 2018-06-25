## 1. API Description
This API (GetMongoDBJobInfo) is used to query execution status of a task.
Domain for API request: <font style='color:red'>mongodb.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is GetMongoDBJobInfo.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | String | Task ID returned when the task is executed |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Object | Execution result of the task |

Parameter data indicates the task execution result, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.status | Int | Task status. 0: To be executed; 1: Executing, 2: Succeeded; 3: Failed; -1: Execution Error |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11050 | InvalidParameter |Incorrect business parameter |


## 5. Example
<pre>
https://mongodb.api.qcloud.com/v2/index.php?Action=GetMongoDBJobInfo
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&jobId=11963
</pre>
The returned results are as below:
```
{
    "code": 0,
	"message": "",
	"codeDesc": "Success",
    "data": {
        "status": 2
    }
}
```
