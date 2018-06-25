## 1. API Description

This API (ModifyImageSharePermission) is used to modify the image sharing information.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>.

* The accounts to which an image is shared can create instances from this image.
* Each custom image can be shared to a maximum of 50 accounts.
* A shared image can only be used to create instances and its name and description cannot be changed.
* An image can only be shared to the accounts in the same region as the source account.


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| ImageId |  String |Yes | Image ID, such as `img-gvbnzy6f`. Image ID can be obtained from either of the following ways: <br><li>Obtained from the `ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418); <br><li>Obtained via [image console](https://console.cloud.tencent.com/cvm/image). <br>The specified image ID must identify an image with a status of `NORMAL`. For more information on image statuses, please see [Image Data Sheet](/document/api/213/9452#image_state). |
| AccountIds | array of Strings | Yes | List of account IDs receiving shared image. For the format of array parameters, please see [API Introduction](/document/api/213/568). The account ID is different from the QQ number. To query the account ID, please see the Account ID column in [Account Information](https://console.cloud.tencent.com/developer). |
| Permission | String | Yes | Operations including `SHARE` and `CANCEL`. `SHARE` means sharing, and `CANCEL` means canceling sharing. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique RequestId is returned for each request. The value of RequestId need to be provided to the backend developer if you fail to call the API. |

## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://intl.cloud.tencent.com/document/product/213/11657).

| Error Code | Description |
|---------|---------|
| InvalidAccountId.NotFound | Invalid Account ID. |
| InvalidAccountIs.YourSelf | Account ID. You cannot specify your own account ID. |
|OverQuota | The number of times for image sharing exceeds the limit. |

## 5. Example 

Input
<pre>
https://image.api.qcloud.com/v2/index.php?Action=ModifyImageSharePermission
&Version=2017-03-12
&ImageId=img-6pb6lrmy
&AccountIds.1=1038493875
&Permission=SHARE
&<<a href="/doc/api/229/6976">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
</pre>
