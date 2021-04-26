## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (CreateVpc) is used to create VPCs.
* The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses). For more information, please see the document about VPC IP address ranges.
* You can create a subnet while creating a VPC. When you create a subnet, you should also configure the subnet IP address range and the availability zone in which the subnet resides. Subnet IP address ranges in the same VPC cannot overlap with each other, and the disaster recovery across different availability zones is allowed. For more information, please see the document about VPC availability zones.
* If you create a subnet while creating a VPC, the system will create a default route table and associate it with this subnet.
* The number of VPC resources that can be created in a region is also limited. For more information, please see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Use Limits">VPC Use Limits</a>. To request more resources, contact the customer service.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateVpc |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpcName | Yes | String | VPC name, which is limited to 60 bytes. |
| CidrBlock | Yes | String | VPC CIDR, which can only lie within these three private IP address ranges: 10.0.0.0/16, 172.16.0.0/12, and 192.168.0.0/16. |
| EnableMulticast | No | String | Indicates whether to enable multicast. true: Enable; false: Disable. |
| DnsServers.N | No | Array of String | DNS address. A maximum of 4 addresses are supported. |
| DomainName | No | String | Domain name |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Vpc | [Vpc](/document/api/215/##Vpc) | VPC object. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. |
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| LimitExceeded | Quota exceeded. |

## 5. Example

### Example 1 Create a VPC

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateVpc
&Version=2017-03-12
&VpcName=TestVPC
&CidrBlock=10.8.0.0/16
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
    "Vpc": {
      "CidrBlock": "10.8.0.0/16",
      "EnableMulticast": false,
      "VpcId": "vpc-4tboefn3",
      "VpcName": "TestVPC"
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

