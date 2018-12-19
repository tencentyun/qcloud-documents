
## 1. API Description

This API (ModifyImageAttribute) is used to modify the image attributes.

* Modifying attributes is not allowed for a shared image.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifyImageAttribute |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| ImageId | Yes | String | Image ID, such as `img-gvbnzy6f`, which can be obtained by either of the following ways:<li>From the `ImageId` field in the returned values of the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).</li><li>Via the [Image console](https://console.cloud.tencent.com/cvm/image).
| ImageName | No | String | Set a new image name, which must meet the following requirements:<li>It must have a length of not more than 20 characters.</li><li>It must be unique.</li> |
| ImageDescription | No | String | Set a new image description, which must meet the following requirement:<li>It must have a length of not more than 60 characters.</li> |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidImageId.IncorrectState | Invalid image status. |
| InvalidImageId.Malformed | Incorrect format of image ID. |
| InvalidImageId.NotFound | This image cannot be found. |
| InvalidImageName.Duplicate | The specified image name already exists. |
| InvalidParameter.ValueTooLarge | The length of parameter exceeds the limit. |

## 5. Example

## Example 1: Modify the image name

### Scenario description

Change the name of the image img-6pb6lrmy to "sample".

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ModifyImageAttribute
&ImageId=img-6pb6lrmy
&ImageName=sample
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


        
