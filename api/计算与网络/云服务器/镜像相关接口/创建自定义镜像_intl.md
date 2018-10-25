## 1. API Description

This API (CreateImage) is used to create an new image from the system disk of an instance. The created image can be used to create instances.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>.

* For your data security, shut down the instance before creating an image.
* An account can create a maximum of 10 custom images for each region.

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceId |  String |Yes | The ID of the instance used for creating image. Instance ID can be obtained by either of the following ways: <br><li>Obtained from the `InstanceId` field in the returned values of API [DescribeInstances](/document/api/213/9388);<br><li>Obtained via [instance console](https://console.cloud.tencent.com/cvm/index).
| ImageName |  String | Yes | Image name, which must meet the following requirements: <br><li>Has a length of not more than 20 characters;<br><li>Must be unique.
| ImageDescription |  String |No | Image description, which must meet the following requirements: <br><li>Has a length of not more than 60 characters. <br>If this parameter is not specified, it is left empty.
| Sysprep | Boolean | No | Whether to enable SysPrep (Windows only) when creating an image. Default is `False`.


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique RequestId is returned for each request. The value of RequestId need to be provided to the backend developer if you fail to call the API. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://intl.cloud.tencent.com/document/product/213/11657).

| Error Code | Description |
|---------|---------|
|InvalidParameter.ValueTooLarge|The length of parameter exceeds the limit.|
|InvalidImageName.Duplicate|The specified image name already exists.|
|MutexOperation.TaskRunning|The same task is running.|
|InvalidInstanceId.NotFound|This instance cannot be found.|
|ImageQuotaLimitExceeded|Image quota exceeds the limit.|
|InvalidInstance.NotSupported|Unsupported instance|

## 5. Example 

Request Parameters
<pre>
https://image.api.qcloud.com/v2/index.php?Action=CreateImage
&Version=2017-03-12
&InstanceId=ins-6pb6lrmy
&<<a href="/doc/api/229/6976">Common request parameters</a>>
</pre>

Response Parameters
<pre>
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
</pre>



