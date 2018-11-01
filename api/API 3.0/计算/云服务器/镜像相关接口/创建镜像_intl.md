## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (CreateImage) is used to create an new image from the system disk of an instance. The created image can be used to create instances.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateImage |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | The ID of the instance used to create an image |
| ImageName | Yes | String | Image name |
| ImageDescription | No | String | Image description |
| ForcePoweroff | No | String | Indicates whether to perform a forced shutdown to create an image when soft shutdown fails |
| Sysprep | No | String | Indicates whether Sysprep is enabled when creating a Windows image |
| Reboot | No | String | Indicates whether shutdown of a running instance is allowed to create an image |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| ImageQuotaLimitExceeded | Image quota exceeds the limit. |
| InvalidImageName.Duplicate | The specified image name already exists. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.NotFound | No instance found. |
| InvalidParameter.ValueTooLarge | The length of parameter exceeds the limit. |
| MutexOperation.TaskRunning | The same task is running. |

## 5. Example

### Example 1 Create an image

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=CreateImage
&InstanceId=ins-6pb6lrmy
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
  }
}
```


