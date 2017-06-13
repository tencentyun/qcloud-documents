## 1. API Description
This API (CreateBmNatGateway) is used to create a BM NAT gateway
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateBmNatGateway.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| natName | Yes | string | NAT gateway name, which has a length of 1-25 characters, and can contain uppercase and lowercase English letters, numbers, and underscores.  |
| vpcId | Yes | string | VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. You can query this through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>.  |
| maxConcurrent | Int | Maximum gateway concurrent connections. For example: 1,000,000, 3,000,000, 10,000,000.  |
| assignedEipSet.n | No | Array | At least one of the two EIP arrays bound to the gateway, assignedEipSet and autoAllocEipNum, must be passed, for example: assignedEipSet.0=10.0.0.1. For more information about EIP, please see Elastic IP. |
| subnetIds.n | No | Array | Array of unique IDs of subnets bound to a gateway. For example: subnet-k20jbhp0. You can query the subnet through API <a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>. |
| subnetAll | No | int | Whether to contain all the subnets under the VPC, including the new ones. If subnetAll is 0, you must pass subnetIds subnet information |
| autoAllocEipNum | No | int | The number of EIPs for new requests. The system will generate several EIPs according to your needs. At least one of the assignedEipSet and autoAllocEipNum must be passed. For more information on EIP, please see Elastic IP.  |



## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Successful; other values: Failed |
| message | string | Error message |
| data | Array | Returned operation task ID. You can query the creation result by calling API <a href="" title="Query Production Status of NAT Gateway">Query Production Status of NAT Gateway</a> |

 ## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, please see <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Error Message | Error Description |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct. You can query VPC through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>.  |
| -3030 | InvalidBmSubnet.NotFound | Invalid subnet. Subnet resource does not exist. Please verify whether the resource information entered is correct. You can query the subnet through API <a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>.  |
| 13006 | InvalidBmVpc.NatGatewayLimitExceeded |The number of created NAT gateways exceeds the limit. Please contact customer service for more resources. The maximum number of NAT gateways allowed to be created for each VPC is 5 |
| 13010 | BmVpcNat.InvalidEip | EIP bound to NAT gateway does not exist.  |
| 13011 | BmVpcNat.InvalidEipVpcId | EIP and NAT gateway do not belong to the same VPC.  |
| 13012 | BmVpcNat.SubnetUsed | Subnet has been bound to another NAT gateway.  |
| 13013 | BmVpcNat.EipUsed | EIP bound to NAT gateway is already in use.  |
| 13015 | BmVpcNat.EipLimitExceeded | The number of EIPs bound to NAT gateway has reached the limit.  |
## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">Public Request Parameters</a>>
&natName=zhezhe
&vpcId=vpc-kd7d06of
&maxConcurrent=1000000
&autoAllocEipNum=1
</pre>
Output
```
{
	"code": 0,
	"message": "",
	"data": {
		"taskId": 9641
	}
}
```


