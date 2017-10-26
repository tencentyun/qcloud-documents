## 1. API Description
 API DeleteLoadBalancerListeners is used to delete one or more listeners of application-based cloud Load balancer instances.
 
Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DeleteForwardLBSeventhListeners.
 
| Parameter Name | Required | Type | Description |
|-|-|-|-|-|
| loadBalancerId | Yes | String | Uniform ID of cloud load balancer instance, i.e. unLoadBalancerId. It can be queried by entering 1 or -1 in input parameter "forward" field of API <a href="https://cloud.tencent.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerIds.n | Yes | String | ID of application-based cloud load balancer listener. It can be queried through API DescribeForwardLBListeners. |
 
## 3. Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| requestId | Int | Request task ID. The operation status can be queried through API [DescribeLoadBalancersTaskResult](/doc/api/244/4007). |

## 4. Example
 
Input
```
https://lb.api.qcloud.com/v2/index.php?Action=DeleteForwardLBSeventhListeners
&<Common request parameters>
&loadBalanceId=lb-abcdefgh
&listenerIds.0=lbl-20cxbf40
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 27689
}
```


