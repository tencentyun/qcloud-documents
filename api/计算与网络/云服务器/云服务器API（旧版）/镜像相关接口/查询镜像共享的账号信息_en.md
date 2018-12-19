## 1. API Description

This API (GetImageShareUinInfo) is used to query the image sharing information of current account, including the list of accounts the images are shared to.

Domain name for API request: <font style="color:red"> image.api.qcloud.com</font>

* You can make a query by a maximum of 10 image IDs.


## 2. Input Parameters

The following list of request parameters lists only API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| imageIds.n | Yes | String | Image ID, which can be obtained from unImgId in the returned value of [DescribeImages](http://cloud.tencent.com/document/api/213/1272) API (This API allows passing multiple IDs at a time). For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568)). |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| data | Array | Image sharing data |

data contains image sharing data with the following structure:

| Parameter Name | Type | Description |
|---------|---------|---------|
| imageNum | Int | Number of images. | 
| maxImgShareNum | Int | Maximum number of images allowed to be shared. | 
| imageList | Array | List of shared images. | 

imageList contains data of a number of images. The data structure for each image is as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| imageId | String | Image ID. | 
| shareUinInfo | Array | Information on sharing. | 

In imageList, shareUinInfo contains details of a number of sharers. The data structure of details for each sharer is as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| uin | Int | The account to which the image is shared. | 
| shareTimeStamp | String | Time of sharing. | 


## 4. Example
Input

<pre>
https://image.api.qcloud.com/v2/index.php?Action=GetImageShareUinInfo
&imageIds.0=img-jgggrva9
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```
{
    "code":"0",
    "message":"",
    "data":{
        "imageNum":"1",
        "maxImgShareNum":"50",
        "imageList":[
            {
                "imageId":"img-jgggrva9",
                "shareUinInfo":[
                    {
                        "uin":"1621874004",
                        "shareTimeStamp":"2016-01-13 15:16:53"
                    },
                    {
                        "uin":"877354327",
                        "shareTimeStamp":"2016-01-18 13:14:17"
                    }
                ]
            }
        ]
    }
}
```





