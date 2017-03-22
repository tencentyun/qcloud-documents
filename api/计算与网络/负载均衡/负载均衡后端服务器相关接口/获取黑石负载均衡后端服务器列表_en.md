## 1. API Description
Domain: lb.api.qcloud.com
API: DescribeBmLoadBalancerBackends

Acquire list of BM load balancer backend servers

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of Cloud Load Balancer |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  succeeded, other values:  Failed |
| message | String | Error message |
| totalCount | Int | Total number |
| instanceId | String | Server instance ID |
| weight | String |Server weight |
| instanceName |String| Backend server name |
| lanIp | String | Private IP of the server |
| wanIpSet | Array | Public IP of the server |
| instanceStatus | String | Status of the server |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?
&loadBalancerId=lb-5xunivs0
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "totalCount":1,
    "backendSet":[
        {
			"instanceId" : "cpm-12345",
			"instanceName" : "my-backend-name1",
			"weight" : 10,
			"lanIp" : "10.10.10.1",
			"wanIpSet":["203.195.179.123"],
			"instanceStatus" : 2
		},
    ]
}
```


