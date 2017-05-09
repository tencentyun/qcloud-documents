## 1. API Description
 This API (DescribeBmLoadBalancers) is used to acquire the list of BM load balancer instances. BM load balancer instances matching the conditions will be returned based on the parameters you entered. The entered filter parameter can be the name, type or public VIP of the BM load balancer instance. All BM load balancer instances under the account will be returned if no parameter is specified.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is DescribeBmLoadBalancers.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerIds.n
<td> No
<td> Array
<td> ID of the BM load balancer instance.

<tr>
<td> loadBalancerType
<td> No
<td> Int
<td>Type of BM load balancer. Value can be 2 or 3. 2 indicates public network type (with daily rate), 3 indicates private network type.

<tr>
<td> loadBalancerName
<td> No
<td> String
<td>Name of the BM load balancer.

<tr>
<td> domain
<td> No
<td> String
<td>Domain of the BM load balancer. Naming rule: 1-60 characters, including English letters (in lowercase), numbers, "." or "-". This field is not applicable to private network-based BM load balancers

<tr>
<td> loadBalancerVips.n
<td> No
<td> Array
<td>Public IP address obtained by the BM load balancer instance. You may enter multiple addresses.

<tr>
<td> backendWanIps.n
<td> No
<td> Array
<td>Public IP of the backend server.

<tr>
<td> offset
<td> No
<td> Int
<td>Data offset, default is 0.

<tr>
<td> limit
<td> No
<td> Int
<td>Length of returned data. Default: 20.

<tr>
<td> searchKey
<td> No
<td> String
<td>Name, domain or VIP used for fuzzy search.

<tr>
<td> orderBy
<td> No
<td> String
<td>Field used for sorting, which can be: loadBalancerName, createTime, domain and loadBalancerType.

<tr>
<td> orderType
<td> No
<td> Int
<td>1: Descending; 0: Ascending. Default is ascending.

<tr>
<td> projectId
<td> No
<td> Int
<td>Project ID.
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
<td> loadBalancerSet
<td> Array
<td>Returned array containing the load balancer instances.

<tr>
<td> totalCount
<td> Int
<td>The total number of BM load balancer instances meeting the filter criteria.

</tbody></table>

loadBalancerSet structure
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>

<tr>
<td> loadBalancerId
<td> String
<td>The unique ID of the BM load balancer instance.

<tr>
<td> loadBalancerName
<td> String
<td>Name of the BM load balancer instance.

<tr>
<td> loadBalancerType
<td> Int
<td>Type of the BM load balancer instance. 2 indicates public network, 3 indicates private network.

<tr>
<td> domain
<td> String
<td>Domain of the BM load balancer instance. There is no domain for private network-based BM load balancer instance.

<tr>
<td> loadBalancerVips
<td> Array
<td>VIP list of the BM load balancer instance.

<tr>
<td> status
<td> Int
<td>Status of the BM load balancer instance, 0: creating, 1: running.

<tr>
<td> createTime
<td> String
<td>Creation time of the BM load balancer instance.

<tr>
<td> statusTime
<td> String
<td>Time of the last status change for the BM load balancer instance.

<tr>
<td> vpcId
<td> Int
<td>The numerical digits of the VPC ID. 0 means basic network.

<tr>
<td> subnetId
<td> Int
<td>The numerical digits of the VPC subnet ID. 0 means default subnet.

<tr>
<td> projectId
<td> Int
<td>Project ID.

<tr>
<td> latestPayMode
<td> String
<td>The latest billing mode of the BM load balancer. Value can be "flow" (Pay by Traffic) or "bandwidth" (Pay by Bandwidth).

<tr>
<td> payMode
<td> String
<td>Current billing mode of the BM load balancer instance.

<tr>
<td> bandwidth
<td> Int
<td>Bandwidth. The value is 0 when the billing mode is "flow".

</tbody></table>

Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeBmLoadBalancers
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerIds.0=lb-aaaa
&loadBalancerIds.1=lb-bbbb
&loadBalancerType=2
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
            "loadBalancerName": "11a-LB",
            "loadBalancerType": 2,
            "domain": "12f.bj.1251001002.hslb.myqcloud.com",
            "loadBalancerVips": [
                "112.159.241.61"
            ],
            "status": 1,
            "createTime": "2016-10-12 19:57:29",
            "statusTime": "2016-10-13 14:31:06",
            "vpcId": "vpc-aaaaa",
            "subnetId": "0",
            "projectId": 0,
            "latestPayMode": "flow",
            "payMode": "bandwidth",
            "bandwidth": 0
        },
        {
            "loadBalancerId": "lb-bbbb",
            "loadBalancerName": "112-LB",
            "loadBalancerType": 2,
            "domain": "130.bj.1251001002.hslb.myqcloud.com",
            "loadBalancerVips": [
                "125.119.211.111"
            ],
            "status": 1,
            "createTime": "2016-10-12 19:57:29",
            "statusTime": "2016-10-13 03:01:06",
            "vpcId": "vpc-bbbb",
            "subnetId": "0",
            "projectId": 0,
            "latestPayMode": "flow",
            "payMode": "flow",
            "bandwidth": 0
        }
    ],
    "totalCount": 2
}
```
