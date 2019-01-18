## 1. API Description

This API (CancelShareImage) is used to cancel the sharing of image.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>

* Image service is FREE of charge now.
* Each custom image can be shared to a maximum of 50 accounts. Canceling the sharing of image can free the quota on account.
* To completely cancel the sharing, first [query sharers](https://cloud.tencent.com/doc/api/229/2391) to obtain all the account IDs to which the image is shared, and specify all of them when calling this API.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|---------|
| imageId | Yes | String | Image ID, which can be obtained from unImgId in the returned field of [DescribeImages](http://cloud.tencent.com/document/api/213/1272) API. |
| uinList.n | Yes | String | Account ID to which the sharing of image is canceled. (This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568)). |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://intl.cloud.tencent.com/document/product/213/10146) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://intl.cloud.tencent.com/document/product/213/10146) on Error Code page. |
 
## 4. Example
Input
<pre>
https://image.api.qcloud.com/v2/index.php?Action=CancelShareImage
&imageId=img-jgggrva9
&uinList.0=877354327
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output
```
{
    "code":"0",
    "message":""
}
```





