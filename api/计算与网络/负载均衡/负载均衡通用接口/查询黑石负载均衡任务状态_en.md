## 1. API Description
Domain: lb.api.qcloud.com
API: DescribeBmLoadBalancersTaskResult

Query the task status of BM load balancer task

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| requestId | Yes | Int | Task ID|


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| status | Int | Task status.  0: Succeeded; 1: Failed; 2: In progress.| 


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeBmLoadBalancersTaskResult
&requestId=1
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "status":1
    }
}
```


