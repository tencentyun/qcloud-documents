## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (ReplaceSecurityGroupPolicy) is used to replace a single security group policy (SecurityGroupPolicy).
Only one policy in one direction can be replaced in one request, and the PolicyIndex parameter must be specified.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ReplaceSecurityGroupPolicy |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| SecurityGroupId | Yes | String | Security group instance ID, such as sg-33ocnj9n. It can be obtained through DescribeSecurityGroups. |
| SecurityGroupPolicySet | Yes | [SecurityGroupPolicySet](/document/api/215/##SecurityGroupPolicySet) | Security group policy set object. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter | Invalid input parameter. |
| InvalidParameterValue | Invalid parameter value. |
| ResourceNotFound | Resource does not exist. |
| UnsupportedOperation.VersionMismatch | The specified version number of the security group policy is inconsistent with the latest version. |

## 5. Example

### Example 1 Replace a single routing policy of a security group

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=ReplaceSecurityGroupPolicy
&Version=2017-03-12
&SecurityGroupId=sg-ohuuioma
&SecurityGroupPolicySet.Version=20
&SecurityGroupPolicySet.Egress.0.PolicyIndex=2
&SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId=ppm-f5n1f8da
&SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId=ipmg-2uw6ujo6
&SecurityGroupPolicySet.Egress.0.Action=accept
&SecurityGroupPolicySet.Egress.0.PolicyDescription=TestPolicy
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
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

