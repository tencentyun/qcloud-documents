## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (InquiryPriceResetInstance) is used to inquire the prices of reinstalled instances. * If you have specified `ImageId` parameter, the price inquiry is performed with the specified image. Otherwise, the image used by the current instance is used. * You can use this API to inquire prices after the operating system switch between `Linux` and `Windows` only for the instances with a [system disk type](/document/api/213/9452#block_device) of `CLOUD_BASIC`, `CLOUD_PREMIUM` and `CLOUD_SSD`. * For the instances in overseas regions, this operation is not supported.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceResetInstance |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | Instance ID You can obtain the parameter value from the `InstanceId` field value in the returned result of API [DescribeInstances](https://cloud.tencent.com/document/api/213/15728). |
| ImageId | No | String | Specifies a valid [image](/document/product/213/4940) ID, such as `img-xxx`. There are four types of images: <br/><li>Public image</li><li>Custom image</li><li>Shared image</li><li>Marketplace image</li><br/> You can obtain the available image IDs by either of the following ways: <br/><li>Query the image ID of a `public image`, `custom image` or `shared image` by logging in to the [Console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE); query the image ID of a `marketplace image` via [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li> Call the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715) to obtain the `ImageId` field value in the returned result. </li> |
| SystemDisk | No | [SystemDisk](/document/api/213/##SystemDisk) | Configuration information of the system disk in the instance. For the instances with a cloud disk as the system disk, you can specify the system disk capacity after re-installation using this parameter to allow the capacity expansion of the system disk. If the parameter is not specified, the system disk capacity remains unchanged by default. You can only expand the system disk capacity (capacity reduction is not supported for a system disk). Re-installing the system can only modify the system disk capacity, and cannot modify the system disk type. |
| LoginSettings | No | [LoginSettings](/document/api/213/##LoginSettings) | Login settings of an instance. This parameter is used to set the instance login method, password and key, or to keep the original login settings of image. By default, a password is generated randomly and notified to the user via internal message. |
| EnhancedService | No |  [EnhancedService](/document/api/213/##EnhancedService) | Enables enhanced services. This parameter is used to specify whether to enable Cloud Security, Cloud Monitor and other services. If this parameter is not specified, Cloud Monitor and Cloud Security services are enabled by default. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/##Price) | Indicates the price of the reinstalled instance. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidInstanceId.NotFound | No instance found. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Inquire the price of a postpaid instance after adjusting its configuration

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceResetInstancesType
&InstanceId=ins-fd8spnmq
InternetAccessible.InternetMaxBandwidthOut=20
&<Common request parameters>
```

#### Output example

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


