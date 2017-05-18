## 1. API Description
Domain: lb.api.qcloud.com
API: InquiryBmLBPrice

Query the price of BM load balancer

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerType | Yes | Int | Type of the cloud load balancer: 2. Public network with daily rate 3. Private network |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  succeeded, other values:  Failed |
| message | String | Error message |
| price | Int | Price |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=InquiryBmLBPrice
&loadBalancerType=3
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "price":"0"
}
```


