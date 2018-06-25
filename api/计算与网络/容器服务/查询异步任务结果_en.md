## 1. API Description
 
This API (DescribeClusterTaskResult) is used to query the result of asynchronous task

Domain for API request: <font style="color:red">ccs.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| requestId   | Yes    | Int | Asynchronous task ID |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed |
| message | String | Module error message description depending on API. For more information, please see Module Error Codes on Error Codes page. |
| status | String | succ, fail, running. |



## 4. Example
Input

```
  https://domain/v2/index.php?Action=DescribeClusterTaskResult
  &requestId=123
  &Other common parameters
```
Output

```
{
    "code": 0,
    "message": "",
    "data": {
        "status": "succ"
    }
}
```
