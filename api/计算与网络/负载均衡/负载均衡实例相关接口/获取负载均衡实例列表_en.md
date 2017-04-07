## 1. API Description
 DescribeLoadBalancers is used to get the user's list of cloud load balancer instances. The cloud load balancer instance matching the criteria will be returned based on the parameters you entered. The following request parameters can be entered for filtering.

Domain for API access: lb.api.qcloud.com


## 2. Request Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeLoadBalancers.

| Parameter Name | Required | Type | Description |
|---|---|---|---|
| loadBalancerIds.n | No | String | The unique ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). |
| loadBalancerType | No | Int | Type of the cloud load balancer instance <br>1: public network (without daily rate) 2: public network (with daily rate) 3: private network. |
| loadBalancerName | No | String | Name of the cloud load balancer instance. |
| domain | No | String | Domain of the cloud load balancer instance assigned by Tencent Cloud. This field is not applicable to application-based cloud load balancers. |
| loadBalancerVips.n | No | String | VIP address of the cloud load balancer instance. You may enter multiple addresses. |
| backendWanIps.n | No | String | Public IP of the backend CVM, which filters out the cloud load balancers that have bound to such public IP. |
| backendLanIps.n | No | String | Private IP of the backend CVM, which filters out the cloud load balancers that have bound to such private IP. |
| offset | No | Int | Data offset. Default: 0. |
| limit | No | Int | Length of returned data. Default: 20. |
| searchKey | No | String | Search field: name, domain, and VIP (fuzzy match). |
| projectId | No | Int | The project ID of the cloud load balancer instance.　You can query it via <a href="/doc/api/403/4400">DescribeProject</a>. |
| forward | No | Int | 1: Pull the application-based cloud load balancer only; -1: pull all types; 0: pull non-application-based cloud load balancer only. The default is 0. |


## 3. Response Parameters

| Parameter Name | Type | Description |
|----|---|----|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| totalCount | Int | Total number of cloud load balancer instances that meet the filtering conditions. |
| loadBalancerSet | Array | The returned array of the cloud load balancer instance | |

- loadBalancerSet structure

| Parameter Name | Type | Description |
|----|---|----|
| unLoadBalancerId | String | The unified ID of the cloud load balancer instance. (This field is recommended for other APIs.) |
| loadBalancerName | String | Name of the cloud load balancer instance. |
| loadBalancerType | Int | Type of the cloud load balancer instance. <br>1: Public network without static IP; 2: public network with static IP (including application-based); 3: private network. |
| forward | Int | Indicate whether it is an application-based cloud load balancer. 1: Application-based cloud load balancer; 0: non-application-based cloud load balancer. |
| domain | String | The domain of the cloud load balancer instance. This field is not applicable to the cloud load balancer of private network and application-based cloud load balancer instance. |
| loadBalancerVips | Array | VIP list of the cloud load balancer instance. |
| status | Int | Status of the cloud load balancer instance, <br>0: creating, 1: running. |
| createTime | String | Creation time of the cloud load balancer instance. |
| statusTime | String | Time of the last status change of the cloud load balancer instance. |
| projectId | Int | The project ID of the cloud load balancer instance. 0: default project. |
| vpcId | Int | The numerical digits of VPC ID. 0: basic network. |
| subnetId | Int | The numerical digits of VPC subnet ID. 0: default subnet. |
| loadBalancerId | String | The unique ID of the cloud load balancer instance. |
| openBgp | Int | Indicate whether it is an anti-DDoS cloud load balancer. 1: Anti-DDoS cloud load balancer; 0: non-anti-DDoS cloud load balancer. |


## 4. Example

Use the default parameters to query the list of cloud load balancer instances:
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancers
&<Common request parameters>
&forward=-1
```

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerSet": [
         {
            "loadBalancerId": "qlb8e2fe70327928898848ac1def05fcd51",
            "unLoadBalancerId": "lb-6efswuxa",
            "loadBalancerName": "fasfs",
            "loadBalancerType": 2,
            "domain": "hebfda.gz.1351000042.clb.myqcloud.com",
            "loadBalancerVips": [
                "112.90.8.180"
            ],
            "status": 1,
            "createTime": "2016-07-15 17:29:23",
            "statusTime": "2016-10-22 14:28:42",
            "vpcId": 20,
            "subnetId": 0,
            "projectId": 0,
            "forward": 1,
            "openBgp": false
        },
        {
            "loadBalancerId": "qlba4f89771ea5c1a99d69f5edbf9af0bf3",
            "unLoadBalancerId": "lb-ltkip4do",
            "loadBalancerName": "jj",
            "loadBalancerType": 2,
            "domain": "ouie.gz.1351000042.clb.myqcloud.com",
            "loadBalancerVips": [
                "183.60.249.52"
            ],
            "status": 1,
            "createTime": "2016-05-27 16:31:25",
            "statusTime": "2016-10-24 10:51:17",
            "vpcId": 20,
            "subnetId": 0,
            "projectId": 0,
            "forward": 0,
            "openBgp": false
        }
    ],
    "totalCount": 2
}

```
