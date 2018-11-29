## 1. API Description

This API (ModifyNatGateway) is used to modify NAT gateways.
Domain for API request: vpc.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. 

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | string | Virtual private cloud ID or unified ID (unified ID is recommended), for example: vpc-x7d44d. |
| natId | Yes | string | Unified ID of NAT gateway, for example: nat-df45454. |
| natName | No | string | NAT gateway name. It supports 1-25 characters, including uppercase and lowercase English letters, numbers, and underscores.   |
| bandwidth | No | int | The maximum public network output bandwidth of the gateway (unit: Mbps),  which is 100 Mbps by default. For more information about supported data, please refer to <a href="https://cloud.tencent.com/doc/product/215/1682" title="Gateway Description" >Virtual Private Cloud Gateway Description</a>.  |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  succeeded, other values:  Failed |
| message | String | Error message |

## 4. Error Codes
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> API |
| InvalidNatGatewayId.NotFound | Invalid NAT gateway, NAT gateway resource does not exist. Please verify that the resource information you entered is correct. You can query the NAT gateway via the <a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway">DescribeNatGateway</a> API |
| InvalidNatGatewayName | The NAT gateway name is invalid. Valid NAT gateway name shall have a length of 1-60 characters, and can contain uppercase and lowercase English letters, numbers, and underscores |

## 5. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyNatGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&natId=nat-jngbqyfs
&vpcId=314
&natName=cici
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```



