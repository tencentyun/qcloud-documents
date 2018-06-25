
## 1. API Description

This API (ModifyDisksRenewFlag) is used to modify the renewal flag of the cloud disk, which supports batch modification.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifyDisksRenewFlag |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskIds.N | Yes | Array of String | ID(s) of one or more cloud disks to be operated. |
| RenewFlag | Yes | String | The renewal flag of the cloud disk. Value range: <li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically</li><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically.

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Set Auto Renewal for Cloud Disk

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=ModifyDisksRenewFlag
&DiskIds.0=disk-5w50lrms
&RenewFlag=NOTIFY_AND_AUTO_RENEW
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "1f01171e-6a0f-4208-bb04-d342d97d42c8"
  }
}
```


        
