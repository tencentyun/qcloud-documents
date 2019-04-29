## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (ModifyDisksRenewFlag) is used to modify the renewal flag of the cloud disk, which supports batch modification.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyDisksRenewFlag |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskIds.N | Yes |  Array of String | ID(s) of one or more cloud disks to be operated. |
| RenewFlag | Yes | String | The renewal flag of the cloud disk. Value range: <br><li>NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify expiry nor renew automatically. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Set auto renewal for cloud disk

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=ModifyDisksRenewFlag
&DiskIds.0=disk-5w50lrms
&RenewFlag=NOTIFY_AND_AUTO_RENEW
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "1f01171e-6a0f-4208-bb04-d342d97d42c8"
  }
}
```


