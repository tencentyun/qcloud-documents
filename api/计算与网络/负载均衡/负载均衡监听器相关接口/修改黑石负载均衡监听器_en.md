## 1. API Description
Domain: lb.api.qcloud.com
API: ModifyBmLoadBalancerListener

Modify BM load balancer listeners

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of cloud load balancer |
| listenerId | Yes | String | Listener ID |
| listenerName | No | String | Listener name |
| sessionExpire | No | Int | Session duration. 0 means disabled. |
| healthSwitch | No | Int | Indicate whether to enable Health Check: 1 (On) and 0 (Off) |
| timeOut | No | Int | Response timeout. The default is 2 seconds |
| intervalTime | No | Int | Check interval. The default is 5 seconds |
| healthNum | No | Int | Healthy threshold. The default is 3 |
| unhealthNum | No | Int | Unhealthy threshold. The default is 3 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  succeeded, other values:  Failed |
| message | String | Error message |
| requestId | Int | Task ID |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyBmLoadBalancerListener
&loadBalancerId=lb-l9w92y5p
&listenerId=lbl-815iz539
&listenerName=hh
&healthSwitch=1
&timeOut=6
&intervalTime=10
&healthNum=8
&unhealthNum=8
&sessionExpire=800
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "requestId":"2375553"
}
```


