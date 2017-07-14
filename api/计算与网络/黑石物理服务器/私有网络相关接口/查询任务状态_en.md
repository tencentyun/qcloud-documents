## 1. API Description
 
This API (QueryBmTaskResult) is used to query the status of task of adding or removing CPM to or from the subnet.  
Domain name for API request: vpc.api.qcloud.com


 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is QueryBmTaskResult.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| taskId | Yes | String | Task ID.  |


 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned status of operations performed on CPM. |


## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| 10001  | BmVpc.InvalidParameterValue | Invalid parameter  |

## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=QueryBmTaskResult
	&<Common Request Parameters>
	&taskId=9999
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "tcpm-g5lyzbqd": "success"
    }
}

```


