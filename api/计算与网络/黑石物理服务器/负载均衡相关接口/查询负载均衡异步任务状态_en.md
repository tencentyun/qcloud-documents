## 1. API Description
 
This API (DescribeBmLoadBalancersTaskResult) is used to query asynchronous task execution status of BM load balancer instances.

Domain for API request: <font style="color:red">lb.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| requestId | Yes | Int | Task ID. This is provided by specific asynchronous operation API. |




## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| Data | Obj | Returned object. |

data is used to describe the status information of the current task. It includes the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Current task status. 0: Succeeded; 1: Failed; 2: In progress. |


## 4. Example
 
Input

<pre>
	https://domain/v2/index.php?
	Action=DescribeBmLoadBalancersTaskResult
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
	&requestId=12345
</pre>
Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "status": 1
    }
}

```
