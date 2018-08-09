## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ImportImage) is used to import images that can be used to create instances.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ImportImage |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Architecture | Yes | String | The operating system architecture (`x86_64` or `i386`) of the imported image |
| OsType | Yes | String | The operating system type of the imported image, which can be obtained via `DescribeImportImageOs`. |
| OsVersion | Yes | String | The operating system version of the imported image, which can be obtained via `DescribeImportImageOs`. |
| ImageUrl | Yes | String | The address of COS where the imported image is stored |
| ImageName | Yes | String | Image name |
| ImageDescription | No | String | Image description |
| DryRun | No | Boolean | Check parameters only, and do not execute tasks |
| Force | No | Boolean | Indicates whether to perform the forced image import. For more information, please see [Forced Image Import](https://cloud.tencent.com/document/product/213/12849) |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| ImageQuotaLimitExceeded | Image quota exceeds the limit. |
| InvalidImageName.Duplicate | The specified image name already exists. |
| InvalidImageOsType.Unsupported | The operating system type is not supported. |
| InvalidImageOsVersion.Unsupported | The operating system version is not supported. |
| InvalidParameter.InvalidParameterUrlError | Incorrect URL. |
| RegionAbilityLimit.UnsupportedToImportImage | Image import is not supported for this region. |

## 5. Example

### Example 1 Import an image

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ImportImage
&OsType=CentOS
&OsVersion=6
&ImageName=sample
&ImageDescription=sampleimage
&ImageUrl=http://111-1251233127.cosd.myqcloud.com/Windows%20Server%202008%20R2%20x64a.vmdk
&Architecture=x86_64
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


