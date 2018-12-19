
## 1. API Description

This API (CreateImage) is used to create an new image from the system disk of an instance. The created image can be used to create instances.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: CreateImage |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceId | Yes | String | The ID of the instance used to create an image |
| ImageName | Yes | String | Image name |
| ImageDescription | No | String | Image description |
| ForcePoweroff | No | String | Whether to perform a forced shutdown to create an image when soft shutdown fails |
| Sysprep | No | String | Whether Sysprep is enabled when creating a Windows image |
| Reboot | No | String | Whether to allow users to shut down running instances to create images |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| ImageQuotaLimitExceeded | Image quota exceeds the limit. |
| InvalidImageName.Duplicate | The specified image name already exists. |
| InvalidInstance.NotSupported | Instance not supported. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameter.ValueTooLarge | The length of parameter exceeds the limit. |
| MutexOperation.TaskRunning | The same task is running. |

## 5. Example

## Example 1: Create an image

### Scenario description

Create an image with the instance ins-6pb6lrmy. Perform a soft shutdown on a running instance, and the task ends if soft shutdown fails (default semantics).

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=CreateImage
&InstanceId=ins-6pb6lrmy
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
  }
}
```


        
