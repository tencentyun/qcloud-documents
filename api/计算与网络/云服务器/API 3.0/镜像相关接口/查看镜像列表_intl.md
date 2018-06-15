## 1. API Description

This API (DescribeImages) is used to view the image list.

* You can query the details of the specified images by specifying image IDs, or set filters to query the details of the images that satisfy the filter conditions.
* You can specify Offset and Limit to select a part of the results. The information of the first 20 images satisfying the condition is returned by default.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DescribeImages |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| ImageIds.N | No | Array of String | List of image IDs, such as `img-gvbnzy6f`. For the format of array parameter, please see [API Introduction](https://cloud.tencent.com/document/api/213/15688). Image ID can be obtained by either of the following ways:<li>From the `ImageId` field returned by the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).</li><li>Via the [Image console](https://console.cloud.tencent.com/cvm/image). |
| Filters.N | No | Array of [Filter](/document/api/213/15753#Filter) | Filter condition. The maximum number of `Filters` for each request is 0 and that of `Filters.Values` is 5. This parameter does not support specifying both `ImageIds` and `Filters`. Specific filter conditions are described as follows:<li> image-id - String - Required: No - (Filter condition) Filter by image ID.</li><li> image-type - String - Required: No - (Filter condition) Filter by image type. Value range: for more information, please see [Image Type](https://cloud.tencent.com/document/product/213/9452#image_type).</li><li> image-state - String - Required: No - (Filter condition) Filter by image status. Value range: for more information, please see [Image Status](https://cloud.tencent.com/document/product/213/9452#image_state). |
| Offset | No | Integer | Offset. Default is 0. For more information on Offset, please see [API Introduction](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89). |
| Limit | No | Integer | Limit on the number of results. Default is 20, and maximum is 100. For more information on Limit, please see [API Introduction](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89). |
| InstanceType | No | String | Instance type, such as `S1.SMALL1` |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| ImageSet | Array of [Image](/document/api/213/15753#Image) | An array of the details of an image, including the main statuses and attributes of the image. |
| TotalCount | Integer | Number of images satisfying the filter conditions. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidFilter | Invalid filter. |
| InvalidParameter.InvalidParameterCoexistImageIdsFilters | ImageIds and Filters cannot be specified at the same time. |
| InvalidParameterValue.InvalidParameterValueLimit | Incorrect parameter value. |

## 5. Example

## Example 1: Query images by image IDs

### Scenario description

Query the information of an image by the known image ID.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeImages
&Filters.0.Name=image-type
&Filters.0.Values.0=PRIVATE_IMAGE
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "ImageSet": [
      {
        "Creator": "PUBLIC",
        "ImageCreateTime": "1970-01-01T00:00:00+00:00",
        "ImageDescription": "CentOS 6.6 32-bit",
        "ImageId": "img-pmqg1cw7",
        "ImageName": "CentOS 6.6 32-bit",
        "ImageOsName": "centos6.6x86_32",
        "ImageStatus": "NORMAL",
        "ImageType": "PUBLIC_IMAGE"
      }
    ],
    "RequestId": "5920380e-277a-420a-a221-0caac3eb7159",
    "TotalCount": 1
  }
}
```

## Example 2: Query images by image types

### Scenario description

Query all the private images under the account.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeImages
&Filters.0.Name=image-type
&Filters.0.Values.0=PRIVATE_IMAGE
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "ImageSet": [
      {
        "Creator": "PUBLIC",
        "ImageCreateTime": "1970-01-01T00:00:00+00:00",
        "ImageDescription": "CentOS 6.6 32-bit",
        "ImageId": "img-pmqg1cw7",
        "ImageName": "CentOS 6.6 32-bit",
        "ImageOsName": "centos6.6x86_32",
        "ImageStatus": "NORMAL",
        "ImageType": "PUBLIC_IMAGE"
      }
    ],
    "RequestId": "5920380e-277a-420a-a221-0caac3eb7159",
    "TotalCount": 1
  }
}
```
