## 1. API Description
Domain: lb.api.qcloud.com
API: DescribeBmLBHealthStatus

Query the health status of BM load balancer

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalanceId | Yes | String | ID of the cloud load balance resource |
| listenerId | No | String | Listener ID |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  succeeded, other values:  Failed |
| message | String | Error message |
| ip | String | Server IP address | 
| protocol | String | Protocol | 
| port | Int | Server port | 
| vport | Int | Port of cloud load balancer | 
| healthStatus | Int | Health check result. 1: healthy; 0: unhealthy; -1: incomplete target. | 


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeBmLBHealthStatus
&loadBalanceId=lb-5xunivs0
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "lb-5xunivs0":[
            {
                "ip":"10.6.100.131",
                "protocol":"tcp",
                "port":"80",
                "vport":"80",
                "healthStatus":"0"
            },
            {
                "ip":"10.6.100.132",
                "protocol":"tcp",
                "port":"80",
                "vport":"80",
                "healthStatus":"0"
            }
        ]
    }
}
```


