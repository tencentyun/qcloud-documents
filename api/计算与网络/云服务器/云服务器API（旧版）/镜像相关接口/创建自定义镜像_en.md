## 1. API Description
 

This API (CreateImage) is used to make the current status of the instance system disk into a new image, which can be used to quickly create instances.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>

* Image service is FREE of charge now.
* The target instance needs to be shut down before you can create a custom image.
* A maximum of 10 custom images are allowed to be created for each region.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | The instance ID to be operated. It can be obtained from unInstanceId in the returned value of  [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API.
| imageName | Yes | String |Image name, which cannot be identical to an existing image name. Naming rule: Contain 1-16 characters, including English letters, numbers, "-".
| imageDescription | No | String | Image description information. Naming rule: Limited to 0-64 characters, including Chinese characters, English letters, numbers, "-", and "_".

 

## 3. Output Parameters
 

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://intl.cloud.tencent.com/document/product/213/10146) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://intl.cloud.tencent.com/document/product/213/10146) on Error Code page. |
| requestId | Int | Task ID.

 
## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=CreateImage
  &instanceId=ins-12345678
  &imageName=test
  &imageDescription=desc
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```
{
  "code" : 0,
  "message" : "ok",
  "requestId" : 24534341s
}

```




