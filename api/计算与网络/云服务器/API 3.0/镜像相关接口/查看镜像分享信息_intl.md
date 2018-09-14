File address

master/
 
Content  

## 1. API Description

This API (ModifyImageSharePermission) is used to modify the image sharing information.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DescribeImageSharePermission |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| ImageId | Yes | String | The ID of the image to be shared |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| SharePermissionSet | Array of [SharePermission](/document/api/213/15753#SharePermission) | Image sharing information |
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
&AccountIds.0=1038493875
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


        
