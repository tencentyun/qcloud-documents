## 1. API Description

This API (DescribeSubnet) is used to query subnet attribute.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 
 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is DescribeSubnet.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID of the subnet, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-piztzbpy. Can be queried via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  | 
| subnetId | Yes | String | Subnet ID assigned by the system. Both subnetId and unSubnetId are supported. unSubnetId is recommended. For example: subnet-piztzbpy. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Succeeded, other values:  Failed.  |
| message | String | Error message.  |
| subnetId | String | Subnet ID assigned by the system. For example: subnetId_GZ_23.  |
| subnetName | String | Subnet name. |
| subnetCreateTime | String | Subnet creation time, for example: 2015-10-30 16:10:49. |
| cidrBlock | String | Subnet network segment, for example: 192.168.0.0/25. |
| routeTableId | String | ID of the default routing table that is bound to the subnet. For example: gz_rtb_8751. |
| zoneId | String | ID of the availability zone in which the subnet resides. For example: 200001. |
| totalIPNum | Int | Number of IPs within the subnet. |
| availableIPNum | Int | Number of available IPs within the subnet. |

 ## 4. Error Code Table
  The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidSubnet.NotFound | Invalid subnet. Subnet resource does not exist. Please verify that the resource information you entered is correct. You can query subnets via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>.  |

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeSubnet
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=gz_vpc_265
  &subnetId=subnet-piztzbpy
  &subnetName=apiSubnetTest
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "subnetId": "gz_subnet_18712",
    "subnetName": "apiSubnetTest",
    "subnetCreateTime": "2015-10-30 16:10:49",
    "routeTableId": "gz_rtb_8747",
    "cidrBlock": "10.100.100.0\/25",
    "zoneId": 800001,
    "totalIPNum": 125,
    "availableIPNum": 125
}

```


