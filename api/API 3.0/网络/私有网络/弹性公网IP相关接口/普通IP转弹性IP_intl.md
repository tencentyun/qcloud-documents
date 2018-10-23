## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (TransformAddress) is used to convert an ordinary public IP into an [Elastic IP](https://cloud.tencent.com/document/product/213/1941) (EIP).
* The platform imposes a quota on the number of attempts to unbind an EIP and reallocate an ordinary public IP per day for each region (See [Overview of EIP products](/document/product/213/1941)). The above quota can be obtained through API [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378).

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: TransformAddress |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | ID of the instance with a public IP you are working with, such as `ins-11112222`. It can be queried through the [console](https://console.cloud.tencent.com/cvm) or obtained from the `InstanceId` field value in the returned result of API [DescribeInstances](https://cloud.tencent.com/document/api/213/9389). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| AddressQuotaLimitExceeded | Account quota is exceeded. At most 20 EIPs can be created by each Tencent Cloud account in each region. |
| AddressQuotaLimitExceeded.DailyAllocate | The maximum number of requests is exceeded. The maximum number of requests can be made by each Tencent Cloud account in each region equals to two times the quota. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.NotFound | Invalid instance ID. The specified instance ID does not exist. |

## 5. Example

### Example 1 Convert an ordinary IP to an EIP

#### Input example

```
https://eip.tencentcloudapi.com/?Action=TransformAddress
&InstanceId=ins-3ea0qeu6
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
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

