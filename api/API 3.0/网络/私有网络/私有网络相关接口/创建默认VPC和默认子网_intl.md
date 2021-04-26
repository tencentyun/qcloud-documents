## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (CreateDefaultVpc) is used to create a default VPC.

The default VPC is suitable for getting started with and launching public instances, which can be used just like an ordinary VPC. If you want to create a standard VPC, that is, to specify a VPC name, VPC IP address range, subnet IP address range and subnet availability zone, use the regular API "Create VPC" (CreateVpc).

Generally, a default VPC may not be created with this API, which depends on the network attributes (DescribeAccountAttributes) of your account.
* If both basic network and VPC are supported, VpcId returned is 0.
* If only VPC is supported, the default VPC information is returned.

You can also use the Force parameter to forcibly return a default VPC.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateDefaultVpc |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Zone | No | String | ID of the availability zone in which the subnet resides. A random availability zone is used if it is not specified. |
| Force | No | Boolean | Indicates whether to forcibly return a default VPC |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Vpc | [DefaultVpcSubnet](/document/api/215/##DefaultVpcSubnet) | Default VPC and subnet IDs |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

There is no error code related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

## 5. Example

### Example 1 Create a default VPC

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateDefaultVpc
&Version=2017-03-12
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "a2353d77-5c08-49c4-a28a-632a8af5e294",
    "Vpc": {
      "SubnetId": "subnet-ixzf2m42",
      "VpcId": "vpc-pin7sxcd"
    }
  }
}
```

### Example 2 Create a non-default VPC

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateDefaultVpc
&Version=2017-03-12
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "c52dda11-9e53-440f-b034-6292f2144dd0",
    "Vpc": {
      "SubnetId": "0",
      "VpcId": "0"
    }
  }
}
```

### Example 3 Forcibly create a default VPC

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateDefaultVpc
&Version=2017-03-12
&Force=true
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "91348b0a-6846-49ff-822b-a21eef848c9f",
    "Vpc": {
      "SubnetId": "subnet-l9emqwnw",
      "VpcId": "vpc-8mpwlbdv"
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

