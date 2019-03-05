## 1. API Description
 
This API (CreateVpc) is used to create VPCs.

Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>

1) The subnet mask of the smallest possible IP address range that a user can create is 28 (16 IP addresses), while the subnet mask of the largest possible IP address range is 16 (65,536 IP addresses). For the VPC IP address range layout, refer to the VPC Network Segment Layout Instruction.
2) When creating a VPC, you can also create a subnet. Please have the subnet IP address range and the availability zone in which the subnet resides well organized if a subnet is created. Subnet IP address ranges cannot overlap with each other within the same VPC, and disaster tolerance across different availability zones is allowed. For more information, refer to VPC Availability Zone Instruction.
3) If you create a subnet at the same time, the system will create a default routing table and associate the subnet with this default routing table.
4) The number of VPC resources that can be created in a region is also limited. For more information, please see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Service Limits">VPC Service Limits</a>. If you need to create more resources, please contact the online customer service. 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is CreateVpc.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcName | Yes | String | VPC name. You can specify any name you like, but its length should be limited to 60 characters. The VPC name must be unique under the same region.  |
| cidrBlock | Yes | String | VPC IP address range. Available values include 10.0.0.0/16, 172.16.0.0/16 and 192.168.0.0/16 as well as their subnets. Please refer to VPC Network Segment Layout Instruction for details.  |
| subnetSet.n | No | Array | (Optional) Subnet information array. You can create subnets as you create the VPC. |
| subnetSet.n.subnetName | Yes | String | Subnet name. You can specify any name you like, but its length should be limited to 60 characters. |
| subnetSet.n.cidrBlock | Yes | String | Subnet IP address range. It must lie within the range of the VPC network segment. Subnet IP address range must not overlap with each other within the same VPC. |
| subnetSet.n.zoneId | Yes | Int | ID of the availability zone in which the subnet resides. You may set up disaster tolerance across availability zones by choosing different availability zones for different subnets. Refer to <a href="https://cloud.tencent.com/doc/product/215/4927#.E5.8F.AF.E7.94.A8.E5.8C.BA.EF.BC.88zone.EF.BC.89">VPC Availability Zone Instruction</a> for available values.  | 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| vpcId | String | vpcId assigned by the system. For example: gz_vpc_266. |
| unVpcId | String | Unified ID for VPC assigned by the system, which is upgraded from vpcId. The system supports both IDs for compatibility purpose, but the unified ID is recommended. For example: vpc-2ari9m7h. |
| vpcCreateTime | String | VPC creation time, for example: 2015-11-06 11:33:52. |
| subnetSet.n | Array | Subnet information, which is returned when a subnet is added. |
| subnetSet.n.subnetId | String | Subnet ID assigned by the system. For example: subnetId_GZ_23. |
| subnetSet.n.unSubnetId | String | Unified subnet ID assigned by the system, upgraded from subnet ID. For example: subnet-5gu2jxf4. The system supports both IDs for compatibility purpose. |
| subnetSet.n.routeTableId | String | ID of the default routing table that is bound to the subnet. For example: gz_rtb_8751. |
| subnetSet.n.subnetName | String | Subnet name. |
| subnetSet.n.cidrBlock | String | Subnet IP address range, for example: 192.168.0.0/25. |
| subnetSet.n.zoneId | String | ID of the availability zone in which the subnet resides. For example: 200001. |
| routeTableSet.n | Array | Routing table information. By default, a subnet is associated with the default routing table. |
| routeTableSet.n.routeTableId | String | Routing table ID assigned by the system. For example: gz_rtb_8751. |
| routeTableSet.n.routeTableType | Int | Routing table type. 0: ordinary routing table; 1: default routing table. |
| routeTableSet.n.routeTableName | String | Routing table name. |

## 4. Error Codes
 The following error code list only provides the error codes for this API. For common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.
 
| Error Code | Description |
|---------|---------|
| InvalidVpcName | Invalid VPC name. It should be within 60 characters.  |
| InvalidVpcName.InUse | The VPC name is already in use. The VPC name of the same developer within the same region must be unique.  |
| InvalidVpcCidr | Invalid VPC CIDR. Available values include 10.0.0.0/16, 172.16.0.0/16 and 192.168.0.0/16 as well as their subnets. Please refer to VPC Network Segment Layout Instruction for details.  |
| VpcLimitExceeded | The limit of requested VPC resources for the specific region has been reached. Please contact customer service for more resources. For more information, please see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Service Limits">VPC Service Limits</a>.  |
| InvalidVpc.NotFound |The VPC does not exist. Please check the information you entered. |

## 5. Example
 
Input
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=CreateVpc
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcName=bbbtest
  &cidrBlock=192.168.0.0/16
  &subnetSet.0.subnetName=wikitest
  &subnetSet.0.cidrBlock=192.168.1.0/24
  &subnetSet.0.zoneId=800001

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "vpcId": "gz_vpc_266",
    "uniqVpcId": "vpc-2ari9m7h",
    "vpcCreateTime": "2015-11-06 11:33:52",
    "subnetSet": [
        {
            "subnetId": "gz_subnet_18720",
            "unSubnetId": "subnet-5gu2jxf4",
            "routeTableId": "gz_rtb_8751",
            "subnetName": "wikitest",
            "cidrBlock": "192.168.1.0/24",
            "zoneId": 800001
        }
    ],
    "routeTableSet": [
        {
            "routeTableId": "gz_rtb_8751",
            "routeTableType": 1,
            "routeTableName": "Default"
        }
    ]
}

```


