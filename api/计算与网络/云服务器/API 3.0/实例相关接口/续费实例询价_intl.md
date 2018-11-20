## 1. API Description

This API (InquiryPriceRenewInstances) is used to inquire the price of prepaid instance renewal.

* Only inquiry for renewal prices of prepaid instances is supported.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: InquiryPriceRenewInstances |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instance to be operated, which can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). The maximum number of instances for batch request is 100 each time. |
| InstanceChargePrepaid | Yes | [InstanceChargePrepaid](/document/api/213/15753#InstanceChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter can specify the renewal period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. |
| DryRun | No | Boolean | Dry run. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/15753#Price) | This parameter indicates the price of the corresponding instance configuration. |
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

## Example 1 Inquire the Price of Instance Renewal

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceRenewInstances
&InstanceIds.0=ins-2zvpghhc
&InstanceChargePrepaid.Period=1
&InstanceChargePrepaid.RenewFlag=NOTIFY_AND_MANUAL_RENEW
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "Price": {
      "InstancePrice": {
        "DiscountPrice": "1.20",
        "OriginalPrice": "120.00"
      }
    },
    "RequestId": "e2e81b08-d747-455e-b27a-aecc5acafdba"
  }
}
```

