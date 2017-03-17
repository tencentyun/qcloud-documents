## 1. API Description
Domain: lb.api.qcloud.com
API: DeleteBmLoadBalancers

Delete BM load balancers

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerIds.n  | Yes | String | ID of cloud load balancer |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| requestId | Int | Task ID |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DeleteBmLoadBalancers
&loadBalancerIds.1=lb-fi018waq
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "requestId":"16916"
}
```


