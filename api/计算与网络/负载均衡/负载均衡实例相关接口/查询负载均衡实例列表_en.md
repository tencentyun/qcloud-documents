# API Description
 This API (DescribeLoadBalancers) is used to obtain the list of load balancer instances. Load balancer instances matching the criteria are returned based on the parameters you entered.

Domain name for API access: `lb.api.qcloud.com`


## Request Parameters
 The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DescribeLoadBalancers.

| Parameter Name | Required | Type | Description |
|---|---|---|---|
| loadBalancerIds.n | No | String | ID of the load balancer instance. |
| loadBalancerType | No | Int | Network type of the load balancer instance: <br>2: Public network-based; 3: Private network-based. |
| forward | No | Int | 1: Application-based; 0: Conventional; -1: All types. |
| loadBalancerName | No | String | Name of the load balancer instance. |
| domain | No | String | Domain name assigned by Tencent Cloud for a conventional public network-based load balancing instance. This field is not applicable to private network-based and application-based cloud load balancing instances.|
| loadBalancerVips.n | No | String | VIP address of load balancer instance. You may enter multiple addresses. |
| backendWanIps.n | No | String | Public IP of the backend CVM |
| backendLanIps.n | No | String | Private IP of the backend CVM |
| offset | No | Int | Data offset. Default is 0. |
| limit | No | Int | The number of returned load balancer instances. Default is 20. |
| orderBy | No | String | Sorting field, which can be: loadBalancerName, createTime, domain, loadBalancerType |
| orderType | No | Int | 1: Descending; 0: Ascending. The default is descending by creation time. |
| searchKey | No | String | Search field: name, domain, and VIP (fuzzy match). |
| projectId | No | Int | ID of the project to which the load balancer instance belongs.　It can be obtained via the API <a href="https://cloud.tencent.com/document/api/214/1261">DescribeProject</a>. |
| withRs | No | Int | Whether the load balancer to be queried is bound to the backend CVM. 0: Not bound to CVM , 1: Bound to CVM, 2: All. |

## Response Parameters

| Parameter Name | Type | Description |
|----|---|----|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| totalCount | Int | The total number of load balancer instances meeting the filter criteria. |
| loadBalancerSet | Array | Returned array of load balancer instances. |

- `loadBalancerSet` is composed as follows:

| Parameter Name | Type | Description |
|----|---|----|
| loadBalancerId | String | ID of the load balancer instance. |
| unLoadBalancerId | String | ID of the load balancer instance. |
| loadBalancerName | String | Name of the load balancer instance. |
| loadBalancerType | Int | Network type of the cloud load balancer instance: <br>2: Public network-based, 3: Private network-based. |
| forward | Int | Indicate whether it is an application-based cloud load balancer. 1: Application-based cloud load balancer; 0: Conventional cloud load balancer. |
| domain | String | Domain name assigned by Tencent Cloud for a conventional public network-based load balancing instance. This field is not applicable to private network-based and application-based cloud load balancing instances. |
| loadBalancerVips | Array | VIP list of the load balancer instance. |
| status | Int | Status of the load balancer instance. <br>0: Creating; 1: Running. |
| createTime | String | The time when the load balancer instance is created. |
| statusTime | String | Time of the last status change for the load balancer instance. |
| projectId | Int | ID of the project to which the load balancer instance belongs. 0: Default project. |
| vpcId | Int | The numerical digits of VPC ID. 0: Basic network. |
| subnetId | Int | The numerical digits of VPC subnet ID. 0: Default subnet. |
| openBgp | Int | Indicate whether it is a high defense LB. 1: High defense LB; 0: Non-high defense LB. |
| snat | Bool | `snat` is enabled for all conventional private network-based load balancers created prior to December 2016. |
| isolation | Int | 0: Not isolated; 1: Isolated. |
| log | String | Whether log is activated by users. Log is only applicable to public network-based load balancers with HTTP and HTTPS listeners created. |


## Example

Use the default parameters to query the list of load balancer instances:
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancers
&<Common request parameters>
&forward=-1
```

Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerSet": [
        {
            "loadBalancerId": "lb-hc1vni0f",
            "unLoadBalancerId": "lb-hc1vni0f",
            "loadBalancerName": "cls-qbesvs66_ng1",
            "loadBalancerType": 2,
            "domain": "cls-qbesvs66-ng1.gz.1251707795.clb.myqcloud.com",
            "loadBalancerVips": [
                "111.230.83.36"
            ],
            "status": 1,
            "createTime": "2017-11-30 14:28:45",
            "statusTime": "2017-11-30 14:29:11",
            "vpcId": 2968,
            "uniqVpcId": "vpc-b2h3xykt",
            "subnetId": 1,
            "projectId": 0,
            "forward": 0,
            "snat": false,
            "openBgp": 0,
            "isolation": 0,
            "log": "",
        }
    ],
    "totalCount": 1
}

```
