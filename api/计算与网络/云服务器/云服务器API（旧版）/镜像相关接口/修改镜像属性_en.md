## 1. API Description
 
This API (ModifyImageAttributes) is used to modify the information of an image such as name and description.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>

* Attributes of shared images are not allowed to be modified.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| imageId | Yes | String | Image ID, which can be obtained from unImgId in the returned field of [DescribeImages](http://cloud.tencent.com/document/api/213/1272) API. |
|imageName | No | String |Image name, which cannot be identical to an existing image name. If you don't want to modify it, left it blank. Naming rule: The name should contain 1-16 characters, including English letters, numbers, and "-".
| imageDescription | No | String | Description of the image. If you don't want to modify it, left it blank. Naming rule: The name contains 0-64 characters, including English letters, numbers, "-", and "_".

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
 
## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ModifyImageAttributes
  &imageId=img-12345678
  &imageName=testName
  &imageDescription=descrip
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```
{
  "code" : 0,
  "message" : ""
}

```





