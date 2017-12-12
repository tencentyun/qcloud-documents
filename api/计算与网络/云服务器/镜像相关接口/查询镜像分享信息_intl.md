## 1. API Description

This API (DescribeImageSharePermission) is used to query the information on image sharing, including the list of the accounts to which an image is shared.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>.

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| ImageId | String | Yes | ID of the image to be queried, such as `img-gvbnzy6f`. Image ID can be obtained by either of the following ways: <br><li>Obtained from the `ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418);<br><li>Obtained via [image console](https://console.cloud.tencent.com/cvm/image).


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique RequestId is returned for each request. The value of RequestId need to be provided to the backend developer if you fail to call the API. |
| SharePermissionSet |array of SharePermissions| An array of information on image sharing, which is composed of as follows. |

Table of Image Sharing Information

| Parameter Name | Type | Description |
|------|------|------|
|CreatedTime|String| The time when the image is shared. |
|Account|String| ID of the account to which the image is shared. The account ID is different from QQ number. To query the account ID, please see the Account ID column in [Account Information](https://console.cloud.tencent.com/developer).|

## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://intl.cloud.tencent.com/document/product/213/11657).

| Error Code | Description |
|---------|---------|
|InvalidImageId.NotFound|This image cannot be found.|

## 5. Example 

Request Parameters
<pre>
https://image.api.qcloud.com/v2/index.php?Action=DescribeImageSharePermission
&Version=2017-03-12
&ImageId=img-6pb6lrmy
&<<a href="/doc/api/229/6976">Common request parameters</a>>
</pre>

Response Parameters
<pre>
{
    "Response": {
        "SharePermissionSet": [
            {
                "CreatedTime"："2016-03-07T20:30:12Z",
                "Account": "50344530"
            }
        ],
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
</pre>





