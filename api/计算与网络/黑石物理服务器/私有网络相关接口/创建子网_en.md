## 1. API Description
 
This API (CreateBmSubnet) is used to create a BM VPC subnet.  
Domain name for API request: vpc.api.qcloud.com

1) You must create a VPC before you can create subnets.  
2) After a subnet is created, you cannot change its IP address range. The subnet IP address range must fall within the VPC IP address range, and they can be the same (on condition that the VPC only has one subnet). It is recommended to keep subnet IP address range within VPC IP address range in order to reserve IP address range for other subnets.  
3) The subnet mask of the smallest possible IP address range you can create is 28 (16 IP addresses), while the subnet mask of the largest possible IP address range is 16 (65,536 IP addresses).  
4) IP address ranges of different subnets must not overlap with each other within the same VPC.  
5) A subnet will be automatically associated to the default routing table once it is created.

 

## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateBmSubnet.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | VPC ID assigned by the system, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-kd7d06of. You can query this through API DescribeBmVpcEx.  |
| subnetSet.n | Yes | Array | Subnet information array. You can create subnets when creating VPC. This is optional.  |
| subnetSet.n.subnetName | Yes | String | Subnet name. You can name the subnet as you like, but its length should be limited to 60 characters.  |
| subnetSet.n.cidrBlock | Yes | String | Subnet IP address range. It must fall within the VPC IP address range. Subnet IP address ranges must not overlap with each other within the same VPC.  |
| vlanId | No | Int | vlanId bound to subnet. Default is 5.  |

 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| subnetSet.n | Array | Subnet information, which is returned when a subnet is added. |
| subnetSet.n.subnetId | String | Subnet ID assigned by the system. For example: subnetId_GZ_23. |
| subnetSet.n.unSubnetId | String | Unified subnet ID assigned by the system, upgraded from subnet ID. For example: subnet-5gu2jxf4. The system supports both IDs for compatibility purpose. |
| subnetSet.n.subnetName | String | Subnet name. |
| subnetSet.n.cidrBlock | String | Subnet IP address range, for example: 192.168.0.0/25. |
| subnetSet.n.zoneId | String | ID of the availability zone in which the subnet resides. For example: 1000800001. |

## 4. Error Codes
 
| Error Code | Error Message | Description |
|--------|---------|---------|
| -3047  | InvalidBmVpc.NotFound | Invalid VPC. VPC resource does not exist. Please verify whether the resource information entered is correct.  |
| -3001  | InvalidInputParams | The format of input parameter is incorrect. For example, the length of the name must not more than 60 characters.  |
| -3046  | BmVpc.SubnetCidr.Conflict | Subnet IP address range is in conflict with other subnet IP address range within the VPC.  |
| -3240  | BmVpc.VlanId.Conflict | Repeated subnet VLANID.  |
| -3058  | BmVpc.SubnetLimitExceeded | The limit of requested subnet resources for the specific region has been reached.  |
| -3055  | BmVpc.InvalidSubnetCidr | Subnet CIDR is invalid or does not fall within the VPC IP address range.  |

## 5. Example
 
Input
```

  https://vpc.api.qcloud.com/v2/index.php?Action=DescribeBmVpcEx
	&<Common Request Parameters>
	&vpcId=vpc-kd7d06of
    &subnetSet.0.subnetName=tttt
    &subnetSet.0.cidrBlock=10.0.200.0/24
    &vlanId=2000
```

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "subnetSet": [
        {
            "subnetId": "gz_subnet_8949",
            "unSubnetId": "subnet-gvt14y8u",
            "subnetName": "tttt",
            "cidrBlock": "10.10.30.0/24",
            "zoneId": 1000800001
        }
    ]
}

```


