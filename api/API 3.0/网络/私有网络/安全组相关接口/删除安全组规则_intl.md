## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DeleteSecurityGroupPolicies) is used to delete security group policies (SecurityGroupPolicy).
* SecurityGroupPolicySet.Version is used to specify the version of the security group you are working with. If the passed Version is not equal to the latest version of the current security group, a failure will be returned. If Version is not passed, the policy with the specified PolicyIndex will be deleted directly.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DeleteSecurityGroupPolicies |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| SecurityGroupId | Yes | String | Security group instance ID, such as sg-33ocnj9n. It can be obtained through DescribeSecurityGroups. |
| SecurityGroupPolicySet | Yes | [SecurityGroupPolicySet](/document/api/215/##SecurityGroupPolicySet) | Security group policy set. Only one or more policies in a single direction can be deleted in one request. Both PolicyIndex-based matching and security group policy-based matching are supported for deletion. Only one matching method can be used in one request. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| ResourceNotFound | Resource does not exist. |
| UnsupportedOperation.VersionMismatch | The specified version number of the security group policy is inconsistent with the latest version. |

## 5. Example

### Example 1 Delete ingress policies of a security group via policy-based matching

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DeleteSecurityGroupPolicies
&Version=2017-03-12
&SecurityGroupId=sg-ohuuioma
&SecurityGroupPolicySet.Version=37
&SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceGroupId=ppmg-ei8hfd9a
&SecurityGroupPolicySet.Ingress.0.CidrBlock=10.9.89.9/25
&SecurityGroupPolicySet.Ingress.0.Action=accept
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
  }
}
```

### Example 2 Delete egress policies of a security group via policy-based matching

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DeleteSecurityGroupPolicies
&Version=2017-03-12
&SecurityGroupId=sg-ohuuioma
&SecurityGroupPolicySet.Version=38
&SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceGroupId=ppmg-ei8hfd9a
&SecurityGroupPolicySet.Egress.0.CidrBlock=10.9.89.9/25
&SecurityGroupPolicySet.Egress.0.Action=accept
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
  }
}
```

### Example 3 Delete ingress policies of a security group via index-based matching

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DeleteSecurityGroupPolicies
&Version=2017-03-12
&SecurityGroupId=sg-ohuuioma
&SecurityGroupPolicySet.Version=39
&SecurityGroupPolicySet.Ingress.0.PolicyIndex=0
&SecurityGroupPolicySet.Ingress.1.PolicyIndex=1
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
  }
}
```

### Example 4 Delete egress policies of a security group via index-based matching

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DeleteSecurityGroupPolicies
&Version=2017-03-12
&SecurityGroupId=sg-ohuuioma
&SecurityGroupPolicySet.Version=40
&SecurityGroupPolicySet.Egress.0.PolicyIndex=0
&SecurityGroupPolicySet.Egress.1.PolicyIndex=1
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
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

