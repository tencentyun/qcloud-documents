## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ModifyImageSharePermission) is used to modify the image sharing information.

* The accounts to which an image is shared can create instances from this image.
* Each custom image can be shared to a maximum of 50 accounts.
* A shared image can only be used to create instances and its name and description cannot be changed.
* An image can only be shared to the accounts in the same region as the source account.


A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyImageSharePermission |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| ImageId | Yes | String | Image ID, such as `img-gvbnzy6f`. Image ID can be obtained by either of the following ways:<br><li>From the `ImageId` field returned by the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).<br><li> Via the [Image console](https://console.cloud.tencent.com/cvm/image). <br>The specified image ID must identify an image with a status of `NORMAL`. For more information on image statuses, please see [Image Data Sheet](/document/api/213/9452#image_state). |
| AccountIds.N | Yes | Array of String | List of account IDs receiving shared image. For the format of array parameters, please see [API Introduction](/document/api/213/568). The account ID is different from QQ number. To query the account ID, please see the Account ID column in [Account Information](https://console.cloud.tencent.com/developer). |
| Permission | Yes | String | Operations including `SHARE` and `CANCEL`. `SHARE` means sharing, and `CANCEL` means canceling sharing. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidAccountId.NotFound | Invalid account ID. |
| InvalidAccountIs.YourSelf | You cannot share images to yourself. |
| OverQuota | The number of shared images exceeds the quota limit. |

## 5. Example

### Example 1 Share an image

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ModifyImageSharePermission
&ImageId=img-6pb6lrmy
&AccountIds.0=1038493875
&Permission=SHARE
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


