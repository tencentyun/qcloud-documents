## 1. API Description
Domain: lb.api.qcloud.com
API: ModifyBmLoadBalancerBackends

Modify the weight of BM Load Balancer backend servers

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of Cloud Load Balancer |
| backends.n.instanceId  | Yes | String | Mapped backend machine |
| backends.n.weight	  | Yes | String | Weight of the mapped backend machine, value range 0-100, default is 10 |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| requestId | Int | Task ID |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?
&loadBalancerId=lb-51jf1v2l
&backends.0.instanceId=cpm-owlr8otf
&backends.0.weight=32
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "requestId":"2375529"
}
```


