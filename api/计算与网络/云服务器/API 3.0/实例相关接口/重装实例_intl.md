## 1. API Description

This API (ResetInstance) is used to reinstall the operating system for the specified instance.

* If you have specified `ImageId` parameter, the re-installation is performed with the specified image. Otherwise, the image used by the current instance is used.
* The system disk will be formatted and reset. Please ensure that there is no important file in the system disk.
* As the operating system is switched between `Linux` and `Windows`, the system disk `ID` of the instance will change, and the snapshot associated with the system disk can't be rolled back and used to recover data.
* If no password is specified, a random password is issued via internal message.
* Currently, using this API for switching between `Linux` and `Windows` operating systems is only supported for the instances with a [system disk type](https://cloud.tencent.com/document/api/213/9452#block_device) of `CLOUD_BASIC`, `CLOUD_PREMIUM` and `CLOUD_SSD`.
* For the instances in overseas regions, this feature is not supported.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ResetInstance |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceId | Yes | String | Instance ID. It can be obtained from `InstanceId` in the returned value of API [DescribeInstances](https://cloud.tencent.com/document/api/213/9388). |
| ImageId | No | String | Valid [image](https://cloud.tencent.com/document/product/213/4940) ID, such as `img-xxx`. There are four types of images:<li>Public Images</li><li>Custom Images</li><li>Shared Images</li><li>Marketplace Images</li>You can obtain the available image IDs by the following ways:<li>For `public images`, `custom images` and `shared images`, log in to [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>This value can be obtained from the `ImageId` field in the returned values of API [DescribeImages](https://cloud.tencent.com/document/api/213/9418).</li> |
| SystemDisk | No | [SystemDisk](/document/api/213/15753#SystemDisk) | Configuration information of the instance's system disk. For the instances with a cloud disk as the system disk, you can specify the system disk capacity after re-installation using this parameter to allow the capacity expansion of the system disk. If the parameter is not specified, the system disk capacity remains unchanged by default. Only expansion, instead of reduction, is supported for system disk capacity. You can only modify the system disk capacity for re-installation. The system disk type cannot be modified. |
| LoginSettings | No | [LoginSettings](/document/api/213/15753#LoginSettings) | Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and notified to the user via the internal message. |
| EnhancedService | No | [EnhancedService](/document/api/213/15753#EnhancedService) | Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, the Cloud Monitoring and Cloud Security are enabled by default. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
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

## Example 1 Reinstall an instance

### Scenario description

This example shows how to reinstall an instance by specifying the image, login password and enhanced service, and also how to expand the system disk of the instance.


### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ResetInstance
&InstanceId=ins-r8hr2upy
&ImageId=img-pmqg1cw7
&SystemDisk.DiskSize=60
&LoginSettings.Password=Qcloud@TestApi123++
&EnhancedService.SecurityService.Enabled=TRUE
&EnhancedService.MonitorService.Enabled=TRUE
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestId": "a0a66377-b79f-4a21-846c-d997d6022968"
  }
}
```


​        
