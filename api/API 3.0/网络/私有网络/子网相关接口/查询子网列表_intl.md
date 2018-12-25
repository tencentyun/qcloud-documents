## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DescribeSubnets) is used to query the list of subnets.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeSubnets |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| SubnetIds.N | No | Array of String | Queries the subnet instance ID, Such as subnet-pxir56ns. A maximum of 100 instances are allowed for each request. SubnetIds and Filters cannot be specified at the same time. |
| Filters.N | No | Array of [Filter](/document/api/215/##Filter) | Filter condition. SubnetIds and Filters cannot be specified at the same time.<br/><li> subnet-id - String - (Filter condition) Subnet instance name.</li><li> vpc-id - String - (Filter condition) VPC instance ID, such as vpc-f49l6u0z.</li><li> cidr-block - String - (Filter condition) VPC CIDR.</li><li> is-default - Boolean - (Filter condition) Whether it is the default subnet.</li><li> subnet-name - String - (Filter condition) Subnet name.</li><li> zone - String - (Filter condition) Availability zone.</li> |
| Offset | No | String | Offset |
| Limit | No | String | Number of values to be returned |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances matching the filter condition. |
| SubnetSet | Array of [Subnet](/document/api/215/##Subnet) | Subnet object. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter.Coexist | Parameters specified conflict with each other. |
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| ResourceNotFound | Resource does not exist. |

## 5. Example

### Example 1 Query the subnet list

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeSubnets
&Version=2017-03-12
&Filters.0.Name=subnet-name
&Filters.0.Values.0=Default subnet in Guangzhou Zone 2
&Filters.1.Name=vpc-id
&Filters.1.Values.0=vpc-2at5y1pn
&Filters.2.Name=subnet-id
&Filters.2.Values.0=subnet-otu92seu
&Filters.3.Name=cidr-block
&Filters.3.Values.0=172.16.16.0
&Filters.4.Name=is-default
&Filters.4.Values.0=true
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
    "SubnetSet": [
      {
        "AvailableIpAddressCount": 4002,
        "CidrBlock": "172.16.16.0/20",
        "CreatedTime": "2017-04-20 11:30:48",
        "EnableBroadcast": false,
        "IsDefault": true,
        "RouteTableId": "rtb-l2h8d7c2",
        "SubnetId": "subnet-otu92seu",
        "SubnetName": "Default subnet in Guangzhou Zone 2",
        "VpcId": "vpc-2at5y1pn",
        "Zone": "ap-guangzhou-dev-2"
      }
    ],
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

