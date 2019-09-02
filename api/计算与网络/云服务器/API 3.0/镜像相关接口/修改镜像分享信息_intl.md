 
Content  

## 1. API Description

This API (ModifyImageSharePermission) is used to modify the image sharing information.

* The accounts to which an image is shared can create instances from this image.
* Each custom image can be shared to a maximum of 50 accounts.
* A shared image can only be used to create instances and its name and description cannot be changed.
* An image can only be shared to the accounts in the same region as the source account.


## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifyImageSharePermission |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| ImageId | Yes | String | Image ID, such as `img-gvbnzy6f`, which can be obtained by either of the following ways:<li>From the `ImageId` field returned by the API [DescribeImages](https://cloud.tencent.com/document/api/213/15715).</li><li>Via the [Image console](https://console.cloud.tencent.com/cvm/image).</li>The specified image ID must identify an image with a status of `NORMAL`. For more information on image statuses, please see [Image Data Sheet](/document/api/213/9452#image_state). |
| AccountIds.N | Yes | Array of String | List of account IDs receiving shared image. For the format of array parameters, please see [API Introduction](/document/api/213/568). The account ID is different from the QQ number. To query the account ID, please see the Account ID column in [Account Information](https://console.cloud.tencent.com/developer). |
| Permission | Yes | String | Operations including `SHARE` and `CANCEL`. `SHARE` means sharing, and `CANCEL` means canceling sharing. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidAccountId.NotFound | Invalid account ID. |
| InvalidAccountIs.YourSelf | You cannot share images to yourself. |
| OverQuota | The number of shared images exceeds the quota limit. |

## 5. Example

## Example 1: Share an image

### Scenario description

Share the image img-6pb6lrmy to the account 1038493875.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ModifyImageSharePermission
&ImageId=img-6pb6lrmy
&AccountIds.1=1038493875
&Permission=SHARE
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


     
