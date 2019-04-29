## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (CreateSubnet) is used to create subnets.
* You must create a VPC before creating a subnet.
* Once a subnet is created, its IP address range cannot be changed. The subnet IP address range must lie within the VPC IP address range. They can be the same, in which case the VPC only has one subnet. It is recommended to keep the subnet IP address range within the VPC IP address range to reserve IP address range for other subnets.
* The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).
* IP address ranges of different subnets cannot overlap with each other within the same VPC.
* A subnet is automatically associated to the default route table once created.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateSubnet |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpcId | Yes | String | ID of the VPC instance you are working with. You can obtain the parameter value from the VpcId field value in the returned result of API DescribeVpcs. |
| SubnetName | Yes | String | Subnet name, which is limited to 60 bytes. |
| CidrBlock | Yes | String | Subnet IP address range. It must lie within the VPC IP address range. Subnet IP address ranges cannot overlap with each other within the same VPC. |
| Zone | Yes | String | ID of the availability zone in which the subnet resides. You may set up disaster recovery across availability zones by choosing different availability zones for different subnets. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Subnet | [Subnet](/document/api/215/##Subnet) | Subnet object. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue.SubnetConflict | Subnet CIDR conflict. |
| InvalidParameterValue.SubnetRange | Invalid subnet CIDR. |
| LimitExceeded | Quota exceeded. |

## 5. Example

### Example 1 Create a subnet

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateSubnet
&Version=2017-03-12
&VpcId=vpc-m3ul053f
&VpcName=TestSubnet
&CidrBlock=10.8.0.0/16
&Zone=ap-guangzhou-1
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
    "Subnet": {
      "AvailableIpAddressCount": 253,
      "CidrBlock": "10.8.255.0/24",
      "IsDefault": false,
      "SubnetId": "subnet-2qhl25io",
      "SubnetName": "TestSubnet",
      "VpcId": "vpc-m3ul053f",
      "Zone": "ap-guangzhou-1"
    }
  }
}
```


## 6. Other Resources

Cloud API 3.0 comes with the following development tools to make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

