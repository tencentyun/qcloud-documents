## 1. API Description

This API (ShareImage) is used to share images.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>

* Sharers of the image can use this image to create instances.
* Each custom image can be shared to a maximum of 50 accounts.
* A shared image can only be used to create instances and its name and description cannot be changed.
* The share-to region of image should be the region of the sharer.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| imageId | Yes | String | Image ID, which can be obtained from unImgId in the returned field of [DescribeImages](http://www.qcloud.com/document/api/213/1272) API. |
| uinList.n | Yes | String | Account ID of the user sharing the image (This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://www.qcloud.com/doc/api/229/568)). |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
 
## 4. Example
Input

<pre>
https://image.api.qcloud.com/v2/index.php?Action=ShareImage
&imageId=img-apatyoed
&uinList.0=909619400
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output

```
{
    "code":"0",
    "message":""
}
```



