Location: CVM -> API Documentation -> Image Related APIs -> Import Image from External Resource Change Log (Latest version: 2017.4.5)
     Operation
Basic Information Content Extended Configuration
  
 URL for documentation (Chinese)

master/
 
Content  

## 1. API Description

This API (ImportImage) is used to import images that can be used to create instances.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ImportImage |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| Architecture | Yes | String | The operating system architecture (`x86_64` or `i386`) of the imported image |
| OsType | Yes | String | The operating system type of the imported image, which can be obtained via `DescribeImportImageOs`. |
| OsVersion | Yes | String | The operating system version of the imported image, which can be obtained via `DescribeImportImageOs`. |
| ImageUrl | Yes | String | The address of COS where the imported image is stored |
| ImageName | Yes | String | Image name |
| ImageDescription | No | String | Image description |
| DryRun | No | Boolean | Check parameters only, and do not execute tasks |
| Force | No | Boolean | Whether to perform the forced image import. For more information, please see [Forced Image Import](https://cloud.tencent.com/document/product/213/12849) |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| ImageQuotaLimitExceeded | Image quota exceeds the limit. |
| InvalidImageName.Duplicate | The specified image name already exists. |
| InvalidImageOsType.Unsupported | The operating system type not supported |
| InvalidImageOsVersion.Unsupported | The operating system version not supported |
| InvalidParameter.InvalidParameterUrlError | Incorrect URL |
| RegionAbilityLimit.UnsupportedToImportImage | Image import is not supported for this region. |

## 5. Example

## Example 1: Import an image

### Scenario description

An user imports an image.

                
### Request parameters

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
### Response parameters

```
{
  "Response": {
    "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
  }
}
```


        
