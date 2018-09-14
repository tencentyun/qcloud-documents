## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ModifyImageAttribute) is used to modify the image attributes.

* Modifying attributes is not allowed for a shared image.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyImageAttribute |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| ImageId | Yes | String | Image ID, such as `img-gvbnzy6f`. Image ID can be obtained by either of the following ways:<br><li>From the `ImageId` field returned by the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).<br><li> Via the [Image console](https://console.cloud.tencent.com/cvm/image). |
| ImageName | No | String | Set a new image name, which must meet the following requirements:<br> <li> It cannot exceed 20 characters.<br> <li> It must be unique. |
| ImageDescription | No | String | Set a new image description, which must meet the following requirements:<br> <li> It cannot exceed 60 characters. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidImageId.IncorrectState | Invalid image status. |
| InvalidImageId.Malformed | Incorrect format of image ID. |
| InvalidImageId.NotFound | The image cannot be found. |
| InvalidImageName.Duplicate | The specified image name already exists. |
| InvalidParameter.ValueTooLarge | The length of parameter exceeds the limit. |

## 5. Example

### Example 1 Modify the image name

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ModifyImageAttribute
&ImageId=img-6pb6lrmy
&ImageName=sample
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


