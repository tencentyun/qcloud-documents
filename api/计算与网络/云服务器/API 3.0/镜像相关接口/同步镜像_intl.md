
## 1. API Description

This API (SyncImages) is used to sync a custom image to other regions.

* Each call to this API can only sync a single image.
* This API supports syncing to multiple regions.
* For a single account, a maximum of 10 custom images are allowed for each region.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: SyncImages |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| ImageIds.N | Yes | Array of String | List of image Ids. Image ID can be obtained by either of the following ways:<li>From the `ImageId` field in the returned values of the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).</li><li>Via the [Image console](https://console.cloud.tencent.com/cvm/image).<br>Image ID must meet the following requirements:<li>It must identify an image with a status of `NORMAL`.</li><li>It must identify an image smaller than 50 GB.</li>For more information on image statuses, please see [Image Data Sheet](/document/api/213/9452#image_state). |
| DestinationRegions.N | Yes | Array of String | List of destination regions for synchronization. Destination region must meet the following requirements:<li>It cannot be the source region.</li><li>It must be valid.</li><li>Synchronization is not supported for some regions.</li>For more information on region parameters, please see [Region](https://cloud.tencent.com/document/product/213/6091).

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidImageId.IncorrectState | Invalid image status. |
| InvalidImageId.NotFound | This image cannot be found. |
| InvalidImageId.TooLarge | Image size exceeds the limit. |
| InvalidRegion.NotFound | The region was not found. |
| InvalidRegion.Unavailable | Synchronization of images is not supported for this region. |

## 5. Example

## Example 1: Sync an image

### Scenario description

Sync the image img-o3ycss2p to Guangzhou.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=SyncImages
&ImageIds.0=img-o3ycss2p
&DestinationRegions.0=ap-guangzhou
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


        
