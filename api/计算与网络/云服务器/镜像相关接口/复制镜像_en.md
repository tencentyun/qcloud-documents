## 1. API Description
 
This API (SyncCvmImage) is used to synchronize a custom image to another region.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>

* Currently, image service is provided for free.
* Users can synchronize custom images to different regions.
* A maximum of 10 custom images are allowed to be created for each region.
* You can use [DescribeImages](http://www.qcloud.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%8F%AF%E7%94%A8%E7%9A%84%E9%95%9C%E5%83%8F%E5%88%97%E8%A1%A8) API to query the synchronization information of images. Status of 4 indicates that the image is being synchronized (destination region), and status of 5 indicates that the image is being copied (source region).
* This does not apply to North America region.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.
 
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| srcRegion | Yes | String | The region to which the source image belongs. Input the code such as gz, sh. It can be obtained from [DescribeProductRegionList](https://www.qcloud.com/doc/api/229/1286) API.
| imgIdList.n | Yes | String | Image ID. It can be obtained from unImgId in the returned value of [DescribeImages](/document/product/213/1272) API (this API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://www.qcloud.com/doc/api/229/568)).
| dstRegion.n | Yes | String | The region to which the image need to be synchronized. Input the code, such as gz, sh. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
 

## 4. Example
 
Input
<pre>
  https://image.api.qcloud.com/v2/index.php?Action=SyncCvmImage
  &srcRegion=gz
  &imgIdList.0=1
  &dstRegion.0=sh
  &desRegion.1=hk
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output
```
{
    "code": 0,
    "message": ""
}
```





