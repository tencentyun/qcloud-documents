## 1. API Description
 This API (CreateBmLoadBalancer) is used to create BM load balancer instances. To use BM load balance service, you must create one or multiple BM load balancer instances. When the API is successfully called, the unique ID of the BM load balancer instance will be returned. You can purchase two types of BM load balancer instances: public network type and private network type. Public network-based BM load balancer has a corresponding BGP VIP which is used to quickly access the CPM bound to the public network-based BM load balancer. Private network-based BM load balancer has a corresponding Tencent Cloud internal VIP which is used to quickly access the CPM bound to the private network-based BM load balancer, but cannot be accessed via Internet.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is CreateBmLoadBalancer.
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>

<tr>
<td> vpcId
<td> Yes
<td> String
<td> ID of the VPC to which the BM load balancer instance belongs.

<tr>
<td> subnetId
<td> No
<td> String
<td> You need to specify subnet ID when purchasing the private network-based BM load balancer instance within the VPC. The VIP of the private network-based BM load balancer instance will be generated from this subnet. You can leave this field empty in other situations.

<tr>
<td> projectId
<td> No
<td> Int
<td> ID of the project to which the BM load balancer belongs. If left empty, the instance will belong to the default project.

<tr>
<td> loadBalancerType
<td> Yes
<td> Int
<td> Type of the BM load balancer. The value can be 2 or 3. 2 indicates public network; 3 indicates private network.

<tr>
<td> goodsNum
<td> No
<td> Int
<td> Number of BM load balancer instances to purchase. Default is 1, and maximum is 20.

<tr>
<td> payMode
<td> No
<td> String
<td> Billing mode of BM load balancer. Value can be flow (Pay by Traffic) or bandwidth (Pay by Bandwidth). Default is flow.

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
<td> loadBalancerIds
<td> Array
<td> ID of the BM load balancer instance created
</tbody></table>

Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 12010 | InvalidResource.LBNumberOverOrderLimit | The number of load balancer instances to be purchased in this order has exceeded the limit |
| 12011 | InvalidResource.LBNumberOverTotalLimit | The number of purchased load balancer instances has exceeded the limit |
| 20002 | InvalidParameter.VpcIdSubnetIdNotExist | The account has no such VPC information and subnet information in this region |

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=CreateBmLoadBalancer
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=vpc-xxxx
&loadBalancerType=2
&goodsNum=2
&payMode=flow
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerIds": [
        "lb-aaaa",
        "lb-bbbb"
    ]
}
```
