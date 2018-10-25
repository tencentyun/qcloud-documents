## 1. API Description

This API (DeleteImages) is used to delete one or more images.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>.

* The images with a [status](/document/api/213/9452#image_state) of `Creating` or `In Use` cannot be deleted. Image status can be obtained via API [DescribeImages](/document/api/213/9418).
* A maximum of 10 custom images are allowed to be created for each region. Deletion of images can free the quota on account.
* A shared image cannot be deleted.

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| ImageIds.N |  array of Strings |Yes | List of image IDs. Image ID can be obtained by either of the following ways: <br><li>Obtained from the `ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418); <br><li>Obtained via [image console](https://console.cloud.tencent.com/cvm/image). <br>Image ID must meet the following requirements: <br><li>It must identify an image with a status of `NORMAL`;<br><li>It must identify an image that has not been shared to other accounts.<br>For more information on image statuses, please see [Image Data Sheet](/document/api/213/9452#image_state). 


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique RequestId is returned for each request. The value of RequestId need to be provided to the backend developer if you fail to call the API. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](/document/api/213/10146).

| Error code | Description |
|---------|---------|
|InvalidImageId.InShared|The image is being shared.|
|InvalidImageId.IncorrectState|Invalid image status.|
|InvalidImageId.NotFound|This image cannot be found.|
|InvalidImageId.Malformed| Incorrect format of image ID.|


## 5. Example 

Request Parameters
<pre>
https://image.api.qcloud.com/v2/index.php?Action=DeleteImages
&Version=2017-03-12
&ImageIds.0=img-o3ycss2p
&imageIds.1=img-kb1a392d
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




