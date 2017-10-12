## 1. API Description

This API (EipUnBindNatGateway) is used to unbind EIP from NAT gateway.
Domain for API request: vpc.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| natId | Yes | String | Unified ID of NAT gateway, for example: nat-8pbrkzh6 |
| vpcId | Yes | String | Virtual private cloud ID or unified ID (unified ID is recommended), for example: vpc-ddf411 |
| assignedEipSet.n | Yes | array | Elastic IP array, for example: assignedEipSet.0=183.60.249.122 |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed |
| message | string | Error message |
| taskId | int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">DescribeVpcTaskResult</a> API.  |

## 4. Error Code List
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNatGatewayId.NotFound | Invalid NAT gateway, NAT gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the NAT gateway via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway">DescribeNatGateway</a> API |
| NatGatewayEipNotEmpty | NAT gateway must retain an EIP, the last EIP can not be unbound |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=EipUnBindNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&natId=nat-8pbrkzh6
&vpcId=vpc-ddf411
&assignedEipSet.0=183.60.249.122
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "taskId":16168
}
```


