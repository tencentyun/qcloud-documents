## 1. API Description
This API (CdbTdsqlInitInstance) is used to initialize instances.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlInitInstance.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceIds.n (cdbInstanceIds is an array. The input parameters here are the array elements) | Yes | String | Instances to be initialized, with n starting with 0 |
| config.n (config is an array. The input parameters here are the array elements) | No | String | List of parameters. Each element is a combination of Param and Value, with n starting with 0. For more information on parameters, please see [View Database Parameters](/doc/api/309/5403). |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Logic error code description |
| data | Array | Returned data |
| data.ids | Array | IDs of affected instances | 
| data.flowid | Int | Task flow ID | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| IllegalInitParam | Invalid parameter for instance initialization |
| InnerSystemError | Internal system error (unrelated to service) |
| InstanceStatusError | Instance status error |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlInitInstance
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&cdbInstanceIds.0=40727
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "ids":[
            "40727"
        ],
        "flowid":"3329"
    }
}
```


