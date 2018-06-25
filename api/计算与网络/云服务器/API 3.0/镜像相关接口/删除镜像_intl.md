## 1. API Description

This API (DeleteImages) is used to delete one or more images.

* The images with a [status](https://cloud.tencent.com/document/api/213/9452#image_state) of `Creating` or `In Use` cannot be deleted. Image status can be obtained via the API [DescribeImages](https://cloud.tencent.com/document/api/213/9418).
* A maximum of 10 custom images are allowed to be created for each region. Deletion of images can free the quota on account.
* A shared image cannot be deleted.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DeleteImages |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| ImageIds.N | Yes | Array of String | The list of IDs of the instances to be deleted |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidImageId.InShared | The image is being shared. |
| InvalidImageId.IncorrectState | Invalid image status. |
| InvalidImageId.Malformed | Incorrect format of image ID. |
| InvalidImageId.NotFound | This image cannot be found. |

## 5. Example

## Example 1: Delete an image

### Scenario description

Delete the image img-34vaef8fe. No operation is performed and an error code is returned when this image is in use or the image ID does not exist.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DeleteImage
&ImageIds.0=img-34vaef8fe
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

