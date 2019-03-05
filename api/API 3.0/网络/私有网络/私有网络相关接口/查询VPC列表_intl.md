## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DescribeVpcs) is used to query the VPC list.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeVpcs |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpcIds.N | No | Array of String | VPC instance ID. such as vpc-f49l6u0z. A maximum of 100 instances are allowed for each request. This parameter does not support specifying both VpcIds and Filters. |
| Filters.N | No | Array of [Filter](/document/api/215/##Filter) | Filter condition. This parameter does not support specifying both VpcIds and Filters.<br/><li> vpc-name - String - (Filter condition) VPC instance name.</li><li> is-default - String - (Filter condition) Indicates whether it is the default VPC.</li><li> vpc-id - String - (Filter condition) VPC instance ID, such as vpc-f49l6u0z.</li><li> cidr-block - String - (Filter condition) VPC CIDR.</li> |
| Offset | No | String | Offset |
| Limit | No | String | Number of values to be returned |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of objects that meet the condition. |
| VpcSet | Array of [Vpc](/document/api/215/##Vpc) | VPC object. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter.Coexist | Parameters specified conflict with each other. |
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| ResourceNotFound | Resource does not exist. |

## 5. Example

### Example 1 Query the VPC list

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeVpcs
&Version=2017-03-12
&Offset=0
&Limit=2
&Filters.0.Name=is-default
&Filters.0.Values.0=false
&Filters.1.Name=cidr-block
&Filters.1.Values.0=10.8.0.0
&Filters.1.Values.1=192.168.0.0
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "6a44afb7-0644-4ff9-9761-3502f99d3a15",
    "TotalCount": 2,
    "VpcSet": [
      {
        "CidrBlock": "10.0.0.0/16",
        "CreatedTime": "2018-04-25 10:26:26",
        "DhcpOptionsId": "dopt-8g7k5qfq",
        "DnsServerSet": [
          "10.0.0.1",
          "183.60.82.98"
        ],
        "DomainName": "aa.bb.cc",
        "EnableMulticast": false,
        "IsDefault": false,
        "VpcId": "vpc-p5sf61yj",
        "VpcName": "Test DHCP"
      },
      {
        "CidrBlock": "172.16.0.0/16",
        "CreatedTime": "2017-04-17 15:41:07",
        "EnableMulticast": true,
        "IsDefault": true,
        "VpcId": "vpc-0akbol5v",
        "VpcName": "Default VPC"
      }
    ]
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

