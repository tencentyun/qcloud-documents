## 1. API Description
Domain: lb.api.qcloud.com
API: CreateBmLoadBalancer

Create BM load balancers

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerType | Yes | Int | Type of the cloud load balancer: 2. Public network with daily rate 3. Private network |
| vpcId | Yes | String | VPC ID |
| subnetId | Yes | String | VPC subnet ID |
| projectId | No | Int | Project ID of the cloud load balancer |
| goodsNum | No | Int | Number of cloud load balancers purchased. The default is 1, and the maximum is 20 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  succeeded, other values:  Failed |
| message | String | Error message |
| loadBalancerIds | Array | Description (to be added) |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=CreateBmLoadBalancer
&vpcId=vpc-k7j1t2q1
&subnetId=subnet-keqt3oty
&loadBalancerType=3
&loadBalancerName=test5
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "loadBalancerIds":[
        "lb-17hjqgbx"
    ]
}
```


