## 1. API Description
 This API (DescribeBmLoadBalancers) is used to acquire the list of BM load balancer instances. BM load balancer instances matching the criteria are returned based on the parameters you entered. The input filter parameter can be the name, type or public VIP of the load balancer instance. If no parameter is specified, all load balancer instances under the account are returned.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, see [Common Request Parameters](/document/product/386/6718). The Action field for this API is DescribeBmLoadBalancers.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerIds.n
<td> No
<td> Array
<td> ID of load balancer instance.

<tr>
<td> loadBalancerType
<td> No
<td> String
<td>Type of load balancer. Value can be open or internal. "open" represents public network (with daily rate), and "internal" represents private network.

<tr>
<td> loadBalancerName
<td> No
<td> String
<td>Name of load balancer.

<tr>
<td> domain
<td> No
<td> String
<td>Domain name of load balancer. The domain name should be a combination of 1-60 characters comprised of lowercase letters, numbers, "." or "-". This field is not applicable to private network-based BM load balancers

<tr>
<td> loadBalancerVips.n
<td> No
<td> Array
<td>Public IP obtained by the load balancer instance. Multiple IPs are allowed.

<tr>
<td> offset
<td> No
<td> Int
<td>Data offset. Default is 0.

<tr>
<td> limit
<td> No
<td> Int
<td>Length of returned data. Default is 20.

<tr>
<td> searchKey
<td> No
<td> String
<td>Name, domain name or VIP used for fuzzy search.

<tr>
<td> orderBy
<td> No
<td> String
<td>Field used for sorting (loadBalancerName, createTime, domain and loadBalancerType).

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

<tr>
<td> exclusive
<td> No
<td> Int
<td>Whether TGW cluster is exclusive.

<tr>
<td> tgwSetType
<td> No
<td> String
<td>TGW cluster type of load balancer. Value can be tunnel or fullnat. "tunnel" represents tunnel cluster and "fullnat" represents FULLNAT cluster.

<tr>
<td> unVpcId
<td> No
<td> String
<td>"unVpcId" to which the load balancer belongs.
</tbody></table>

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Successful; other values: Failed. For more information, please see <a href="/document/product/386/6725" title="Common Error Codes">Common Error Codes</a> on Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> loadBalancerSet
<td> Array
<td>Returned array of load balancer instances.

<tr>
<td> totalCount
<td> Int
<td>The total number of load balancer instances meeting the filter criteria.

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
<td>The unique ID of the load balancer instance.

<tr>
<td> loadBalancerName
<td> String
<td>Name of the load balancer instance.

<tr>
<td> loadBalancerType
<td> String
<td>Type of the load balancer instance.  "open" represents public network, and "internal" represents private network.

<tr>
<td> domain
<td> String
<td>Domain name of the load balancer instance. Private network-based load balancer instance has no domain name.

<tr>
<td> loadBalancerVips
<td> Array
<td>VIP list of the load balancer instance.

<tr>
<td> status
<td> Int
<td>Status of the load balancer instance. 0: Creating; 1: Running.

<tr>
<td> createTime
<td> String
<td>The time when the load balancer instance is created.

<tr>
<td> statusTime
<td> String
<td>Time of the last status change for the load balancer instance.

<tr>
<td> unVpcId
<td> String
<td>Unique ID of BM VPC.

<tr>
<td> unSubnetId
<td> String
<td>Unique ID of BM VPC subnet.

<tr>
<td> vpcId
<td> Int
<td>Integer ID of BM VPC.

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
<td>The last billing mode of the load balancer. Value can be flow (Pay by Traffic) or bandwidth (Pay by Bandwidth).

<tr>
<td> payMode
<td> String
<td>Current billing mode of the load balancer instance.

<tr>
<td> bandwidth
<td> Int
<td>Bandwidth. The value is 0 when the billing mode is "flow".

<tr>
<td> tgwSetType
<td> String
<td>TGW cluster type of load balancer.
</tbody></table>

Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeBmLoadBalancers
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerType=open
&tgwSetType=fullnat
&unVpcId=vpc-abcdefgh
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerSet": [
        {
            "loadBalancerId": "lb-abcdefgh",
            "loadBalancerName": "XXX",
            "loadBalancerType": "open",
            "domain": "abc.hslb.myqcloud.com",
            "loadBalancerVips": [
                "115.115.115.115"
            ],
            "status": 1,
            "createTime": "2017-03-08 15:38:00",
            "statusTime": "2017-04-25 21:03:40",
            "unVpcId": "vpc-abcdefgh",
            "unSubnetId": "0",
            "vpcId": 1000,
            "subnetId": 0,
            "projectId": 0,
            "latestPayMode": "flow",
            "payMode": "flow",
            "bandwidth": 0,
            "tgwSetType": "fullnat"
        }
    ],
    "totalCount": 1
}
```
