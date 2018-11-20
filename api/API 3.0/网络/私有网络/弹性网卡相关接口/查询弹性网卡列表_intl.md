## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DescribeNetworkInterfaces) is used to query the ENI list.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeNetworkInterfaces |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| NetworkInterfaceIds.N | No | Array of String | ENI instance ID, such as eni-pxir56ns. A maximum of 100 instances are allowed for each request. NetworkInterfaceIds and Filters cannot be specified at the same time. |
| Filters.N | No | Array of [Filter](/document/api/215/##Filter) | Filter condition. NetworkInterfaceIds and Filters cannot be specified at the same time.<br/><li> vpc-id - String - (Filter condition) VPC instance ID, such as vpc-f49l6u0z.</li><li> subnet-id - String - (Filter condition) Subnet instance ID, such as subnet-f49l6u0z.</li><li> network-interface-id - String - (Filter condition) ENI instance ID, such as eni-5k56k7k7.</li><li> attachment.instance-id - String - (Filter condition) CVM instance ID, such as ins-3nqpdn3i.</li><li> groups.security-group-id - String - (Filter condition) ID of the security group instance, such as sg-f9ekbxeq.</li><li> network-interface-name - String - (Filter condition) ENI instance name.</li><li> network-interface-description - String - (Filter condition) ENI instance description.</li> |
| Offset | No | Integer | Offset. Default is 0. |
| Limit | No | Integer | Number of values to be returned. Default is 20. Maximum is 100. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| NetworkInterfaceSet | Array of [NetworkInterface](/document/api/215/##NetworkInterface) | List of details of an instance. |
| TotalCount | Integer | Number of instances matching the filter condition. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter.Coexist | Parameters specified conflict with each other. |
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| ResourceNotFound | Resource does not exist. |

## 5. Example

### Example 1 Query ENI list

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeNetworkInterfaces
&Version=2017-03-12
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "NetworkInterfaceSet": [
      {
        "Attachment": {},
        "CreatedTime": "2017-11-16 19:56:00",
        "GroupSet": [
          "sg-c2r7lnxh",
          "sg-f9ekbxeq"
        ],
        "MacAddress": "20: 90: 6F: F3: 3D: BD",
        "NetworkInterfaceDescription": "",
        "NetworkInterfaceId": "eni-f1xjkw1b",
        "NetworkInterfaceName": "royhyangtest-main",
        "Primary": false,
        "PrivateIpAddressSet": [
          {
            "Description": "",
            "IsWanIpBlocked": false,
            "Primary": true,
            "PrivateIpAddress": "192.168.0.13",
            "PublicIpAddress": "",
            "State": "AVAILABLE"
          },
          {
            "Description": "",
            "IsWanIpBlocked": false,
            "Primary": false,
            "PrivateIpAddress": "192.168.0.15",
            "PublicIpAddress": "",
            "State": "AVAILABLE"
          },
          {
            "Description": "",
            "IsWanIpBlocked": false,
            "Primary": false,
            "PrivateIpAddress": "192.168.0.17",
            "PublicIpAddress": "",
            "State": "AVAILABLE"
          },
          {
            "Description": "",
            "IsWanIpBlocked": false,
            "Primary": false,
            "PrivateIpAddress": "192.168.0.24",
            "PublicIpAddress": "",
            "State": "AVAILABLE"
          }
        ],
        "State": "AVAILABLE",
        "SubnetId": "subnet-nao8lfro",
        "VpcId": "vpc-mrzkofih",
        "Zone": "ap-guangzhou-2"
      }
    ],
    "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1",
    "TotalCount": 1
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

