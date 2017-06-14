## 1. API Description

This API (QueryBmNatGatewayProductionStatus) is used to query the operation status of the BM NAT gateway
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is QueryBmNatGatewayProductionStatus.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| taskId | Yes | String | Task ID. You can use this ID to query the final result |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  Successful; other values:  Failed |
| message | string | Error message |
| data.result | int | 0: Execution successful; 1: Execution failed; 2: Executing |

 ## 4. Error Codes
 The API does not have a business error code.



## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=QueryBmNatGatewayProductionStatus
&<<a href="https://www.qcloud.com/doc/api/229/6976">Public Request Parameters</a>>
&taskId=2160000000
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
          "result":1
		}
}
```


