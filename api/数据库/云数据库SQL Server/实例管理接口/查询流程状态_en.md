## 1. API Description
This API (GetFlowStatus) is used to query flow status.
Domain for API request: sqlserver.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see<a href='https://cloud.tencent.com/document/api/238/7328
' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetFlowStatus.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| flowId | Yes | Int | Flow ID |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/238/7334#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned data |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Status. 0: Successful. 1: Failed. 2: In progress |

## 4. Error Codes

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 1000 | SystemError | System error. Contact customer service. |
| 1002 | DBConnectError | Database connection error |

## 5. Example
Input
<pre>
https://sqlserver.api.qcloud.com/v2/index.php?Action=GetFlowStatus
&<<a href="https://cloud.tencent.com/document/api/238/7328">Common request parameters</a>>
&flowId=3329
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "status":"0"
    }
}
```


