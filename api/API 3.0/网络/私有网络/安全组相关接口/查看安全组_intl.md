## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DescribeSecurityGroups) is used to query security groups.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeSecurityGroups |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| SecurityGroupIds.N | No | Array of String | Security group instance ID, such as sg-33ocnj9n. It can be obtained through DescribeSecurityGroups. A maximum of 100 instances are allowed for each request. SecurityGroupIds and Filters cannot be specified at the same time. |
| Filters.N | No | Array of [Filter](/document/api/215/##Filter) | Filter condition. SecurityGroupIds and Filters cannot be specified at the same time.<br/><li> project-id - Integer - (Filter condition) Project ID.</li><li> security-group-name - String - (Filter condition) Security group name.</li> |
| Offset | No | String | Offset. |
| Limit | No | String | Number of values to be returned. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| SecurityGroupSet | Array of [SecurityGroup](/document/api/215/##SecurityGroup) | Security group object. |
| TotalCount | Integer | Number of instances matching the filter condition. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| ResourceNotFound | Resource does not exist. |

## 5. Example

### Example 1 View security groups

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeSecurityGroups
&Version=2017-03-12
&Limit=1
&Filters.0.Name=project-id
&Filters.0.Values.0=0
&Filters.1.Name=security-group-name
&Filters.1.Values.0=TestGroup
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b",
    "SecurityGroupSet": [
      {
        "CreateTime": "2017-04-18 21:02:30",
        "ProjectId": "0",
        "SecurityGroupDesc": "test-group-desc",
        "SecurityGroupId": "sg-05bb4upy",
        "SecurityGroupName": "TestGroup"
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

