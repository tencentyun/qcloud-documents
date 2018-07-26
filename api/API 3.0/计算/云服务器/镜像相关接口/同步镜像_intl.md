## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (SyncImages) is used to sync a custom image to other regions.

* Each call to this API can only sync a single image.
* This API supports syncing to multiple regions.
* For a single account, a maximum of 10 custom images are allowed for each region.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: SyncImages |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| ImageIds.N | Yes | Array of String | Image ID list. Image ID can be obtained by either of the following ways:<br><li>From the `ImageId` field returned by the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).<br><li> Via the [Image console](https://console.cloud.tencent.com/cvm/image).<br> Image ID must meet the following requirements: <br><li>It must identify an image with a status of `NORMAL`.<br><li> It must identify an image smaller than 50 GB.<br> For more information on image statuses, please see [Image Data Sheet](/document/api/213/9452#image_state). |
| DestinationRegions.N | Yes | Array of String | List of destination regions for synchronization. Destination region must meet the following requirements: <br><li>It cannot be the source region.<br><li>It must be valid.<br><li> Synchronization is not supported for some regions.<br> For more information on region parameters, please see [Region](https://cloud.tencent.com/document/product/213/6091). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidImageId.IncorrectState | Invalid image status. |
| InvalidImageId.NotFound | The image cannot be found. |
| InvalidImageId.TooLarge | Image size exceeds the limit. |
| InvalidRegion.NotFound | The region cannot be found. |
| InvalidRegion.Unavailable | Synchronization of images is not supported for this region. |

## 5. Example

### Example 1 Sync an image

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=SyncImages
&ImageIds.0=img-o3ycss2p
&DestinationRegions.0=ap-guangzhou
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


