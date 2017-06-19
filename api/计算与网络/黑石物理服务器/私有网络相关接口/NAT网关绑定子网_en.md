## 1. API Description

This API (SubnetBindBmNatGateway) is used to bind subnet to BM NAT gateway.  
Domain name for API request: vpc.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is EipBindNatGateway.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| natId | Yes | string | Unified ID of BM gateway, for example: nat-df5dfd |
| vpcId | Yes | string | VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. You can query this through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>. |
| subnetIds.n | No | array | Unique ID of subnet. At least one of the two input parameters subnetIds and subnetAll must be passed, for example: subnetIds.0=	subnet-8pca7qqf. You can query the subnet through API <a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>.  |
| subnetAll | No | int | Whether to contain all the subnets, including the new ones. Value: 0 or 1 |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  Successful; other values:  Failed |
| message | String | Error message |
| data | Array | Returned operation task ID. You can query the creation result by calling API <a href="" title="QueryBmNatGatewayProductionStatus">QueryBmNatGatewayProductionStatus</a>. |

## 4. Error Codes
 The following error codes only include the business logic error codes for this API. For additional common error codes, please see <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Error Message | Error Description |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct. You can query the VPC through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>.  |
| -3030 | InvalidBmSubnet.NotFound | Invalid subnet. Subnet resource does not exist. Please verify whether the resource information entered is correct. You can query the subnet through API <a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>.  |
| 13014 | BmVpcNat.NotFound | Invalid NAT gateway. NAT gateway resource does not exist. Please verify whether the resource information entered is correct. You can query the NAT gateway through API DescribeBmNatGateway |
| 13012 | BmVpcNat.SubnetUsed | Subnet has been bound to another NAT gateway.  |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=SubnetBindBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&natId=nat-8pbrkzh6
&vpcId=vpc-ddf411
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


