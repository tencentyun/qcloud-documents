## 1. API Description
This API (CreateSubnet) is used to create subnets.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 

1) You must have created the VPC before you can create subnets.
2) Once a subnet is created, you can no longer change its network segment. The subnet network segment must lie within the VPC network segment. They can be the same, in which case the VPC will only have one subnet. It is recommended to keep subnet network segment within the range of VPC network segment in order to reserve network segment for other subnets.
3) The subnet mask of the smallest possible network segment you can create is 28 (16 IP addresses), while the subnet mask of the largest possible network segment is 16 (65,536 IP addresses).
4) Network segments of different subnets must not overlap with each other within the same VPC.
5) A subnet will be automatically associated to the default routing table once it is created.
 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is CreateSubnet.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID of the subnet, which can be vpcId or unVpcId. unVpcId is recommended. Can be queried via API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| subnetSet.n | Yes | Array | Subnet information array. You can create subnets as you create the VPC. Optional. |
| subnetSet.n.subnetName | Yes | String | Subnet name. You can specify any name you like, but its length should be limited to 60 characters. |
| subnetSet.n.cidrBlock | Yes | String | Subnet network segment. It must lie within the range of the VPC network segment. Subnet network segments must not overlap with each other within the same VPC. |
| subnetSet.n.zoneId | Yes | Int | ID of the availability zone in which the subnet resides. You may set up disaster tolerance across availability zones by choosing different availability zones for different subnets. Refer to <a href="https://cloud.tencent.com/doc/product/215/4927#.E5.8F.AF.E7.94.A8.E5.8C.BA.EF.BC.88zone.EF.BC.89">VPC Availability Zone Instruction</a> for available values.  |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://intl.cloud.tencent.com/document/product/215/4781" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| subnetSet.n | Array | Subnet information, which is returned when a subnet is added. |
| subnetSet.n.subnetId | String | Subnet ID assigned by the system. For example: subnetId_GZ_23. |
| subnetSet.n.unSubnetId | String | Unified subnet ID assigned by the system, upgraded from subnet ID. For example: subnet-5gu2jxf4. The system supports both IDs for compatibility purpose. |
| subnetSet.n.subnetName | String | Subnet name. |
| subnetSet.n.cidrBlock | String | Subnet network segment, for example: 192.168.0.0/25. |
| subnetSet.n.routeTableId | String | ID of the default routing table that is bound to the subnet. For example: gz_rtb_8751. |
| subnetSet.n.zoneId | String | ID of the availability zone in which the subnet resides. For example: 200001. |

 ## 4. Error Code Table
 The following error code list only provides the business logic error codes for this API. For additional common error codes, refer to <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify that the resource information you entered is correct. You can query the VPC via the API <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  |
| InvalidSubnetName | Invalid subnet name. You can specify any name you like, but its length should be limited to 60 characters.  |
| InvalidSubnetCidr | Subnet CIDR is invalid or does not lie within the range of the VPC network segment. Subnet CIDR value range: 10.0.0.0/16, 172.16.0.0/16, 192.168.0.0/16 and their subnets.  |
| InvalidSubnet.Conflict | Subnet network segment is in conflict with other segments within the VPC.  |
| SubnetLimitExceeded | The limit of requested subnet resources for the specific region has been reached. Please contact customer service for more resources. For more information on VPC resource restrictions, see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Usage Restrictions">VPC Usage Restrictions</a>.  |
| InvalidZone.NotFound | Invalid availability zone ID. The availability zone you have entered does not exist or does not support VPC. Refer to <a href="">VPC Availability Zone Instruction</a> for more information on availability zones.  |


## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=CreateSubnet
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-kd7d06of
  &subnetSet.0.subnetName=tttt
  &subnetSet.0.cidrBlock=10.0.200.0/24
  &subnetSet.0.zoneId=800001
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "subnetSet": [
        {
            "subnetId": "gz_subnet_18748",
            "unSubnetId": "subnet-3lzrkspo",
            "routeTableId": "gz_rtb_359",
            "unRouteTableId": null,
            "subnetName": "tttt",
            "cidrBlock": "10.0.200.0\/24",
            "zoneId": 800001
        }
    ]
}

```


