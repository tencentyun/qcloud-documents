## 1. API Description

This API (RenewInstances) is used to renew prepaid instances.

* Only the prepaid instances are supported.
* Make sure the account balance is sufficient when renewing. You can query the account balance via the [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397) API.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: RenewInstances |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instance to be operated, which can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). The maximum number of instances for batch request is 100 each time. |
| InstanceChargePrepaid | Yes | [InstanceChargePrepaid](/document/api/213/15753#InstanceChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter can specify the renewal period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidAccount.InsufficientBalance | Insufficient balance. |
| InvalidAccount.UnpaidOrder | There is an unpaid order in the account. |
| InvalidInstance.NotSupported | The instance is not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` format is incorrect. For example, `ins-1122` indicates an ID length error. |
| InvalidInstanceId.NotFound | The corresponding instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| InvalidPeriod | Invalid period. The periods supported are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] (in month). |
| MissingParameter | Missing parameters. The request does not have the required parameters. |

## 5. Example

## Example 1 Renew an Instance

### Scenario description

This example is used to renew an instance.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=RenewInstances
&InstanceIds.0=ins-r8hr2upy
&InstanceChargePrepaid.Period=1
&InstanceChargePrepaid.RenewFlag=NOTIFY_AND_MANUAL_RENEW
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

