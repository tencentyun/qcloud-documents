## API Description
This API (ModifyForwardLBName) is used to modify the name of application-based load balancer.
 
Domain name for API access: `lb.api.qcloud.com`

## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/product/214/4183) page. The Action field for this API is ModifyForwardLBName.


| Parameter Name | Required | Type | Description |
|-|-|-|-|-|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| loadBalancerName | Yes | String | New name of load balancer instance, which should be a combination of 1-20 characters comprised of letters, numbers, en dashes (-) or undercores (_). |
 
## Response Parameters
 

| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |

## Example
 
Request
```
https://lb.api.qcloud.com/v2/index.php?Action=ModifyForwardLBName
&<Common request parameters>
&loadBalancerId=lb-abcdefgh
&loadBalancerName=newLBName
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```


