
## 1. API Description

This API (ModifyInstancesRenewFlag) is used to modify the renewal flags of prepaid instances.

* Any instance marked "Auto Renewal" is automatically renewed for one month whenever it expires.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifyInstancesRenewFlag |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instance to be operated. It can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). The maximum number of instances in a batch for each request is 100. |
| RenewFlag | Yes | String | Automatic renewal flag. Value range:<li>NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically</li><li>NOTIFY_AND_MANUAL_RENEW: notify expiry but not renew automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify expiry nor renew automatically</li>If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidInstance.NotSupported | Instance not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |

## 5. Example

## Example 1 Modify the Renewal Flags of Two Instances

### Scenario description

This example is used to modify the renewal flags of two instances.


### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ModifyInstancesRenewFlag
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&RenewFlag=NOTIFY_AND_AUTO_RENEW
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```

