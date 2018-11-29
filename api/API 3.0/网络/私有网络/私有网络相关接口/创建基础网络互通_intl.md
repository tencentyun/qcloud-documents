## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (AttachClassicLinkVpc) is used to create a classiclink.
* The VPC and basic network devices must be in the same region.
* For the differences between VPC and basic network, please see <a href="https://cloud.tencent.com/document/product/215/535#2.-.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B8.8E.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C">VPC and Basic Network</a> in the VPC product documentation.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: AttachClassicLinkVpc |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpcId | Yes | String | VPC instance ID |
| InstanceIds.N | Yes | Array of String | CVM instance ID |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| LimitExceeded | Quota exceeded. |
| ResourceNotFound | Resource does not exist. |
| UnsupportedOperation | Operation is not supported. |
| UnsupportedOperation.CIDRUnSupportedClassicLink | The specified VPC CIDR range does not support the classiclink. |
| UnsupportedOperation.ClassicInstanceIdAlreadyExists | The instance has been bound to the VPC. |

## 5. Example

### Example 1 Create a classiclink

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=AttachClassicLinkVpc
&Version=2017-03-12
&VpcId=vpc-gjui0b5t
&InstanceIds.0=ins-0x5msjda
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

