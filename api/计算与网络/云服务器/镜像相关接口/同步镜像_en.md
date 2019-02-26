## 1. API Description

This API (SyncImages) is used to synchronize a custom image to other regions.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>.

* Each call to this API can only synchronize a single image.
* This API supports synchronizing to multiple regions.
* For a single account, a maximum of 10 custom images are allowed for each region.

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| ImageIds.N |  array of Strings |Yes | List of image IDs. Image ID can be obtained by either of the following ways: <br><li>Obtained from the `ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418); <br><li>Obtained via [image console](https://console.cloud.tencent.com/cvm/image). <br>Image ID must meet the following requirements: <br><li>It must identify an image with a status of `NORMAL`;<br><li>It must identify an image smaller than 50 GB.<br>For more information on image statuses, please see [Image Data Sheet](/document/api/213/9452#image_state).
| DestinationRegions.N |  array of String |Yes | List of destination regions for synchronization. Destination region must meet the following requirements: <br><li>It cannot be the source region;<br><li>It must be valid. <br><li>Synchronization is not supported for some regions. <br>For more information on region parameters, please see [Region](/document/product/213/6091).


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique RequestId is returned for each request. The value of RequestId need to be provided to the backend developer if you fail to call the API. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](/document/api/213/10146).

| Error Code | Description |
|---------|---------|
|InvalidImageId.IncorrectState|Invalid image status.|
|InvalidImageId.NotFound|This image cannot be found.|
|InvalidImageId.Malformed|Incorrect format of image ID.|
|InvalidImageId.TooLarge|Image size exceeds the limit.|
|InvalidRegion.NotFound|This region cannot be found.|
|InvalidRegion.Unavailable| synchronization of images is not supported for this region.|


## 5. Example 

Request Parameters
<pre>
https://image.api.qcloud.com/v2/index.php?Action=SyncImages
&Version=2017-03-12
&ImageIds.0=img-o3ycss2p
&DestinationRegions.0=ap-guangzhou
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




