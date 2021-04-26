## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DescribeAddressTemplates) is used to query an IP address template.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeAddressTemplates |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Filters.N | No | Array of [Filter](/document/api/215/##Filter) | Filter conditions.<br/><li> address-template-name - String - (Filter condition ) IP address template name.</li><li> address-template-id - String - (Filter condition ) IP address template instance ID, such as ipm-mdunqeb6.</li> |
| Offset | No | String | Offset. Default is 0. |
| Limit | No | String | Number of values to be returned. Default is 20. Maximum is 100. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances matching the filter condition. |
| AddressTemplateSet | Array of [AddressTemplate](/document/api/215/##AddressTemplate) | IP address template. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue.Malformed | Invalid input parameter format. |

## 5. Example

### Example 1 Query an IP address template

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeAddressTemplates
&Version=2017-03-12
&Filters.0.Name=address-template-name
&Filters.0.Values.0=TestName
&Filters.1.Name=address-template-id
&Filters.1.Values.0=ipm-mdunqeb6
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "AddressTemplateSet": [
      {
        "AddressSet": [
          "192.168.0.0/16",
          "192.128.8.8/17"
        ],
        "AddressTemplateId": "ipm-mdunqeb6",
        "AddressTemplateName": "TestName",
        "CreatedTime": "2017-12-31 10:06:05"
      }
    ],
    "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
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

