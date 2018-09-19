## 1. API Description

This API (UpgradeNatGateway) is used to upgrade the NAT gateway specification.
Domain for API request: vpc.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | string | Virtual private cloud ID or unified ID (unified ID is recommended), for example: vpc-xdf54d |
| natId | Yes | string | Unified ID of highly available gateway, for example: nat-xdf54d |
| maxConcurrent | Yes | int | Maximum gateway concurrent connections. Available values include 1,000,000 (small), 3,000,000 (medium) and 10,000,000 (large) |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed.|
| message | String | Error message |
| billId | string | Order ID. You can query the upgrade result by calling <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3%e7%9a%84%e7%94%9f%e4%ba%a7%e7%8a%b6%e6%80%81?viewType=preview" title="Query Upgrade Status of NAT Gateway">Query Upgrade Status of NAT Gateway</a> |


## 4. Error Codes
The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNatGatewayId.NotFound | Invalid NAT gateway, NAT gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the NAT gateway via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway">DescribeNatGateway</a> API |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=UpgradeNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=314
&natId=nat-et8e970y
&maxConcurrent=3000000
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "billId":"20160416160000002485261276560190"
}
```


