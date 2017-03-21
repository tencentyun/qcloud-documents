## 1. API Description
Domain: lb.api.qcloud.com
API: ModifyBmLoadBalancerAttributes

Modify the attributes of BM load balancers

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of cloud load balancer |
| loadBalancerName | No | String | The name of cloud load balancer. The name can contain 1-20 characters, including English letters, Chinese characters, numbers, "-" or "_". |
| domainPrefix | No | String | Domain prefix. The domain name of cloud load balancer instance consists of the domain prefix entered by user and the domain suffix in configuration file to ensure the uniqueness. Naming rule: 1-20 characters, including English letters (in lowercase), numbers or "-" This field is not applicable to the cloud load balancer of private network. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| requestId | Int | Task ID |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyBmLoadBalancerAttributes
&loadBalancerId=lb-51jf1v2l
&loadBalancerName=adafad
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "requestId":"2375550"
}
```


