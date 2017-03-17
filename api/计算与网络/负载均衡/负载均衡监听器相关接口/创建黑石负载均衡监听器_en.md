## 1. API Description
Domain: lb.api.qcloud.com
API: CreateBmLoadBalancerListeners

Create BM load balancer listener

## 2. Input Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> The ID of the cloud load balancer, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="http://www.qcloud.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E9%A1%B9%E7%9B%AE%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>
<tr>
<td> listeners.n.loadBalancerPort
<td> Yes
<td> Int
<td> Cloud load balance listening port for the listener, 1-65535
<tr>
<td> listeners.n.instancePort
<td> Yes
<td> Int
<td> Backend server listening port for the listener, 1-65535
<tr>
<td> listeners.n.protocol
<td> Yes
<td> Int
<td> Protocol type of the listener. <br>2: TCP, 3: UDP.<br>
Public network (with daily rate) supports UDP and TCP;<br>
Private network supports TCP and UDP.
<tr>
<td> listeners.n.listenerName
<td> No
<td> String
<td> Listener name
<tr>
<td> listeners.n.sessionExpire
<td> No
<td> Int
<td> Session duration. 0 means disabled. Default is 0. <br>900-3600 seconds;
<tr>
<td> listeners.n.healthSwitch
<td> No
<td> Int
<td> Indicate whether to enable Health Check: 1 (On) and 0 (Off). Default is 1.
<tr>
<td> listeners.n.timeOut
<td> No
<td> Int
<td> Response timeout, default is 2 seconds. Value range is 2-60 seconds, must be smaller than intervalTime<br>
<tr>
<td> listeners.n.intervalTime
<td> No
<td> Int
<td> Health check time interval, default is 5 seconds. Value range is 5-300 seconds. Value range for http listeners (with daily rate) is 30-300 seconds, default is 30 seconds.
<tr>
<td> listeners.n.healthNum
<td> No
<td> Int
<td> Healthy threshold. Default is 3. Value range: 2-10.
<tr>
<td> listeners.n.unhealthNum
<td> No
<td> Int
<td> Unhealthy threshold, default is 3 times. Value range: 2-10 
<tr>
</tbody></table>


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  succeeded, other values:  Failed |
| message | String | Error message |
| requestId | Int | Description (to be appended) |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=CreateBmLoadBalancerListeners
&loadBalancerId=lb-l9w92y5p
&listeners.0.loadBalancerPort=80
&listeners.0.instancePort=80
&listeners.0.protocol=2
&listeners.0.listenerName=1
&listeners.0.healthSwitch=1
&listeners.0.timeOut=6
&listeners.0.intervalTime=10
&listeners.0.healthNum=8
&listeners.0.unhealthNum=8
&listeners.0.sessionExpire=900
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "requestId":"2375551"
}
```


