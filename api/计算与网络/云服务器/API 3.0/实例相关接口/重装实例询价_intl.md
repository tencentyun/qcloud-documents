## 1. API Description

This API (InquiryPriceResetInstance) is used to inquire the prices of reinstalled instances. * If you have specified `ImageId` parameter, the price inquiry is performed with the specified image. Otherwise, the image used by the current instance is used. * Currently, using this API for price inquiry of reinstalled instances after switching between `Linux` and `Windows` operating systems is only supported for the instances with a [system disk type](/document/api/213/9452#block_device) of `CLOUD_BASIC`, `CLOUD_PREMIUM` and `CLOUD_SSD`.* For the instances in overseas regions, this feature is not supported.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: InquiryPriceResetInstance |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceId | Yes | String | Instance ID. It can be obtained from `InstanceId` in the returned value of API [DescribeInstances](https://cloud.tencent.com/document/api/213/15728). |
| ImageId | No | String | Valid [image](/document/product/213/4940) ID, such as `img-xxx`. There are four types of images:<ul><li>Public Images</li><li>Custom Images</li><li>Shared Images</li><li>Marketplace Images</li></ul>You can obtain the available image IDs by the following ways:<ul><li>For `public images`, `custom images` and `shared images`, log in to [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>This value can be obtained from the `ImageId` field in the returned values of API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).</li></ul> |
| SystemDisk | No | [SystemDisk](/document/api/213/15753#SystemDisk) | Configuration information of the instance's system disk. For the instances with a cloud disk as the system disk, you can specify the system disk capacity after re-installation using this parameter to allow the capacity expansion of the system disk. If the parameter is not specified, the system disk capacity remains unchanged by default. Only expansion, instead of reduction, is supported for system disk capacity. You can only modify the system disk capacity for re-installation. The system disk type cannot be modified. |
| LoginSettings | No | [LoginSettings](/document/api/213/15753#LoginSettings) | Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and notified to the user via the internal message. |
| EnhancedService | No | [EnhancedService](/document/api/213/15753#EnhancedService) | Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, the Cloud Monitoring and Cloud Security are enabled by default. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/15753#Price) | The price of the reinstalled instance. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Inquire the price of adjusting the configuration of a postpaid instance

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceResetInstancesType
&InstanceId=ins-fd8spnmq
InternetAccessible.InternetMaxBandwidthOut=20
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "Price": {
      "InstancePrice": {
        "ChargeUnit": "HOUR",
        "UnitPrice": 0.66
      }
    },
    "RequestId": "56d68b92-7004-4716-b3bf-3c2c231035c9"
  }
}
```
