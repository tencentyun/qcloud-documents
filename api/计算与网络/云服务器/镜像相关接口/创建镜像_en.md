## 1. API Description

This API (CreateImage) is used to make the current status of the instance system disk into a new image, which can be used to quickly create instances.


Note: This API is the updated API. For information on the old API, please see [CreateImage (old)](https://cloud.tencent.com/document/api/213/1273)


Domain name for API request: <font style="color:red">image.api.qcloud.com</font>


* The target instance needs to be shut down before you can create a custom image.
* A maximum of 10 custom images are allowed to be created for each region.


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | Indicates API version No., used for identifying the API version of the request. To indicate the first version of this API, you can input the value "2017-03-12" to the parameter. |
| InstanceId | String | Yes | The ID of the instance to be made into the image.
| ImageName | String | Yes | Image name, which shall meet the following restrictions: <br> * Valid ImageName with no more than 20 characters <br> * The image name must be unique.
| ImageDescription | String | No | Image description; valid image description with no more than 60 characters. Default is ``
| Sysprep | Boolean | No | Whether to enable SysPrep (Windows only) when creating an image. Default is `False`


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. Each request returns a unique RequestId. The RequestId should be provided to the backend developer for a help when the user fails to call the API. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/10146).


> Tencent Cloud may decrease or increase error codes in rare cases. Developers need to prepare robust applications.

| Error code | Description |
|---------|---------|
| InvalidParameter.ValueTooLarge | Invalid parameter: Parameter is too long |
| InvalidImageName.Duplicate | Invalid ImageName: Duplicate with existing image. |
| MutexOperation.TaskRunning | Exclusive operation. Previous task is still running |
| InvalidInstanceId.NotFound | Corresponding instance not found |
| ImageQuotaLimitExceeded | Image quota exceeds the limit |
| InvalidInstance.NotSupported | Instance not supported |


## 5. Example 

>**GET** `https://image.api.qcloud.com/v2/index.php?Action=CreateImage`
>&Version=2017-03-12
>&InstanceId=ins-6pb6lrmy<br>
>&[Common Request Parameters](/doc/api/229/6976)

```json

{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}

```




