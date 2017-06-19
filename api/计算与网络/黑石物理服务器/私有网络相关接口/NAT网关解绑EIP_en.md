## 1. API Description

This API (EipUnBindBmNatGateway) is used to unbind EIP from BM NAT gateway.  
Domain name for API request: vpc.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is EipUnBindNatGateway.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| natId | Yes | String | Unified ID of NAT gateway, for example: nat-8pbrkzh6 |
| vpcId | Yes | String | VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. You can query this through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>. |
| assignedEipSet.n | Yes | array | EIP array, for example: assignedEipSet.0=183.60.249.122 |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | int | Error code. 0: Successful; other values: Failed |
| message | string | Error message |
| data | Array | Returned operation task ID. You can query the creation result by calling API <a href="" title="QueryBmNatGatewayProductionStatus">QueryBmNatGatewayProductionStatus</a>. |

## 4. Error Codes
 The following error codes only include the business logic error codes for this API. For additional common error codes, please see <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Error Message | Error Description |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct. You can query VPC through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>.  |
| 13014 | BmVpcNat.NotFound | Invalid NAT gateway. NAT gateway resource does not exist. Please verify whether the resource information entered is correct. You can query the NAT gateway through API DescribeBmNatGateway |
| 13010 | BmVpcNat.InvalidEip | EIP bound to NAT gateway does not exist.  |
| 13011 | BmVpcNat.InvalidEipVpcId | EIP and NAT gateway do not belong to the same VPC.  |
| 13008 | BmVpcNat.MustLeaveOneEip | NAT gateway must retain at least one EIP, and the last EIP cannot be unbound.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=EipUnBindBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&natId=nat-8pbrkzh6
&vpcId=vpc-ddf411
&assignedEipSet.0=183.60.249.122
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


