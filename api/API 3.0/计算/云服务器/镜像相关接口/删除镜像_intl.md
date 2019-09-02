## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DeleteImages) is used to delete one or more images.

* The images with a [status](https://cloud.tencent.com/document/api/213/9452#image_state) of `Creating` or `In Use` cannot be deleted. The image status can be obtained via [DescribeImages](https://cloud.tencent.com/document/api/213/9418).
* A maximum of 10 custom images are allowed to be created for each region. Deletion of images can free the quota on account.
* A shared image cannot be deleted.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DeleteImages |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| ImageIds.N | Yes | Array of String | The list of IDs of the instances to be deleted |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidImageId.InShared | The image is being shared. |
| InvalidImageId.IncorrectState | Invalid image status. |
| InvalidImageId.Malformed | Incorrect format of image ID. |
| InvalidImageId.NotFound | The image cannot be found. |

## 5. Example

### Example 1 Delete an image

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DeleteImage
&ImageIds.0=img-34vaef8fe
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


