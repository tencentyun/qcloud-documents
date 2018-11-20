## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ModifyInstancesChargeType) is used to switch the billing method of an instance.

* This API only supports switching the billing method from `POSTPAID_BY_HOUR` to `PREPAID`.
* This operation is not supported for instances that are not charged for shutdown period, that belong to `BC1` and `BS1 model families, and that will be terminated at a certain time.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyInstancesChargeType |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes |  Array of String | ID(s) of one or more instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). A maximum of 100 instances are allowed in a batch for each request. |
| InstanceChargeType | Yes | String | [Billing type](https://cloud.tencent.com/document/product/213/2180) of the instance.<br><li> PREPAID: Prepaid. |
| InstanceChargePrepaid | No | [InstanceChargePrepaid](/document/api/213/##InstanceChargePrepaid) | Indicates the relevant parameter setting for the prepaid mode. This parameter can specify the usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. This parameter is required if the billing method for the specified instance is prepaid. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
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
| InvalidParameter | Invalid parameter. The parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidPeriod | Invalid period. Supported period values are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36 (in month). |
| InvalidPermission | The operation is not supported for the account. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Switch the billing method of an instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ModifyInstancesChargeType
&InstanceIds.0=ins-r8hr2upy
&InstanceChargeType=PREPAID
&InstanceChargePrepaid.Period=1
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
  }
}
```


