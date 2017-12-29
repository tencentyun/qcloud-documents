## 1. API Description

This API (ModifyImageAttribute) is used to modify the image attributes.

Domain name for API request: image.api.qcloud.com.

* This API is NOT available to shared images.

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| ImageId |  String |Yes | Image ID, such as `img-gvbnzy6f`. Image ID can be obtained by either of the following ways: <br><li>`ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418);<br><li>Obtained via [image console](https://console.cloud.tencent.com/cvm/image). 
| ImageName | String | No | Set a new image name, which must meet the following requirements: <br><li>No more than 20 characters;<br><li>Must be unique.|
| ImageDescription | String | No | Set a new image description, which must meet the following requirements: <br><li>No more than 60 characters. |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique RequestId is returned for each request. The value of RequestId need to be provided to the backend developer if you fail to call the API. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](/document/api/213/10146).

| Error Code | Description |
|---------|---------|
|InvalidImageId.IncorrectState|Invalid image status.|
|InvalidImageId.NotFound|The image cannot be found.|
|InvalidImageId.Malformed|The specified image name is invalid.|
|InvalidImageName.Duplicate|The specified image name already exists.|
|InvalidParameter.ValueTooLarge| The length of parameter exceeds the limit |


## 5. Example

Input
<pre>
https://image.api.qcloud.com/v2/index.php?Action=ModifyImageAttribute
&Version=2017-03-12
&ImageId=img-6pb6lrmy
&ImageName=sample
&<<a href="/doc/api/229/6976">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
</pre>



