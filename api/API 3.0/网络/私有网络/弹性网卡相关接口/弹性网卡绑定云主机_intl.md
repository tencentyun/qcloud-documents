## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (AttachNetworkInterface) is used to bind an ENI to a CVM.
* A CVM can be bound with multiple ENIs, but can only be bound with one primary ENI. For more information about ENI limits, please see <a href="https://cloud.tencent.com/document/product/215/6513">ENI Use Limits</a>.
* An ENI can only be bound to one CVM at a time.
* An ENI can only be bound to a CVM that is running or has been shut down. For more information about the CVM status, please see <a href="https://cloud.tencent.com/document/api/213/9452#instance_state">Tencent CVM Information</a>.
* An ENI can only be bound to a CVM in VPC, and the CVM must resides in the same availability zone as the subnet of the ENI.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: AttachNetworkInterface |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| NetworkInterfaceId | Yes | String | ENI instance ID, such as eni-m6dyj72l. |
| InstanceId | Yes | String | CVM instance ID. such as ins-r8hr2upy. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| ResourceNotFound | Resource does not exist. |
| UnsupportedOperation.VpcMismatch | The resources are not in the same VPC. |

## 5. Example

### Example 1 Bind an ENI to a CVM

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=AttachNetworkInterface
&Version=2017-03-12
&NetworkInterfaceId=eni-afo43z61
&InstanceId=ins-ins-r8hr2upy
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
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

