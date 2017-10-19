## 1. API Description

This API (DeleteNatGateway) is used to delete NAT gateways.
Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

When the NAT gateway is deleted, the routing entry containing this NAT gateway in the routing table will also be deleted.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID or unified ID (unified ID is recommended), for example: vpc-xfd55df |
| natId | Yes | String | Unified ID of highly available gateway, for example: nat-7t9nf3pu |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  succeeded, other values:  Failed |
| message | String | Error message |
| taskId | Int | Task ID. The operation result can be queried with taskId. For more information, refer to <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">QueryNatGatewayProductionStatus</a> API.  |

## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API. |
| InvalidNatGatewayId.NotFound | Invalid NAT gateway, NAT gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the NAT gateway via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway">DescribeNatGateway</a> API. |


## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DeleteNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=190
&natId=nat-7t9nf3pu
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "taskId":"16284"
}
```


