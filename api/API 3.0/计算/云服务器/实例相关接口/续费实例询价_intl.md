## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (InquiryPriceRenewInstances) is used to inquiry the price of prepaid instance renewal.

* Only supports querying the renewal price of the prepaid instances.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceRenewInstances |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes |  Array of String | ID(s) of one or more instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). A maximum of 100 instances are allowed in a batch for each request. |
| InstanceChargePrepaid | Yes | [InstanceChargePrepaid](/document/api/213/##InstanceChargePrepaid) | Indicates the relevant parameter setting for the prepaid mode. This parameter can specify the renewal length, whether to set automatic renewal and other attributes for the instance purchased on a prepaid basis. |
| DryRun | No | Boolean | Dry run. |
| RenewPortableDataDisk | No | Boolean | Whether to renew elastic data disks. Supported values: <br><li>TRUE: Indicates renewing the elastic data disks mounted to the instance when renewing a prepaid instance<br><li>FALSE: Indicates not renewing the elastic data disks mounted to the instance when renewing a prepaid instance<br><br>Default: TRUE. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/##Price) | Indicates the price of the instance with specified configuration. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidAccount.InsufficientBalance | Insufficient account balance. |
| InvalidAccount.UnpaidOrder | There is an order to be paid in the account. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidInstanceId.NotFound | No instance found. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidPeriod | Invalid period. Supported period values are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36 (in month). |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Inquire the price of renewing an instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceRenewInstances
&InstanceIds.0=ins-2zvpghhc
&InstanceChargePrepaid.Period=1
&InstanceChargePrepaid.RenewFlag=NOTIFY_AND_MANUAL_RENEW
&<Common request parameters>
```

#### Output example

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


