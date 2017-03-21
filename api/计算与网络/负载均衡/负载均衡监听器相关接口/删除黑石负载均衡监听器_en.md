## 1. API Description
Domain: lb.api.qcloud.com
API: DeleteBmLoadBalancerListeners

Delete BM load balancer listeners

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of cloud load balancer |
| listenerIds.n | Yes | String | Listener ID |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  succeeded, other values:  Failed |
| message | String | Error message |
| requestId | Int | Task ID |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DeleteBmLoadBalancerListeners
&loadBalancerId=lb-51jf1v2l
&listenerIds.0=lbl-5xunivs1
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "requestId":"2375530"
}
```


