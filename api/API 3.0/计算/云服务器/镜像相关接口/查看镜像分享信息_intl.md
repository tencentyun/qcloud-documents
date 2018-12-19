## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeImageSharePermission) is used to query the information on image sharing.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeImageSharePermission |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| ImageId | Yes | String | The ID of the image to be shared |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| SharePermissionSet | Array of [SharePermission](/document/api/213/##SharePermission) | Information on image sharing |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidAccountId.NotFound | Invalid account ID. |
| InvalidAccountIs.YourSelf | You cannot share images to yourself. |
| OverQuota | The number of shared images exceeds the quota limit. |

## 5. Example

### Example 1 View the sharing information of a specified image

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeImageSharePermission
&ImageId=img-6pb6lrmy
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "MaxSharePermission": 50,
    "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be",
    "SharePermissionSet": [
      {
        "AccountId": "101104350000",
        "CreatedTime": "2018-06-10T11:02:50Z"
      },
      {
        "AccountId": "101104350001",
        "CreatedTime": "2018-06-13T15:03:25Z"
      }
    ]
  }
}
```


