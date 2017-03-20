## 1. API Description
DescribeBmLoadBalancers is used to get the list of BM load balancer instances.
Domain name for API request:<font style='color:red'>lb.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the<a href='/doc/api/372/4153' title='Common request parameters'> Common Request Parameters</a> page for details. The Action field for this API is DescribeBmLoadBalancers.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerIds.n (loadBalancerIds is an array, whose elements need to be entered as input parameters) | No | String | ID of the cloud load balancer |
| loadBalancerType | No | Int | Type of the cloud load balancer. 2: Public network with daily rate 3: Private network |
| loadBalancerName | No | String | Name of the cloud load balancer |
| domain | No | String | Domain of the cloud load balancer. Naming rule: 1-60 characters, including English letters (in lowercase), numbers, "." or "-". This field is not applicable to the cloud load balancer of private network |
| loadBalancerVips.n (loadBalancerVips is an array, whose elements need to be entered as input parameters) | No | String | Public IP of the cloud load balancer. You may enter multiple addresses. |
| backendWanIps.n (backendWanIps for the array, is an array, whose elements need to be entered as input parameters) | No | String | Public IP of backend server |
| offset | No | Int | Data offset. Default: 0 |
| limit | No | Int | Length of returned data. Default: 20 |
| searchKey | No | String | Name, domain, and VIP (fuzzy match) |
| orderBy | No | String | Sorting field, which can be: loadBalancerName, createTime, domain, and loadBalancerType |
| orderType | No | Int | 1: Backward sequence; 0: Forward sequence. The default is forward sequence. |
| projectId | No | Int | Project ID. You can query it via v2/DescribeProject. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common request parameters'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| loadBalancerSet | Array | Description (to be added) |
| totalCount | Int | Description (to be appended) |
| codeDesc | String | Description (to be added) |


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeBmLoadBalancers
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalance=1
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "loadBalancerSet":[
        
    ],
    "totalCount":"0",
    "codeDesc":"Success"
}
```


