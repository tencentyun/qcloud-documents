## 1. API Description

This API (ResetInstance) is used to reinstall the operating system for the specified instance.

Domain name for API request: cvm.api.qcloud.com


* If you have specified `ImageId` parameter, the re-installation is performed with the specified image. Otherwise, the image used by the current instance is used.
* The system disk will be formatted and reset. Please ensure that there is no important file in the system disk.
* As the operating system is switched between `Linux` and `Windows`, the system disk `ID` of the instance will change, and the snapshot associated with the system disk can't be rolled back and used to recover data.
* If no password is specified, a random password is issued via internal message.
* Currently, using this API for switching between `Linux` and `Windows` operating systems is only supported for the instances with a [system disk type](/document/api/213/9452#block_device) of `CLOUD_BASIC`, `CLOUD_PREMIUM` and `CLOUD_SSD`.
* This feature is only available to instances in China.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| instanceId | Yes | String | Instance ID. It can be obtained from `InstanceId` in the returned values of API [DescribeInstances](/document/api/213/9388).
| ImageId | String | No | Valid [image](/document/product/213/4940) ID, such as `img-xxx`. There are four types of images: <br/><li>Public Images</li><li>Custom Images</li><li>Shared Images</li><li>Marketplace Images</li><br/>You can obtain the available image IDs by the following ways:<br/><li> For `public images`, `custom images` and `shared images`, log in to [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the image IDs; for `marketplace images`, query the image IDs through [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>This value can be obtained from the `ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418).</li>|
|SystemDisk|[SystemDisk](/document/api/213/9451#systemdisk) object|No| Configuration information of instance's system disk. For the instances with a cloud disk as the system disk, you can specify the system disk capacity after re-installation using this parameter to allow the capacity expansion of the system disk. If the parameter is not specified, the system disk capacity remains unchanged by default. Only expansion, instead of reduction, is supported for system disk capacity. You can only modify the system disk capacity for re-installation. The system disk type cannot be modified. |
| LoginSettings | [LoginSettings object](https://cloud.tencent.com/document/api/213/9451#loginsettings) | No | Login settings of the instance. This parameter is used to set the login password and key for the instance, or to keep the original login settings for the image. By default, a random password is generated and sent to the user via the internal message. |
| EnhancedService | [EnhancedService object](https://cloud.tencent.com/document/api/213/9451#enhancedservice) | No | This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, the Cloud Monitoring and Cloud Security are enabled by default. |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| MissingParameter | A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | The specified instance ID does not exist. |
| InvalidInstanceId.Malformed | The specified instance ID is in an incorrect format. For example, `ins-1122` indicates an ID length error. |
| InvalidParameterValue | Parameter value is in an incorrect format or is not supported. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InternalServerError | Tencent Cloud server error. |


## 5. Example
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ResetInstance
&Version=2017-03-12
&InstanceId=ins-r8hr2upy
&ImageId=img-pmqg1cw7
&SystemDisk.DiskSize=60
&LoginSettings.Password=Qcloud@TestApi123++
&EnhancedService.SecurityService.Enabled=TRUE
&EnhancedService.MonitorService.Enabled=TRUE
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "RequestId": "a0a66377-b79f-4a21-846c-d997d6022968"
    }
}
</pre>

