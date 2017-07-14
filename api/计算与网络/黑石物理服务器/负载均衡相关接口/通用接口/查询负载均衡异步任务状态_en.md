## 1. API Description
 
This API (DescribeBmLoadBalancersTaskResult) is used to query asynchronous task execution status of load balancer instances.

Domain for API request: lb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| requestId | Yes | Int | Task ID. This is provided by specific asynchronous operation API. |




## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed. For more information, please see [Common Error Codes](/document/product/386/6725). |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| data | Obj | Returned object. |

"data" is used to describe the status information of the current task and is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| status | Int | Current task status. 0: Successful; 1: Failed; 2: In progress. |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?
Action=DescribeBmLoadBalancersTaskResult
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
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
