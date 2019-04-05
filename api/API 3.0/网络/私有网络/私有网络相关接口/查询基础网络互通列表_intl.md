## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DescribeClassicLinkInstances) is used to query the classiclink instances.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeClassicLinkInstances |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Filters.N | No | Array of [FilterObject](/document/api/215/##FilterObject) | Filter conditions.<br/><li> vpc-id - String - (Filter condition) VPC instance ID.</li><li> vm-ip - String - (Filter condition) Basic network CVM IP.</li> |
| Offset | No | String | Offset |
| Limit | No | String | Number of values to be returned |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances matching the filter condition. |
| ClassicLinkInstanceSet | Array of [ClassicLinkInstance](/document/api/215/##ClassicLinkInstance) | Classiclink instances. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue.Range | The parameter value is not in the specified range. |

## 5. Example

### Example 1 Query the list of classiclink instances

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeClassicLinkInstances
&Version=2017-03-12
&Filters.0.Name=vpc-id
&Filters.0.Values.0=vpc-gjui0b5t
&Filters.1.Name=vm-ip
&Filters.1.Values.0=10.9.0.3.0
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "ClassicLinkInstanceSet": [
      {
        "InstanceId": "ins-0x5msjda",
        "VpcId": "vpc-gjui0b5t"
      }
    ],
    "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
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

