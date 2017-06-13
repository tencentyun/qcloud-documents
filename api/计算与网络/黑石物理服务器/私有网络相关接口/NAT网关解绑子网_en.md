## 1. API Description

This API (SubnetUnBindBmNatGateway) is used to unbind subnet from BM NAT gateway
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is SubnetUnBindBmNatGateway.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| natId | Yes | String | Unified ID of NAT gateway, for example: nat-8pbrkzh6 |
| vpcId | Yes | String | VPC ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. You can query this through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>. |
| subnetIds.n | Yes | array | Unique ID of subnet. For example: subnetIds.0=subnet-8pca7qqf. You can query the subnet through API <a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Successful; other values: Failed |
| message | string | Error message |
| data | Array | Returned operation task ID. You can query the creation result by calling API <a href="" title="Query Task Status of Binding EIP to BM NAT Gateway">Query Task Status of Binding EIP to BM NAT Gateway</a> |

 ## 4. Error Codes
 The following error codes only include the business logic error codes for this API. For additional common error codes, please see <a href="https://www.qcloud.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Error Message | Error Description |
|---------|---------|---------|
| -3047 | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct. You can query VPC through API <a href="https://www.qcloud.com/document/api/386/6646" title="DescribeBmVpcEx">DescribeBmVpcEx</a>.  |
| -3030 | InvalidBmSubnet.NotFound | Invalid subnet. Subnet resource does not exist. Please verify whether the resource information entered is correct. You can query the subnet through API <a href="https://www.qcloud.com/document/api/386/6648" title="DescribeBmSubnetEx">DescribeBmSubnetEx</a>.  |
| 13014 | BmVpcNat.NotFound | Invalid NAT gateway. NAT gateway resource does not exist. Please verify whether the resource information entered is correct. You can query the NAT gateway through API DescribeBmNatGateway |  |



## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=SubnetUnBindBmNatGateway
&<<a href="https://www.qcloud.com/doc/api/229/6976">Public Request Parameters</a>>
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


