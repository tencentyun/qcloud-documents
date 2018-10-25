## 1. API Description

This API (DescribeVpcTaskResult) is used to query task execution result APIs
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

## 2. Request Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeVpcTaskResult.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| taskId | Yes | Int | ID of request task. For example: 15454. This is provided by specific asynchronous operation API.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned information.  |
| data.status | Int | Current status of the task. 0: Succeeded; 1: Failed; 2: In progress.  | 
| codeDesc | String | Error code  |


## 4. Error Codes
The API does not have a business error code. For common error codes, see <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes">VPC Error Codes</a>

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeVpcTaskResult
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&taskId=6356081
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "status": 0
    }
}
```
