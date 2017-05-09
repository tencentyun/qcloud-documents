## 1. API Description
 This API (DescribeBmLoadBalancersByInstances) is used to query the BM load balancer instances associated with a CPM. The information of the CPM can be its unique ID or its name. You can specify the number of BM load balancer instances returned for the query. Default is 20.
 
Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is DescribeBmLoadBalancersByInstances.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> backendInstanceIds.n
<td> No
<td> Array
<td> Unique ID of the Cloud Physical Machine.
<tr>
<td> backendInstanceName
<td> No
<td> String
<td> Device name of Cloud Physical Machine.
<tr>
<td> offset
<td> No
<td> Int
<td> Data offset, default is 0.
<tr>
<td> limit
<td> No
<td> Int
<td> Length of returned data. Default is 20, maximum is 100.
</tbody></table>

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="/doc/api/456/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> totalCount
<td> Int
<td> The total number of BM load balancer instances meeting the filter criteria.
<tr>
<td> loadBalancerSet
<td> Array
<td> An array of returned BM load balancer instances. The data structure is as follows.
</tbody></table>

</b></th>loadBalancerSet structure</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> String
<td> The unique ID of the BM load balancer instance.
<tr>
<td> loadBalancerName
<td> String
<td> Name of the BM load balancer instance.
<tr>
<td> loadBalancerType
<td> Int
<td> Type of the BM load balancer instance. 2 indicates public network; 3 indicates private network.
<tr>
<td> domain
<td> String
<td> Domain of the BM load balancer instance.
<tr>
<td> loadBalancerVips
<td> Array
<td> VIP list of the BM load balancer instance.
<tr>
<td> status
<td> Int
<td> Status of the BM load balancer instance, <br>0: creating, 1: running.
<tr>
<td> createTime
<td> String
<td> Creation time of the BM load balancer instance.

<tr>
<td> statusTime
<td> String
<td> Time of the last status change for the BM load balancer instance.

<tr>
<td> projectId
<td> Int
<td>Project ID.

<tr>
<td> vpcId
<td> String
<td>VPC ID.

<tr>
<td> subnetId
<td> String
<td>Subnet ID of the VPC.

<tr>
<td> unInstanceId
<td> String
<td>Unique ID of the Cloud Physical Machine.

<tr>
<td> backendLanIp
<td> String
<td>Private IP of the Cloud Physical Machine.

<tr>
<td> backendWanIpSet
<td> Array
<td>A set of public IPs of the Cloud Physical Machine.

<tr>
<td> instanceName
<td> String
<td>Name of the CPM.

</tbody></table>

Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeBmLoadBalancersByInstances
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&backendInstanceIds.0=cpm-aaaa
&backendInstanceName=xx60-yyy
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerSet": [
        {
            "loadBalancerId": "lb-aaaa",
            "loadBalancerName": "test3_aaa",
            "loadBalancerType": 2,
            "domain": "test.bj.123456.aaa.bbb.com",
            "loadBalancerVips": [
                "125.119.210.117"
            ],
            "status": 1,
            "createTime": "2016-01-13 11:08:45",
            "statusTime": "2016-10-13 03:01:04",
            "projectId": 0,
            "vpcId": "vpc-aaaaa",
            "subnetId": "subnet-aaaaa",
            "unInstanceId": "cpm-aaaa",
            "backendLanIp": "10.6.2.11",
            "backendWanIpSet": [
                "125.159.210.228"
            ],
            "instanceName": "xx60-yyy"
        },
        {
            "loadBalancerId": "cpm-aaaa",
            "loadBalancerName": "adafad_test_detail",
            "loadBalancerType": 2,
            "domain": "teyy.gz.45678.aaa.bbb.com",
            "loadBalancerVips": [
                "115.159.240.104"
            ],
            "status": 1,
            "createTime": "2016-05-13 11:07:14",
            "statusTime": "2016-10-13 03:01:04",
            "projectId": 0,
            "vpcId": "vpc-bbbbb",
            "subnetId": "subnet-bbbbb",
            "unInstanceId": "cpm-aaaa",
            "backendLanIp": "10.6.10.66",
            "backendWanIpSet": [
                "115.119.240.228"
            ],
            "instanceName": "xx60-yyy"
        }
    ],
    "totalCount": 2
}
```
