## 1. API Description
 This API (CreateBmLoadBalancer) is used to create BM load balancer instances. To use BM load balance service, you must create one or more BM load balancer instances. When the API is successfully called, the unique ID of the BM load balancer instance will be returned. You can purchase two types of BM load balancer instances: public network-based and private network-based. Public network-based load balancer has a BGP VIP which is used to quickly access the CPM bound to the load balancer. Private network-based load balancer has a Tencent Cloud internal VIP which is used to quickly access the CPM bound to the load balancer, but cannot be accessed via Internet.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/document/product/386/6718). The Action field for this API is CreateBmLoadBalancer.
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>

<tr>
<td> unVpcId
<td> Yes
<td> String
<td> ID of the VPC to which the BM load balancer instance belongs.

<tr>
<td> unSubnetId
<td> No
<td> String
<td> You need to specify a subnet ID when purchasing the private network-based load balancer instance within the VPC. The VIP of the private network-based load balancer instance will be generated from this subnet. This field can be left empty in other cases.

<tr>
<td> projectId
<td> No
<td> Int
<td> ID of the project to which the load balancer belongs. If it is left empty, the instance belongs to the default project.

<tr>
<td> loadBalancerType
<td> Yes
<td> String
<td> Type of load balancer. Value can be open or internal. "open" represents public network (with daily rate), and "internal" represents private network.

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

<tr>
<td> tgwSetType
<td> No
<td> String
<td> TGW cluster type of BM load balancer. Value can be tunnel or fullnat. "tunnel" represents tunnel cluster and "fullnat" represents FULLNAT cluster. Default is fullnat. Select tunnel if you want to acquire Client IP.

</tbody></table>

## 3. Response Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Successful; other values: Failed. For more information, please see <a href="/document/product/386/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> loadBalancerIds
<td> Array
<td> ID of the BM load balancer instance created
</tbody></table>

Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 12010 | InvalidResource.LBNumberOverOrderLimit | The number of load balancer instances to be purchased in this order has exceeded the limit |
| 12011 | InvalidResource.LBNumberOverTotalLimit | The number of purchased load balancer instances has exceeded the limit |
| 20002 | InvalidParameter.VpcIdSubnetIdNotExist | The VPC and subnet information does not exist for this account in this region |

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=CreateBmLoadBalancer
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&unVpcId=vpc-xxxx
&loadBalancerType=open
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
        "lb-abcdefgh",
        "lb-abcdefge"
    ]
}
```
