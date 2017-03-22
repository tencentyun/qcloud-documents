## 1. API Description
Domain: lb.api.qcloud.com
API: DescribeBmLoadBalancerListeners

Acquire list of BM load balancer listeners

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of cloud load balancer |
| listenerIds.n | No | String | Listener ID |
| protocol | No | Int | Protocol type of listener. 2: TCP, 3: UDP |
| loadBalancerPort | No | Int | Listener port |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  succeeded, other values:  Failed |
| message | String | Error message |
| listenerSet.loadBalancerPort | Int | Listening port of the cloud load balancer | 
| listenerSet.instancePort | Int | Listening port of the backend server | 
| listenerSet.protocol | Int | Protocol type of listener. 2: TCP, 3: UDP | 
| listenerSet.status | Int | Listener status. <br>0: binding, 1: bind successful, 2: bind failed, 3: unbinding, 4: unbind failed | 
| listenerSet.listenerName | String | Listener name | 
| listenerSet.listenerId | String | Listener ID | 
| listenerSet.sessionExpire | Int | Session duration | 
| listenerSet.healthSwitch | Int | Indicate whether Health Check is enabled: 1 (On) and 0 (Off). | 
| listenerSet.timeOut | Int | Response timeout | 
| listenerSet.intervalTime | Int | Health check time interval | 
| listenerSet.healthNum | Int | Healthy threshold | 
| listenerSet.unhealthNum | Int | Unhealthy threshold| 


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeBmLoadBalancerListeners
&loadBalancerId=lb-k6p4918n
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "listenerSet":[
        {
            "loadBalancerPort":"80",
            "instancePort":"80",
            "protocol":"2",
            "status":"1",
            "listenerName":"1",
            "listenerId":"lbl-odn5baps",
            "sessionExpire":"900",
            "healthSwitch":"1",
            "timeOut":"6",
            "intervalTime":"10",
            "healthNum":"8",
            "unhealthNum":"8"
        }
    ],
    "totalCount":"1"
}
```


