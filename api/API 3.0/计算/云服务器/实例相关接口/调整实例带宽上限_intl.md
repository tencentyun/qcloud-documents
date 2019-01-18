## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ResetInstancesInternetMaxBandwidth) is used to adjust the public network bandwidth cap of an instance.

* The bandwidth cap varies with different models. For more information, please see [Purchase Network Bandwidth](https://cloud.tencent.com/document/product/213/509).
* For a bandwidth with the `BANDWIDTH_PREPAID` billing method, the parameters `StartTime` and `EndTime` are required to specify the validity period of the adjusted bandwidth. Bandwidth downgrade is not supported in this scenario. Since fee deduction is involved, make sure to keep sufficient balance in your account. You can query the account balance via API [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397).
* For a bandwidth with the `TRAFFIC_POSTPAID_BY_HOUR`, the `BANDWIDTH_POSTPAID_BY_HOUR`, or the `BANDWIDTH_PACKAGE` billing method, the adjustment of the bandwidth cap using this API takes effect in real time. Bandwidth upgrade and downgrade in the permitted range are supported, and the input of parameters `StartTime` and `EndTime` is not supported.
* This API does not support adjusting a bandwidth with the `BANDWIDTH_POSTPAID_BY_MONTH` billing method.
* This API does not support batch adjustment of bandwidths with the `BANDWIDTH_PREPAID` or the `BANDWIDTH_POSTPAID_BY_HOUR` billing method.
* This API does not support batch adjustment of bandwidths with hybrid billing methods. For example, it does not support adjusting bandwidths with the `TRAFFIC_POSTPAID_BY_HOUR` and the `BANDWIDTH_PACKAGE` billing methods at the same time.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ResetInstancesInternetMaxBandwidth |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes |  Array of String | ID(s) of one or more instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). A maximum of 100 instances are allowed in a batch for each request. |
| InternetAccessible | Yes | [InternetAccessible](/document/api/213/##InternetAccessible) | The outbound bandwidth configuration of the public network. The bandwidth cap varies with different models. For more information, please see the bandwidth limit reconciliation. Only the parameter `InternetMaxBandwidthOut` is supported. |
| StartTime | No | String | The date from which the bandwidth takes effect. Format: `YYYY-MM-DD`, such as `2016-10-30`. The start date cannot be earlier than the current date. If the start date is today, the newly set bandwidth takes effect immediately. This parameter is only valid for the prepaid bandwidth. Corresponding error code will be returned by this API if a bandwidth with other billing methods is selected. |
| EndTime | No | String | The date until which the bandwidth is effective. Format: `YYYY-MM-DD`, such as `2016-10-30`. The validity period of the newly set bandwidth includes the end date. The end date cannot be later than the expiry date of the prepaid instance. The expiry date of an instance can be obtained from `ExpiredTime` in the returned value of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). This parameter is only valid for the prepaid bandwidth. Corresponding error code will be returned by this API if a bandwidth with other billing methods is selected. |

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
| InvalidParameterValue.Range | Invalid parameter value. The parameter value range is invalid. |
| InvalidPermission | The operation is not supported for the account. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Adjust the public network bandwidth cap of an instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ResetInstancesInternetMaxBandwidth
&InstanceIds.0=ins-r8hr2upy
&InternetAccessible.InternetMaxBandwidthOut=10
&StartTime=2017-03-15
&EndTime=2017-03-16
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


