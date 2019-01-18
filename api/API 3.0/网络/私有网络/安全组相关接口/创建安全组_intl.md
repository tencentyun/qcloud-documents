## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (CreateSecurityGroup) is used to create security groups (SecurityGroup).
* <a href="https://cloud.tencent.com/document/product/213/500#2.-.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84.E9.99.90.E5.88.B6">Limit on the number of security groups</a> for each project in each region under each account.
Both the ingress and egress policies for a created security group are Deny All by default. Usually, you need to call CreateSecurityGroupPolicies to set the security group policy to the desired one after creation is complete.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateSecurityGroup |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| GroupName | Yes | String | Security group name, which is limited to 60 characters. |
| GroupDescription | Yes | String | Security group remark, which is limited to 100 characters. |
| ProjectId | No | String | Project ID. Default is 0. It can be found on the project management page in the Tencent Cloud console. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| SecurityGroup | [SecurityGroup](/document/api/215/##SecurityGroup) | Security group object. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| LimitExceeded | Quota exceeded. |
| ResourceNotFound | Resource does not exist. |

## 5. Example

### Example 1 Create a security group

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateSecurityGroup
&Version=2017-03-12
&GroupName=TestGroup
&GroupDescription=test-group-desc
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
    "SecurityGroup": {
      "CreateTime": "2018-01-13 19:26:33",
      "ProjectId": "0",
      "SecurityGroupDesc": "test-group-desc",
      "SecurityGroupId": "sg-3g7ftkp3",
      "SecurityGroupName": "TestGroup"
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

